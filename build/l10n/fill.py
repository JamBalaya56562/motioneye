"""Fills the new strings in the en and ja catalogs (the others go through Weblate)."""

import re

NEW = {
    'the key used to authenticate with the upload service, usually only needed during setup; for Google, the whole address of the page that cannot be loaded after allowing access': (
        'po',
        'アップロードサービスの認証で使用されるキー（通常、設定時のみ必要）。Google の場合は、アクセスを許可した後に表示される、読み込めないページのアドレス全体',
    ),
    'Sign in to Google in the new tab, and allow access.': (
        'js',
        '新しいタブで Google にログインし、アクセスを許可してください。',
    ),
    'The tab then shows a page that cannot be loaded, at an address starting with http://127.0.0.1/. This is expected.': (
        'js',
        'その後、タブには http://127.0.0.1/ で始まるアドレスの、読み込めないページが表示されます。これは想定どおりです。',
    ),
    'Copy the whole address from the address bar of that tab, and paste it as the authorization key.': (
        'js',
        'そのタブのアドレスバーからアドレス全体をコピーし、認証キーとして貼り付けてください。',
    ),
    'The key only works with this link, and until motionEye is restarted.': (
        'js',
        'このキーはこのリンクからのみ、motionEye を再起動するまで有効です。',
    ),
    'Obtaining the key from Google': ('js', 'Google からキーを取得'),
}

for lang in ('en', 'ja'):
    for kind, file in (('po', 'motioneye.po'), ('js', 'motioneye.js.po')):
        path = f'motioneye/locale/{lang}/LC_MESSAGES/{file}'
        with open(path, encoding='utf-8', newline='') as f:
            text = f.read()
        for msgid, (where, ja) in NEW.items():
            if where != kind:
                continue
            translation = msgid if lang == 'en' else ja
            escaped = msgid.replace('\\', '\\\\').replace('"', '\\"')
            pattern = f'msgid "{escaped}"\nmsgstr ""\n'
            assert text.count(pattern) == 1, (path, msgid)
            text = text.replace(
                pattern,
                f'msgid "{escaped}"\nmsgstr "{translation.replace(chr(34), chr(92) + chr(34))}"\n',
            )
        with open(path, 'w', encoding='utf-8', newline='') as f:
            f.write(text)
        print('filled', path)
