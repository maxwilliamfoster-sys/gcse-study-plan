"""Builds the study plan page with each week's videos baked in.
  src/plan.html + videos/videos.json -> index.html (GitHub Pages) and dist/plan.html (Claude artifact)
"""
import json, pathlib
root = pathlib.Path(__file__).parent
src = (root / 'src' / 'plan.html').read_text(encoding='utf-8')
videos = json.loads((root / 'videos' / 'videos.json').read_text(encoding='utf-8'))
slim = {k: [{f: v[f] for f in ('id', 'title', 'channel', 'length')} for v in vs] for k, vs in videos.items() if vs}
data = json.dumps(slim, ensure_ascii=False).replace('</', r'<\/')
frag = src.replace('/*VIDEOS*/{}', data, 1)
(root / 'dist').mkdir(exist_ok=True)
(root / 'dist' / 'plan.html').write_text(frag, encoding='utf-8')
head = '\n'.join([
    '<!doctype html>',
    '<html lang="en-GB">',
    '<head>',
    '<meta charset="utf-8">',
    '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">',
    '<link rel="icon" href="icon-192.png" type="image/png">',
    '<link rel="apple-touch-icon" href="icon-180.png">',
    '<link rel="manifest" href="manifest.webmanifest">',
    '<meta name="theme-color" content="#2f5bd3">',
    '',
])
page = head + frag.replace('<div class="wrap">', '</head>\n<body>\n<div class="wrap">', 1) + '\n</body>\n</html>\n'
(root / 'index.html').write_text(page, encoding='utf-8')
print('built', len(frag) // 1024, 'KB,', sum(len(v) for v in slim.values()), 'videos')
