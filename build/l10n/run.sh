set -e
apt-get -qq update >/dev/null && DEBIAN_FRONTEND=noninteractive apt-get -qq --no-install-recommends install gettext git >/dev/null
pip install -q --root-user-action=ignore babel jinja2 >/dev/null
mkdir /w && cd /w && tar xf /x/src.tar
pybabel extract -F l10n/babel.cfg --omit-header --no-wrap -o motioneye/locale/motioneye.pot motioneye/ 2>/dev/null
sed -i -e '/^#, python-format$/d' -e '${/^$/d}' motioneye/locale/motioneye.pot
find -name '*.js' ! -name '*.min.js' | sort | xargs xgettext --from-code=UTF-8 --no-wrap -o motioneye/locale/motioneye.js.pot
sed -i '/^# SOME DESCRIPTIVE TITLE.$/,/^$/d' motioneye/locale/motioneye.js.pot
git init -q . && git add -A && git -c user.email=x -c user.name=x commit -qm base
echo "== pot diff vs committed:"; git diff --stat -- motioneye/locale/*.pot
for po in motioneye/locale/*/LC_MESSAGES/motioneye.po; do msgmerge --no-wrap -N -q -U --backup=none "$po" motioneye/locale/motioneye.pot; done
for po in motioneye/locale/*/LC_MESSAGES/motioneye.js.po; do msgmerge --no-wrap -N -q -U --backup=none "$po" motioneye/locale/motioneye.js.pot; done
echo "== po diff after msgmerge:"; git diff --stat -- 'motioneye/locale/*/LC_MESSAGES/*.po' | tail -3

tar cf /x/locale.tar motioneye/locale
