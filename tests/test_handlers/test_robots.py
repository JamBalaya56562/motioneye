from motioneye.handlers.base import BaseHandler
from tests.test_handlers import HandlerTestCase


class RobotsTest(HandlerTestCase):
    """Search engines are asked to index nothing, without a login (#1244); Tornado
    serves /robots.txt from the static folder."""

    handler_cls = BaseHandler

    def test_everything_is_disallowed(self):
        response = self.fetch('/robots.txt')

        self.assertEqual(200, response.code)
        self.assertTrue(response.headers['Content-Type'].startswith('text/plain'))
        self.assertEqual(b'User-agent: *\nDisallow: /\n', response.body)

    def test_head_has_the_length(self):
        response = self.fetch('/robots.txt', method='HEAD')

        self.assertEqual(200, response.code)
        self.assertEqual('26', response.headers['Content-Length'])
