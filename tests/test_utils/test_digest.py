import hashlib
import re
import unittest

from motioneye.utils import build_digest_header


def md5_hex(s: str) -> str:
    return hashlib.md5(s.encode()).hexdigest()  # nosec: B324


def fields(header: str) -> dict:
    return {
        k: v.strip('"') for k, v in re.findall(r'(\w+)=("[^"]*"|[^,\s]+)', header[7:])
    }


class TestBuildDigestHeader(unittest.TestCase):
    # the challenge from RFC 2617, section 3.5
    def state(self, **kwargs):
        state = {
            'realm': 'testrealm@host.com',
            'nonce': 'dcd98b7102dd2f0e8b11d0f600bfb0c093',
            'opaque': '5ccc069c403ebaf9f0171e9517f40e41',
            'qop': 'auth',
        }
        state.update(kwargs)
        return state

    def expected(self, f: dict, ha1: str) -> str:
        ha2 = md5_hex('GET:/dir/index.html')
        return md5_hex(f"{ha1}:{f['nonce']}:{f['nc']}:{f['cnonce']}:auth:{ha2}")

    def build(self, state: dict):
        return build_digest_header(
            'GET', 'http://host.com/dir/index.html', 'Mufasa', 'Circle Of Life', state
        )

    def test_md5(self):
        # motion 4.5 sends algorithm=md5, motion 4.7 algorithm=MD5
        for algorithm in (None, 'md5', 'MD5'):
            with self.subTest(algorithm=algorithm):
                state = self.state()
                if algorithm:
                    state['algorithm'] = algorithm
                header = self.build(state)
                self.assertTrue(header.startswith('Digest '))
                f = fields(header)

                ha1 = md5_hex('Mufasa:testrealm@host.com:Circle Of Life')
                self.assertEqual(self.expected(f, ha1), f['response'])
                self.assertEqual('00000001', f['nc'])
                self.assertEqual(state['opaque'], f['opaque'])

    def test_md5_sess(self):
        f = fields(self.build(self.state(algorithm='MD5-sess')))

        ha1 = md5_hex('Mufasa:testrealm@host.com:Circle Of Life')
        ha1 = md5_hex(f"{ha1}:{f['nonce']}:{f['cnonce']}")
        self.assertEqual(self.expected(f, ha1), f['response'])

    def test_nonce_count(self):
        state = self.state()
        self.build(state)
        f = fields(self.build(state))

        self.assertEqual('00000002', f['nc'])

    def test_other_algorithms(self):
        # motion only asks for MD5; another algorithm is not answered with a
        # wrong hash
        for algorithm in ('SHA', 'SHA-256', 'SHA-512-256'):
            with self.subTest(algorithm=algorithm):
                self.assertIsNone(self.build(self.state(algorithm=algorithm)))


if __name__ == '__main__':
    unittest.main()
