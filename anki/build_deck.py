"""Builds Max's GCSE 2027 Anki decks: one top-level deck per subject.

Card sources:
  * app_data.json  - exported from the GCSE Plan app (topic cards, the AQA 8662 vocab list, History dates/people)
  * cards/*.py     - extra cards written for the 2027 timetable (Science, Maths, History, English, German grammar)
Facts printed on the 2027 exam sheets (every Physics equation, the Edexcel formula sheet) are left out (EXCLUDE).

New cards follow the timetable: week-1 topics first, then week 2, and so on. Each subject has its own preset
("GCSE German", "GCSE Science", ...) whose daily new-card limit finishes that subject on schedule.

Usage (needs the official `anki` package, same version as the desktop app):
  python build_deck.py --apkg GCSE-2027.apkg     # build a shareable package
  Inside Anki (Tools > Debug Console), to update a live collection in place:
    import sys; sys.path.insert(0, r'<this folder>'); import build_deck; build_deck.build(mw.col); mw.reset()
Re-running is safe: notes have stable GUIDs, so existing notes are updated or moved, not duplicated.
Do NOT pass --collection with a path under AppData from the Claude app: it writes to a sandboxed copy.
"""
import argparse, hashlib, importlib.util, json, math, os, tempfile
from collections import defaultdict

from anki.collection import Collection, ExportAnkiPackageOptions

HERE = os.path.dirname(os.path.abspath(__file__))
# One top-level deck per subject (no shared parent), each with its own preset and daily new-card limit.
DECKS = {
    'DE_VOC_F': 'German (AQA 8662)::1 Vocab - Foundation list',
    'DE_VOC_H': 'German (AQA 8662)::2 Vocab - Higher list',
    'DE_GRAM': 'German (AQA 8662)::3 Grammar',
    'DE_TOPICS': 'German (AQA 8662)::4 Topics and phrases',
    'DE_SPEAK': 'German (AQA 8662)::5 Speaking and dictation',
    'H_IR': 'History (OCR J410)::1 Paper 1 - International Relations 1918-75',
    'H_USA': 'History (OCR J410)::2 Paper 1 - USA 1919-48',
    'H_MIG': 'History (OCR J410)::3 Paper 2 - Migration to Britain',
    'H_EMP': 'History (OCR J410)::4 Paper 3 - Empire 1688-1730 and Spitalfields',
    'H_SKILLS': 'History (OCR J410)::5 Exam skills',
    'BIO': 'Science (AQA Trilogy)::1 Biology',
    'CHEM': 'Science (AQA Trilogy)::2 Chemistry',
    'PHYS': 'Science (AQA Trilogy)::3 Physics (units and ideas - equations are given)',
    'RP': 'Science (AQA Trilogy)::4 Required practicals',
    'MATHS_TOPICS': 'Maths (Edexcel 1MA1)::1 Topics',
    'MATHS_LEARN': 'Maths (Edexcel 1MA1)::2 Formulae NOT on the sheet and facts',
    'RJ': 'English Literature (AQA 8702)::1 Romeo and Juliet',
    'JH': 'English Literature (AQA 8702)::2 Jekyll and Hyde',
    'AIC': 'English Literature (AQA 8702)::3 An Inspector Calls',
    'PC': 'English Literature (AQA 8702)::4 Power and Conflict and unseen',
    'LANG': 'English Language (AQA 8700)',
}
LEGACY_ROOT = 'GCSE 2027'   # the old single parent deck; emptied and removed by build()
# Days over which each subject's new cards are introduced: German vocab runs to about the end of February,
# everything else finishes by early January (Phase 1 plus the Christmas catch-up).
INTRO_DAYS = {'German (AQA 8662)': 140}
DEFAULT_INTRO_DAYS = 85
def root_of(deck_key):
    return DECKS[deck_key].split('::')[0]

# Facts the exam gives you (2027 AQA Physics equation sheet, Edexcel 1MA1 formula sheet) - never drilled.
EXCLUDE = {
    ('p-energy', 'Kinetic energy equation'), ('p-energy', 'GPE equation'), ('p-energy', 'Specific heat capacity equation'),
    ('p-energy', 'Efficiency'), ('p-elec', 'V = ?'), ('p-particles', 'Density equation'),
    ('p-particles', 'Specific latent heat equation'), ('p-forces', "Newton's second law"), ('p-forces', 'Weight equation'),
    ('p-forces', "Hooke's law"), ('p-forces', 'Momentum equation (H)'), ('p-waves', 'Wave speed equation'),
    ('p-waves', 'Frequency 50 Hz, wavelength 2 m \u2014 speed?'), ('p-magnet', 'Motor effect equation (H)'),
    ('m-area', 'Area of a circle, radius 5 (in terms of \u03c0)'), ('m-area', 'Trapezium a = 6, b = 10, h = 4'),
    ('m-area', 'Cylinder volume, r = 3, h = 10 (in terms of \u03c0)'), ('m-trig', 'Hypotenuse when the other sides are 5 and 12'),
    ('m-trig', 'Area: a = 8, b = 5, C = 30\u00b0'), ('m-frac', '\u00a3200 at 3% compound interest for 4 years'),
    ('m-quad', 'Solve 2x\u00b2 + 3x \u2212 4 = 0 to 2 d.p.'),
}

SUBJECT = {  # deck key -> (label, css code)
    'DE': ('German', 'de'), 'H': ('History', 'hist'), 'BIO': ('Biology', 'sci'), 'CHEM': ('Chemistry', 'sci'),
    'PHYS': ('Physics', 'sci'), 'RP': ('Required practical', 'sci'), 'MATHS': ('Maths', 'maths'),
    'RJ': ('Romeo and Juliet', 'lit'), 'JH': ('Jekyll and Hyde', 'lit'), 'AIC': ('An Inspector Calls', 'lit'),
    'PC': ('Power and Conflict', 'lit'), 'LANG': ('English Language', 'lang'),
}
def subject_of(deck_key):
    for k in (deck_key, deck_key.split('_')[0]):
        if k in SUBJECT:
            return SUBJECT[k]
    raise KeyError(deck_key)

# App topic id -> (deck key, plan week)
TOPIC_MAP = {
    # maths
    'm-num': 1, 'm-frac': 1, 'm-bounds': 1, 'm-surds': 1, 'm-alg': 2, 'm-sheet': 2, 'm-eq': 3, 'm-quad': 3, 'm-simul': 3,
    'm-lines': 4, 'm-graphs': 4, 'm-ratio': 5, 'm-rates': 5, 'm-angles': 6, 'm-transf': 6, 'm-circle': 6, 'm-trig': 7,
    'm-area': 8, 'm-vectors': 8, 'm-prob': 9, 'm-stats': 9, 'm-seq': 10, 'm-proof': 10, 'm-exam': 10,
    # science
    'b-cells': 1, 'b-div': 1, 'b-transport': 1, 'c-atoms': 1, 'p-energy': 1, 'b-digest': 2, 'b-heart': 2, 'b-disease': 2,
    'c-bonding': 2, 'p-elec': 2, 'b-infection': 3, 'c-quant': 3, 'p-equations': 3, 'b-energy': 4, 'c-changes': 4,
    'p-particles': 4, 'c-energy': 5, 'p-atomic': 5, 'p-skills': 5, 'b-nerves': 6, 'b-hormones': 6, 'c-rates': 6,
    'p-forces': 6, 'b-genetics': 7, 'c-organic': 7, 'b-evolution': 8, 'c-analysis': 8, 'p-waves': 8, 'b-ecology': 9,
    'c-atmos': 9, 'c-resources': 9, 'p-magnet': 9,
    # english
    'el-p1q1': 1, 'el-lang': 1, 'el-struct': 2, 'el-eval': 3, 'el-creative': 4, 'el-compare': 6, 'el-viewpoint': 9, 'el-spag': 10,
    'aic-plot': 1, 'aic-chars': 2, 'rj-plot': 3, 'rj-themes': 4, 'jh-plot': 5, 'jh-themes': 6, 'pc-1': 7, 'pc-2': 8, 'pc-3': 9, 'lit-unseen': 10,
    # history
    'h-ir-peace': 1, 'h-ir-war': 2, 'h-ir-interp': 3, 'h-ir-cw1': 4, 'h-ir-cw2': 5, 'h-ir-vietnam': 6, 'h-usa-20s': 7,
    'h-usa-prej': 8, 'h-usa-30s': 9, 'h-usa-war': 10, 'h-mig-med': 1, 'h-mig-early': 2, 'h-mig-modern': 4, 'h-mig-20c': 5,
    'h-empire': 8, 'h-empire-econ': 9, 'h-empire-soc': 10, 'h-spitalfields': 10, 'h-skills': 5,
    # german
    'de-rel': 1, 'de-health': 2, 'de-cases': 2, 'de-school': 3, 'de-tenses': 3, 'de-free': 4, 'de-fest': 5, 'de-wordorder': 5,
    'de-celeb': 6, 'de-travel': 7, 'de-media': 8, 'de-env': 9, 'de-exam': 10,
}
def topic_deck(subject, tid):
    if subject == 'maths': return 'MATHS_TOPICS'
    if subject == 'science':
        if tid == 'p-skills': return 'RP'
        return {'b': 'BIO', 'c': 'CHEM', 'p': 'PHYS'}[tid[0]]
    if subject == 'englang': return 'LANG'
    if subject == 'englit':
        return {'aic': 'AIC', 'rj': 'RJ', 'jh': 'JH'}.get(tid.split('-')[0], 'PC')
    if subject == 'hist':
        if tid.startswith('h-ir'): return 'H_IR'
        if tid.startswith('h-usa'): return 'H_USA'
        if tid.startswith('h-mig'): return 'H_MIG'
        if tid == 'h-skills': return 'H_SKILLS'
        return 'H_EMP'
    if subject == 'german':
        return 'DE_GRAM' if tid in ('de-tenses', 'de-wordorder', 'de-cases', 'de-exam') else 'DE_TOPICS'
    raise KeyError((subject, tid))

def hist_date_place(i):
    """histDates index -> (deck, week); the app list is ordered IR, USA, Migration, Empire."""
    if i <= 53:
        w = 1 if i <= 12 else 2 if i <= 29 else 3 if i <= 31 else 4 if i <= 40 else 5 if i <= 46 else 6
        return 'H_IR', w
    if i <= 73: return 'H_USA', 7 if i <= 62 else 9 if i <= 68 else 10
    if i <= 104: return 'H_MIG', 1 if i <= 78 else 2 if i <= 82 else 4 if i <= 87 else 5 if i <= 93 else 6
    return 'H_EMP', 8 if i <= 110 else 9 if i <= 118 else 10

def hist_person_place(i):
    if i <= 15: return 'H_IR', [1, 1, 1, 1, 2, 3, 3, 4, 4, 5, 5, 5, 6, 6, 6, 7][i]
    if i <= 25: return 'H_USA', [9, 9, 8, 8, 8, 8, 9, 9, 9, 10][i - 16]
    if i <= 37: return ('H_EMP', 10) if i == 37 else ('H_MIG', [2, 4, 4, 3, 3, 2, 2, 4, 6, 6, 6][i - 26])
    if i <= 41: return 'H_EMP', [8, 8, 8, 9][i - 38]
    if i <= 45: return 'H_IR', [2, 4, 6, 7][i - 42]
    return 'H_USA', [7, 7, 8, 9, 9, 10][i - 46]

CSS = """
.card { font-family: "Segoe UI", system-ui, -apple-system, sans-serif; font-size: 22px; line-height: 1.45;
  color: #1b2330; background: #f6f7fb; text-align: center; padding: 18px; }
.nightMode.card, .night_mode .card { color: #e8ecf3; background: #151a22; }
.subj { display: inline-block; font-size: 13px; font-weight: 700; letter-spacing: .06em; text-transform: uppercase;
  padding: 3px 10px; border-radius: 999px; color: #fff; background: #5a6575; margin-bottom: 14px; }
.s-de { background: #c2337a; } .s-hist { background: #9a4a1c; } .s-sci { background: #1f8a4c; }
.s-maths { background: #2f5bd3; } .s-lit { background: #7a3fc4; } .s-lang { background: #b8860b; }
.q { font-weight: 600; } .a { margin-top: 6px; } .big { font-size: 34px; font-weight: 700; }
.info { margin-top: 16px; font-size: 15px; color: #6b7585; }
.nightMode .info, .night_mode .info { color: #9aa5b6; }
hr#answer { border: 0; border-top: 1px solid #c9d0db; margin: 16px 0; }
"""

def basic_model(col):
    mm = col.models
    m = mm.by_name('GCSE 2027 Basic')
    if m: return m
    m = mm.new('GCSE 2027 Basic')
    for f in ('Front', 'Back', 'Subject', 'Code', 'Info'):
        mm.add_field(m, mm.new_field(f))
    t = mm.new_template('Card 1')
    t['qfmt'] = '<div class="subj s-{{Code}}">{{Subject}}</div><div class="q">{{Front}}</div>'
    t['afmt'] = '{{FrontSide}}<hr id="answer"><div class="a">{{Back}}</div>{{#Info}}<div class="info">{{Info}}</div>{{/Info}}'
    mm.add_template(m, t)
    m['css'] = CSS
    mm.add(m)
    return mm.by_name('GCSE 2027 Basic')

def vocab_model(col):
    mm = col.models
    m = mm.by_name('GCSE 2027 German Vocab')
    if m: return m
    m = mm.new('GCSE 2027 German Vocab')
    for f in ('German', 'English', 'List', 'Reverse'):
        mm.add_field(m, mm.new_field(f))
    t1 = mm.new_template('German to English')
    t1['qfmt'] = '<div class="subj s-de">German → English · {{List}}</div><div class="big">{{German}}</div>'
    t1['afmt'] = '{{FrontSide}}<hr id="answer"><div class="a">{{English}}</div>'
    t2 = mm.new_template('English to German')
    t2['qfmt'] = ('{{#Reverse}}<div class="subj s-de">English → German · {{List}}</div><div class="big">{{English}}</div>'
                  '<div class="info">Say it out loud. Nouns: include der/die/das.</div>{{/Reverse}}')
    t2['afmt'] = '{{FrontSide}}<hr id="answer"><div class="big">{{German}}</div>'
    mm.add_template(m, t1); mm.add_template(m, t2)
    m['css'] = CSS
    mm.add(m)
    return mm.by_name('GCSE 2027 German Vocab')

def guid(*parts):
    return 'gcse27-' + hashlib.sha1('|'.join(parts).encode('utf-8')).hexdigest()[:16]

def esc(s):
    return str(s).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

def load_extra():
    out = []
    for name in ('science', 'maths', 'history', 'english', 'german'):
        spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, 'cards', name + '.py'))
        mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
        out += mod.CARDS
    return out

def collect(app):
    """Returns a list of items: dict(kind, deck, week, guid, fields, tags, rev_week?)."""
    items, seen = [], set()
    def add_basic(deck, week, front, back, tags, info=''):
        key = (deck, ' '.join(front.lower().split()))
        if key in seen: return
        seen.add(key)
        label, code = subject_of(deck)
        items.append(dict(kind='basic', deck=deck, week=week, guid=guid(deck, front),
                          fields=[esc(front), esc(back), label, code, esc(info)], tags=tags))
    # extra cards written for the timetable come first so their wording wins on duplicates
    for deck, week, tag, q, a in load_extra():
        add_basic(deck, week, q, a, [tag.replace(' ', '_'), 'wk%02d' % week])
    for t in app['topics']:
        if t['id'] not in TOPIC_MAP: continue
        deck, week = topic_deck(t['subject'], t['id']), TOPIC_MAP[t['id']]
        for q, a in t['cards']:
            if (t['id'], q) in EXCLUDE: continue
            add_basic(deck, week, q, a, [t['id'], 'wk%02d' % week], info=t['name'])
    for i, (event, date) in enumerate(app['histDates']):
        deck, week = hist_date_place(i)
        add_basic(deck, week, 'When? ' + event, date, ['dates', 'wk%02d' % week])
    for i, (who, what) in enumerate(app['histPeople']):
        deck, week = hist_person_place(i)
        add_basic(deck, week, 'Who or what was… ' + who + '?', what, ['people', 'wk%02d' % week])
    # AQA 8662 vocabulary: German->English for every word, English->German for the Foundation list
    for lst, words, deck, w0, w1 in (('F', app['vocab']['F'], 'DE_VOC_F', 1, 16), ('H', app['vocab']['H'], 'DE_VOC_H', 6, 18)):
        n = len(words)
        for i, (de, en) in enumerate(words):
            week = w0 + (i * (w1 - w0 + 1)) // n
            items.append(dict(kind='vocab', deck=deck, week=week, rev_week=week + 3 if lst == 'F' else None,
                              guid=guid('vocab', lst, de, en),
                              fields=[esc(de), esc(en), 'Foundation' if lst == 'F' else 'Higher', 'y' if lst == 'F' else ''],
                              tags=['vocab', 'list_' + lst, 'wk%02d' % week]))
    return items

def plan_order(items):
    """Global order for new cards: by plan week, subjects interleaved round-robin. Returns [(guid, template ord)]."""
    slots = defaultdict(lambda: defaultdict(list))
    for it in items:
        group = it['deck'].split('_')[0]
        slots[it['week']][group].append((it['guid'], 0))
        if it['kind'] == 'vocab' and it['fields'][3]:
            slots[it['rev_week'] or it['week']][group].append((it['guid'], 1))
    order = []
    for week in sorted(slots):
        queues = [list(q) for q in slots[week].values()]
        while any(queues):
            for q in queues:
                if q: order.append(q.pop(0))
    return order

def ensure_presets(col, items, deck_ids):
    """One preset per subject: daily new cards = cards / intro days, gathered in plan order."""
    cards_per_root = defaultdict(int)
    for it in items:
        cards_per_root[root_of(it['deck'])] += 2 if (it['kind'] == 'vocab' and it['fields'][3]) else 1
    existing = {c['name']: c for c in col.decks.all_config()}
    limits = {}
    for root, n in cards_per_root.items():
        name = 'GCSE ' + root.split(' (')[0]
        conf = existing.get(name) or col.decks.get_config(col.decks.add_config_returning_id(name))
        per_day = max(2, math.ceil(n / INTRO_DAYS.get(root, DEFAULT_INTRO_DAYS)))
        conf['new']['perDay'] = per_day
        conf['new']['bury'] = True
        conf['rev']['perDay'] = 400
        conf['rev']['bury'] = True
        conf['newGatherPriority'] = 1   # lowest position first = timetable order
        conf['newSortOrder'] = 1        # keep gathered order
        conf['newMix'] = 0              # mix new cards with reviews
        conf['desiredRetention'] = 0.9
        col.decks.update_config(conf)
        limits[root] = per_day
        for deck_name, did in deck_ids.items():
            if deck_name == root or deck_name.startswith(root + '::'):
                d = col.decks.get(did)
                col.decks.set_config_id_for_deck_dict(d, conf['id'])
                col.decks.save(d)
    try:
        col.set_config('fsrs', True)
    except Exception:
        pass
    return limits

def build(col, log=print):
    """Adds/updates every card, moves cards into the per-subject decks, removes cards that are no longer
    in the plan (e.g. equation-sheet facts), and re-orders new cards to follow the timetable.
    Safe to run on a live collection (it is also run from inside Anki's debug console)."""
    with open(os.path.join(HERE, 'app_data.json'), encoding='utf-8') as f:
        app = json.load(f)
    items = collect(app)
    basic, vocab = basic_model(col), vocab_model(col)
    deck_ids = {}
    for name in DECKS.values():
        parts = name.split('::')
        for i in range(1, len(parts) + 1):
            deck_ids['::'.join(parts[:i])] = col.decks.id('::'.join(parts[:i]))
    existing = dict(col.db.all('select guid, id from notes'))
    added = updated = moved = 0
    card_for = {}
    for it in items:
        did = deck_ids[DECKS[it['deck']]]
        nid = existing.get(it['guid'])
        if nid:
            note = col.get_note(nid)
            if list(note.fields) != it['fields']:
                note.fields = it['fields']; col.update_note(note); updated += 1
            wrong = [c.id for c in note.cards() if c.did != did and c.odid != did]
            if wrong:
                col.set_deck(wrong, did); moved += len(wrong)
        else:
            note = col.new_note(basic if it['kind'] == 'basic' else vocab)
            note.guid = it['guid']
            note.fields = it['fields']
            note.tags = ['GCSE2027'] + it['tags']
            col.add_note(note, did)
            added += 1
        for c in col.get_note(note.id).cards():
            card_for[(it['guid'], c.ord)] = c
    # Remove GCSE notes that are no longer in the plan (equation-sheet facts, reworded cards)
    keep = {it['guid'] for it in items}
    stale = [nid for g, nid in col.db.all("select guid, id from notes where tags like '% GCSE2027 %'") if g not in keep]
    if stale:
        col.remove_notes(stale)
    # Re-order the cards that are still new so they follow the plan week by week
    order = [card_for[k].id for k in plan_order(items) if k in card_for and card_for[k].type == 0]
    if order:
        col.sched.reposition_new_cards(card_ids=order, starting_from=1, step_size=1, randomize=False, shift_existing=False)
    limits = ensure_presets(col, items, deck_ids)
    # Remove the old single parent deck once nothing is left in it
    old = col.decks.id_for_name(LEGACY_ROOT)
    if old and col.decks.card_count(old, include_subdecks=True) == 0:
        col.decks.remove([old])
    total = col.db.scalar("select count() from cards c join notes n on c.nid = n.id where n.tags like '% GCSE2027 %'")
    log(f'notes added {added}, updated {updated}, removed {len(stale)}; cards moved {moved}; GCSE cards now {total}')
    roots = sorted({root_of(k) for k in DECKS})
    for root in roots:
        log(f'  {col.decks.card_count(deck_ids[root], include_subdecks=True):5d} cards, {limits.get(root)} new/day  {root}')
    return [deck_ids[r] for r in roots]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--collection')
    ap.add_argument('--apkg')
    a = ap.parse_args()
    if a.collection:
        os.makedirs(os.path.dirname(a.collection), exist_ok=True)
        col = Collection(a.collection)
        try:
            build(col)
        finally:
            col.close()
    if a.apkg:
        tmp = os.path.join(tempfile.mkdtemp(), 'build.anki2')
        col = Collection(tmp)
        try:
            build(col)
            col.export_anki_package(out_path=os.path.abspath(a.apkg),
                                    options=ExportAnkiPackageOptions(with_scheduling=True, with_deck_configs=True, with_media=False, legacy=False),
                                    limit=None)
            print('wrote', a.apkg)
        finally:
            col.close()

if __name__ == '__main__':
    main()
