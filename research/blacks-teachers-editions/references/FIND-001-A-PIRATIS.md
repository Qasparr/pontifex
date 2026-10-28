# FIND-001 — Two entries folded into a neighbour (found via the author's screenshot, 2026-10-28)

**Status: MARKED for the scan-verification audit (OZ Road brick 21). Not
repaired here — repairs ride the audit pass, with scan-page evidence, per
the standing rule. Nothing is silently altered.**

## The evidence
- The author's screenshot (filed beside this note) shows the entry:
  *A piratis aut latronibus capti liberi permanent. Persons taken by pirates
  or robbers remain free. Dig. 49, 15, 19, 2; Gro. de J. B. lib. 3, c. 3, § 1.*
- Our source text (djvu ll. 726–743) carries BOTH entries, OCR-garbled:
  - "A plratis ant latronibns oaptl liberi permanent…" (the screenshot's entry)
  - "A plratis et latronibns oapta domininm non mutant. Things taken or
    captured by pirates and robbers do not change their ownership. Bynk.
    bk. 1, c. 17; 1 Kent, Comm. 108, 184…"
- In the shipped parse (`entries.json`), neither has a headword: both were
  folded into the body of **A PAXATIO** (entry idx 14), because the garbled
  headword lines ("A plratis ant latronibns…") did not match the parser's
  headword pattern. Their text survives in the book, inside the wrong entry.

## The finding
The parse's 13,145 headwords undercount the book by at least two at this
locus. The class of error — headword lines too garbled to parse, entries
folded into neighbours — is exactly what brick 21 (scan-verification audit)
exists to census. This locus is its first documented specimen, found not by
the pipeline but by the author's own screenshot: the desk records the
provenance honestly.

## Disposition
MARKED, not repaired. At the audit pass: restore both headwords from the
page image, re-seat the folded text, and census the class book-wide.
