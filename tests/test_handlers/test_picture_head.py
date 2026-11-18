from __future__ import annotations

from unittest.mock import AsyncMock, patch

from motioneye.handlers.picture import PictureHandler
from motioneye.utils import GetCurrentPictureResponse
from tests.test_handlers import RemoteCameraTestCase


class PictureHeadTest(RemoteCameraTestCase):
    """HEAD answers as GET does, without the body (#165)."""

    handler_cls = PictureHandler

    def head(self, path, cookie=True):
        answer = GetCurrentPictureResponse(
            motion_detected=False, capture_fps=2.0, monitor_info='', picture=b'jpg'
        )
        headers = {'Cookie': self.make_session_cookie('admin')} if cookie else {}
        with patch(
            'motioneye.remote.get_current_picture', AsyncMock(return_value=answer)
        ):
            return self.fetch(path, method='HEAD', headers=headers)

    def test_the_current_picture_has_its_type_and_length(self):
        response = self.head('/picture/1/current/')

        self.assertEqual(200, response.code)
        self.assertEqual('image/jpeg', response.headers['Content-Type'])
        self.assertEqual('3', response.headers['Content-Length'])
        self.assertEqual(b'', response.body)

    def test_an_unknown_camera_is_not_found(self):
        response = self.head('/picture/9/current/')

        self.assertEqual(404, response.code)

    def test_it_needs_a_login_as_get_does(self):
        response = self.head('/picture/1/current/', cookie=False)

        self.assertEqual(403, response.code)
