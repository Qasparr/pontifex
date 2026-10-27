# PONTIFEX tools

> "Let the log be the witness." — the scribe

Diagnostic and reporting instruments for the PONTIFEX work, collected under
one roof so no project confuses them with its own. Findings, never doctrine —
the red pen rules.

## The `ptk` package

The PONTIFEX toolkit: four instruments, one honest API.

| Module | Instrument | Example |
|---|---|---|
| `ptk.weigh` | Letter-number weighing (gematria) | `weigh.hebrew('עז')` → `77` |
| `ptk.cipher` | Classical substitution ciphers | `cipher.atbash_he('בבל')` → `'ששך'` |
| `ptk.table` | One table, three mouths (Markdown / CSV / PDF) | `Table(h, r).to_pdf(path)` |
| `ptk.chart` | Figures through one API (bar / line / spread) | `chart.spread(data, path)` |

Every module ships in the educational and thelemic format: meticulous
`MECHANISM` / `DOCTRINE` comments throughout, written to teach.

```python
from ptk import weigh, cipher, table, chart

weigh.calibrate()            # the anchorage — nothing unverified enters
weigh.selftest()             # the στ dual-readout checks (ruling 2026-10-27)
weigh.hebrew('עז')            # 77
weigh.greek_dual('σταυρος')  # {'ligature': 777, 'strict': 1271, ...} — both
                             # readings reported where στ fuses/diverges;
                             # see ptk/RULING-2026-10-27-SIGMA-TAU-DUAL-READOUT.md
weigh.breakdown('עז', weigh.HEBREW)   # show your work: [('ע', 70), ('ז', 7)]

cipher.atbash_he('בבל')       # 'ששך' — the biblical mirror
cipher.caesar('AXONEME', 3)   # shift is required, never default

t = table.Table(["concept", "value"], [["unity", "89"]])
t.save_markdown("t.md"); t.to_csv("t.csv"); t.to_pdf("t.pdf")

chart.bar(["unity", "war"], [89, 42], "bars.png", title="Two weighings")
```

**Doctrine.** `weigh.py` carries ATTESTED copies of the letter-number banks
(provenance: `pontifex/pontifex/tables.py`, synced 2026-10-11 — correct them
there, re-sync here, never edit silently). `cipher.py` ships only schemes
verified against sources; anything unverifiable raises instead of guessing.

## `scripts/`

Replayable diagnostic and reporting scripts from the research sprints,
organized by project:

- `scripts/twelve-tongues/` — the correspondence sweep: per-language weigh
  scripts, `build_correspondence.py`, `weigh_unity_war.py`, and the PDF
  builders (`build_report_pdf.py` renders any work-log Markdown).
- `scripts/crowley-race-question/` — `build_defense_brief_pdf.py`,
  `sweep-D-weigh.py`.

The research folders keep their working copies; this is the canonical home.

## `md2pdf.py`

The original Markdown→PDF builder (weasyprint-based) that started this
collection. Superseded for work logs by `scripts/twelve-tongues/build_report_pdf.py`
(fpdf2-based, handles tables); kept for provenance.

---
Live, Love, and let Love, Live. — 93.
All Rights Reserved, Without Prejudice.
