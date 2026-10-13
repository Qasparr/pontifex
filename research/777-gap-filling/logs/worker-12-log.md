# WORKER-12 thought log — PONTIFEX 777 gap-filling
# Cells: XLIV/4, XLIV/6, XLIV/11, XLIV/13, XLIV/14, XLIV/15, XLIV/16, XLIV/17, XLIV/18
# Standing ruling: ALL thoughts logged, ultra-verbose: hypothesis -> method -> observation -> result.
# Dead ends and discarded lines included.

## Session open — 2026-10-13

### Reading the assignment
- 9 cells, all in column XLIV. Quick-ref said XLII-XLIV = Perfumes / Vegetable Drugs / Mineral Drugs.
- First hypothesis: my column might be XLIV = Mineral Drugs (the third of the three).
- Method: read the source directly at lines 890-930.
- Observation: header line reads "XLIV.*" then "Mineral Drugs." — CONFIRMED by source, not just the quick-ref.
- Result: column title = "Mineral Drugs". Column title verified against source (quick-ref agreed).

### Cell emptiness verification
- Method: sed the exact LINE_REF lines.
- Observations:
  - line 904: row 4 row ends ". . . . . . . ." in the XLIV column. EMPTY.
  - line 906: row 6, XLIV = ". . . . . . . .". EMPTY.
  - line 913: row 11, XLIV = ". . . . . . . .". EMPTY.
  - line 917: row 13, XLIV = ". . . . . . . .". EMPTY.
  - line 918: row 14, XLIV = ". . . . . . . .". EMPTY.
  - line 920: row 15, XLIV = ". . . . . . . .". EMPTY.
  - line 921: row 16, XLIV = ". . . . . . . .". EMPTY.
  - line 922: row 17, XLIV = ". . . . . . . .". EMPTY.
  - line 923: row 18, XLIV = ". . . . . . . .". EMPTY.
- Result: all 9 confirmed empty. None is row 0 (the by-design blank row), so the "row 0 is blank by design" rule does not apply.

### Row meanings (from source columns I-V, lines 206-260, read directly)
- 4 = Chesed = Mercy (Jupiter's sephira)
- 6 = Tiphareth = Beauty (Sun's sephira)
- 11 = Aleph = Ox (Air, the first mother letter)
- 13 = Gimel = Camel (Moon)
- 14 = Daleth = Door (Venus)
- 15 = Heh = Window (Aries / Mars-ruled)
- 16 = Vav = Nail (Taurus / Venus-ruled)
- 17 = Zain = Sword (Gemini / Mercury-ruled)
- 18 = Cheth = Fence (Cancer / Moon-ruled)

### Surveying the filled XLIV cells for the column's internal logic
- Method: read the full table segment lines 904-950.
- Filled cells observed:
  - 0 = Carbon | 1 = Aur. Pot. | 2 = Phosphorus | 3 = Silver | 5 = Iron, Sulphur
  - 7 = Arsenic | 8 = Mercury | 9 = Lead | 10 = Mag. Sulph. | 12 = Mercury
  - 23 = Sulphates | 31 = Nitrates | 31 bis = Carbon | 32 = Lead | 32 bis = Bismuth
- Pattern analysis (hypothesis): partial classical planetary-metal logic.
  - 5 = Geburah/Mars -> Iron (Mars's metal: YES, classical).
  - 8 = Hod/Mercury-planet -> Mercury (YES).
  - 12 = Beth/Mercury-planet -> Mercury (YES — Crowley repeats the same value at 8 and 12).
  - 32 = Tau/Saturn -> Lead (Saturn's metal: YES, classical).
  - 9 = Yesod/Moon -> Lead (does NOT follow planet-metal; Moon = Silver classically. Crowley put Silver at 3 = Binah instead. Odd, but it is what it is — not my row to fix).
  - Duplication is Crowley's own habit in this column: Mercury at 8 AND 12; Lead at 9 AND 32; Carbon at 0 AND 31 bis.
- Conspicuous gaps: 4 (Chesed/Jupiter) has NO Tin though Jupiter's metal is tin classically; 6 (Tiphareth/Sun) has NO Gold though 1 = Aur. Pot. (a gold preparation) sits at Kether. These two holes look like incompleteness, not design — he filled Mars/Iron, Mercury/Mercury, Saturn/Lead but skipped Jupiter/Tin and Sun/Gold.
- The path-rows (11-32) are mostly blank except 12 (Mercury), 23 (Sulphates), 31 (Nitrates), 31 bis (Carbon), 32 (Lead), 32 bis (Bismuth). So Crowley DID fill some path rows when he had a correspondence. My path rows 11, 13-18 fall in the blank band 13-22 (all blank) plus 11 (blank) and 14-18 (blank). I will propose fillings grounded in (a) planetary metal of the path's planet, (b) attested mineral-drug names from the old pharmacopoeia, (c) letter-meaning where apt — and weigh every candidate, tier everything, flag bridges and chance-hits honestly.
- Deliberately NOT forcing: the INTENTIONALLY_EMPTY outcome stays live for any cell where no honest correspondence presents itself. After analysis, none of my 9 rows looks "by design" empty (row 0 rule does not apply; path-band blanks are Crowleyan incompleteness, and he filled neighbors 12 and 23 in the same band).

### Next: read the weighing engine API, then calibrate.

## Weighing engine
- Hypothesis: ptk/weigh.py is the honest table set; calibrate() must pass before any weighing.
- Method: ran calibrate(); then a quick smoke weighing.
- Observation: calibrate() → True (עז=77, θελημα=93, αγαπη=93, AXONEME=77, CELL=32, אעם gadol=671 all reproduce). latin('TIN')=43.
- Result: engine trusted. Rule adopted: never retype a letter table; import only.

## Attestation verification (before proposing — TRVVTH gate on every historical claim)
- Hypothesis: the drug-name claims I want to cite are real historical terms, not my inventions.
- Method: web searches, one per term; summaries only, no reliance on a single source.
- Observations:
  - "Crocus Martis": ATTESTED — Webster 1913 defines colcothar as "called also crocus Martis" (reddish-brown iron oxide); Antonio Neri's L'Arte Vetraria gives four recipes for making it; RCPE People's Dispensary lists "Salt Of Crocus Martis" as a treatment; one source glosses it as poetically "saffron of Mars" (Martis = of Mars).
  - "Lunar caustic": ATTESTED — Merriam-Webster: "silver nitrate especially when fused and molded into sticks for use as a caustic"; etymology: lunar "of silver," from alchemists' luna = moon/silver.
  - Coral as medicine: ATTESTED — Pereira's Materia Medica: "Prepared Red Coral (Corallium rubrum præparatum) was formerly used in medicine"; Frontiers in Pharmacology review (2023) on coral in traditional medicine; 17th-c. English tract "Coral and steel" by R.B., M.D. built a whole practice on red coral.
  - Malachite as medicine/cosmetic: ATTESTED — ISHM abstract (Barroso): used as cosmetic and medicine in ancient Egypt; name from Greek "molochitis lithos" (mallow-green stone); consecrated to Aphrodite in Greece, Venus in Rome. (Folk-healing claims on other sites NOT relied on.)
  - "Sal volatile": ATTESTED — Wikipedia/smelling salts: "also known as ammonia inhalants, spirit of hartshorn, or sal volatile... The usual active compound is ammonium carbonate."
  - "Blue vitriol": ATTESTED — PharmaCompass: "A sulfate salt of copper. It is a potent emetic"; materia medica texts list it as Cupri Sulphas with emetic dosing.
  - Cinnabar as mineral drug: ATTESTED — OSTI/PubMed: "has long been used in combination with traditional Chinese medicine as a sedative for more than 2000 years" (zhusha); Frontiers: cinnabar among the most-used mineral medical materials in TCM.
  - Classical planet-metal doctrine (Jupiter=tin, Sun=gold, Venus=copper, Mars=iron, Mercury=quicksilver, Saturn=lead): ATTESTED tradition, and — critically — Crowley himself applies it inside this very column (5=Geburah/Mars→Iron; 8=Hod/Mercury-planet→Mercury; 12=Beth/Mercury-planet→Mercury; 32=Tau/Saturn→Lead). So extending it to 4 (Jupiter→Tin) and 6 (Sun→Gold) is derivation from the column's own logic, not importation.
- Dead end noted: I briefly considered "Stannum" (Latin for tin) as an alternate for XLIV/4, then discarded it — one clean proposal (Tin) is more honest than padding with synonyms.
- Dead end noted: for XLIV/15 I considered plain "Iron" (Vav=Nail→iron nail; Heh=Aries→Mars→iron) but Iron already sits at 5=Geburah; "Crocus Martis" is the distinct Mars-drug and the attested name literally contains the planet — stronger, so Iron was discarded as the primary.
- Dead end noted: for XLIV/18 I weighed Pearl vs Coral. Both are genuine old-pharmacopoeia lunar drugs. Coral won primary because Cancer is the WATER sign — sea-born fits the element; Pearl kept as alternate rather than discarded silently.
- Dead end noted: for XLIV/16, "Emerald" was considered (green, Venus) and discarded — not a mineral drug in the pharmacopoeia sense; malachite has the Egyptian medical attestation and the Aphrodite/Venus consecration.

## The weighing run
- Method: worker-12-weigh.py — calibrate, weigh every (proposal, bank) pair, unknown() audit each, letter breakdowns, programmatic bridge detection (same WORD required, not just same number), chance-flag watch-list {11,13,32,77,93,418,666,777}.
- Observation: 29 rows written. Every unknown() audit returned skipped=[] — no silent letter drops. Breakdowns all reconcile (spot-check: SALVOLATILE = 19+1+12+22+15+12+1+20+9+12+5 = 128 — my hand tally of 138 was wrong; the script is authoritative, which is why the script does the math).
- Bridge detection: NO bridges found anywhere. I had privately hoped TIN might bridge somewhere or CORAL 49/hebrew 80 might rhyme — they don't. The honest result is null; recorded as bridge="no" on every row.
- Chance-flags: none triggered. Nearest watch-number adjacency: none within 1 of any watch number. CROCUSMARTIS=159 (not 160-ish special), MALACHITE latin=72 (not 77 — a near-miss is not a hit; noted here, not claimed).

## Per-cell results
1. XLIV/4 (Chesed/Mercy, Jupiter): TIN — latin 43, agrippa 149, hebrew בדיל 46. Tier derived. Reasoning: Jupiter's classical metal; the column already does Mars→Iron, Mercury→Mercury, Saturn→Lead, so the Jupiter hole is the column's own logic unfinished. Hebrew word attested.
2. XLIV/6 (Tiphareth/Beauty, Sun): GOLD — latin 38, agrippa 81, hebrew זהב 14. Tier derived. Reasoning: the Sun's metal; Aur. Pot. at row 1 is a preparation, Gold here is the metal proper — not duplicative in kind.
3. XLIV/11 (Aleph/Ox, Air): SAL VOLATILE — latin 128, agrippa 516. Tier constructed. Reasoning: the volatile (flying) salt, the inhaled drug of the Airy path. No Hebrew weighing attempted — a constructed transliteration would be dishonest.
4. XLIV/13 (Gimel/Camel, Moon): LUNAR CAUSTIC — latin 142, agrippa 747. Tier derived. Reasoning: the name literally means "of the Moon" (luna); silver nitrate, attested drug; cross-ref row 31=Nitrates (this is the lunar nitrate).
5. XLIV/14 (Daleth/Door, Venus): COPPER — latin 73, agrippa 258, hebrew נחשת 758. Tier derived (Venus's classical metal). Alternate: BLUE VITRIOL — latin 145, agrippa 695, tier derived (copper sulphate, the copper drug; echoes row 23=Sulphates).
6. XLIV/15 (Heh/Window, Aries, Mars-ruled): CROCUS MARTIS — latin 159, agrippa 736. Tier derived. Reasoning: "saffron of Mars" — the name literally names the path's ruler; red iron oxide, attested; distinct from Iron at 5 (duplication is Crowley's own habit in this column).
7. XLIV/16 (Vav/Nail, Taurus, Venus-ruled): MALACHITE — latin 72, agrippa 177, greek μαλαχιτης 1190. Tier constructed. Reasoning: green copper carbonate — copper=Venus's metal, green=Venus's color, consecrated to Aphrodite/Venus; Greek word attested (Theophrastus). The placement chain is mine — constructed, honestly marked.
8. XLIV/17 (Zain/Sword, Gemini, Mercury-ruled): CINNABAR — latin 62, agrippa 176, arabic زنجفر 340. Tier derived. Reasoning: Mercury's own ore (mercury sulphide), the red sulphide suits the Sword; attested TCM mineral drug; Arabic word attested classical.
9. XLIV/18 (Cheth/Fence, Cancer, Moon-ruled): CORAL — latin 49, agrippa 154, hebrew אלמוג 80. Tier constructed (sea-born → watery Moon sign; Hebrew word attested). Alternate: PEARL — latin 52, agrippa 166, hebrew מרגלית 683, tier constructed (the lunar jewel, old-pharmacopoeia drug, Hebrew word attested).

## Honesty ledger
- INTENTIONALLY_EMPTY: none of the 9. All rows got proposals; none is row 0, and the blank band 13–22 sits inside a column whose own logic (planet→metal) is visibly unfinished at 4 and 6. Forcing nothing — every proposal carries its derivation or its constructed flag.
- Bridges: zero. Reported as zero. A null bridge result is a result.
- Chance-flags: zero triggered; watch-list checked programmatically.
- Findings, never doctrine. The red pen rules.
