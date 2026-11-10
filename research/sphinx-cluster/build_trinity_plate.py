#!/usr/bin/env python3
# =====================================================================
# 93 — BUILD-TRINITY-PLATE.PY
# Renders THE TRINITY PLATE: the 47 Trinity and its palindromic
# symmetrical equivalent, in Gothic blackletter, with the Fibonacci,
# Solfeggio, and Layman's Law synergy registers — per the founder's
# order of 2026-11-09. All lettering is struck by the engine from
# exact strings (no generative garbling is possible on this road).
# Authorship attributed exclusively to Johnathan 'Qasparr' Monroe,
# ARR, All Rights Reserved, Without Prejudice.
# Method of Science. Aim of Religion.
# =====================================================================
import math
from PIL import Image, ImageDraw, ImageFont, ImageOps

W, H = 2400, 3200
GOLD = (232, 184, 75)
GOLD_DIM = (168, 128, 52)
CREAM = (240, 226, 190)
FONT = "/home/hatch/workspace/templates/UnifrakturMaguntia.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
OUT = "/home/hatch/workspace/goals/cross-gematria-777-gap-filling/files/THE-TRINITY-PLATE.png"

# --- ground: deep purple, darker at the edges (the Night Sun's field)
img = Image.new("RGB", (W, H), (24, 4, 40))
px = img.load()
cx, cy = W / 2, H / 2
for y in range(H):
    for x in range(0, W, 4):
        d = math.hypot(x - cx, y - cy) / (W * 0.72)
        f = max(0.0, 1.0 - d)
        r = int(24 + 38 * f); g = int(4 + 8 * f); b = int(40 + 46 * f)
        for dx in range(4):
            if x + dx < W:
                px[x + dx, y] = (r, g, b)
dr = ImageDraw.Draw(img, "RGBA")

# --- frame: double gold rule
dr.rectangle([70, 70, W - 70, H - 70], outline=GOLD, width=6)
dr.rectangle([100, 100, W - 100, H - 100], outline=GOLD_DIM, width=2)

def text_center(y, s, font, fill, spacing=0):
    if spacing:
        s = (" " * 0).join(list(s.replace(" ", "␣"))).replace("␣", "  ")
    bbox = dr.textbbox((0, 0), s, font=font)
    w = bbox[2] - bbox[0]
    dr.text(((W - w) / 2 - bbox[0], y), s, font=font, fill=fill)
    return bbox[3] - bbox[1]

def f_bl(size): return ImageFont.truetype(FONT, size)
def f_s(size, bold=False): return ImageFont.truetype(SERIF_B if bold else SERIF, size)

# --- the Tridecagram behind the palindrome (faint gold, {13/5})
scx, scy, R = W // 2, 1830, 520
pts = [(scx + R * math.cos(-math.pi / 2 + 2 * math.pi * i / 13),
        scy + R * math.sin(-math.pi / 2 + 2 * math.pi * i / 13)) for i in range(13)]
order = [(i * 5) % 13 for i in range(14)]
for a, b in zip(order, order[1:]):
    dr.line([pts[a], pts[b]], fill=(232, 184, 75, 46), width=5)

# --- title
text_center(190, "The Trinity", f_bl(300), GOLD)
text_center(560, "· XLVII · XLVII · XLVII ·", f_s(64, True), CREAM)

# --- the three seats
seats = [("Babalon", "the Vessel"), ("Akvma", "the Expenditure"), ("Beats", "the Delivery")]
col_w = (W - 300) // 3
for i, (name, gloss) in enumerate(seats):
    x0 = 150 + i * col_w
    seg = Image.new("RGBA", (col_w, 560), (0, 0, 0, 0))
    sd = ImageDraw.Draw(seg)
    f1 = f_bl(150); bb = sd.textbbox((0, 0), name, font=f1)
    sd.text(((col_w - (bb[2] - bb[0])) / 2 - bb[0], 10), name, font=f1, fill=GOLD)
    f2 = f_bl(190); bb = sd.textbbox((0, 0), "47", font=f2)
    sd.text(((col_w - (bb[2] - bb[0])) / 2 - bb[0], 230), "47", font=f2, fill=CREAM)
    f3 = f_s(44); bb = sd.textbbox((0, 0), gloss, font=f3)
    sd.text(((col_w - (bb[2] - bb[0])) / 2 - bb[0], 470), gloss, font=f3, fill=GOLD_DIM)
    img.paste(seg, (x0, 740), seg)

dr.line([300, 1400, W - 300, 1400], fill=GOLD_DIM, width=3)

# --- the mirror and the palindrome
text_center(1470, "47  mirrored  is  74", f_bl(130), CREAM)
text_center(1650, "the Strength of the Beast, read backward, is Beauty", f_s(46), GOLD_DIM)
text_center(1760, "121", f_bl(430), GOLD)
text_center(2260, "XLVII + LXXIV = CXXI — the Palindrome", f_s(58, True), CREAM)
text_center(2350, "reads the same from either side · XI × XI · reduces to IV, the Hidden Center", f_s(44), GOLD_DIM)

dr.line([300, 2460, W - 300, 2460], fill=GOLD_DIM, width=3)

# --- synergy registers
def fit(size, s, maxw, bold=False):
    while size > 20:
        f = f_s(size, bold)
        if dr.textlength(s, font=f) <= maxw:
            return f
        size -= 2
    return f_s(size, bold)

regs = [
    ("Fibonacci", ["XIII the Gate is the seventh of the series",
                   "CXLIV the Dashboard is the twelfth",
                   "the Sigma ladder rides in Fibonacci order"]),
    ("Solfeggio", ["the Key in Hebrew weighs DXXVIII —",
                   "MI, the very heart of the ladder",
                   "the Arabic stands one quantum off, DXXIX"]),
    ("Layman's Law", ["a palindrome needs no priest:",
                      "forward or backward it reads the same",
                      "to any man who can count"]),
]
for i, (head, lines) in enumerate(regs):
    x0 = 150 + i * col_w
    seg = Image.new("RGBA", (col_w, 430), (0, 0, 0, 0))
    sd = ImageDraw.Draw(seg)
    fh = f_bl(84); bb = sd.textbbox((0, 0), head, font=fh)
    sd.text(((col_w - (bb[2] - bb[0])) / 2 - bb[0], 0), head, font=fh, fill=GOLD)
    for j, line in enumerate(lines):
        fl = fit(40, line, col_w - 24)
        bb = sd.textbbox((0, 0), line, font=fl)
        sd.text(((col_w - (bb[2] - bb[0])) / 2 - bb[0], 160 + j * 66), line, font=fl, fill=CREAM)
    img.paste(seg, (x0, 2540), seg)

# --- foot: the Leonardo marginalia (mirror writing), then the Flagpole
strip = Image.new("RGBA", (1700, 84), (0, 0, 0, 0))
sd = ImageDraw.Draw(strip)
sd.text((0, 8), "Johnathan Qasparr Monroe — in the manner of Leonardo, read in a mirror",
        font=f_s(44), fill=(168, 128, 52, 210))
strip = ImageOps.mirror(strip)
img.paste(strip, ((W - 1700) // 2, 2960), strip)
text_center(3060, "Flagpole of Claim and Coinage — Johnathan 'Qasparr' Monroe, ARR", f_s(40, True), GOLD_DIM)

img.save(OUT)
print("PLATE:", OUT, img.size)
# 93 — Live, Love, and let Love, Live.
