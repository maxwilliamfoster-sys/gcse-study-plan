# Max's GCSE Study Plan (exams May–June 2027)

A home-study GCSE timetable and revision guide, built around the Year 11 online-school lessons.

> **October 2026: merged into the GCSE Plan app** (https://maxwilliamfoster-sys.github.io/gcse-plan/, repo `gcse-plan`). Its Today and Week tabs now run this timetable, with the live lessons, weekly focus, recipes and videos. This Pages site redirects there. This repo still holds the **video scraper** (`videos/`, which the app's build reads) and the **Anki deck builder** (`anki/`). `src/plan.html` is kept as the record of the old page.

**Old live page (now a redirect):** https://maxwilliamfoster-sys.github.io/gcse-study-plan/

| Subject | Board | Tier |
|---|---|---|
| Maths | Edexcel 1MA1 | Higher |
| Combined Science (Trilogy) | AQA 8464 | Higher |
| English Language | AQA 8700 | – |
| English Literature (R&J, Jekyll & Hyde, An Inspector Calls, Power and Conflict) | AQA 8702 | – |
| History (IR 1918–75 + USA 1919–48, Migration, Empire + Spitalfields) | OCR J410 | – |
| German | AQA 8662 | Higher |

## What's in it

- **Today:** every 45-minute period from 08:00 to 16:20, fitted around the live lessons, with what to do minute by minute, links, and specific YouTube videos that change week to week.
- **Week:** the full grid, plus why each subject gets the time it does.
- **Plan to May:** four phases. Learn everything (to 18 Dec) → exam technique (Jan–Mar) → past papers + German speaking (Apr–May) → exam mode.
- **Subject guides:** paper structure, what's given in the exam, tips, free resources, topic checklists.
- **Exam dates:** all 19 papers (AQA provisional and OCR final 2027 timetables).

## Anki deck — `anki/`

`anki/GCSE-2027.apkg` holds about 4,100 cards in **six subject decks** (German, History, Science, Maths, English Literature, English Language), each with its own daily limit: the full AQA 8662 vocab list, History dates, people and key events for every paper, all Trilogy topics and required practicals, maths formulae that aren't on the sheet, Literature quotes, and Language techniques.

Anything printed on the 2027 exam sheets (every Physics equation, the Edexcel formula sheet) is deliberately left out. New cards are ordered to match the plan week by week. To import on another device, double-click the `.apkg` file (or use File → Import).

To rebuild after editing `anki/cards/*.py`, you need the `anki` Python package at the same version as the desktop app:

```
node anki/export_app_data.js ../GCSE-Plan/src anki/app_data.json
python anki/build_deck.py --apkg anki/GCSE-2027.apkg
```

## Videos — `videos/`

`videos/queries.py` lists one to five searches per subject per week. `videos/find_videos.py` picks a specific video for each, preferring Cognito, Freesciencelessons, Corbettmaths, Mr Bruff and Mr Salles. It checks every pick is live, then writes `videos/videos.json`. Run `py build.py` to bake the videos into `index.html`.
