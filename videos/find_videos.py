"""Finds one specific YouTube video for every query in queries.py and writes videos.json.

It prefers the trusted channels listed in PREFER, skips Shorts and anything over 40 minutes,
and checks each pick with YouTube's oEmbed endpoint (so dead or private videos are never linked).
Run: py videos/find_videos.py
"""
import json, os, re, sys, time, urllib.parse, urllib.request
sys.path.insert(0, os.path.dirname(__file__))
from queries import PREFER, P1, P2, P3

UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130 Safari/537.36'
OUT = os.path.join(os.path.dirname(__file__), 'videos.json')

def get(url):
    req = urllib.request.Request(url, headers={'User-Agent': UA, 'Accept-Language': 'en-GB', 'Cookie': 'SOCS=CAI; CONSENT=YES+'})
    return urllib.request.urlopen(req, timeout=30).read().decode('utf-8', 'ignore')

def search(q):
    html = get('https://www.youtube.com/results?hl=en&gl=GB&search_query=' + urllib.parse.quote(q))
    m = re.search(r'var ytInitialData = (\{.*?\});</script>', html, re.S)
    if not m: return []
    data = json.loads(m.group(1))
    out = []
    def walk(o):
        if isinstance(o, dict):
            if 'videoRenderer' in o:
                v = o['videoRenderer']
                try:
                    out.append(dict(id=v['videoId'], title=''.join(r['text'] for r in v['title']['runs']),
                                    channel=v['ownerText']['runs'][0]['text'], length=v.get('lengthText', {}).get('simpleText', '')))
                except (KeyError, IndexError):
                    pass
                return
            for x in o.values(): walk(x)
        elif isinstance(o, list):
            for x in o: walk(x)
    walk(data)
    return out

def minutes(length):
    parts = [int(p) for p in length.split(':') if p.isdigit()]
    if not parts: return 999
    secs = 0
    for p in parts: secs = secs * 60 + p
    return secs / 60

def pick(results, prefer, used):
    ok = [r for r in results if 1 <= minutes(r['length']) <= 40 and r['id'] not in used]
    for name in prefer:
        for r in ok:
            if name.lower() in r['channel'].lower():
                return r
    return ok[0] if ok else None

def oembed(vid):
    try:
        j = json.loads(get('https://www.youtube.com/oembed?format=json&url=' + urllib.parse.quote('https://www.youtube.com/watch?v=' + vid)))
        return j.get('title'), j.get('author_name')
    except Exception:
        return None, None

def main():
    prev = {}
    if os.path.exists(OUT):
        with open(OUT, encoding='utf-8') as f: prev = json.load(f)
    result, used = {}, set()
    for phase, plan in (('1', P1), ('2', P2), ('3', P3)):
        for week, subjects in plan.items():
            for subj, queries in subjects.items():
                key = f'{phase}-{week}-{subj}'
                items = []
                for q, label in queries:
                    cached = next((v for v in prev.get(key, []) if v.get('q') == q), None)
                    if cached:
                        items.append(cached); used.add(cached['id']); continue
                    try:
                        r = pick(search(q), PREFER[subj], used)
                    except Exception as e:
                        print('search failed', q, e); r = None
                    time.sleep(1.2)
                    if not r:
                        print('NO RESULT', key, q); continue
                    title, author = oembed(r['id'])
                    if not title:
                        print('OEMBED FAIL', key, q, r['id']); continue
                    used.add(r['id'])
                    items.append(dict(q=q, label=label, id=r['id'], title=title, channel=author, length=r['length']))
                    print(f'{key:10s} {label[:28]:28s} | {author[:24]:24s} | {r["length"]:>6s} | {title[:70]}')
                result[key] = items
                with open(OUT, 'w', encoding='utf-8') as f: json.dump(result, f, ensure_ascii=False, indent=1)
    print('videos:', sum(len(v) for v in result.values()))

if __name__ == '__main__':
    main()
