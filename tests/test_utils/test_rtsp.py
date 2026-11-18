import os
import re
import ssl
from base64 import b64encode
from socket import create_connection
from unittest import mock

import tornado.test
from tornado.iostream import StreamClosedError
from tornado.tcpserver import TCPServer
from tornado.testing import AsyncTestCase, bind_unused_port, gen_test, main

from motioneye import settings
from motioneye.utils.http import RtspsUrl
from motioneye.utils.rtsp import test_rtsp_url


class RtspCamera(TCPServer):
    # answers the OPTIONS request with a fixed reply, then keeps the connection open
    def __init__(self, reply: bytes, ssl_options=None):
        super().__init__(ssl_options=ssl_options)
        self.reply = reply
        self.requests: list = []

    async def handle_stream(self, stream, address):
        try:
            self.requests.append(await stream.read_until(b'\r\n\r\n'))
            await stream.write(self.reply)
            await stream.read_until_close()
        except StreamClosedError:
            pass


class BasicAuthRtspCamera(TCPServer):
    # asks for Basic authentication and accepts only the given user:password
    def __init__(self, credentials: bytes):
        super().__init__()
        self.credentials = credentials
        self.authorizations: list = []

    async def handle_stream(self, stream, address):
        try:
            request = await stream.read_until(b'\r\n\r\n')
            auth = re.search(rb'Authorization: (.*)\r\n', request)
            self.authorizations.append(auth and auth.group(1))
            expected = b'Basic ' + b64encode(self.credentials)
            if auth and auth.group(1) == expected:
                await stream.write(b'RTSP/1.0 200 OK\r\nCSeq: 1\r\n\r\n')
            else:
                await stream.write(
                    b'RTSP/1.0 401 Unauthorized\r\nCSeq: 1\r\n'
                    b'WWW-Authenticate: Basic realm="cam"\r\n\r\n'
                )
            await stream.read_until_close()
        except StreamClosedError:
            pass


class UtilsRtspTest(AsyncTestCase):
    async def check(self, camera: TCPServer, **data):
        sock, port = bind_unused_port()
        camera.add_sockets([sock])
        try:
            return await test_rtsp_url({'port': port, **data})
        finally:
            camera.stop()

    @gen_test
    async def test_test_rtsp_url_camera(self):
        camera = RtspCamera(b'RTSP/1.0 200 OK\r\nCSeq: 1\r\nServer: Cam\r\n\r\n')
        resp = await self.check(camera)
        self.assertIsNone(resp.error)
        self.assertEqual(['tcp', 'udp'], [c['id'] for c in resp.cameras])

    @gen_test
    async def test_test_rtsp_url_connect_timeout(self):
        # Linux drops new connections to a listener whose accept queue is full,
        # so connect() hangs like with a camera that does not answer
        sock, port = bind_unused_port()
        sock.listen(0)
        queued = create_connection(('127.0.0.1', port))
        try:
            with mock.patch.object(settings, 'MJPG_CLIENT_TIMEOUT', 1):
                resp = await test_rtsp_url({'port': port})
        finally:
            queued.close()
            sock.close()

        self.assertIsNone(resp.cameras)
        self.assertEqual('timeout connecting to rtsp netcam', resp.error)

    @gen_test
    async def test_test_rtsp_url_401_without_auth_scheme(self):
        camera = RtspCamera(b'RTSP/1.0 401 Unauthorized\r\nCSeq: 1\r\n\r\n')
        resp = await self.check(camera, username='u')
        self.assertIsNone(resp.cameras)
        self.assertEqual('timeout waiting for rtsp netcam response', resp.error)

    @gen_test
    async def test_test_rtsp_url_basic_auth(self):
        camera = BasicAuthRtspCamera(b'u:s')
        resp = await self.check(camera, username='u', password='s')  # noqa: S106
        self.assertIsNone(resp.error)
        self.assertEqual(['tcp', 'udp'], [c['id'] for c in resp.cameras])
        self.assertIsNotNone(camera.authorizations[-1])

    @gen_test
    async def test_test_rtsp_url_basic_auth_wrong_password(self):
        camera = BasicAuthRtspCamera(b'u:s')
        resp = await self.check(camera, username='u', password='x')  # noqa: S106
        self.assertIsNone(resp.cameras)
        self.assertEqual('authentication failed', resp.error)

    @gen_test
    async def test_test_rtsp_url_basic_auth_empty_password(self):
        camera = BasicAuthRtspCamera(b'u:')
        resp = await self.check(camera, username='u')
        self.assertIsNone(resp.error)
        self.assertEqual(['tcp', 'udp'], [c['id'] for c in resp.cameras])


class UtilsRtspsTest(AsyncTestCase):
    """An rtsps:// camera is tested over TLS, with its self-signed certificate."""

    def _tls_camera(self):
        # the self-signed certificate that tornado tests itself with
        certs = os.path.dirname(tornado.test.__file__)
        context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        context.load_cert_chain(
            os.path.join(certs, 'test.crt'), os.path.join(certs, 'test.key')
        )
        return RtspCamera(
            b'RTSP/1.0 200 OK\r\nCSeq: 1\r\nServer: Cam\r\n\r\n',
            ssl_options=context,
        )

    async def check(self, camera: TCPServer, scheme: str):
        sock, port = bind_unused_port()
        camera.add_sockets([sock])
        try:
            return await test_rtsp_url({'scheme': scheme, 'port': port})
        finally:
            camera.stop()

    @gen_test
    async def test_a_tls_camera_is_found_over_tcp(self):
        camera = self._tls_camera()
        resp = await self.check(camera, 'rtsps')

        self.assertIsNone(resp.error)
        # FFmpeg plays RTSPS over TCP only, so there is no UDP camera to choose
        self.assertEqual(['tcp'], [c['id'] for c in resp.cameras])
        self.assertTrue(resp.cameras[0]['name'].endswith('RTSPS Camera'))
        self.assertTrue(camera.requests[0].startswith(b'OPTIONS rtsps://127.0.0.1:'))

    @gen_test
    async def test_a_tls_camera_fails_as_rtsp(self):
        with self.assertLogs(level='ERROR'):
            resp = await self.check(self._tls_camera(), 'rtsp')

        self.assertIsNone(resp.cameras)

    def test_the_default_port_is_322(self):
        url = RtspsUrl.from_dict({'host': 'cam', 'path': '/live'})
        self.assertEqual('rtsps://cam:322/live', str(url))


if __name__ == '__main__':
    main()
