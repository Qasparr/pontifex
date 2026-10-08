# PONTIFEX API Reference — v0.3.0 "The Third Span"

Three doors into the same engine: the **Python API** (import it), the **CLI** (script it), the **HTTP API** (query it on loopback). All three speak the same result shape.

## The result shape

Every weighing returns a dict:

```json
{
  "word": "CELL",
  "system": "latin_ordinal",
  "value": 32,
  "provenance": "ATTESTED",
  "breakdown": [{"token": "C", "value": 3}, ...]
}
```

`breakdown` is the audit trail — TRVVTH requires that every number show its work. `provenance` is load-bearing: ATTESTED / DERIVED / CONSTRUCTED (see METHOD.md §1).

`bridge()` returns:

```json
{
  "a": { ...weighing... },
  "b": { ...weighing... },
  "convergent": true,
  "standing": "CANDIDATE BRIDGE (attested)"
}
```

---

## 1. Python API

```python
import pontifex

# Weigh a word in a system
pontifex.weigh('CELL', 'latin_ordinal')
pontifex.weigh('עז', 'hebrew')
pontifex.weigh('test', 'braille')          # CONSTRUCTED carrier

# Check a convergent point
pontifex.bridge('AXONEME', 'latin_ordinal', 'עז', 'hebrew')

# The music bridge — ABC notation or bare notes
pontifex.weigh_melody('C E G')
pontifex.weigh_melody('X:1\nT:Cooleys\nK:Edor\n|:E2BE B2EB|')

# Hebrew fallback with merger reporting
pontifex.weigh_via_hebrew_fallback('cell')
pontifex.transliterate_latin_to_hebrew('cell')   # -> ('קהלל', ['ה', 'ק'])

# Tables, systems, conventions
pontifex.SYSTEMS            # {'hebrew': {'provenance': 'ATTESTED'}, ...}
pontifex.HEBREW, pontifex.GREEK, pontifex.LATIN_ORDINAL,
pontifex.AGRIPPA, pontifex.ARABIC_ABJAD, pontifex.BRAILLE
pontifex.MUSIC_CONVENTIONS  # the stated extraction rules
pontifex.to_jsonable(result)  # normalize a result for JSON

# The instrument checks itself
pontifex.self_test()        # True when every established bridge reproduces
```

Systems: `hebrew`, `greek`, `latin_ordinal`, `agrippa`, `arabic_abjad`, `braille`, `abc_notes`.

---

## 2. CLI

Run with `python -m pontifex` from the repo root.

```bash
python -m pontifex weigh CELL latin_ordinal
python -m pontifex bridge AXONEME latin_ordinal עז hebrew
python -m pontifex fallback cell
python -m pontifex music "C E G"
python -m pontifex music "X:1\nT:Cooleys\nK:Edor\n|:E2BE B2EB|"
python -m pontifex systems
python -m pontifex selftest
python -m pontifex serve [--port 8077] [--host 127.0.0.1]
```

`--json` goes anywhere on the command line and switches output to machine-readable JSON:

```bash
python -m pontifex weigh CELL latin_ordinal --json
```

### Exit codes (a contract for scripts)

| Code | Meaning |
|------|---------|
| 0 | success — for `bridge`, the point **converged** |
| 1 | runtime error (unknown system, bad input) |
| 2 | usage error |
| 3 | success, but the `bridge` point **diverged** |

```bash
# A script that only cares whether the bridge held:
python -m pontifex bridge AXONEME latin_ordinal עז hebrew >/dev/null && echo "the bridge holds"
```

---

## 3. HTTP API

```bash
python -m pontifex serve --port 8077   # loopback only, by doctrine
```

**Doctrine: loopback only.** The server binds 127.0.0.1 (or localhost) and refuses any other host — the instrument serves its own machine, never the wire.

All endpoints are GET and return JSON in one shape: `{"ok": true, "data": ...}` or `{"ok": false, "error": ...}`.

| Endpoint | Query | Returns |
|----------|-------|---------|
| `/` | — | name, version, endpoint list |
| `/systems` | — | systems and their provenance |
| `/weigh` | `word`, `system` | the weighing |
| `/bridge` | `word1`, `system1`, `word2`, `system2` | the convergent-point check |
| `/fallback` | `word` | Hebrew-fallback weighing, mergers shown |
| `/music` | `tune` | the melody weighing |
| `/selftest` | — | every check, `all_pass` verdict |

```bash
curl "http://127.0.0.1:8077/weigh?word=CELL&system=latin_ordinal"
curl "http://127.0.0.1:8077/bridge?word1=AXONEME&system1=latin_ordinal&word2=עז&system2=hebrew"
```

---

Johnathan 'Qasparr' (Κασπάρρ) Monroe, Keeper of the Secret Treasure
All Rights Reserved, Without Prejudice.
"Live, Love, and let Love, Live." 93.
