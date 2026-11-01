set -e
apt-get -qq update >/dev/null && DEBIAN_FRONTEND=noninteractive apt-get -qq --no-install-recommends install gettext gawk >/dev/null
mkdir /w && cd /w && tar xf /x/cur.tar
mkdir -p motioneye/static/js
for l in en ja; do
  msgfmt -c -o motioneye/locale/$l/LC_MESSAGES/motioneye.mo motioneye/locale/$l/LC_MESSAGES/motioneye.po
  msgfmt -c -o /dev/null motioneye/locale/$l/LC_MESSAGES/motioneye.js.po
  sh l10n/po2json motioneye/locale/$l/LC_MESSAGES/motioneye.js.po motioneye/static/js/motioneye.$l.json
done
python3 -c "import json;[json.load(open(f'motioneye/static/js/motioneye.{l}.json')) for l in ('en','ja')];print('json ok')"
tar cf /x/compiled.tar motioneye/locale/en/LC_MESSAGES/motioneye.mo motioneye/locale/ja/LC_MESSAGES/motioneye.mo motioneye/static/js/motioneye.en.json motioneye/static/js/motioneye.ja.json
