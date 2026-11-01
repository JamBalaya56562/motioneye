import os, time, logging, traceback
logging.basicConfig(level=logging.INFO, format='%(levelname)s %(message)s')
from motioneye import settings
settings.CONF_PATH = '/tmp/conf'; os.makedirs(settings.CONF_PATH, exist_ok=True)
from motioneye import uploadservices
url = uploadservices.get_authorize_url('gdrive')
open('/x/url.txt', 'w').write(url)
print('link created with PKCE:', 'code_challenge=' in url and 'code_challenge_method=S256' in url, flush=True)
for _ in range(600):
    if os.path.exists('/x/redirect.txt') and os.path.getsize('/x/redirect.txt'):
        break
    time.sleep(1)
key = open('/x/redirect.txt').read().strip()   # the whole address the browser was sent to
open('/x/redirect.txt', 'w').close()
print('pasting the whole address as key', flush=True)
s = uploadservices.GoogleDrive('1')
s.load({'location': '/motioneye-2516-test', 'authorization_key': key})
print('test_access:', s.test_access(), flush=True)
try:
    s.upload_data('2516-pkce-check.txt', 'text/plain', b'motionEye #2516 PKCE check\n', 0, 'Camera1')
    print('upload: ok')
except Exception:
    traceback.print_exc(); print('upload: FAILED')
print('verifier dropped after use:', 'gdrive' not in uploadservices._code_verifiers)
print('refresh token stored:', bool((s.dump().get('credentials') or {}).get('refresh_token')))
