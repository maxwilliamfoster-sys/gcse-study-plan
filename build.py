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
# Oct 2026: the study plan was merged into the GCSE Plan app, so the Pages site now forwards there
# (old tab links map to the matching screen). dist/plan.html is still built as a record of the old page.
NEW = 'https://maxwilliamfoster-sys.github.io/gcse-plan/'
page = f'''<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="icon" href="icon-192.png" type="image/png">
<link rel="apple-touch-icon" href="icon-180.png">
<title>GCSE Study Plan has moved</title>
<meta http-equiv="refresh" content="0; url={NEW}#/today">
<script>
var tabs = {{today: '/today', week: '/week', plan: '/plan', subjects: '/subjects', exams: '/plan/exams', method: '/plan/method'}};
location.replace('{NEW}#' + (tabs[location.hash.slice(1)] || '/today'));
</script>
</head>
<body style="font:16px/1.5 system-ui,sans-serif;max-width:32rem;margin:15vh auto;padding:0 16px">
<h1 style="font-size:1.4rem">Your study plan has moved</h1>
<p>The timetable, live lessons and weekly videos are now part of your GCSE Plan app.</p>
<p><a href="{NEW}#/today">Open GCSE Plan</a></p>
</body>
</html>
'''
(root / 'index.html').write_text(page, encoding='utf-8')
print('built', len(frag) // 1024, 'KB,', sum(len(v) for v in slim.values()), 'videos')
