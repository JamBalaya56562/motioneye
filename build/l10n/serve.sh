mkdir /app && cd /app && tar xf /x/branch.tar && pip install -q --root-user-action=ignore . >/dev/null 2>&1
mkdir -p /etc/motioneye /var/lib/motioneye /run/motioneye
printf 'conf_path /etc/motioneye\nrun_path /run/motioneye\nmedia_path /var/lib/motioneye\nlog_level info\nlisten 0.0.0.0\nport 8765\n' > /etc/motioneye/motioneye.conf
exec meyectl startserver -c /etc/motioneye/motioneye.conf
