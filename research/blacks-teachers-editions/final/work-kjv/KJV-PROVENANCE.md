# KJV Provenance — sources used for the mechanical text-diff

Diff run: 2026-10-25 (Worker B, Black's Teacher's Edition final build).
Nothing in this folder was pushed to git.

## Primary source — DIFFED AGAINST

- **Project Gutenberg eBook #10, "The King James Version of the Bible"**
- File in this folder: `pg10.txt` (4.3 MB, CRLF line endings)
- Downloaded from: `https://www.gutenberg.org/cache/epub/10/pg10.txt`
- PG header data: Release date August 1, 1989 [eBook #10]; most
  recently updated October 29, 2024; Language: English.
- SHA-256: `0204adaed1f25700aa854218cae63c7172228c41088f335e99167a071eed83c0`
- The King James Version text is public domain. The file is stored
  verbatim as downloaded, including the Project Gutenberg license
  header/footer (the parser skips both).
- Parse validation: the verse index built from this file contains
  exactly **31,102 verses across 66 books**, and its key set
  {(book, chapter, verse)} is identical to the structured source
  below — zero missing, zero extra.

## Cross-check source — NOT diffed against; comparison only

- **thiagobodruk/bible, `json/en_kjv.json`** — a verse-indexed JSON
  transcription of the KJV (books in canonical order, chapters and
  verses as nested arrays).
- File in this folder: `kjv-structured-thiagobodruk.json` (4.1 MB)
- Downloaded from:
  `https://raw.githubusercontent.com/thiagobodruk/bible/master/json/en_kjv.json`
- SHA-256: `f627b3c24a617013a4514ab24b6dd1bb305b09af237994c018f74cb9c7e71f41`
- Also parses to exactly 31,102 verses / 66 books.

## Cross-check result (detail in `crosscheck-report.json`)

All **833 distinct cited verses** were compared between the two
sources (833 includes Deuteronomy 25:22 and 25:23, which exist in
NEITHER source — Deuteronomy 25 has 19 verses; see the GALLOWS
wrong-reference flag):

- **816 / 833 agree word-for-word** after normalization.
- 3 differ only in word division / hyphenation
  (1 Samuel 7:16 Beth-el; 2 Chronicles 25:24 Obed-edom;
  Genesis 27:19 firstborn / first born).
- 12 differ in text, of which **8 are æ-ligature-only**
  (structured prints Cæsar, Judæa, Alphæus, Zacchæus, Timæus,
  Bartimæus where PG spells Caesar, Judaea, Alphaeus, Zacchaeus,
  Timaeus, Bartimaeus): Luke 2:1; Luke 3:1; Luke 6:15; Luke 19:8;
  Mark 10:46; Mark 12:17; Matthew 22:21; John 19:12.
- 4 are genuine inter-edition reading/spelling differences:
  Acts 24:16 (PG "void **to** offence" vs structured "void **of**
  offence"), Leviticus 19:15 (PG "hon**or**" vs structured
  "hon**our**"), Proverbs 6:26 (PG "adul**tress**" vs structured
  "adulter**ess**"), Isaiah 62:6 (PG "ye that **make mention of**
  the LORD" vs structured's "remembrancers" reading).

Rule applied: the diff runs against PG #10. Where an annotation
matches the structured transcription but not PG #10 at a point where
the two KJV sources themselves disagree, the annotation is FLAGGED
as an edition variant — never "corrected" toward one printing over
the other. That rule produced 7 of the 10 flags.
