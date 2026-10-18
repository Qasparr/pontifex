#!/usr/bin/env python3
# ============================================================================
# THE FOUR L'S \u2014 TWO TEACHER'S EDITIONS (A: IAO131's essays; B: Heart of the Master)
# ----------------------------------------------------------------------------
# "The Law of your being becomes Light, Life, Love and Liberty."
#   -- Crowley, Liber DCCCXXXVII (The Law of Liberty)
#
# Built: 2026-10-18 | 93
# Author: Johnathan 'Qasparr' (\u039a\u03b1\u03c3\u03c0\u03b1\u03c1\u03c1) Monroe, Keeper of the Secret Treasure
# Method: Scientific Illuminism. Copyright rule: brief quotation for study
#   (well under 50 words per work), summary in our own words, full texts
#   linked -- never reproduced. Findings, never doctrine; the red pen rules.
#
# MECHANISM: two PDFs from shared audit data --
#   Edition A: the IAO131 Four-L essays (summaries + brief quotes + links).
#   Edition B: Crowley's Heart of the Master (summary + brief quotes).
#   Both carry the Teaching, the Marriage (correspondence tables between the
#   works), and the full TRVVTH + PONTIFEX findings.
# DOCTRINE: the correspondence Lion=Love, Cow=Life, Babe=Liberty, Eagle=Light
#   is read straight off Crowley's own words in the Vision -- observed, not
#   invented. What is observed is stated; what is inferred is flagged.
#
# "Live, Love, and let Love, Live."
# ============================================================================

import os
from fpdf import FPDF, XPos, YPos

HERE = os.path.dirname(os.path.abspath(__file__))
GOLD  = (176, 124, 12)
INK   = (25, 20, 12)
DARK  = (20, 16, 11)
MUT   = (120, 105, 75)

class PDF(FPDF):
    def section_page(self):
        self.add_page()
    def h1(self, t):
        self.set_font("DejaVu", "B", 20); self.set_text_color(*GOLD)
        self.multi_cell(0, 11, t, new_x=XPos.LMARGIN, new_y=YPos.NEXT); self.ln(2)
    def h2(self, t):
        self.set_font("DejaVu", "B", 15); self.set_text_color(*INK)
        self.multi_cell(0, 9, t, new_x=XPos.LMARGIN, new_y=YPos.NEXT); self.ln(1)
    def h3(self, t):
        self.set_font("DejaVu", "B", 12); self.set_text_color(*GOLD)
        self.multi_cell(0, 8, t, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    def body(self, t):
        self.set_font("DejaVu", "", 10.5); self.set_text_color(*INK)
        self.multi_cell(0, 6.2, t, new_x=XPos.LMARGIN, new_y=YPos.NEXT); self.ln(1.5)
    def bullet(self, t):
        self.set_font("DejaVu", "", 10.5); self.set_text_color(*INK)
        self.multi_cell(0, 6.2, "\u2022  " + t, new_x=XPos.LMARGIN, new_y=YPos.NEXT); self.ln(1)
    def quote(self, t, src=""):
        self.set_font("DejaVu", "I", 10.5); self.set_text_color(*MUT)
        x = self.get_x(); self.set_x(x + 8)
        self.multi_cell(0, 6.2, "\u201c" + t + "\u201d" + (" \u2014 " + src if src else ""),
                        new_x=XPos.LMARGIN, new_y=YPos.NEXT); self.ln(1.5)
    def rule(self):
        self.ln(2); self.set_draw_color(*GOLD); self.set_line_width(0.6)
        self.line(20, self.get_y(), 190, self.get_y()); self.ln(4)
    def caption(self, t):
        self.set_font("DejaVu", "I", 9); self.set_text_color(*MUT)
        self.multi_cell(0, 5.5, t, align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT); self.ln(3)
    def table(self, headers, rows, widths=None, fs=9):
        W = self.w - self.l_margin - self.r_margin
        n = len(headers)
        if widths is None: widths = [W / n] * n
        self.set_font("DejaVu", "B", fs); self.set_text_color(*GOLD)
        self.set_fill_color(*DARK)
        for i, htxt in enumerate(headers):
            self.cell(widths[i], 7.5, htxt, border=1, align="C", fill=True)
        self.ln()
        self.set_font("DejaVu", "", fs); self.set_text_color(*INK)
        for row in rows:
            hmax = 6.5
            for i, val in enumerate(row):
                nl = max(1, int(self.get_string_width(str(val)) / (widths[i] - 2)) + 1)
                hmax = max(hmax, nl * 6.2)
            y0 = self.get_y()
            if y0 + hmax > self.h - 20: self.add_page(); y0 = self.get_y()
            x0 = self.l_margin
            for i, val in enumerate(row):
                self.set_xy(x0, y0)
                self.multi_cell(widths[i], 6.2, str(val), border=1, new_x=XPos.RIGHT, new_y=YPos.TOP)
                x0 += widths[i]
            self.set_y(y0 + hmax)
        self.ln(3)
    def cover(self, title, sub, lines):
        self.add_page(); self.ln(36)
        self.set_font("DejaVu", "B", 28); self.set_text_color(*GOLD)
        self.multi_cell(0, 15, title, align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT); self.ln(4)
        self.set_font("DejaVu", "", 13); self.set_text_color(*INK)
        self.multi_cell(0, 8, sub, align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT); self.ln(6)
        self.rule()
        for ln in lines:
            self.set_font("DejaVu", "", 10.5); self.set_text_color(*MUT)
            self.multi_cell(0, 7, ln, align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

def new_pdf():
    pdf = PDF(orientation="P", unit="mm", format="A4")
    pdf.set_auto_page_break(True, 20); pdf.set_margins(20, 18, 20)
    pdf.add_font("DejaVu", "", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")
    pdf.add_font("DejaVu", "B", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf")
    pdf.add_font("DejaVu", "I", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")
    pdf.add_font("DejaVu", "BI", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf")
    return pdf

def render_markup(pdf, text):
    for line in text.strip().split("\n"):
        s = line.strip()
        if not s: continue
        if s.startswith("## "): pdf.h2(s[3:])
        elif s.startswith("### "): pdf.h3(s[4:])
        elif s.startswith("- "): pdf.bullet(s[2:])
        elif s.startswith(">> "): pdf.quote(*s[3:].split(" || "))
        elif s.startswith(">>> "): pdf.caption(s[4:])
        else: pdf.body(s)

def colophon(pdf, edition_note):
    pdf.section_page(); pdf.h1("Colophon")
    pdf.body(
        "This Teacher's Edition was built 2026-10-18: " + edition_note +
        " Every quotation was checked against its source; every number recomputed. "
        "Brief quotations are given for study under fair use; the full texts are linked, never reproduced."
    )
    pdf.body(
        "Standing: findings, never doctrine. The correspondences stated here are read off the "
        "authors' own words; what is inferred beyond them is flagged as inferred. The red pen rules."
    )
    pdf.ln(6)
    pdf.set_font("DejaVu", "B", 13); pdf.set_text_color(*GOLD)
    pdf.multi_cell(0, 9, "Live, Love, and let Love, Live.", align="C",
                   new_x=XPos.LMARGIN, new_y=YPos.NEXT)

# Shared audit tables ---------------------------------------------------------
GEMATRIA_ROWS = [
    ["LOVE", "12+15+22+5", "54", "derived"],
    ["LIFE", "12+9+6+5", "32", "derived"],
    ["LIGHT", "12+9+7+8+20", "56", "derived"],
    ["LIBERTY", "12+9+2+5+18+20+25", "91", "derived"],
    ["Four L's total", "54+32+56+91", "233", "derived"],
    ["LION", "12+9+15+14", "50", "derived"],
    ["COW", "3+15+23", "41", "derived"],
    ["BABE", "2+1+2+5", "10", "derived"],
    ["EAGLE", "5+1+7+12+5", "30", "derived"],
    ["WISDOM", "23+9+19+4+15+13", "83", "derived"],
]
MARRIAGE_ROWS = [
    ["Lion", "The Wrath of the Master\nis the Energy of Love", "LOVE", "Law of Liberty;\nGnostic Mass Creed", "strength manifesto"],
    ["Cow", "The Work of the Master\nis the Nourishment of Life", "LIFE", "Law of Liberty", "greater community\n(the well of Life)"],
    ["Babe", "The Way of the Master\nis the Innocence of Liberty", "LIBERTY", "Law of Liberty", "strength (liberty\nof the individual)"],
    ["Eagle", "The Woe of the Master\nis the Rapture of Light", "LIGHT", "Law of Liberty;\nGnostic Mass Creed", "Jung essay\n(company of heaven)"],
    ["Wheel", "Wisdom = Justice\nof Time (observed)", "the harmony\nof the four", "\u2014", "\u2014"],
]

# ============================================================================
# EDITION A \u2014 THE IAO131 FOUR-L ESSAYS
# ============================================================================
pdf = new_pdf()
pdf.cover(
    "THE FOUR L'S",
    "Teacher's Edition A \u2014 The IAO131 Essays\nLight, Life, Love, Liberty",
    [
        "\u201cThe Law of your being becomes Light, Life, Love and Liberty.\u201d",
        "\u2014 Crowley, Liber DCCCXXXVII (The Law of Liberty)",
        "",
        "2026-10-18  \u00b7  93",
        "Johnathan 'Qasparr' (\u039a\u03b1\u03c3\u03c0\u03b1\u03c1\u03c1) Monroe, Keeper of the Secret Treasure",
        "All Rights Reserved, Without Prejudice",
        "Scientific Illuminism \u00b7 findings, never doctrine",
    ],
)

pdf.section_page(); pdf.h1("Preface: The Marriage")
pdf.body(
    "Two bodies of work, one formula. In Crowley's Heart of the Master, four living "
    "creatures stand around the Master's throne \u2014 and each speaks one of four words: "
    "Love, Life, Liberty, Light. In the essays of IAO131, the same four words return as "
    "a formula: the Law of Life, Light, Love, and Liberty, promulgated, established, "
    "and confessed. This edition presents the IAO131 side of the marriage: the essays "
    "summarized faithfully, quoted briefly for study, and linked whole."
)
pdf.body(
    "Copyright honesty: IAO131's essays are his. They are summarized here in our own "
    "words with brief quotations for study; the full texts live at iao131.com and are "
    "linked, never reproduced. Read! Judge! Keep silence \u2014 his own colophon."
)
pdf.body(
    "The four essays: (1) the \u201cstrength\u201d manifesto \u2014 the four L's as the AIM; "
    "(2) \u201cWhy should we contribute to the greater community?\u201d \u2014 the four L's as the LAW "
    "to promulgate; (3) the Jung / Gnostic Mass essay \u2014 the four L's as the CHURCH; "
    "(4) \u201cThelemic Eightfold Path pt.2\u201d \u2014 the four L's at their SOURCE, Crowley's own formula."
)

pdf.section_page(); pdf.h1("Part I \u2014 The Essays")

pdf.h2("1. \u201cStrength\u201d \u2014 a manifesto")
pdf.body("Source: iao131.com/tag/strength/ \u2014 a manifesto for every man and every woman who recognizes their own right to Divine Kingship.")
pdf.body(
    "Summary: the aim is the complete establishment of the Kingdom of Ra-Hoor-Khuit on earth \u2014 "
    "the permeating of all facets of life with the Word of Thelema. The proper spirit is overflowing joy "
    "and strength (never regret, malice, or sorrow); obstacles are chances to grow. Relations with the world: "
    "immerse in its fecundity, do not retreat \u2014 jobs, duties, children, laughter, all to the glory of "
    "Ra-Hoor-Khuit. Material things are not shunned. The daily regimen: a strong body and a concentrated mind; "
    "\u201cexceed! exceed!\u201d With fellow soldiers: each a pyramid, sufficient unto themselves \u2014 yet stars "
    "gather into galaxies, whose gravity is inconceivable."
)
pdf.quote("the establishment of Life, Liberty, Love, and Light in the hearts of all men.", "IAO131, \u201cstrength\u201d")
pdf.body("Teaching: here the four L's are the AIM \u2014 the telos of the manifesto, what the whole engine is for.")

pdf.h2("2. \u201cWhy should we contribute to the greater community?\u201d")
pdf.body("Source: iao131.com/tag/thelemites/ \u2014 the full essay, fetched 2026-10-18.")
pdf.body(
    "Summary: prologue \u2014 the alpha and omega is \u201cDo what thou wilt\u201d; the essay argues, not commands. "
    "A maturing view of True Will: from \u201cmy needs trump all\u201d to the star in the company of stars. "
    "The argument: communities band together to preserve and promulgate the Law \u2014 and the image is Crowley's "
    "well in the desert sheltered by four great palms (Liber CXXIV): the community nourishes all around it and is "
    "fortified thereby. Basic needs first \u2014 Crowley to Frieda Harris: food, shelter, love, freedom \u2014 "
    "Maslow's hierarchy four decades early. From \u201cDuty\u201d: relieve distress not from pity but to make manifest "
    "the perfection of the Universe. Objections answered: too Christian, too humanitarian, focus on our own."
)
pdf.quote("we band together into communities in order to preserve and promulgate the Law of Life, Light, Love, and Liberty.", "IAO131")
pdf.body("Teaching: here the four L's are the LAW \u2014 what is promulgated outward, the well with four palms.")

pdf.h2("3. The Jung essay \u2014 the Gnostic Mass Creed")
pdf.body("Source: iao131.com/tag/carl-jung/ \u2014 on the congregation as Final Heh of Tetragrammaton.")
pdf.body(
    "Summary: the People are the Final Heh \u2014 humanity, the Earth, the bride of Baphomet (Vav) as the Church "
    "is the bride of Christ. The Creed confesses \u201cone Gnostic and Catholic Church of Light, Life, Love and "
    "Liberty, the Word of whose Law is \u0398\u0395\u039b\u0397\u039c\u0391.\u201d The brethren are the company of heaven; "
    "each individual a source of Light and Life on earth as the stars are in heaven (Matthew 5:14: \u201cYe are "
    "the light of the world\u201d)."
)
pdf.quote("one Gnostic and Catholic Church of Light, Life, Love and Liberty", "Gnostic Mass Creed, via IAO131")
pdf.body("Teaching: here the four L's are the CHURCH \u2014 the collective body, the company of heaven.")

pdf.h2("4. \u201cThelemic Eightfold Path pt.2 \u2014 Right intention\u201d")
pdf.body("Source: iao131.livejournal.com/5294.html \u2014 quoting Liber DCCCXXXVII.")
pdf.body(
    "Summary: on samma sankappa \u2014 right resolve, the will to change; renunciation, freedom from ill will, "
    "harmlessness. AL II:70-72 (\u201cexceed! exceed!\u201d). The essay quotes Crowley's Law of Liberty at length, "
    "including the formula itself."
)
pdf.quote("The Law of your being becomes Light, Life, Love and Liberty.", "Liber DCCCXXXVII, via IAO131")
pdf.body("Teaching: here the four L's stand at their SOURCE \u2014 Crowley's own 1916 formula, Class E.")

pdf.section_page(); pdf.h1("Part II \u2014 Teaching the Four L's")
render_markup(pdf, """
## LIGHT
First in the Creed's order. "Ye are the light of the world" (Matthew 5:14) \u2014 the Jung essay's warrant for each individual as source. In the marriage: the Eagle's word, the Rapture of Light \u2014 woe transmuted to rapture.

## LIFE
"Remember all ye that existence is pure joy" (AL II:9, quoted in "strength"). The well of Life for those who struggle to subsist (greater community). In the marriage: the Cow's word, the Nourishment of Life \u2014 work transmuted to nourishment.

## LOVE
"Love is the law, love under will" (AL I:57). \u1f00\u03b3\u03ac\u03c0\u03b7 = 93 = \u03b8\u03ad\u03bb\u03b7\u03bc\u03b1 (attested; cf. the Ma'at Teacher's Edition). In the marriage: the Lion's word, the Energy of Love \u2014 wrath transmuted to energy.

## LIBERTY
"There is no law beyond Do what thou wilt" (AL III:60). The Law of Liberty itself (Liber DCCCXXXVII, 1916, Class E). In the marriage: the Babe's word, the Innocence of Liberty \u2014 the way transmuted to innocence.

## On the orders
The set is stable; the order is fluid \u2014 Light, Life, Love, Liberty (Creed, Law of Liberty); Life, Liberty, Love, Light (strength); Life, Light, Love, Liberty (greater community). Teach the set, not the sequence: four L's, one Law.
""")

pdf.section_page(); pdf.h1("Part III \u2014 The Marriage")
pdf.body(
    "The correspondence, read straight off Crowley's own words in the Vision. Each creature "
    "speaks its L; each L answers in the essays. Observed, not invented."
)
pdf.table(
    ["Creature (Heart of the Master)", "Word of the Master", "The L", "IAO131 witness"],
    [
        ["Lion", "\u201cThe Wrath of the Master\nis the Energy of Love.\u201d", "LOVE", "\u201cstrength\u201d: Love in\nthe hearts of all men"],
        ["Cow", "\u201cThe Work of the Master\nis the Nourishment of Life.\u201d", "LIFE", "\u201cgreater community\u201d:\nthe well of Life"],
        ["Babe", "\u201cThe Way of the Master\nis the Innocence of Liberty.\u201d", "LIBERTY", "\u201cstrength\u201d: liberty\nof the individual"],
        ["Eagle", "\u201cThe Woe of the Master\nis the Rapture of Light.\u201d", "LIGHT", "Jung essay: company\nof heaven, sources\nof Light & Life"],
    ],
    widths=[36, 52, 22, 60], fs=8.5,
)
pdf.body(
    "The fifth, observed: above the four whirls a wheel of many-coloured radiance \u2014 its utterance "
    "is of Wisdom and the Justice of Time, harmonizing all deeds in one. Four L's; one Justice. "
    "The teacher notes the Ma'at-resonance and stops there: observed, not decreed."
)
pdf.body(
    "What is genuine: the words match exactly \u2014 Love, Life, Liberty, Light in both corpora. "
    "What is inferred: that Crowley's 1925 vision and the modern essays draw one formula. Flagged as the "
    "compiler's reading, offered for the author's red pen."
)

pdf.section_page(); pdf.h1("Part IV \u2014 Audit Findings")
pdf.h2("TRVVTH ledger (Edition A)")
pdf.table(
    ["#", "Claim", "Source checked", "Result"],
    [
        ["1", "\u201cestablishment of Life, Liberty,\nLove, and Light...\u201d", "iao131.com/tag/strength/\n(fetched 2026-10-18)", "Verbatim"],
        ["2", "\u201cpreserve and promulgate\nthe Law of Life, Light,\nLove, and Liberty\u201d", "iao131.com/tag/thelemites/\n(fetched 2026-10-18)", "Verbatim"],
        ["3", "Creed: \u201cChurch of Light,\nLife, Love and Liberty\u201d", "Gnostic Mass (Liber XV),\nvia iao131.com/tag/carl-jung/", "Standard text"],
        ["4", "\u201cThe Law of your being\nbecomes Light, Life,\nLove and Liberty\u201d", "Liber DCCCXXXVII \u2014\nthe-equinox.org, oto-bg.org", "Verbatim (3 sources)"],
        ["5", "\u201cWalk forth with us in\nLight and Life and\nLove and Liberty\u201d", "Liber DCCCXXXVII, \u00a76", "Verbatim"],
        ["6", "Four creature utterances", "Heart of the Master\n(O.T.O. 1985 e.v. text)", "Verbatim"],
        ["7", "HotM: 1925 / 1938 / Class B", "Wikipedia; hellfireclubbooks", "Confirmed"],
        ["8", "Correspondence table", "Both corpora", "Observed \u2014 words\nmatch exactly"],
    ],
    widths=[10, 52, 52, 56], fs=8.5,
)
pdf.h2("PONTIFEX findings (English ordinal \u2014 native for English)")
pdf.table(
    ["Term", "Breakdown", "Value", "Tier"],
    GEMATRIA_ROWS,
    widths=[36, 62, 22, 50], fs=9,
)
pdf.body(
    "Findings: LOVE=54, LIFE=32, LIGHT=56, LIBERTY=91; the four sum to 233. The creatures: "
    "LION=50, COW=41, BABE=10, EAGLE=30. WISDOM=83 \u2014 verified: not a bridge. It coincides "
    "with FAFO=83, but FAFO's 83 rides the author's own cipher (F\u2192Vav, O\u2192Ayin \u2014 free "
    "choices; F\u2192\u05e4 alone makes it 231), so the bank is not honest, and no honest-bank pairing "
    "yields 83=83 anywhere. What stands without the numbers is the semantic correspondence: "
    "wisdom is acquired through trial and error. The author's dictum:"
)
pdf.quote("Experience is the only real pathway to wisdom.", "the author, 2026-10-18")
pdf.h2("Verdict")
pdf.body("TRVVTH: PASS \u2014 8/8 ledger entries verified or honestly flagged. PONTIFEX: PASS \u2014 10/10 recomputed. Zero falsehoods.")

colophon(pdf, "the four IAO131 essays summarized, quoted briefly for study, and linked whole; the marriage with Heart of the Master stated as observed correspondence.")
pdf.output(os.path.join(HERE, "teachers-edition-a-four-l-essays.pdf"))
print("A done", os.path.getsize(os.path.join(HERE, "teachers-edition-a-four-l-essays.pdf")))

# ============================================================================
# EDITION B \u2014 HEART OF THE MASTER
# ============================================================================
pdf = new_pdf()
pdf.cover(
    "HEART OF THE MASTER",
    "Teacher's Edition B \u2014 Crowley's Vision, Married with the Four L's",
    [
        "\u201cThe Wrath of the Master is the Energy of Love.\u201d",
        "\u2014 The Vision",
        "",
        "2026-10-18  \u00b7  93",
        "Johnathan 'Qasparr' (\u039a\u03b1\u03c3\u03c0\u03b1\u03c1\u03c1) Monroe, Keeper of the Secret Treasure",
        "All Rights Reserved, Without Prejudice",
        "Scientific Illuminism \u00b7 findings, never doctrine",
    ],
)

pdf.section_page(); pdf.h1("Preface: The Work and Its Standing")
pdf.body(
    "The Heart of the Master, by Aleister Crowley (as Khaled Khan): written mostly in 1925 at "
    "Sidi Bou Said, Tunisia; first published 1938 by the O.T.O. in a limited edition of 100. "
    "Crowley classed it B \u2014 ordinary scholarship, not revelation \u2014 though its reception "
    "(trance-vision in the Mediterranean, his proclamation as Ipsissimus, \u201cTO MAN\u201d) borders the inspired."
)
pdf.body(
    "Copyright honesty: the work is the O.T.O.'s. It is summarized here in our own words with "
    "brief quotations for study; the full text (e.g., the archive.org e-text of the 1985 O.T.O. "
    "edition) is linked, never reproduced."
)
pdf.body(
    "Three parts: I. The Vision \u2014 the sleeping army, the Voice, the Hill, the Master, the four "
    "living creatures, the wheel, the nine birds. II. The Voice \u2014 the Tree of Life exposition. "
    "III. The Temple of Truth \u2014 the Great White Brotherhood, the emissaries, and \u201cThe Mystery of Sin.\u201d"
)

pdf.section_page(); pdf.h1("Part I \u2014 The Work, Summarized")

pdf.h2("I. The Vision")
pdf.body(
    "Penumbra: the narrator among a sleeping concourse on a fog-bound plain \u2014 lethargy, not "
    "exhaustion; a few half-awake, gazing east where no light answers. Vox: a soldier's voice rings "
    "from behind \u2014 \u201cBehold, the Star in the West!\u201d \u2014 and a whisper of absolute authority: "
    "\u201cZero is Two.\u201d The sleepers mock (\u201cStar in the West? Beware: that is the Star called Wormwood\u201d). "
    "Umbra/Phantasma: nightmare \u2014 blood, mud, phantoms \u2014 exhausting itself into stupor. Lux: waking \u2014 "
    "the Star is a Sun piercing the mists; the spectres were shadows cast by light on vapour. "
    "The Hill: a colossal pyramid crowned by a silent figure against the Sun's orb."
)
pdf.body(
    "Homo: the Master \u2014 helm of ruddy gold, the black diamond between his brows, arms folded, "
    "rod of amber in the right hand, amethyst lotus in the left; tears of mingled sorrow and joy "
    "melt the rock and roses spring. Around him four living creatures, begotten of his will:"
)
pdf.quote("The Wrath of the Master is the Energy of Love.", "the Lion")
pdf.quote("The Work of the Master is the Nourishment of Life.", "the Cow")
pdf.quote("The Way of the Master is the Innocence of Liberty.", "the Babe")
pdf.quote("The Woe of the Master is the Rapture of Light.", "the Eagle")
pdf.body(
    "Above them whirls a wheel of many-coloured radiance harmonizing all deeds in one \u2014 its utterance "
    "is of Wisdom and the Justice of Time. A serpent with a sphinx's head touches the Master's mouth; "
    "His voice breaks into song: the Word of the Law is Thelema. Then the Aves: nine birds \u2014 swan, "
    "phoenix, raven, eagle, hawk, pelican, dove, ibis, vulture \u2014 each singing one part of the Spirit. "
    "The seer is absorbed: \u201cnothing separate any more at all.\u201d"
)

pdf.h2("II. The Voice")
pdf.body(
    "Summary: the narrator, fallen from rapture, is attuned \u201cjust so far\u201d to the Heart. What follows "
    "is the Tree of Life exposition \u2014 the ten sephiroth and the twenty-two paths \u2014 the Qabalistic "
    "anatomy underlying the Vision. (Per the publisher's account; the e-text's second movement.)"
)

pdf.h2("III. The Temple of Truth")
pdf.body(
    "Summary: the philosophical foundations of the Great White Brotherhood \u2014 those guiding mankind's "
    "spiritual evolution since time immemorial. The emissaries: one of their fellows every two thousand "
    "years with one Word as a new formula of Magick; lesser prophets at intervals to prepare the Way. "
    "The chart of names Khaled Khan could partly read. The close: \u201cThe Mystery of Sin\u201d \u2014 among the "
    "most concentrated instructions on True Will in the corpus: sin is restriction; the aspirant is sent "
    "back to it with regularity."
)

pdf.section_page(); pdf.h1("Part II \u2014 Teaching")
render_markup(pdf, """
## The fourfold engine
Teach the paradoxical pairings \u2014 this is the Vision's whole method: Wrath/Energy, Work/Nourishment, Way/Innocence, Woe/Rapture. Each creature transmutes its shadow term into its L: wrath becomes energy (not abolished), work becomes nourishment, the way becomes innocence, woe becomes rapture. Nothing is denied; everything is transmuted. That is the Master's alchemy, and the student should feel the pattern before naming it.

## The wheel: the fifth
Above the four, the wheel harmonizes all deeds in one \u2014 Wisdom as the Justice of Time. Four L's; one Justice. Teach it as observed: the text puts the wheel above the creatures, and its word is justice. The Ma'at-resonance (the feather, the balance) is noted and left open \u2014 genuine parallel, not forced identity.

## Class B honesty
The book's own classification is the teaching: a trance-vision, classed as scholarship. Teach the student to hold both \u2014 the remarkable circumstances (the journal: the trance, the inverted cone of blue light seen by another) and the sober classification. The Law does not need every text to be revelation; Class B is not a demotion.

## The Mystery of Sin
Close with the book's practical keystone: the instructions on sin as restriction, and the aspirant's discipline of returning to the study. "Do what thou wilt" is not a slogan here but a formula with a mystery attached \u2014 and the mystery is precision about the Will.
""")

pdf.section_page(); pdf.h1("Part III \u2014 The Marriage")
pdf.body(
    "From this side: the Vision's four creatures speak the four L's \u2014 and the four L's are "
    "independently attested as a Thelemic formula: Crowley's Liber DCCCXXXVII (1916, Class E), "
    "the Gnostic Mass Creed (Liber XV), and IAO131's essays carrying the meme into the present "
    "(the \u201cstrength\u201d manifesto, the greater-community essay, the Jung essay)."
)
pdf.table(
    ["Creature", "Word of the Master", "The L", "Formula witness"],
    [
        ["Lion", "\u201cThe Wrath of the Master\nis the Energy of Love.\u201d", "LOVE", "DCCCXXXVII; Creed;\nIAO131 \u201cstrength\u201d"],
        ["Cow", "\u201cThe Work of the Master\nis the Nourishment of Life.\u201d", "LIFE", "DCCCXXXVII;\nIAO131 (well of Life)"],
        ["Babe", "\u201cThe Way of the Master\nis the Innocence of Liberty.\u201d", "LIBERTY", "DCCCXXXVII\n(Law of Liberty)"],
        ["Eagle", "\u201cThe Woe of the Master\nis the Rapture of Light.\u201d", "LIGHT", "DCCCXXXVII; Creed;\nIAO131 Jung essay"],
        ["Wheel", "Wisdom = Justice of Time\n(observed)", "harmony", "\u2014"],
    ],
    widths=[28, 56, 22, 64], fs=8.5,
)
pdf.body(
    "The marriage statement: the throne-vision of 1925 and the present-day essays speak one "
    "fourfold \u2014 not by borrowing (no borrowing is claimed) but by convergence on the formula "
    "Crowley himself fixed in 1916. Four creatures; four L's; one Law. Offered for the red pen."
)

pdf.section_page(); pdf.h1("Part IV \u2014 Audit Findings")
pdf.h2("TRVVTH ledger (Edition B)")
pdf.table(
    ["#", "Claim", "Source checked", "Result"],
    [
        ["1", "Four creature utterances", "archive.org e-text\n(O.T.O. 1985 ed.)", "Verbatim"],
        ["2", "Written 1925, Sidi Bou Said;\npub. 1938; Class B", "Wikipedia; hellfireclubbooks", "Confirmed"],
        ["3", "\u201cTO MAN\u201d proclamation;\nIpsissimus", "hellfireclubbooks;\nacademia.edu", "Confirmed"],
        ["4", "Three parts: Vision /\nVoice / Temple of Truth", "Wikipedia; publisher", "Confirmed"],
        ["5", "\u201cThe Mystery of Sin\u201d\nas closing section", "hellfireclubbooks", "Confirmed"],
        ["6", "Emissaries every\n2000 years", "academia.edu\n(HotM analysis)", "Confirmed"],
        ["7", "Correspondence table", "HotM text + formula\nwitnesses", "Observed \u2014 words\nmatch exactly"],
    ],
    widths=[10, 52, 52, 56], fs=8.5,
)
pdf.h2("PONTIFEX findings (English ordinal)")
pdf.table(
    ["Term", "Breakdown", "Value", "Tier"],
    GEMATRIA_ROWS,
    widths=[36, 62, 22, 50], fs=9,
)
pdf.body(
    "Findings as in Edition A: LOVE=54, LIFE=32, LIGHT=56, LIBERTY=91 (sum 233); "
    "LION=50, COW=41, BABE=10, EAGLE=30; WISDOM=83 \u2014 verified: not a bridge "
    "(FAFO's 83 rides the author's cipher; no honest-bank pairing yields 83=83). "
    "The semantic correspondence stands without the numbers: wisdom is acquired "
    "through trial and error. The author's dictum:"
)
pdf.quote("Experience is the only real pathway to wisdom.", "the author, 2026-10-18")
pdf.h2("Verdict")
pdf.body("TRVVTH: PASS \u2014 7/7 verified or honestly flagged. PONTIFEX: PASS \u2014 10/10 recomputed. Zero falsehoods.")

colophon(pdf, "Crowley's Heart of the Master summarized with brief study quotations; the marriage with the Four-L essays stated as observed correspondence.")
pdf.output(os.path.join(HERE, "teachers-edition-b-heart-of-the-master.pdf"))
print("B done", os.path.getsize(os.path.join(HERE, "teachers-edition-b-heart-of-the-master.pdf")))
