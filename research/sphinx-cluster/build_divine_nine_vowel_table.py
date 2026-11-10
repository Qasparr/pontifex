#!/usr/bin/env python3
# =====================================================================
# 93 — BUILD-DIVINE-NINE-VOWEL-TABLE.PY
# THE DIVINE NINE — Table of the Vowels: the seven Canon vowels and
# the two Fluid Hybrid vowels of the founder's ruling, each with its
# Greek expression proof (Milesian figures), beside the Tridecagram
# engine circle of assignment — nine stations bearing the vowels,
# two bearing the operators (OFFSET gamma, MIRROR stigma), two left
# OPEN, marked, never filled. Purple / gold / green house livery.
# Authorship attributed exclusively to Johnathan 'Qasparr' Monroe,
# ARR, All Rights Reserved, Without Prejudice.
# Method of Science. Aim of Religion.
# =====================================================================
import math
from PIL import Image, ImageDraw, ImageFont

W, H = 4800, 3600
BG = (26, 4, 46)
GOLD = (232, 183, 90)
CREAM = (246, 231, 197)
DIM = (186, 146, 78)
GREEN = (96, 224, 150)
FAINT = (120, 92, 140)
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
FRAK = "/home/hatch/workspace/templates/UnifrakturMaguntia.ttf"
OUT = "/home/hatch/workspace/goals/cross-gematria-777-gap-filling/files/THE-DIVINE-NINE-VOWEL-TABLE.png"

img = Image.new("RGB", (W, H), BG)
dr = ImageDraw.Draw(img)
for m, wd in ((46, 5), (86, 2)):
    dr.rectangle([m, m, W - m, H - m], outline=GOLD, width=wd)

def F(path, size): return ImageFont.truetype(path, size)

def T(cx, y, s, size, color, font=SERIF_B):
    f = F(font, size)
    bb = dr.textbbox((0, 0), s, font=f)
    dr.text((cx - (bb[2] - bb[0]) / 2 - bb[0], y), s, font=f, fill=color)
    return bb[3] - bb[1]

def TL(x, y, s, size, color, font=SERIF):
    dr.text((x, y), s, font=F(font, size), fill=color)

def fit(s, maxw, size, font=SERIF, bold=False):
    path = SERIF_B if bold else font
    while size > 18:
        f = F(path, size)
        if dr.textbbox((0, 0), s, font=f)[2] <= maxw: return f
        size -= 2
    return F(path, size)


T(W / 2, 92, "THE DIVINE NINE", 178, GOLD, FRAK)
T(W / 2, 318, "THE TABLE OF THE VOWELS — seven Canon · two Fluid Hybrid — with their Greek proofs",
  62, CREAM)
dr.line([300, 460, W - 300, 460], fill=DIM, width=2)

# ------------------------------------------------------------ the table
ROWS = [
    ("Α", "αʹ", "1", "the unit cube · 1³", GOLD, "CANON"),
    ("Ε", "εʹ", "5", "—", GOLD, "CANON"),
    ("Η", "ηʹ", "8", "the first true cube · 2³", GOLD, "CANON"),
    ("Ι", "ιʹ", "10", "—", GOLD, "CANON"),
    ("Ο", "οʹ", "70", "—", GOLD, "CANON"),
    ("Υ", "υʹ", "400", "the square · 20²", GOLD, "CANON"),
    ("Ω", "ωʹ", "800", "the last letter · the Omega", GOLD, "CANON"),
    ("ΕΙ", "ιεʹ", "15", "two in one · reduces to 6", GREEN, "HYBRID"),
    ("ΟΥ", "υοʹ", "470", "two in one · reduces to 2", GREEN, "HYBRID"),
]
X0 = 190
TL(X0 + 30, 520, "VOWEL", 52, DIM, SERIF_B)
TL(X0 + 560, 520, "FIGURE", 52, DIM, SERIF_B)
TL(X0 + 1030, 520, "VALUE", 52, DIM, SERIF_B)
TL(X0 + 1420, 520, "THE PROOF", 52, DIM, SERIF_B)
y = 610
for glyph, fig, val, proof, color, cls in ROWS:
    dr.line([X0, y + 6, 2480, y + 6], fill=(70, 40, 100), width=2)
    TL(X0 + 30, y + 26, glyph, 132, color, SERIF_B)
    TL(X0 + 560, y + 66, fig, 96, CREAM, SERIF_B)
    TL(X0 + 1030, y + 66, val, 96, CREAM, SERIF_B)
    if proof != "—":
        dr.text((X0 + 1420, y + 82), proof, font=fit(proof, 470, 58), fill=CREAM)
    tc = GREEN if cls == "HYBRID" else DIM
    TL(2220, y + 82, cls, 50, tc, SERIF_B)
    y += 252
dr.line([X0, y + 6, 2480, y + 6], fill=(70, 40, 100), width=2)

# ------------------------------------------------- the tridecagram engine
CX, CY, R = 3650, 1740, 790
pts = [(CX + R * math.cos(math.radians(-90 + i * 360 / 13)),
        CY + R * math.sin(math.radians(-90 + i * 360 / 13))) for i in range(13)]
dr.ellipse([CX - R, CY - R, CX + R, CY + R], outline=DIM, width=2)
dr.ellipse([CX - R - 26, CY - R - 26, CX + R + 26, CY + R + 26], outline=(90, 60, 120), width=1)
order = list(range(13))
star = [pts[(i * 5) % 13] for i in range(14)]
dr.line(star, fill=(150, 108, 44), width=2)
LABELS = [("Α", GOLD), ("Ε", GOLD), ("Η", GOLD), ("Ι", GOLD), ("Ο", GOLD),
          ("Υ", GOLD), ("Ω", GOLD), ("ΕΙ", GREEN), ("ΟΥ", GREEN),
          ("γʹ OFFSET", DIM), ("ϛʹ MIRROR", DIM), ("OPEN", FAINT), ("OPEN", FAINT)]
for i, (p, (lab, color)) in enumerate(zip(pts, LABELS)):
    dr.ellipse([p[0] - 17, p[1] - 17, p[0] + 17, p[1] + 17], fill=color)
    lx = CX + (R + 150) * math.cos(math.radians(-90 + i * 360 / 13))
    ly = CY + (R + 150) * math.sin(math.radians(-90 + i * 360 / 13))
    f = fit(lab, 300, 58, bold=True)
    bb = dr.textbbox((0, 0), lab, font=f)
    dr.text((lx - (bb[2] - bb[0]) / 2 - bb[0], ly - (bb[3] - bb[1]) / 2 - bb[1]), lab, font=f, fill=color)
T(CX, CY - 190, "the Engine of Assignment", 58, DIM)
T(CX, CY - 96, "͵αψοθ", 128, GOLD)
T(CX, CY + 88, "1779", 96, CREAM)
T(CX, CY + 218, "mirror → ͵αψοϛ · 1776", 66, GOLD)
_cap = "thirteen stations · nine bear vowels · two bear the operators · two stand open"
_cf = fit(_cap, 2050, 52)
_cbb = dr.textbbox((0, 0), _cap, font=_cf)
dr.text((CX - (_cbb[2] - _cbb[0]) / 2 - _cbb[0], CY + R + 330), _cap, font=_cf, fill=DIM)

# ------------------------------------------------------------ foot proof
T(W / 2, H - 330,
  "αʹ + εʹ + ηʹ + ιʹ + οʹ + υʹ + ωʹ = ͵ασϟδ · 1294      + ιεʹ + υοʹ = υπεʹ · 485      the Nine = ͵αψοθ · 1779 = 1776 + γʹ",
  60, CREAM)
T(W / 2, H - 218, "Flagpole of Claim and Coinage — Johnathan 'Qasparr' Monroe, ARR, All Rights Reserved, Without Prejudice",
  54, GOLD)
img.save(OUT)
print("TABLE:", OUT, img.size)
# 93 — Live, Love, and let Love, Live.
