# MARKER CENSUS — Scan-Limitation Markers, Black's 2e Teacher's Edition (final build)

Worker C, 2026-10-25. Detector: `detect_scan_markers.py` (this folder). Data: `entries.json` (13,145 entries), detection on the CLEANED body (Cleaner R1–R4 replicated from `vol-1/build_vol1_layered.py`). Markers keyed by entry index in `markers.json`. MARK ONLY — nothing in this census repairs, completes, or corrects any text.

## Totals

- Total entries scanned: 13,145
- Rule hits (before dedupe): 778
- Merged markers (after dedupe, per entry+anchor): 775
- Distinct marked entries: 772
- Strong markers: 132 (entries with ≥1 strong marker: 132)
- Candidate markers: 643 (candidate-only entries: 640)

## Count per rule (hits before dedupe / distinct entries)

| Rule | Strength | Hits | Entries |
|---|---|---|---|
| S1 — Empty body | strong | 23 | 23 |
| S2 — Body-final hyphen | strong | 49 | 49 |
| S3 — Body-final comma | strong | 49 | 49 |
| S4 — Named/garbage artifacts (JU8TITIA + clusters) | strong | 4 | 4 |
| S5 — Audit FLAG entries | strong | 8 | 8 |
| C1 — No terminal punctuation | candidate | 601 | 601 |
| C2 — Audit OPEN-SCAN sample entries | candidate | 44 | 44 |

## Dedupe merges (same entry + same anchor, multiple rules)

- idx 3555 DECRETAE ORDER — anchor END — rules S2+S5 (strong)
- idx 5160 FIGTIO — anchor END — rules C1+S5 (merged strength: strong)
- idx 5386 FORLER-LARD — anchor END — rules C1+S5 (merged strength: strong)

## C1 accounting

- Bodies with no terminal punctuation (naive, after trailing quote/bracket strip): 845 = 98 already strong via S2/S3 + 601 C1 candidates + 146 excluded by the authority-tail pattern (final token a single capitalized word ≤14 chars immediately preceded by '. ' or standing alone as a short citation tail — e.g. '… Abbott', '… Blount', '… CowelL'; Black's authorially ends entries with authority names).
- C1 kept subclasses (all kept as candidates, logged as ambiguous where uncertain):
  - capitalized-final-word-not-excluded: 130
  - ends-lowercase-word: 295
  - ends-semicolon-or-colon: 14
  - ends-with-digit-citation-tail: 47
  - other: 115

## Short bodies (not marked)

- Bodies of 1–3 tokens: 274. Unmarked: 255, of which 247 end with terminal punctuation. Shortness alone is NOT a rule: one-line definitions and see-references ('Formerly; heretofore.', 'See Indorsement.') are complete authorial entries.

## S5 mapping log (ledger FLAG → entries.json index, exact headword match)

- FLAG entry 'BREAKING' (XREF-SEE: target not in headword set) -> index 1581, anchor 'See Arbebtment.'
- FLAG entry 'DECRETAE ORDER' (BODY: body ends without terminal punctuation: possible truncation/merge) -> index 3555, anchor 'END'
- FLAG entry 'FIGTIO' (BODY: body ends without terminal punctuation: possible truncation/merge) -> index 5160, anchor 'END'
- FLAG entry 'FORLER-LARD' (BODY: body ends without terminal punctuation: possible truncation/merge) -> index 5386, anchor 'END'
- FLAG entry 'HOMESOKEN, HOMSOKEN' (XREF-SEE: target not in headword set) -> index 6188, anchor 'Haicesokbn.'
- FLAG entry 'IN PR2EMISSOREM FIDEM' (HEADWORD: digit in headword: suspected OCR letter-confusion) -> index 6590, anchor 'HEADWORD'
- FLAG entry 'YEAR' (XREF-SEE: target not in headword set) -> index 13122, anchor 'See Estate foe Years.'
- FLAG entry 'ZEMINDAR' (BODY: body ends without terminal punctuation: possible truncation/merge) -> index 13139, anchor 'END'

## C2 mapping log (52 sampled headwords → index)

- sampled headword 'ADS' -> index 407: C2 candidate added
- sampled headword 'ANTICHRESIS' -> index 820: C2 candidate added
- sampled headword 'BETTER EQUITY' -> index 1403: C2 candidate added
- sampled headword 'BREAKING' -> index 1581: already strong via S5, C2 not added
- sampled headword 'CLAUSUM' -> index 2226: C2 candidate added
- sampled headword 'CONSUETUDO' -> index 2717: C2 candidate added
- sampled headword 'DECRETAE ORDER' -> index 3555: already strong via S5, C2 not added
- sampled headword 'D IS AFFIRM' -> index 3899: C2 candidate added
- sampled headword 'ENJOYMENT' -> index 4469: C2 candidate added
- sampled headword 'EX CONTRACTU' -> index 4704: C2 candidate added
- sampled headword 'FIGTIO' -> index 5160: already strong via S5, C2 not added
- sampled headword 'FORLER-LARD' -> index 5386: already strong via S5, C2 not added
- sampled headword 'GELD' -> index 5664: C2 candidate added
- sampled headword 'GRADES FARENTELS' -> index 5774: C2 candidate added
- sampled headword 'HEPA' -> index 6035: C2 candidate added
- sampled headword 'HOMESOKEN, HOMSOKEN' -> index 6188: already strong via S5, C2 not added
- sampled headword 'IN PR2EMISSOREM FIDEM' -> index 6590: already strong via S5, C2 not added
- sampled headword 'INN' -> index 6841: C2 candidate added
- sampled headword 'JUDICATIO' -> index 7153: C2 candidate added
- sampled headword 'JUS CURIALITATIS' -> index 7223: C2 candidate added
- sampled headword 'KERF' -> index 7330: C2 candidate added
- sampled headword 'KINGDOM' -> index 7355: C2 candidate added
- sampled headword 'LEDGER' -> index 7533: C2 candidate added
- sampled headword 'LIGHTER' -> index 7689: C2 candidate added
- sampled headword 'MARQUE AND REPRISAL, LETTERS OF' -> index 8065: C2 candidate added
- sampled headword 'MIS' -> index 8291: C2 candidate added
- sampled headword 'NEVER INDEBTED, PLEA OF' -> index 8638: C2 candidate added
- sampled headword 'NON SEQUITUR' -> index 8750: C2 candidate added
- sampled headword 'OCCUPATION' -> index 8919: C2 candidate added
- sampled headword 'ORDER' -> index 9025: C2 candidate added
- sampled headword 'PERSONNE' -> index 9499: C2 candidate added
- sampled headword 'PRESCRIBE' -> index 9889: C2 candidate added
- sampled headword 'QUARE' -> index 10326: C2 candidate added
- sampled headword 'QUICK' -> index 10375: C2 candidate added
- sampled headword 'REFUND' -> index 10633: C2 candidate added
- sampled headword 'RESPITE' -> index 10846: C2 candidate added
- sampled headword 'SER VITUS' -> index 11367: C2 candidate added
- sampled headword 'STAGIARIUS' -> index 11672: C2 candidate added
- sampled headword 'TESTAMENT' -> index 12140: C2 candidate added
- sampled headword 'TRABES' -> index 12308: C2 candidate added
- sampled headword 'UNDERLIE THE LAW' -> index 12514: C2 candidate added
- sampled headword 'UPLIFTED HAND' -> index 12570: C2 candidate added
- sampled headword 'VENIRE FACIAS' -> index 12706: C2 candidate added
- sampled headword 'VILLA REGIA' -> index 12790: C2 candidate added
- sampled headword 'WEEK' -> index 12952: C2 candidate added
- sampled headword 'WITHERS ARE' -> index 13032: C2 candidate added
- sampled headword 'XUS LEGITIMUM' -> index 7252: C2 candidate added
- sampled headword 'X. S' -> index 8524: C2 candidate added
- sampled headword 'YEAR' -> index 13122: already strong via S5, C2 not added
- sampled headword 'YORK, STATUTE OF' -> index 13128: C2 candidate added
- sampled headword 'ZANJA' -> index 13134: C2 candidate added
- sampled headword 'ZEMINDAR' -> index 13139: already strong via S5, C2 not added

## COMPLETE LOCUS LIST (merged markers — every marker the builder will print)

| Index | Headword | Strength | Rules | Anchor | Reason |
|---|---|---|---|---|---|
| 7 | A FORTIORI | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 8 | A GRATIA | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 30 | AB EXTRA | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 43 | ABANDONMENT | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 46 | ABATAMENTIIM | strong | S3 | END | body ends with a comma (after stripping trailing quotes/brackets): a printed entry cannot authorially end with a comma; text is cut off in the scan |
| 54 | ABBAOV | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 78 | ABJURE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 81 | ABMATEBTERA | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 85 | ABOLITION | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 86 | ABORDAGE | strong | S3 | END | body ends with a comma (after stripping trailing quotes/brackets): a printed entry cannot authorially end with a comma; text is cut off in the scan |
| 94 | ABRIDGE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 96 | ABRIDGMENT OP DAMAGES | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 98 | ABROGATION | strong | S3 | END | body ends with a comma (after stripping trailing quotes/brackets): a printed entry cannot authorially end with a comma; text is cut off in the scan |
| 107 | ABSQUE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 124 | ACCELERATION | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 133 | ACCESSARY | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 148 | ACCOMMODATION LANDS | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 149 | ACCOMMODATION PAPER | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 152 | ACCORD AND SATISFACTION | strong | S3 | END | body ends with a comma (after stripping trailing quotes/brackets): a printed entry cannot authorially end with a comma; text is cut off in the scan |
| 159 | ACCOUNTANT | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 163 | ACCREDIT | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 168 | ACOROOHER | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 201 | ACRE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 210 | ACTIO IN PERSONAM | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 238 | ACTUS | strong | S3 | END | body ends with a comma (after stripping trailing quotes/brackets): a printed entry cannot authorially end with a comma; text is cut off in the scan |
| 251 | AD CURIAM | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 272 | AD HOMINEM | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 279 | AD INTERIM | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 305 | AD STUDENDUM ET ORANDUM | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 338 | ADIEU | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 407 | ADS | candidate | C2 | ENTRY | stratified sample audit (2026-10-18): scan verification OPEN for this entry |
| 408 | ADVANCEMENT | strong | S1 | EMPTY | cleaned body is empty: no definition text survived the scan-to-text process for this entry |
| 417 | ADULTERATOR | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 422 | ADULTERY | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 479 | AFFIDATIO | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 484 | AFFILIATION | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 490 | AFFIRMANCE | strong | S2 | END | body ends with a hyphen: a word is broken off at the end of the scanned text |
| 507 | AFFREIGHTMENT | strong | S3 | END | body ends with a comma (after stripping trailing quotes/brackets): a printed entry cannot authorially end with a comma; text is cut off in the scan |
| 525 | AGENS | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 526 | AGENT | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 573 | AIELESBE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 709 | AMENDS | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 804 | ANNULUS | strong | S2 | END | body ends with a hyphen: a word is broken off at the end of the scanned text |
| 820 | ANTICHRESIS | candidate | C2 | ENTRY | stratified sample audit (2026-10-18): scan verification OPEN for this entry |
| 832 | APANAGE | strong | S3 | END | body ends with a comma (after stripping trailing quotes/brackets): a printed entry cannot authorially end with a comma; text is cut off in the scan |
| 875 | APPERTAIN | strong | S2 | END | body ends with a hyphen: a word is broken off at the end of the scanned text |
| 876 | PUKTKNANT | strong | S1 | EMPTY | cleaned body is empty: no definition text survived the scan-to-text process for this entry |
| 954 | ARE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 1025 | ARTICEED CLERK | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 1032 | ARTIFICIALLY | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 1125 | ATTAINT D’UNE CAUSE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 1130 | ATTERMINARE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 1171 | AUTHOR | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 1181 | AUTREFOIS | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 1207 | AVOWANT | strong | S3 | END | body ends with a comma (after stripping trailing quotes/brackets): a printed entry cannot authorially end with a comma; text is cut off in the scan |
| 1265 | BALIUS | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 1319 | BARRATOR | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 1323 | BARREN MONET | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 1324 | BARRENNESS | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 1325 | BARRETOR | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 1340 | BASTARDIZE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 1360 | BEACONAGE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 1394 | BERGHMAY8TER | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 1403 | BETTER EQUITY | candidate | C2 | ENTRY | stratified sample audit (2026-10-18): scan verification OPEN for this entry |
| 1455 | BLACKLEG | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 1479 | BLOODY HAND | strong | S2 | END | body ends with a hyphen: a word is broken off at the end of the scanned text |
| 1480 | BLUE LAWS | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 1494 | BOLTING | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 1499 | BODY POLITIC | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 1520 | BORDARXA | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 1524 | BORD-HALFFENNY | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 1532 | BORGH OF HAMHALD | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 1539 | BOSCUS | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 1570 | BRACHIUM MARIS | strong | S2 | END | body ends with a hyphen: a word is broken off at the end of the scanned text |
| 1581 | BREAKING | strong | S5 | See Arbebtment. | stratified audit FLAG (XREF-SEE): target not in headword set |
| 1593 | BREVET | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 1597 | BREVIATE | strong | S3 | END | body ends with a comma (after stripping trailing quotes/brackets): a printed entry cannot authorially end with a comma; text is cut off in the scan |
| 1620 | BROCELLA | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 1633 | BRUTUM FULMEN | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 1664 | BURGESS ROLL | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 1667 | BURGH ENGLOYS | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 1675 | BURGUNDIAN XAW | strong | S2 | END | body ends with a hyphen: a word is broken off at the end of the scanned text |
| 1694 | BUSONES COMITATUS | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 1713 | BY THE BY | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 1719 | C. C. P | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 1731 | CABALLERO | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 1745 | GADUGA | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 1766 | CALUMNY | strong | S2 | END | body ends with a hyphen: a word is broken off at the end of the scanned text |
| 1767 | UMNIA | strong | S1 | EMPTY | cleaned body is empty: no definition text survived the scan-to-text process for this entry |
| 1768 | CAMARA | strong | S2 | END | body ends with a hyphen: a word is broken off at the end of the scanned text |
| 1785 | CANCEL | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 1828 | CAPTIO | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 1834 | CAPUTAGIUM | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 1840 | CARCARE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 1846 | CARE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 1857 | CARLISLE TABLES | strong | S3 | END | body ends with a comma (after stripping trailing quotes/brackets): a printed entry cannot authorially end with a comma; text is cut off in the scan |
| 1882 | CARVAGE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 1889 | CASHLITE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 1895 | OASTELLAIN | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 1917 | CATCHING BARGAIN | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 1930 | CAUR8INES | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 1954 | CAVERS | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 1971 | CENNINGA | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 1973 | OENSARIA | strong | S3 | END | body ends with a comma (after stripping trailing quotes/brackets): a printed entry cannot authorially end with a comma; text is cut off in the scan |
| 2004 | CERTAIN | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 2007 | CERTIFICATION | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 2024 | C E 8 S E T PROCESSUS | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 2064 | CHAMBRE DEPEINTE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 2086 | CHAPITRE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 2089 | CHAPTER | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 2121 | CHADMFEBT | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 2126 | CHEMERAOE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 2143 | CHIMINUS | strong | S2 | END | body ends with a hyphen: a word is broken off at the end of the scanned text |
| 2165 | CHRISTMA 8-DAY | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 2169 | CIBARIA | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 2203 | CIVIL LAW | strong | S3 | END | body ends with a comma (after stripping trailing quotes/brackets): a printed entry cannot authorially end with a comma; text is cut off in the scan |
| 2223 | CLASSIFICATION | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 2226 | CLAUSUM | candidate | C2 | ENTRY | stratified sample audit (2026-10-18): scan verification OPEN for this entry |
| 2237 | CLEARANCE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 2328 | COLLEGE | strong | S2 | END | body ends with a hyphen: a word is broken off at the end of the scanned text |
| 2366 | COME | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 2367 | COMMANDERY | strong | S1 | EMPTY | cleaned body is empty: no definition text survived the scan-to-text process for this entry |
| 2369 | GOMINTJ8 | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 2391 | COMMENDATION | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 2440 | COMMUNX CUSTODIA | strong | S3 | END | body ends with a comma (after stripping trailing quotes/brackets): a printed entry cannot authorially end with a comma; text is cut off in the scan |
| 2448 | COMMUNXNGS | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 2461 | CONTBACT | strong | S1 | EMPTY | cleaned body is empty: no definition text survived the scan-to-text process for this entry |
| 2512 | COMPULSION | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 2520 | CONCEDO | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 2528 | CONCESSIT SOLVERE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 2530 | OONCESSUM | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 2536 | CONCLUDE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 2559 | CONDEMN | strong | S1 | EMPTY | cleaned body is empty: no definition text survived the scan-to-text process for this entry |
| 2560 | CONDITION | strong | S1 | EMPTY | cleaned body is empty: no definition text survived the scan-to-text process for this entry |
| 2585 | CONFESS | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 2588 | CONFESSO, BELL TAKEN PRO | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 2661 | CONSENT-RULE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 2663 | CONSEQUENTS | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 2665 | CONSIDERATIO CURIAE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 2667 | CONSEDERATTJR | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 2695 | CONSTITUENT | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 2705 | CONSTITUTOR | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 2714 | CONSUETUDINES | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 2717 | CONSUETUDO | candidate | C2 | ENTRY | stratified sample audit (2026-10-18): scan verification OPEN for this entry |
| 2743 | COHTINENS | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 2763 | CONTRAESCRITURA | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 2767 | CONTRAMANDATXO | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 2812 | GONVERSANTES | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 2836 | COPARCENARY | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 2846 | COPPER AND SCALES | strong | S2 | END | body ends with a hyphen: a word is broken off at the end of the scanned text |
| 2860 | CORNER | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 2875 | CORPORATION | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 2877 | CORPORATION ACT | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 2890 | CORREI | strong | S3 | END | body ends with a comma (after stripping trailing quotes/brackets): a printed entry cannot authorially end with a comma; text is cut off in the scan |
| 2893 | CORROBORATE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 2906 | COSEN, COZEN | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 2934 | COUNCIL OF CONCILIATION | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 2983 | COURT OF BROTHERHOOD | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 2997 | COURT OF ERROR | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 3005 | COURT OF HIGH COMMISSION | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 3062 | CRAFT | strong | S3 | END | body ends with a comma (after stripping trailing quotes/brackets): a printed entry cannot authorially end with a comma; text is cut off in the scan |
| 3074 | CREATE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 3075 | CREDIBLE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 3082 | CREPARE OCULTJM | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 3145 | CURATOR | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 3149 | CURFEW | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 3153 | CURIALITY | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 3154 | CURNOCK | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 3157 | CURRICULUM | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 3179 | CUSTOM-HOUSE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 3199 | CZARINA | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 3216 | DAMAGE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 3281 | DE BENE ESSE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 3282 | DE BIGAMIS | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 3288 | DE BONIS PROPRUS | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 3315 | DE COMPUTO | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 3342 | DE EJECTIONS FIRMS | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 3348 | DE ESTOVERIIS HABENDIS | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 3369 | DE GESTU ET FAMA | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 3398 | DE LUNATIC O INQUTRENDO | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 3417 | DE ODIO ET ATIA | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 3424 | DE PARCO FRACTO | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 3437 | DE PROPRIETATE PROBANDA | strong | S2 | END | body ends with a hyphen: a word is broken off at the end of the scanned text |
| 3466 | TDRJE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 3498 | DEATH | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 3507 | DEBIT | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 3555 | DECRETAE ORDER | strong | S2,S5 | END | body ends with a hyphen: a word is broken off at the end of the scanned text \| stratified audit FLAG (BODY): body ends without terminal punctuation: possible truncation/merge |
| 3556 | DEB | strong | S1 | EMPTY | cleaned body is empty: no definition text survived the scan-to-text process for this entry |
| 3570 | DEDICATION | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 3599 | DEFENDER | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 3604 | DEFEND IT VIM ET INJTJHIAM | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 3631 | DEFORCEMENT | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 3669 | DEMANDBESS | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 3674 | DEMAIN | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 3721 | DEPASTURE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 3723 | DEPENDENCY | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 3740 | DEPOSITORY | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 3744 | DEPREDATION | strong | S2 | END | body ends with a hyphen: a word is broken off at the end of the scanned text |
| 3765 | DESIGNATION | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 3770 | DESPATCHES | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 3773 | DESPITUS | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 3782 | DESTITUTE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 3785 | DESUBITO | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 3854 | DIFFERENCE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 3890 | Z | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 3898 | DIRIMENT IMPEDIMENTS | strong | S2 | END | body ends with a hyphen: a word is broken off at the end of the scanned text |
| 3899 | D IS AFFIRM | candidate | C2 | ENTRY | stratified sample audit (2026-10-18): scan verification OPEN for this entry |
| 3916 | DISCONTINUANCE OF AN ESTATE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 3925 | DISCRETIONARY TRUSTS | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 3929 | DISFRANCHISE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 3995 | DISTRAHERE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 4109 | DONNEUR D’AVAX | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 4148 | DRAYAGE | strong | S3 | END | body ends with a comma (after stripping trailing quotes/brackets): a printed entry cannot authorially end with a comma; text is cut off in the scan |
| 4183 | DUCES TECUM | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 4184 | DUCES TECUM LICET LANGUTDU8 | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 4198 | DUMHODO | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 4221 | DURHAM | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 4222 | DURSLEY | strong | S3 | END | body ends with a comma (after stripping trailing quotes/brackets): a printed entry cannot authorially end with a comma; text is cut off in the scan |
| 4224 | DUTCH AUCTION | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 4249 | EAR-MARK | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 4280 | ECHEVUT | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 4296 | EFFEKBI | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 4320 | EJECTION | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 4365 | EMBLEM BE GENTZ | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 4368 | EMBBACEBY | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 4394 | EMPIRIC | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 4435 | ENCLOSE | strong | S2 | END | body ends with a hyphen: a word is broken off at the end of the scanned text |
| 4436 | CLOSE | strong | S1 | EMPTY | cleaned body is empty: no definition text survived the scan-to-text process for this entry |
| 4446 | ENDOCARDITIS | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 4469 | ENJOYMENT | candidate | C2 | ENTRY | stratified sample audit (2026-10-18): scan verification OPEN for this entry |
| 4526 | EQUES | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 4533 | EQUIVALENT | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 4554 | ERRONXCE | strong | S2 | END | body ends with a hyphen: a word is broken off at the end of the scanned text |
| 4586 | ESPURIO | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 4622 | ESTATE OF INHERITANCE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 4623 | ESTATE PER AUTRE VIE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 4667 | EUNOMY | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 4675 | EVB8-DROPPERS | strong | S2 | END | body ends with a hyphen: a word is broken off at the end of the scanned text |
| 4676 | PER8 | strong | S1 | EMPTY | cleaned body is empty: no definition text survived the scan-to-text process for this entry |
| 4684 | EWRY | strong | S2 | END | body ends with a hyphen: a word is broken off at the end of the scanned text |
| 4704 | EX CONTRACTU | candidate | C2 | ENTRY | stratified sample audit (2026-10-18): scan verification OPEN for this entry |
| 4725 | EX MALITIA | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 4733 | EX PARTE PATERNA | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 4736 | EX POST FACTO LAW | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 4806 | EXECUTRIX | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 4819 | EXERCITOR NAVIS | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 4850 | EXONERATIONS SECTS | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 4883 | EXPROMISSOR | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 4886 | EXPULSION | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 4887 | FBI | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 4888 | EXPUNGE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 4909 | EXTORT | strong | S2 | END | body ends with a hyphen: a word is broken off at the end of the scanned text |
| 4939 | FABRIC LANDS | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 4981 | FAITOURS | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 4982 | FALANG | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 5005 | FALSE | strong | S2 | END | body ends with a hyphen: a word is broken off at the end of the scanned text |
| 5021 | FAMOSCS | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 5041 | FASTI | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 5060 | FEASOR | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 5102 | FEODUM | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 5114 | FEBCOSTA | strong | S3 | END | body ends with a comma (after stripping trailing quotes/brackets): a printed entry cannot authorially end with a comma; text is cut off in the scan |
| 5117 | FEBDWITE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 5118 | FERIA | strong | S3 | END | body ends with a comma (after stripping trailing quotes/brackets): a printed entry cannot authorially end with a comma; text is cut off in the scan |
| 5142 | FEUD | strong | S3 | END | body ends with a comma (after stripping trailing quotes/brackets): a printed entry cannot authorially end with a comma; text is cut off in the scan |
| 5160 | FIGTIO | strong | C1,S5 | END | stratified audit FLAG (BODY): body ends without terminal punctuation: possible truncation/merge \| body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is no… |
| 5176 | FIEF D'HAUBERT | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 5181 | FIELD REEVE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 5208 | FINDING- | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 5215 | FINIS | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 5217 | FINIUM REGUNDORUM ACTIO | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 5260 | FLEE TO THE WALL | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 5342 | FORDANNO | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 5350 | FOREIGN | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 5352 | FOREIN | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 5358 | FORESHORE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 5386 | FORLER-LARD | strong | C1,S5 | END | stratified audit FLAG (BODY): body ends without terminal punctuation: possible truncation/merge \| body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is no… |
| 5409 | FORSES | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 5416 | FORTAXHTTJM | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 5421 | FORTILITY | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 5437 | FOSSATORUM OPERATIO | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 5438 | FR | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 5457 | FR | strong | S3 | END | body ends with a comma (after stripping trailing quotes/brackets): a printed entry cannot authorially end with a comma; text is cut off in the scan |
| 5482 | FRAUD | strong | S3 | END | body ends with a comma (after stripping trailing quotes/brackets): a printed entry cannot authorially end with a comma; text is cut off in the scan |
| 5501 | FREND DESMAN | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 5503 | FREOBORGH | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 5523 | FRITH | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 5555 | FUNCTIONARY | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 5590 | FUTURI | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 5605 | GAIK | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 5640 | GARNISHMENT | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 5664 | GELD | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 5664 | GELD | candidate | C2 | ENTRY | stratified sample audit (2026-10-18): scan verification OPEN for this entry |
| 5748 | GO | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 5771 | GRACE, DATS OF | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 5774 | GRADES FARENTELS | candidate | C2 | ENTRY | stratified sample audit (2026-10-18): scan verification OPEN for this entry |
| 5787 | GRAND OOETEMIER | strong | S2 | END | body ends with a hyphen: a word is broken off at the end of the scanned text |
| 5788 | M1KR | strong | S1 | EMPTY | cleaned body is empty: no definition text survived the scan-to-text process for this entry |
| 5805 | GRATIS DICTUM | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 5829 | I 1 | strong | S1 | EMPTY | cleaned body is empty: no definition text survived the scan-to-text process for this entry |
| 5849 | GRIT ABU | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 5859 | GUARNIMENTUM | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 5870 | GUILLOTINE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 5878 | GUTI | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 5908 | HABITATIO | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 5921 | HEREDA | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 5972 | HAN G WITE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 5977 | HAGUE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 5990 | HASP AND STAPLE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 6014 | HEADLAND | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 6015 | HEAD-NOTE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 6018 | HEAFODWEARD | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 6023 | HEALTH V | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 6035 | HEPA | candidate | C2 | ENTRY | stratified sample audit (2026-10-18): scan verification OPEN for this entry |
| 6061 | KEORDPENNY | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 6138 | HIKENILD STREET | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 6155 | HLAF JET A | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 6186 | HOMBRE BUENO | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 6188 | HOMESOKEN, HOMSOKEN | strong | S5 | Haicesokbn. | stratified audit FLAG (XREF-SEE): target not in headword set |
| 6229 | HORN WITH HORN, OR HORN UNDER HORN | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 6244 | HOSPITICIDE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 6251 | HOSTES | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 6267 | HOVEL | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 6285 | HUHDREDOR8 | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 6286 | HUNG JURY | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 6297 | HUSPASTNE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 6307 | HYEMS, HIEMS | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 6309 | HYFOBOLUM | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 6346 | IDIOTA INQUIRENDO, WRIT DE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 6351 | IFUNGIA | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 6374 | ILLUD | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 6378 | IMAGINE | strong | S3 | END | body ends with a comma (after stripping trailing quotes/brackets): a printed entry cannot authorially end with a comma; text is cut off in the scan |
| 6401 | IMP ARC ARE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 6403 | IMPARL | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 6409 | IMPED EENS | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 6415 | IMPERATOR | strong | S2 | END | body ends with a hyphen: a word is broken off at the end of the scanned text |
| 6416 | PEBOB | strong | S1 | EMPTY | cleaned body is empty: no definition text survived the scan-to-text process for this entry |
| 6418 | IMPERITIA | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 6425 | IKPETRATION | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 6443 | IMPOTENCE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 6464 | IMPROVEMENT | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 6535 | IN GENE RE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 6546 | IN 1MVITUM | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 6566 | IN MERCY | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 6576 | IN PAIS | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 6582 | IN PECTORE JTJDICIS | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 6587 | IN PIOS TXSUS | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 6590 | IN PR2EMISSOREM FIDEM | strong | S5 | HEADWORD | stratified audit FLAG (HEADWORD): digit in headword: suspected OCR letter-confusion |
| 6594 | IN RE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 6605 | IN TERROREM | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 6620 | INABDIFICATIO | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 6627 | INCARCERATION | strong | S3 | END | body ends with a comma (after stripping trailing quotes/brackets): a printed entry cannot authorially end with a comma; text is cut off in the scan |
| 6628 | INCENDIARY | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 6632 | INCH | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 6646 | INCLUSIVE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 6648 | INCOME | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 6650 | INCOMMUTABLE | strong | S3 | END | body ends with a comma (after stripping trailing quotes/brackets): a printed entry cannot authorially end with a comma; text is cut off in the scan |
| 6655 | INCONSULTO | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 6661 | INCREMENTUM | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 6705 | INDICTIO | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 6707 | INDICTMENT | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 6724 | INDORSEMENT | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 6725 | INDORSER | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 6734 | INDUSTRIAL SCHOOLS | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 6774 | INFORMER | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 6788 | INFRA LIGEANTIAM REGIS | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 6798 | INFUGARE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 6811 | IN HABITANT | strong | S3 | END | body ends with a comma (after stripping trailing quotes/brackets): a printed entry cannot authorially end with a comma; text is cut off in the scan |
| 6817 | INHERITANCE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 6828 | INJURIA | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 6838 | INLEASED | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 6841 | INN | candidate | C2 | ENTRY | stratified sample audit (2026-10-18): scan verification OPEN for this entry |
| 6857 | IN OFFICIO SUM | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 6896 | INSTANTANEOUS | strong | S3 | END | body ends with a comma (after stripping trailing quotes/brackets): a printed entry cannot authorially end with a comma; text is cut off in the scan |
| 6932 | INTENTIO | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 6936 | INTER ALIA | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 6952 | INTERGEDERE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 6968 | INTERMEDIATE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 6974 | INTERNATIONAL LAW | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 6977 | INTERPELLATION | strong | S3 | END | body ends with a comma (after stripping trailing quotes/brackets): a printed entry cannot authorially end with a comma; text is cut off in the scan |
| 6981 | INTERPRET | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 6984 | INTERREGNUM | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 6991 | INTERVENER | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 7001 | INTOL AND ETTOL | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 7017 | INTROMISSION | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 7050 | IOTA | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 7080 | ISSUES | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 7093 | JACET US ORE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 7105 | JAMMA, JTTMMA | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 7106 | JAMMABUKDY, JUMMABUNDY | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 7114 | JEM AN | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 7134 | JOINT | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 7137 | JOCK | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 7153 | JUDICATIO | candidate | C2 | ENTRY | stratified sample audit (2026-10-18): scan verification OPEN for this entry |
| 7182 | J TJRATOR | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 7203 | JURY | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 7205 | JUS | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 7215 | JUS BANCI | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 7223 | JUS CURIALITATIS | candidate | C2 | ENTRY | stratified sample audit (2026-10-18): scan verification OPEN for this entry |
| 7240 | JUS HABENDI | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 7252 | XUS LEGITIMUM | candidate | C2 | ENTRY | stratified sample audit (2026-10-18): scan verification OPEN for this entry |
| 7262 | XUS PATRONATUS | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 7281 | JUS TRIUM UBERORUN | strong | S2 | END | body ends with a hyphen: a word is broken off at the end of the scanned text |
| 7289 | JUSTICES’ COURTS | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 7302 | JU8TITIA | strong | S4 | HEADWORD | named OCR artifact 'JU8TITIA' (digit-for-letter garble of IVSTITIA/JUSTITIA) present in headword |
| 7330 | KERF | candidate | C2 | ENTRY | stratified sample audit (2026-10-18): scan verification OPEN for this entry |
| 7339 | KIDDLE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 7355 | KINGDOM | candidate | C2 | ENTRY | stratified sample audit (2026-10-18): scan verification OPEN for this entry |
| 7381 | LA | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 7427 | LAND A | strong | S3 | END | body ends with a comma (after stripping trailing quotes/brackets): a printed entry cannot authorially end with a comma; text is cut off in the scan |
| 7430 | LANDCHEAP | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 7438 | LANDLOCKED | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 7461 | LASCIVIOUS | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 7473 | LATIMER | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 7488 | LAUDEMIUM | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 7493 | LAURELS | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 7495 | LAYATORTUM | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 7531 | LECTURER | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 7533 | LEDGER | candidate | C2 | ENTRY | stratified sample audit (2026-10-18): scan verification OPEN for this entry |
| 7558 | LEGIOSUS | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 7561 | LEGISLATOR | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 7592 | LESTAGE, LASTAGE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 7603 | LEVANT ET COUCHANT | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 7639 | LIBERUM SERVTTTUM | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 7657 | LICERE, LICERI | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 7678 | LIFT | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 7688 | LIGHT-SHIP, LIGHT-VESSEL | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 7689 | LIGHTER | candidate | C2 | ENTRY | stratified sample audit (2026-10-18): scan verification OPEN for this entry |
| 7691 | LIGHTERMAN | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 7714 | LIQUIDATOR | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 7767 | LOCO PARENTIS | strong | S2 | END | body ends with a hyphen: a word is broken off at the end of the scanned text |
| 7771 | LOOUPLE8 | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 7799 | LOT OF LAND | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 7864 | MAGISTER | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 7895 | MALLE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 7916 | MAITRE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 7930 | MAE-TOETE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 7952 | MALO SENSU | strong | S2 | END | body ends with a hyphen: a word is broken off at the end of the scanned text |
| 8003 | MANSE | strong | S2 | END | body ends with a hyphen: a word is broken off at the end of the scanned text |
| 8025 | MANUPRETITJM | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 8065 | MARQUE AND REPRISAL, LETTERS OF | candidate | C2 | ENTRY | stratified sample audit (2026-10-18): scan verification OPEN for this entry |
| 8090 | MATERIAL | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 8123 | MECHANICAL | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 8159 | MEMORITER | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 8197 | MERCY | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 8207 | MERITORIOUS | strong | S2 | END | body ends with a hyphen: a word is broken off at the end of the scanned text |
| 8219 | MESNE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 8259 | MUX | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 8265 | MILITIA | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 8289 | MINUTES | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 8291 | MIS | candidate | C2 | ENTRY | stratified sample audit (2026-10-18): scan verification OPEN for this entry |
| 8367 | MODUS | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 8368 | MOEB1E | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 8371 | MOHAMMEDAN LAW | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 8375 | MOLENDINUM | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 8379 | MOLLITER MANUS IMPOSUIT | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 8392 | MONITORY LETTERS | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 8397 | MONOGRAPH | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 8406 | MONTES | strong | S3 | END | body ends with a comma (after stripping trailing quotes/brackets): a printed entry cannot authorially end with a comma; text is cut off in the scan |
| 8407 | I 1 | strong | S1 | EMPTY | cleaned body is empty: no definition text survived the scan-to-text process for this entry |
| 8425 | MORGANATIC MARRIAGE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 8426 | BIAGE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 8427 | MORGEN | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 8428 | MORGUE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 8513 | MYN8TER-HAM | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 8519 | X. D | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 8523 | X. B | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 8524 | X. S | candidate | C2 | ENTRY | stratified sample audit (2026-10-18): scan verification OPEN for this entry |
| 8533 | NAME | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 8590 | NE UNQUES ACOOUPLE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 8618 | NEGOTIATION | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 8634 | NETHER HOUSE OF PARLIAMENT | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 8638 | NEVER INDEBTED, PLEA OF | candidate | C2 | ENTRY | stratified sample audit (2026-10-18): scan verification OPEN for this entry |
| 8665 | XOCUBQBXTUM | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 8667 | XOLISSEMEXT | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 8677 | NOMINATING AND REDUCING | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 8704 | NON-CONFORMIST | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 8707 | NON CULPABILIS | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 8709 | NON DECIMANDO | strong | S2 | END | body ends with a hyphen: a word is broken off at the end of the scanned text |
| 8724 | NON-INTERVENTION WILL | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 8741 | NONPAYMENT | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 8750 | NON SEQUITUR | candidate | C2 | ENTRY | stratified sample audit (2026-10-18): scan verification OPEN for this entry |
| 8758 | NON-TERM | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 8840 | NTTMMATA TERRAE | strong | S3 | END | body ends with a comma (after stripping trailing quotes/brackets): a printed entry cannot authorially end with a comma; text is cut off in the scan |
| 8841 | NUNC PRO TUNC | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 8844 | NUNCUPARE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 8853 | KURUS | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 8854 | NYCTHEMERON | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 8864 | OB CONTINGENTIAM | strong | S3 | END | body ends with a comma (after stripping trailing quotes/brackets): a printed entry cannot authorially end with a comma; text is cut off in the scan |
| 8885 | OBLITERATION | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 8893 | OBSCENITY | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 8905 | OBSTRUCTION | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 8907 | OBXEMPERARE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 8914 | OCCASIONES | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 8915 | OCCUPANCY | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 8919 | OCCUPATION | candidate | C2 | ENTRY | stratified sample audit (2026-10-18): scan verification OPEN for this entry |
| 8930 | OCTROI | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 8936 | OF FORCE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 8962 | OLYMPIAD | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 8991 | OPEBA | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 9022 | ORDELS | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 9025 | ORDER | candidate | C2 | ENTRY | stratified sample audit (2026-10-18): scan verification OPEN for this entry |
| 9033 | ORDINES | strong | S4 | 0RDINE8 UAJORES ET MINORE8 | garbage cluster: 2 OCR artifact tokens (letter/digit confusions) within a 12-token window; this passage is garbled in the scan-to-text process |
| 9033 | ORDINES | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 9087 | OUTLAWRY | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 9096 | OUTSUCKEN MULTURES | strong | S2 | END | body ends with a hyphen: a word is broken off at the end of the scanned text |
| 9120 | OWELTY | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 9121 | OWNER | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 9126 | OYER AMO TERMINER | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 9136 | P. P | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 9137 | PAAGE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 9139 | PAOATIO | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 9145 | PACKAGE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 9171 | PALMER ACT | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 9197 | PARATTTM HABEO | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 9205 | FARGO FRACTO | strong | S3 | END | body ends with a comma (after stripping trailing quotes/brackets): a printed entry cannot authorially end with a comma; text is cut off in the scan |
| 9225 | PARIUM JUDICIUM | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 9240 | PARRICIDIUM | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 9250 | FARTTARTUS | strong | S3 | END | body ends with a comma (after stripping trailing quotes/brackets): a printed entry cannot authorially end with a comma; text is cut off in the scan |
| 9259 | PARTNER | strong | S2 | END | body ends with a hyphen: a word is broken off at the end of the scanned text |
| 9262 | PARTURITION | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 9265 | PARTY | strong | S2 | END | body ends with a hyphen: a word is broken off at the end of the scanned text |
| 9270 | PAS | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 9284 | PASSING-TICKET | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 9295 | PATER | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 9317 | PATRONAGE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 9341 | PECK | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 9375 | PEKAL | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 9419 | PER MISADVENTURE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 9442 | PERCEPTION | strong | S2 | END | body ends with a hyphen: a word is broken off at the end of the scanned text |
| 9446 | PERDUELLIO | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 9455 | PERFORM | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 9458 | PERICARDITIS | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 9499 | PERSONNE | candidate | C2 | ENTRY | stratified sample audit (2026-10-18): scan verification OPEN for this entry |
| 9527 | PETITORY ACTION | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 9532 | PEW | strong | S3 | END | body ends with a comma (after stripping trailing quotes/brackets): a printed entry cannot authorially end with a comma; text is cut off in the scan |
| 9548 | PIGNORATIO | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 9558 | PILLORY | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 9569 | PIOUS USES | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 9571 | PIRACY | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 9573 | PIRATICAL | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 9577 | PIT AND GALLOWS | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 9620 | T | strong | S1 | EMPTY | cleaned body is empty: no definition text survived the scan-to-text process for this entry |
| 9625 | PLEDGERY | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 9649 | PLUMBUM | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 9653 | PLURALITY | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 9678 | POLL-TAX | strong | S2 | END | body ends with a hyphen: a word is broken off at the end of the scanned text |
| 9799 | PRACTICES | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 9807 | FRIED IA | strong | S2 | END | body ends with a hyphen: a word is broken off at the end of the scanned text |
| 9834 | PRATER | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 9865 | PREFERENCE SHARES | strong | S2 | END | body ends with a hyphen: a word is broken off at the end of the scanned text |
| 9889 | PRESCRIBE | candidate | C2 | ENTRY | stratified sample audit (2026-10-18): scan verification OPEN for this entry |
| 9891 | PRESENTATION | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 9909 | PRESUMPTIO | strong | S2 | END | body ends with a hyphen: a word is broken off at the end of the scanned text |
| 9910 | SUMPTION | strong | S1 | EMPTY | cleaned body is empty: no definition text survived the scan-to-text process for this entry |
| 9927 | PREVENTIVE JUSTICE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 9929 | PREVIOUS QUESTION | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 9937 | PRIMAGE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 9948 | PRIMOGENITUS | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 9949 | S3- | strong | S1 | EMPTY | cleaned body is empty: no definition text survived the scan-to-text process for this entry |
| 9956 | PRINCIPALIS | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 9957 | PRINCIPLE | strong | S2 | END | body ends with a hyphen: a word is broken off at the end of the scanned text |
| 9974 | PRIVEMENT ENCEINTE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 9976 | PRIVATEER | strong | S2 | END | body ends with a hyphen: a word is broken off at the end of the scanned text |
| 10118 | PROMULGARE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 10124 | FRONOTARY | strong | S2 | END | body ends with a hyphen: a word is broken off at the end of the scanned text |
| 10125 | THONOTABT | strong | S1 | EMPTY | cleaned body is empty: no definition text survived the scan-to-text process for this entry |
| 10134 | PROPIOS, PROFRIOS | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 10141 | PROPRES | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 10142 | PROPRIA PERSONA | strong | S2 | END | body ends with a hyphen: a word is broken off at the end of the scanned text |
| 10143 | PBIA PEB80NA | strong | S1 | EMPTY | cleaned body is empty: no definition text survived the scan-to-text process for this entry |
| 10144 | PROPRIEDAD | strong | S3 | END | body ends with a comma (after stripping trailing quotes/brackets): a printed entry cannot authorially end with a comma; text is cut off in the scan |
| 10150 | PROPRIO VIGORE | strong | S3 | END | body ends with a comma (after stripping trailing quotes/brackets): a printed entry cannot authorially end with a comma; text is cut off in the scan |
| 10155 | PROROGATION | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 10161 | PROSECUTION | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 10180 | PROTESTATION | strong | S2 | END | body ends with a hyphen: a word is broken off at the end of the scanned text |
| 10200 | PROVISO | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 10251 | PURGATION | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 10259 | PURPRISE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 10288 | QUACUNQUE VIA BATA | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 10318 | QUALITY | strong | S2 | END | body ends with a hyphen: a word is broken off at the end of the scanned text |
| 10320 | QUAKED IU SB BENE DEMERIT | strong | S3 | END | body ends with a comma (after stripping trailing quotes/brackets): a printed entry cannot authorially end with a comma; text is cut off in the scan |
| 10326 | QUARE | candidate | C2 | ENTRY | stratified sample audit (2026-10-18): scan verification OPEN for this entry |
| 10370 | QUIA | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 10375 | QUICK | candidate | C2 | ENTRY | stratified sample audit (2026-10-18): scan verification OPEN for this entry |
| 10376 | QUICK WITH CHILD | strong | S2 | END | body ends with a hyphen: a word is broken off at the end of the scanned text |
| 10377 | IRQ | strong | S1 | EMPTY | cleaned body is empty: no definition text survived the scan-to-text process for this entry |
| 10398 | QUO WARRANTO | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 10401 | QUOD BILLA CASSETUR | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 10407 | QUOD NON FUXT NEGATUM | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 10444 | RAILWAY | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 10448 | RAHCHO | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 10513 | RECIPROCAL CONTRACT | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 10534 | RECOMPENSATION | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 10539 | RECONSTRUCTION | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 10542 | RECONVERSION | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 10545 | RECORD ARI FACIAS LOQUELAM | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 10547 | RECORDER OF LONDON | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 10573 | RECTUM | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 10579 | RECUSATION | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 10616 | REFALO | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 10633 | REFUND | candidate | C2 | ENTRY | stratified sample audit (2026-10-18): scan verification OPEN for this entry |
| 10636 | REG | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 10654 | REGICIDE | strong | S3 | END | body ends with a comma (after stripping trailing quotes/brackets): a printed entry cannot authorially end with a comma; text is cut off in the scan |
| 10680 | REGULA | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 10692 | REINSURANCE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 10694 | REJOIN | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 10697 | RELATIONS | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 10703 | U | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 10710 | RELICT | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 10748 | REMOVAL OF PAUPER | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 10802 | REPUDIATE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 10839 | RESISTING AN OFFICER | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 10846 | RESPITE | candidate | C2 | ENTRY | stratified sample audit (2026-10-18): scan verification OPEN for this entry |
| 10872 | RESUMMONS | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 10877 | RETAKING | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 10879 | RETENEMENTUM | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 10880 | RETINENTIA | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 10886 | RETOUR OF SERVICE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 10887 | RETOUR SANS FRAIS | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 10894 | RETREAT TO THE WALL | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 10901 | RETURNABLE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 10910 | REVELAND | strong | S3 | END | body ends with a comma (after stripping trailing quotes/brackets): a printed entry cannot authorially end with a comma; text is cut off in the scan |
| 10916 | REVERSION | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 10919 | REVERT | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 10925 | REVISING ASSESSORS | strong | S3 | END | body ends with a comma (after stripping trailing quotes/brackets): a printed entry cannot authorially end with a comma; text is cut off in the scan |
| 10973 | RIGHTS OF THINGS | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 11004 | ROBBER | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 11010 | ROGARE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 11032 | ROTTEN BOROUGHS | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 11042 | ROYALTY | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 11054 | RUNNING LEASE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 11070 | RYOT | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 11075 | S. P | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 11090 | SACRAMENTALES | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 11120 | SALOON-KEEPER | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 11132 | SANCTIO | strong | S2 | END | body ends with a hyphen: a word is broken off at the end of the scanned text |
| 11140 | SANITARY AUTHORITIES | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 11144 | SANS IMPEACHMENT DE WANT | strong | S1 | EMPTY | cleaned body is empty: no definition text survived the scan-to-text process for this entry |
| 11154 | SATISFACTION | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 11162 | SAVINGS BANK | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 11215 | SCROLL | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 11225 | SCYREGEMOTE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 11230 | SEALING | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 11234 | SEARCH | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 11266 | SEDE PLENA | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 11267 | SEDENTE CURIA | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 11273 | SEDUCTION | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 11276 | SEIGNIORAGE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 11300 | SEMITA | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 11309 | SENATUS OONSULTUM | strong | S4 | 8ENATTJ8 CON8ULTUM /  / 8ENTENOE | garbage cluster: 3 OCR artifact tokens (letter/digit confusions) within a 12-token window; this passage is garbled in the scan-to-text process |
| 11332 | SEPTENNIAL ACT | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 11344 | SEQUESTRATOR | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 11345 | SEQUESTRO HABENDO | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 11367 | SER VITUS | candidate | C2 | ENTRY | stratified sample audit (2026-10-18): scan verification OPEN for this entry |
| 11369 | SEES | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 11370 | SESSIO | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 11395 | SEXTUS DECRETALIUM | strong | S3 | END | body ends with a comma (after stripping trailing quotes/brackets): a printed entry cannot authorially end with a comma; text is cut off in the scan |
| 11396 | SEXUAL INSTINCT, INVERSION AND PERVERSION OF | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 11424 | SHIPPED | strong | S3 | END | body ends with a comma (after stripping trailing quotes/brackets): a printed entry cannot authorially end with a comma; text is cut off in the scan |
| 11435 | SHORT NOTICE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 11443 | SI CONSTET BE PERSONA | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 11452 | SIC | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 11505 | SIX CLERKS | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 11538 | SOBRE-JUEZES | strong | S3 | END | body ends with a comma (after stripping trailing quotes/brackets): a printed entry cannot authorially end with a comma; text is cut off in the scan |
| 11550 | SOCOME | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 11573 | SOLIDARY | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 11593 | SON-IN-LAW | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 11620 | SPEAKING DEMURRER | strong | S2 | END | body ends with a hyphen: a word is broken off at the end of the scanned text |
| 11621 | BEB | strong | S1 | EMPTY | cleaned body is empty: no definition text survived the scan-to-text process for this entry |
| 11627 | SPECIFIC | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 11641 | SPIRITUAL | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 11650 | SPONDES7 SPONDEO | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 11672 | STAGIARIUS | candidate | C2 | ENTRY | stratified sample audit (2026-10-18): scan verification OPEN for this entry |
| 11676 | STAILARIUS | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 11680 | STANDARD | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 11687 | STATE OF FACTS AND PROPOSAL | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 11744 | STOCKS | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 11765 | STREFITTJ8 | strong | S4 | 6TREPITU8 JUD1CIALI8 /  / 6TULTIL0QUIUM | garbage cluster: 3 OCR artifact tokens (letter/digit confusions) within a 12-token window; this passage is garbled in the scan-to-text process |
| 11765 | STREFITTJ8 | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 11772 | STRIKE OFF | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 11782 | STULTIFY | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 11799 | SUBJECT | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 11849 | SUGGESTION | strong | S3 | END | body ends with a comma (after stripping trailing quotes/brackets): a printed entry cannot authorially end with a comma; text is cut off in the scan |
| 11880 | SUPERFXCIARXUS | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 11896 | SUPPLIANT | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 11912 | SURGEON | strong | S3 | END | body ends with a comma (after stripping trailing quotes/brackets): a printed entry cannot authorially end with a comma; text is cut off in the scan |
| 11938 | SUSPICION | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 11943 | SUUS JUDEX | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 11949 | SWEEPING | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 11961 | SYMBOLIC DELIVERY | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 11962 | SYMBOLUM AKIMS | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 11965 | SYNGOPARE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 12003 | TAKING | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 12031 | TAVERN | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 12047 | TEAM | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 12080 | TENOON | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 12102 | TENURA | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 12121 | TERRA | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 12140 | TESTAMENT | candidate | C2 | ENTRY | stratified sample audit (2026-10-18): scan verification OPEN for this entry |
| 12190 | THESMOTHETE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 12197 | THIRDS | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 12199 | THIRTY-NINE ARTICLES | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 12213 | THROW OUT | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 12225 | TIERCE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 12256 | TO ALIA | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 12263 | TOLLAGB | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 12274 | TONNAGE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 12283 | TOP ANNUAL | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 12288 | TOTA CURIA, L | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 12292 | TOTTED | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 12295 | TOUJOURS ET UNCORE PRIST | strong | S3 | END | body ends with a comma (after stripping trailing quotes/brackets): a printed entry cannot authorially end with a comma; text is cut off in the scan |
| 12308 | TRABES | candidate | C2 | ENTRY | stratified sample audit (2026-10-18): scan verification OPEN for this entry |
| 12343 | TRANSIENT | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 12346 | TRANSLATION | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 12347 | TRANSLATIVE FACT | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 12349 | TRANSPORT | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 12351 | TRANSUMPTS | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 12354 | TRASSATUS | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 12358 | TRAVERSER | strong | S3 | END | body ends with a comma (after stripping trailing quotes/brackets): a printed entry cannot authorially end with a comma; text is cut off in the scan |
| 12372 | TREET | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 12397 | TRINITY SITTINGS | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 12422 | TRUSTER | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 12424 | TRUSTOR | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 12431 | TUG | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 12453 | TWA NIGHT GEST | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 12463 | TYRANNY | strong | S2 | END | body ends with a hyphen: a word is broken off at the end of the scanned text |
| 12465 | TYROTOXICON | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 12466 | TYTKE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 12469 | U | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 12472 | TT | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 12492 | UNANIMITY | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 12496 | UNCERTAINTY | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 12514 | UNDERLIE THE LAW | candidate | C2 | ENTRY | stratified sample audit (2026-10-18): scan verification OPEN for this entry |
| 12530 | UNIGENITURE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 12570 | UPLIFTED HAND | candidate | C2 | ENTRY | stratified sample audit (2026-10-18): scan verification OPEN for this entry |
| 12594 | USURIOUS | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 12624 | UXORICIDE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 12627 | V. O | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 12634 | VACATE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 12655 | VALOR BENEFICIORUM | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 12673 | VAVASORY | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 12684 | VEJOUR8 | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 12706 | VENIRE FACIAS | candidate | C2 | ENTRY | stratified sample audit (2026-10-18): scan verification OPEN for this entry |
| 12708 | VENIT ET DEFENDIT | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 12728 | VERSUS | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 12730 | VERU8 | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 12764 | VICARAGE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 12769 | VICINAGE | strong | S3 | END | body ends with a comma (after stripping trailing quotes/brackets): a printed entry cannot authorially end with a comma; text is cut off in the scan |
| 12790 | VILLA REGIA | candidate | C2 | ENTRY | stratified sample audit (2026-10-18): scan verification OPEN for this entry |
| 12797 | VILLANUM SERVITIUM | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 12826 | VIS | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 12867 | VOUCHEE | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 12873 | VS | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 12875 | W. D | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 12891 | WAIVER | strong | S2 | END | body ends with a hyphen: a word is broken off at the end of the scanned text |
| 12901 | WANTONNESS | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 12912 | WAREHOUSE | strong | S2 | END | body ends with a hyphen: a word is broken off at the end of the scanned text |
| 12918 | WARRANTY | strong | S1 | EMPTY | cleaned body is empty: no definition text survived the scan-to-text process for this entry |
| 12930 | WASTORS | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 12952 | WEEK | candidate | C2 | ENTRY | stratified sample audit (2026-10-18): scan verification OPEN for this entry |
| 12973 | WHARFINGER | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 12981 | WHIFFENG-POST | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 12986 | WHITE RENTS | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 13006 | WILD’S CASE, RULE IN | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 13032 | WITHERS ARE | candidate | C2 | ENTRY | stratified sample audit (2026-10-18): scan verification OPEN for this entry |
| 13040 | WOLD | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 13079 | WRIT OF DOWER | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 13099 | WRIT OF TOUT | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 13102 | WRIT FRO RETORNO HABENDO | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 13120 | YARD | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 13122 | YEAR | strong | S5 | See Estate foe Years. | stratified audit FLAG (XREF-SEE): target not in headword set |
| 13126 | YOKELET | candidate | C1 | END | body ends without terminal punctuation (. ! ?) after stripping trailing quotes/brackets, and is not an authority-name tail: possible truncation in the scan |
| 13128 | YORK, STATUTE OF | candidate | C2 | ENTRY | stratified sample audit (2026-10-18): scan verification OPEN for this entry |
| 13134 | ZANJA | candidate | C2 | ENTRY | stratified sample audit (2026-10-18): scan verification OPEN for this entry |
| 13139 | ZEMINDAR | strong | S5 | END | stratified audit FLAG (BODY): body ends without terminal punctuation: possible truncation/merge |

End of census — 775 merged markers over 772 entries.
