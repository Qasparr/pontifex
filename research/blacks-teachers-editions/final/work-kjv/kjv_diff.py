#!/usr/bin/env python3
"""
kjv_diff.py — Mechanical text-diff of the Black's Teacher's Edition
Phase 2 Scripture-well annotations against a public-domain KJV text.

MECHANISM
  1. Parse Project Gutenberg #10 (King James Bible) into a verse index
     {(book, chapter, verse): raw_text}. PG #10 carries verses as
     "C:V text" blocks, sometimes two verses on one physical line;
     a streaming marker scan handles both.
  2. Parse the structured thiagobodruk KJV JSON into the same index
     shape and CROSS-CHECK every cited verse between the two sources.
     The diff itself runs against PG #10; disagreements are logged.
  3. Parse each annotation citation ("[Book C:V-V, KJV]", ranges,
     verse lists "5:34, 37", discontinuous "5:34, 5:37", and
     multi-reference "Prov 11:1; Deut 25:13-15"). Unparseable
     citations are logged and flagged, never guessed.
  4. Extract the quoted span from the annotation `note`. Inspection
     of the full set showed notes are pure quotations (no appended
     commentary); the only admixtures are surrounding quotation
     marks, ' — '-joined quoted segments, and '...' omission marks.
     Extraction therefore splits the note into chunks at those marks
     and diffs chunk-by-chunk, in order, against the cited verses.
  5. Normalize both sides identically: backslash-apostrophe repair,
     curly->straight quotes, case-fold, punctuation stripped,
     whitespace collapsed. Spelling is NOT normalized — a spelling
     difference is a real difference and is classified, not erased.
  6. Classify: exact / partial / corrected / wrong-reference /
     flagged / excluded. Nothing is altered silently: every
     correction records old vs new; everything doubtful is flagged.

DOCTRINE
  Doubtful goes to flags, always. A deliberate partial quote is not
  an error. A wrong reference is flagged for the editor's pen, never
  silently re-cited. This script writes diff-results.json,
  corrections.json, flags.json and crosscheck-report.json into the
  work folder; it never modifies the annotations file.
"""

import difflib
import json
import re
import sys
from pathlib import Path

WORK = Path(__file__).resolve().parent
ANN_PATH = Path.home() / (
    "workspace/your_files/blacks-teachers-editions/well-phases/"
    "phase-2-scripture/scripture-well-annotations.json"
)
PG_PATH = WORK / "pg10.txt"
STRUCT_PATH = WORK / "kjv-structured-thiagobodruk.json"

CANONICAL_BOOKS = [
    "Genesis", "Exodus", "Leviticus", "Numbers", "Deuteronomy",
    "Joshua", "Judges", "Ruth", "1 Samuel", "2 Samuel",
    "1 Kings", "2 Kings", "1 Chronicles", "2 Chronicles", "Ezra",
    "Nehemiah", "Esther", "Job", "Psalms", "Proverbs",
    "Ecclesiastes", "Song of Solomon", "Isaiah", "Jeremiah",
    "Lamentations", "Ezekiel", "Daniel", "Hosea", "Joel", "Amos",
    "Obadiah", "Jonah", "Micah", "Nahum", "Habakkuk", "Zephaniah",
    "Haggai", "Zechariah", "Malachi", "Matthew", "Mark", "Luke",
    "John", "Acts", "Romans", "1 Corinthians", "2 Corinthians",
    "Galatians", "Ephesians", "Philippians", "Colossians",
    "1 Thessalonians", "2 Thessalonians", "1 Timothy", "2 Timothy",
    "Titus", "Philemon", "Hebrews", "James", "1 Peter", "2 Peter",
    "1 John", "2 John", "3 John", "Jude", "Revelation",
]

# Exact standalone header lines in the PG #10 body -> canonical name.
PG_HEADERS = {
    "The First Book of Moses: Called Genesis": "Genesis",
    "The Second Book of Moses: Called Exodus": "Exodus",
    "The Third Book of Moses: Called Leviticus": "Leviticus",
    "The Fourth Book of Moses: Called Numbers": "Numbers",
    "The Fifth Book of Moses: Called Deuteronomy": "Deuteronomy",
    "The Book of Joshua": "Joshua",
    "The Book of Judges": "Judges",
    "The Book of Ruth": "Ruth",
    "The First Book of Samuel": "1 Samuel",
    "The Second Book of Samuel": "2 Samuel",
    "The First Book of the Kings": "1 Kings",
    "The Second Book of the Kings": "2 Kings",
    "The First Book of the Chronicles": "1 Chronicles",
    "The Second Book of the Chronicles": "2 Chronicles",
    "Ezra": "Ezra",
    "The Book of Nehemiah": "Nehemiah",
    "The Book of Esther": "Esther",
    "The Book of Job": "Job",
    "The Book of Psalms": "Psalms",
    "The Proverbs": "Proverbs",
    "Ecclesiastes": "Ecclesiastes",
    "The Song of Solomon": "Song of Solomon",
    "The Book of the Prophet Isaiah": "Isaiah",
    "The Book of the Prophet Jeremiah": "Jeremiah",
    "The Lamentations of Jeremiah": "Lamentations",
    "The Book of the Prophet Ezekiel": "Ezekiel",
    "The Book of Daniel": "Daniel",
    "Hosea": "Hosea",
    "Joel": "Joel",
    "Amos": "Amos",
    "Obadiah": "Obadiah",
    "Jonah": "Jonah",
    "Micah": "Micah",
    "Nahum": "Nahum",
    "Habakkuk": "Habakkuk",
    "Zephaniah": "Zephaniah",
    "Haggai": "Haggai",
    "Zechariah": "Zechariah",
    "Malachi": "Malachi",
    "The Gospel According to Saint Matthew": "Matthew",
    "The Gospel According to Saint Mark": "Mark",
    "The Gospel According to Saint Luke": "Luke",
    "The Gospel According to Saint John": "John",
    "The Acts of the Apostles": "Acts",
    "The Epistle of Paul the Apostle to the Romans": "Romans",
    "The First Epistle of Paul the Apostle to the Corinthians":
        "1 Corinthians",
    "The Second Epistle of Paul the Apostle to the Corinthians":
        "2 Corinthians",
    "The Epistle of Paul the Apostle to the Galatians": "Galatians",
    "The Epistle of Paul the Apostle to the Ephesians": "Ephesians",
    "The Epistle of Paul the Apostle to the Philippians":
        "Philippians",
    "The Epistle of Paul the Apostle to the Colossians": "Colossians",
    "The First Epistle of Paul the Apostle to the Thessalonians":
        "1 Thessalonians",
    "The Second Epistle of Paul the Apostle to the Thessalonians":
        "2 Thessalonians",
    "The First Epistle of Paul the Apostle to Timothy": "1 Timothy",
    "The Second Epistle of Paul the Apostle to Timothy": "2 Timothy",
    "The Epistle of Paul the Apostle to Titus": "Titus",
    "The Epistle of Paul the Apostle to Philemon": "Philemon",
    "The Epistle of Paul the Apostle to the Hebrews": "Hebrews",
    "The General Epistle of James": "James",
    "The First Epistle General of Peter": "1 Peter",
    "The Second General Epistle of Peter": "2 Peter",
    "The First Epistle General of John": "1 John",
    "The Second Epistle General of John": "2 John",
    "The Third Epistle General of John": "3 John",
    "The General Epistle of Jude": "Jude",
    "The Revelation of Saint John the Divine": "Revelation",
}

BOOK_ALIASES = {b.lower(): b for b in CANONICAL_BOOKS}
BOOK_ALIASES.update({
    "psalm": "Psalms",
    "song of songs": "Song of Solomon",
    "canticles": "Song of Solomon",
    "revelations": "Revelation",
    "ecclesiasticus": None,  # apocryphal: not in KJV canon index use
})

VERSE_MARK = re.compile(r"(\d{1,3}):(\d{1,3})(?:\s+|$)")
WORD_RE = re.compile(r"[A-Za-z0-9]+(?:'[A-Za-z]+)?")


def normalize_text(s: str) -> str:
    """Full-string normalization -> single-spaced lowercase word stream."""
    return " ".join(norm_words(s))


def norm_words(s: str) -> list:
    """Normalize a string to a list of comparable word tokens.

    Repairs the literal backslash-apostrophe sequences found in some
    notes (e.g. Caesar\\'s), folds curly quotes to straight, lowercases,
    and tokenizes on word characters (internal apostrophes kept so
    'god's' stays one token on both sides).
    """
    s = s.replace("\\'", "'").replace("\\", " ")
    s = (s.replace("‘", "'").replace("’", "'")
           .replace("“", '"').replace("”", '"')
           .replace("…", "..."))
    return [w.lower() for w in WORD_RE.findall(s)]


def raw_tokens(raw: str):
    """Tokenize KJV raw text keeping char spans: [(norm_word, start, end)].
    Curly apostrophes/quotes are folded to straight first (single-char
    replacements, so spans stay valid) to match norm_words()."""
    raw = (raw.replace("’", "'").replace("‘", "'")
              .replace("“", '"').replace("”", '"'))
    out = []
    for m in re.finditer(r"\S+", raw):
        for w in WORD_RE.finditer(m.group(0)):
            out.append((w.group(0).lower(),
                        m.start() + w.start(), m.start() + w.end()))
    # NOTE: punctuation attached to a token (e.g. 'evil.') — WORD_RE
    # finds the word core inside the \S+ run; span covers the word core
    # only. Span reconstruction expands to neighbouring punctuation
    # separately in raw_span().
    return out


def parse_pg10(path: Path) -> dict:
    text = path.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()
    # Body starts at the SECOND occurrence of the OT title line
    # (the first is the table of contents).
    title = "The Old Testament of the King James Version of the Bible"
    occ = [i for i, ln in enumerate(lines) if ln.strip() == title]
    start = occ[1] if len(occ) > 1 else 0
    index = {}
    book = None
    cur_key = None
    cur_parts = []
    verses_in_book = 0  # verses started since current book header

    def flush():
        if cur_key is not None:
            index[cur_key] = " ".join(" ".join(cur_parts).split())

    for ln in lines[start:]:
        stripped = ln.strip()
        if stripped in PG_HEADERS:
            # PG #10 prints alternate titles as a second header block
            # before any verse ('The First Book of Samuel / Otherwise
            # Called: / The First Book of the Kings'). A header seen
            # while the current book still has no verses is such an
            # alternate title, not a new book — keep the first name.
            if book is not None and verses_in_book == 0:
                continue
            flush()
            cur_key, cur_parts = None, []
            book = PG_HEADERS[stripped]
            verses_in_book = 0
            continue
        if book is None:
            continue
        if stripped.startswith("*** END OF THE PROJECT GUTENBERG"):
            break
        # Scan the line for verse markers; text before the first
        # marker continues the current verse.
        pos = 0
        for m in VERSE_MARK.finditer(ln):
            seg = ln[pos:m.start()].strip()
            if seg and cur_key is not None:
                cur_parts.append(seg)
            flush()
            cur_key = (book, int(m.group(1)), int(m.group(2)))
            cur_parts = []
            verses_in_book += 1
            pos = m.end()
        tail = ln[pos:].strip()
        if tail and cur_key is not None:
            cur_parts.append(tail)
    flush()
    return index


def parse_structured(path: Path) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    index = {}
    assert len(data) == 66, f"expected 66 books, got {len(data)}"
    for pos, bookobj in enumerate(data):
        canon = CANONICAL_BOOKS[pos]
        for ch_i, chapter in enumerate(bookobj["chapters"], start=1):
            for v_i, verse in enumerate(chapter, start=1):
                index[(canon, ch_i, v_i)] = " ".join(verse.split())
    names = [b["name"] for b in data]
    return index, names


# ---------------------------------------------------------------------
# Citation parsing
# ---------------------------------------------------------------------
# Grammar handled:
#   Book C:V            Book C:V-V          Book C:V, V  (verse list)
#   Book C:V, C:V       (discontinuous, same book)
#   Book C:V, C:V-V     Ref; Ref            (multi-reference)
# A bare "V" item inherits chapter; a bare "C:V" item inherits book.

def _parse_refspec(spec: str, book, chapter):
    """Parse one reference like 'Deuteronomy 25:13-15' or '37' or '5:37'.
    Returns (book, chapter, [verses]) or None."""
    spec = spec.strip()
    m = re.match(r"^(.+?)\s+(\d+):(\d+)(?:\s*-\s*(\d+))?$", spec)
    if m:
        b = BOOK_ALIASES.get(m.group(1).strip().lower())
        if b is None:
            return None
        ch, v1 = int(m.group(2)), int(m.group(3))
        v2 = int(m.group(4)) if m.group(4) else v1
        return (b, ch, list(range(v1, v2 + 1)))
    m = re.match(r"^(\d+):(\d+)(?:\s*-\s*(\d+))?$", spec)
    if m and book:
        ch, v1 = int(m.group(1)), int(m.group(2))
        v2 = int(m.group(3)) if m.group(3) else v1
        return (book, ch, list(range(v1, v2 + 1)))
    m = re.match(r"^(\d+)$", spec)
    if m and book and chapter:
        return (book, chapter, [int(m.group(1))])
    return None


def parse_citation(citation: str):
    """-> (refs, error). refs = [(book, ch, [verses]), ...] in order."""
    s = citation.strip()
    if s.startswith("["):
        s = s[1:]
    if s.endswith("]"):
        s = s[:-1]
    s = re.sub(r",\s*KJV\s*$", "", s).strip()
    refs = []
    book = chapter = None
    for part in re.split(r";", s):
        # A part may itself carry a fresh book ('Deuteronomy 25:13-15')
        # or be a continuation list (' 37', ' 5:37').
        first = True
        for item in part.split(","):
            item = item.strip()
            if not item:
                continue
            if first and re.match(r"^[A-Za-z0-9 ]+?\s+\d+:", item):
                parsed = _parse_refspec(item, None, None)
            elif first and book and re.match(r"^\d", item):
                parsed = _parse_refspec(item, book, chapter)
            else:
                parsed = _parse_refspec(item, book, chapter)
            if parsed is None:
                return None, f"unparseable citation component: {item!r}"
            # Merge consecutive same book+chapter verse lists.
            if refs and refs[-1][0] == parsed[0] and refs[-1][1] == parsed[1]:
                refs[-1][2].extend(parsed[2])
            else:
                refs.append([parsed[0], parsed[1], list(parsed[2])])
            book, chapter = parsed[0], parsed[1]
            first = False
    if not refs:
        return None, "no references parsed"
    return [(b, c, vs) for b, c, vs in refs], None


def expand_refs(refs):
    return [(b, c, v) for b, c, vs in refs for v in vs]


def ref_label(refs):
    parts = []
    for b, c, vs in refs:
        if len(vs) == 1:
            parts.append(f"{b} {c}:{vs[0]}")
        elif vs == list(range(vs[0], vs[-1] + 1)):
            parts.append(f"{b} {c}:{vs[0]}-{vs[-1]}")
        else:
            parts.append(f"{b} {c}:" + ",".join(str(v) for v in vs))
    return "; ".join(parts)


# ---------------------------------------------------------------------
# Note chunk extraction
# ---------------------------------------------------------------------
# A note is split into chunks at '...' / '…' omission marks and at
# '" — "' segment joins. Surrounding quotation marks are recorded
# (for correction re-wrapping) and stripped from the word stream.

def split_chunks(note: str):
    s = note.replace("\\'", "'")
    s = s.replace("…", "...")
    # Segment joins: closing quote, em/en dash, opening quote.
    s = re.sub(r'"\s*[—–-]\s*"', "\x00", s)
    chunks_raw = []
    for piece in s.split("\x00"):
        for sub in piece.split("..."):
            chunks_raw.append(sub)
    chunks = []
    for c in chunks_raw:
        words = norm_words(c)
        if words:
            chunks.append(words)
    return chunks


def note_wrapping(note: str):
    s = note.strip()
    if len(s) >= 2 and s[0] == '"' and s[-1] == '"':
        return ('"', '"')
    if len(s) >= 2 and s[0] == "'" and s[-1] == "'":
        return ("'", "'")
    return ("", "")


def find_subseq(hay, needle, start=0):
    """First index >= start where needle occurs contiguously, else -1."""
    if not needle:
        return start
    n, h = len(needle), len(hay)
    for i in range(start, h - n + 1):
        if hay[i:i + n] == needle:
            return i
    return -1


def match_chunks(expected_words, chunks):
    """Match chunks in order as contiguous subsequences of expected.
    Returns (spans, skipped) or None. skipped = expected words not
    covered by any chunk (the omissions)."""
    spans = []
    pos = 0
    for ch in chunks:
        i = find_subseq(expected_words, ch, pos)
        if i < 0:
            return None
        spans.append((i, i + len(ch)))
        pos = i + len(ch)
    covered = sum(e - s for s, e in spans)
    return spans, len(expected_words) - covered


# ---------------------------------------------------------------------
# Spelling / edition variants: a difference made ONLY of these pairs
# is flagged as an edition/spelling variant, never auto-corrected.
# ---------------------------------------------------------------------
VARIANT_PAIRS = {
    frozenset(p) for p in [
        ("judgment", "judgement"),
        ("throughly", "thoroughly"),
        ("enquire", "inquire"),
        ("enquires", "inquires"),
        ("fulfil", "fulfill"),
        ("shew", "show"),
        ("shewed", "showed"),
        ("shewing", "showing"),
        ("spake", "spoke"),
        ("hath", "has"),  # never expected; listed so it FLAGS not fixes
        ("doth", "does"),
        ("saith", "says"),
        ("unto", "to"),
        ("amongst", "among"),
        ("whilst", "while"),
        ("towards", "toward"),
        ("besides", "beside"),
        ("anywise", "any wise"),
        ("meanwhile", "mean while"),
        ("nevertheless", "never the less"),
    ]
}


def opcode_word_diffs(note_words, exp_words):
    sm = difflib.SequenceMatcher(a=note_words, b=exp_words,
                                 autojunk=False)
    diffs = []
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag != "equal":
            diffs.append((tag, note_words[i1:i2], exp_words[j1:j2]))
    return sm, diffs


def only_variant_diffs(diffs):
    if not diffs:
        return False
    for tag, a, b in diffs:
        if tag != "replace" or len(a) != len(b):
            return False
        for x, y in zip(a, b):
            if frozenset((x, y)) not in VARIANT_PAIRS:
                return False
    return True


def raw_span(raw: str, words_norm: list, a: int, b: int) -> str:
    """Raw KJV substring covering normalized words [a, b)."""
    toks = raw_tokens(raw)
    assert len(toks) == len(words_norm), (len(toks), len(words_norm))
    if a == 0 and b == len(toks):
        return raw
    start = toks[a][1]
    end = toks[b - 1][2]
    while end < len(raw) and raw[end] in ".,;:!?)":
        end += 1
    return raw[start:end]


def build_corrected_note(note, note_words, exp_words, exp_raw):
    """Rebuild the note with the KJV wording restored for the quoted
    span; original surrounding quotation marks are preserved. The
    span is bounded by the note's own alignment: expected-only words
    skipped at the edges (a deliberate partial quote's boundaries)
    are NOT pulled into the corrected text."""
    sm = difflib.SequenceMatcher(a=note_words, b=exp_words,
                                 autojunk=False)
    ops = sm.get_opcodes()
    first, last = ops[0], ops[-1]
    # Opcode axes: a = note, b = KJV. 'insert' = KJV words the note
    # skipped; 'delete' = note words with no KJV counterpart.
    start_exp = first[4] if first[0] == "insert" else first[3]
    end_exp = last[3] if last[0] == "insert" else last[4]
    core = raw_span(exp_raw, exp_words, start_exp, end_exp)
    # PG #10 mixes curly and straight apostrophes by verse; the
    # annotations uniformly use straight apostrophes (verified:
    # zero curly characters in all 1,621 notes), so corrected text
    # is folded to the book's own typography.
    core = (core.replace("’", "'").replace("‘", "'")
                .replace("“", '"').replace("”", '"'))
    pre, post = note_wrapping(note)
    return f"{pre}{core}{post}"


# ---------------------------------------------------------------------
# Alternative-verse search (wrong-reference detection)
# ---------------------------------------------------------------------
class AltSearch:
    def __init__(self, pg_index):
        self.index = pg_index
        self.norm = {k: norm_words(v) for k, v in pg_index.items()}
        self.word_to_verses = {}
        for k, ws in self.norm.items():
            for w in set(ws):
                self.word_to_verses.setdefault(w, []).append(k)

    def best_alternatives(self, note_words, cited_keys, topn=3):
        if not note_words:
            return []
        rarity = sorted(set(note_words),
                        key=lambda w: len(self.word_to_verses.get(w, [])))
        cand = {}
        for w in rarity[:4]:
            for k in self.word_to_verses.get(w, []):
                cand[k] = cand.get(k, 0) + 1
        scored = []
        cited_set = set(cited_keys)
        ranked = sorted(cand.items(), key=lambda kv: -kv[1])[:300]
        for k, overlap in ranked:
            if k in cited_set:
                continue
            exp = self.norm[k]
            joined = " ".join(exp)
            if " ".join(note_words) in joined:
                scored.append((2.0, k, "exact-containment"))
                continue
            r = difflib.SequenceMatcher(
                a=note_words, b=exp, autojunk=False).ratio()
            if r >= 0.80:
                scored.append((r, k, "fuzzy"))
        scored.sort(key=lambda t: -t[0])
        return scored[:topn]


def classify(key, idx, ann, pg_index, altsearch, struct_index=None):
    note = ann.get("note", "")
    citation = ann.get("citation", "")
    out = {"class": None, "ref": citation, "detail": ""}

    # Excluded: anything not citing the KJV.
    if "KJV" not in citation:
        out["class"] = "excluded"
        out["detail"] = ("Non-KJV citation (other translation); "
                          "not diffed against KJV.")
        return out, None, None

    refs, err = parse_citation(citation)
    if err:
        out["class"] = "flagged"
        out["detail"] = f"Citation parse failure: {err}"
        return out, None, out

    verse_keys = expand_refs(refs)
    missing = [k for k in verse_keys if k not in pg_index]
    if missing:
        # The cited verse does not exist (e.g. a chapter cited past
        # its end). Scan single verses and verse-pairs for where the
        # quotation actually lives; a strong match elsewhere makes
        # this a wrong-reference flag, never a silent re-citation.
        chunks0 = split_chunks(note)
        nw0 = [w for c in chunks0 for w in c]
        best = None
        keys_sorted = sorted(pg_index.keys(),
                             key=lambda k: (CANONICAL_BOOKS.index(k[0]),
                                            k[1], k[2]))
        for pos, k in enumerate(keys_sorted):
            cand_keys = [k]
            if pos + 1 < len(keys_sorted) and \
                    keys_sorted[pos + 1][0] == k[0] and \
                    keys_sorted[pos + 1][1] == k[1]:
                cand_keys = [k, keys_sorted[pos + 1]]
            for ck in (cand_keys[:1], cand_keys):
                cw = norm_words(" ".join(pg_index[x] for x in ck))
                if len(nw0) >= 4 and nw0[:4] not in (
                        [cw[i:i + 4] for i in range(len(cw) - 3)]):
                    # cheap prefilter: first 4 note words must occur
                    if " ".join(nw0[:4]) not in " ".join(cw):
                        continue
                if match_chunks(cw, chunks0) is not None:
                    best = ck
                    break
            if best:
                break
        if best:
            label = "; ".join(f"{b} {c}:{v}" for b, c, v in best)
            out["class"] = "wrong-reference"
            out["detail"] = (
                f"Cited verse(s) do not exist in the KJV: {missing} "
                f"(chapter cited past its end). The quotation matches "
                f"{label} exactly/as a clean partial. Citation NOT "
                f"changed — editor's pen.")
            out["alt_match"] = label
        else:
            out["class"] = "flagged"
            out["detail"] = (f"Cited verse(s) absent from KJV index: "
                              f"{missing}; no matching verse found.")
        return out, None, out

    exp_raw = " ".join(pg_index[k] for k in verse_keys)
    exp_words = norm_words(exp_raw)
    chunks = split_chunks(note)
    note_words = [w for c in chunks for w in c]

    matched = match_chunks(exp_words, chunks)
    if matched is not None:
        spans, skipped = matched
        if skipped == 0 and len(note_words) == len(exp_words):
            out["class"] = "exact"
            out["detail"] = "Word-for-word match after normalization."
        else:
            out["class"] = "partial"
            out["detail"] = (
                f"Clean in-order subsequence of cited verse(s); "
                f"covers {len(note_words)} of {len(exp_words)} words "
                f"(spans {spans}). Deliberate partial quote; no error.")
        return out, None, None

    # Mismatch path: measure, check edition variants, look
    # elsewhere, then decide.
    sm, diffs = opcode_word_diffs(note_words, exp_words)
    ratio = sm.ratio()
    out["ratio"] = round(ratio, 4)
    out["word_diffs"] = [
        {"op": t, "note": a, "kjv": b} for t, a, b in diffs]

    # Edition-variant guard 1: the note may match the OTHER KJV
    # transcription (structured) for the same verses exactly or as a
    # clean partial, while the two KJV sources themselves differ.
    # That is an edition variant, not a transcription error.
    if struct_index is not None:
        s_raw = " ".join(struct_index[k] for k in verse_keys)
        if normalize_text(s_raw) != normalize_text(exp_raw):
            s_words = norm_words(s_raw)
            if match_chunks(s_words, chunks) is not None:
                out["class"] = "flagged"
                out["detail"] = (
                    "Edition variant: note matches the structured "
                    "KJV transcription (thiagobodruk en_kjv) for the "
                    "cited verse(s) but differs from Project "
                    "Gutenberg #10. PG: " + exp_raw[:200] +
                    " || Structured: " + s_raw[:200])
                return out, None, out

    # Edition-variant guard 2: identical letter stream, different
    # word division / hyphenation (e.g. 'firstborn' vs 'first born',
    # 'Tubal-cain' vs 'Tubalcain').
    note_chars = "".join(note_words)
    exp_chars = "".join(exp_words)
    if note_chars == exp_chars or note_chars in exp_chars:
        out["class"] = "flagged"
        out["detail"] = (
            "Word-division/hyphenation variant only: letter stream "
            "identical to KJV, tokenization differs. Diffs: "
            + "; ".join(f"{t} note={a} kjv={b}" for t, a, b in diffs))
        return out, None, out

    alts = altsearch.best_alternatives(note_words, verse_keys)
    if alts:
        best_r, best_k, kind = alts[0]
        alt_norm = normalize_text(pg_index[best_k])
        if alt_norm != normalize_text(exp_raw) and (
                kind == "exact-containment" or best_r >= 0.97) \
                and best_r > ratio + 0.03:
            out["class"] = "wrong-reference"
            out["detail"] = (
                f"Note matches {best_k[0]} {best_k[1]}:{best_k[2]} "
                f"({kind}, score {best_r:.3f}) better than cited "
                f"{ref_label(refs)} (ratio {ratio:.3f}). Citation "
                f"NOT changed — editor's pen.")
            out["alt_match"] = f"{best_k[0]} {best_k[1]}:{best_k[2]}"
            return out, None, out

    if only_variant_diffs(diffs):
        out["class"] = "flagged"
        out["detail"] = ("Difference consists solely of spelling/"
                           "edition variants: "
                           + "; ".join(f"{a}->{b}" for _, a, b in diffs))
        return out, None, out

    if len(chunks) == 1:
        # Boundary discipline (opcodes: a=note, b=KJV; 'insert' =
        # KJV words the note skipped, 'delete' = note-only words,
        # 'replace' = substitution). A correction may restore KJV
        # wording INSIDE the quoted span; it may not move the span's
        # boundaries, delete words quoted from a neighbouring verse,
        # or silently restore an unmarked omission. Those are
        # flagged for the editor's pen.
        ops = sm.get_opcodes()
        diff_ops = [o for o in ops if o[0] != "equal"]
        sub_ops = [o for o in diff_ops if o[0] in ("replace", "delete")]
        if sub_ops:
            fi = ops.index(sub_ops[0])
            li = ops.index(sub_ops[-1])
            lead_skip = sum(o[4] - o[3] for o in ops[:fi]
                            if o[0] == "insert")
            tail_skip = sum(o[4] - o[3] for o in ops[li + 1:]
                            if o[0] == "insert")
        else:
            lead_skip = tail_skip = 0
        partial = lead_skip > 0 or tail_skip > 0
        matched = sum(b.size for b in sm.get_matching_blocks())
        span_exp_len = len(exp_words) - lead_skip - tail_skip
        span_ratio = (2.0 * matched /
                      max(1, len(note_words) + span_exp_len))
        out["span_ratio"] = round(span_ratio, 4)

        def _adjacent(kkey, delta):
            b, c, v = kkey
            if (b, c, v + delta) in pg_index:
                return (b, c, v + delta)
            if delta > 0 and (b, c + 1, 1) in pg_index:
                return (b, c + 1, 1)
            if delta < 0:
                prevs = [k for k in pg_index
                         if k[0] == b and k[1] == c - 1]
                if prevs:
                    return max(prevs, key=lambda k: k[2])
            return None

        overrun = None
        if ops and ops[-1][0] == "delete" and verse_keys:
            words = note_words[ops[-1][1]:ops[-1][2]]
            nk = _adjacent(verse_keys[-1], +1)
            if words and nk and \
                    words == norm_words(pg_index[nk])[:len(words)]:
                overrun = (f"note continues verbatim into "
                           f"{nk[0]} {nk[1]}:{nk[2]}, beyond the "
                           f"cited range")
        if ops and ops[0][0] == "delete" and verse_keys:
            words = note_words[ops[0][1]:ops[0][2]]
            pk = _adjacent(verse_keys[0], -1)
            if words and pk and \
                    words == norm_words(pg_index[pk])[-len(words):]:
                overrun = (f"note begins with the closing words of "
                           f"{pk[0]} {pk[1]}:{pk[2]}, before the "
                           f"cited range")
        if overrun:
            out["class"] = "flagged"
            out["detail"] = (f"Quote overruns cited range: {overrun}. "
                              f"Trim the quote or extend the citation "
                              f"— editor's pen; not auto-corrected.")
            return out, None, out

        if not sub_ops:
            omitted = sum(o[4] - o[3] for o in diff_ops)
            if omitted <= 2:
                # A one-or-two-word interior omission in an
                # otherwise complete quotation is a transcription
                # slip (dropped article), not an abridgement:
                # correct it like any other interior error.
                new_note = build_corrected_note(
                    note, note_words, exp_words, exp_raw)
                core_words = norm_words(new_note)
                if find_subseq(exp_words, core_words) >= 0 and \
                        core_words != note_words:
                    out["class"] = "corrected"
                    out["detail"] = (
                        f"Transcription omission vs KJV (span "
                        f"similarity {span_ratio:.3f}): omitted "
                        + "; ".join(f"{b}" for _, a, b in diffs)
                        + " restored.")
                    corr = {"key": key, "idx": idx, "ref": citation,
                            "old_note": note, "new_note": new_note}
                    return out, corr, None
            out["class"] = "flagged"
            out["detail"] = (
                "Unmarked omission: note is the cited text minus "
                "interior KJV word(s), with no omission mark. "
                "Omitted: "
                + "; ".join(f"{b}" for _, a, b in diffs)
                + ". Restore or mark the omission — editor's pen.")
            return out, None, out

        if span_ratio < 0.80:
            out["class"] = "flagged"
            out["detail"] = (
                f"Low similarity to cited verse(s) within the "
                f"quoted span ({span_ratio:.3f}) and no better-"
                f"matching verse found. Diffs: "
                + "; ".join(f"{t} note={a} kjv={b}"
                            for t, a, b in diffs[:6]))
            return out, None, out

        if partial and any(o is ops[0] or o is ops[-1]
                           for o in sub_ops):
            out["class"] = "flagged"
            out["detail"] = (
                "Partial quote with a discrepancy at its boundary "
                "(first/last quoted word differs from KJV at the "
                "span edge); not auto-corrected. Diffs: "
                + "; ".join(f"{t} note={a} kjv={b}"
                            for t, a, b in diffs))
            return out, None, out

        new_note = build_corrected_note(note, note_words,
                                        exp_words, exp_raw)
        core_words = norm_words(new_note)
        if find_subseq(exp_words, core_words) < 0 or \
                core_words == note_words:
            out["class"] = "flagged"
            out["detail"] = ("Correction reconstruction failed "
                              "verification; flagged for manual review.")
            return out, None, out
        out["class"] = "corrected"
        out["detail"] = (f"Transcription error(s) vs KJV "
                          f"(span similarity {span_ratio:.3f}): "
                          + "; ".join(
                              f"{t} note={a} kjv={b}"
                              for t, a, b in diffs))
        corr = {"key": key, "idx": idx, "ref": citation,
                "old_note": note, "new_note": new_note}
        return out, corr, None

    if ratio >= 0.80 and len(chunks) > 1:
        out["class"] = "flagged"
        out["detail"] = (f"Multi-segment note with mismatch vs KJV "
                          f"(similarity {ratio:.3f}); not auto-"
                          f"corrected. Diffs: "
                          + "; ".join(f"{t} note={a} kjv={b}"
                                      for t, a, b in diffs))
        return out, None, out

    out["class"] = "flagged"
    out["detail"] = (f"Low similarity to cited verse(s) "
                      f"({ratio:.3f}) and no better-matching verse "
                      f"found. Diffs: "
                      + "; ".join(f"{t} note={a} kjv={b}"
                                  for t, a, b in diffs[:6]))
    return out, None, out


# ---------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------
def main():
    pg_index = parse_pg10(PG_PATH)
    struct_index, struct_names = parse_structured(STRUCT_PATH)
    print(f"PG #10 index: {len(pg_index)} verses, "
          f"{len(set(k[0] for k in pg_index))} books")
    print(f"Structured index: {len(struct_index)} verses")
    print(f"Structured book names (first/last): "
          f"{struct_names[0]} / {struct_names[-1]}")

    ann = json.loads(ANN_PATH.read_text(encoding="utf-8"))
    total = sum(len(v) for v in ann.values())
    print(f"Annotations: {len(ann)} keys, {total} annotations")

    # Cross-check: every DISTINCT cited verse, PG vs structured.
    cited = set()
    for v in ann.values():
        for a in v:
            if "KJV" not in a.get("citation", ""):
                continue
            refs, err = parse_citation(a["citation"])
            if refs:
                cited.update(expand_refs(refs))
    agree, disagreements = 0, []
    blind_agree = 0
    for k in sorted(cited):
        p, s = pg_index.get(k), struct_index.get(k)
        if p is None or s is None:
            disagreements.append(
                {"verse": f"{k[0]} {k[1]}:{k[2]}",
                 "pg": p, "structured": s,
                 "kind": "missing-in-one-source"})
        elif normalize_text(p) == normalize_text(s):
            agree += 1
            blind_agree += 1
        elif "".join(norm_words(p)) == "".join(norm_words(s)):
            blind_agree += 1
            disagreements.append(
                {"verse": f"{k[0]} {k[1]}:{k[2]}",
                 "pg": p, "structured": s,
                 "kind": "word-division-or-hyphenation-only"})
        else:
            disagreements.append(
                {"verse": f"{k[0]} {k[1]}:{k[2]}",
                 "pg": p, "structured": s, "kind": "text-differs"})
    cross = {
        "diffed_against": "Project Gutenberg #10 (pg10.txt)",
        "crosscheck_against": "thiagobodruk/bible en_kjv.json",
        "distinct_cited_verses_compared": len(cited),
        "agreements": agree,
        "agreements_letterstream_blind": blind_agree,
        "disagreements": disagreements,
    }
    (WORK / "crosscheck-report.json").write_text(
        json.dumps(cross, indent=1, ensure_ascii=False),
        encoding="utf-8")
    print(f"Cross-check: {agree}/{len(cited)} cited verses agree; "
          f"{len(disagreements)} disagreements (see report)")

    altsearch = AltSearch(pg_index)
    results, corrections, flags = {}, [], []
    counts = {}
    for key, anns in ann.items():
        for idx, a in enumerate(anns):
            out, corr, flag = classify(key, idx, a, pg_index, altsearch,
                                       struct_index)
            results[f"{key}#{idx}"] = out
            counts[out["class"]] = counts.get(out["class"], 0) + 1
            if corr:
                corrections.append(corr)
            if out["class"] in ("wrong-reference", "flagged"):
                flags.append({"key": key, "idx": idx,
                              "ref": a.get("citation", ""),
                              "reason": out["detail"],
                              "note": a.get("note", "")})
    print("Counts:", counts, "sum:", sum(counts.values()))
    assert sum(counts.values()) == total == 1621, (
        sum(counts.values()), total)

    (WORK / "diff-results.json").write_text(
        json.dumps({"counts": counts, "results": results},
                   indent=1, ensure_ascii=False), encoding="utf-8")
    (WORK / "corrections.json").write_text(
        json.dumps(corrections, indent=1, ensure_ascii=False),
        encoding="utf-8")
    (WORK / "flags.json").write_text(
        json.dumps(flags, indent=1, ensure_ascii=False),
        encoding="utf-8")
    print(f"Wrote diff-results.json ({len(results)}), "
          f"corrections.json ({len(corrections)}), "
          f"flags.json ({len(flags)})")


if __name__ == "__main__":
    sys.exit(main())
