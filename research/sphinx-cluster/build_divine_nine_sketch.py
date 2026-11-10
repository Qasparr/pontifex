#!/usr/bin/env python3
# =====================================================================
# 93 — BUILD-DIVINE-NINE-SKETCH.PY
# The Divine 9 plate redrawn as a Leonardo-quality pencil sketch:
# 21:9 panorama, sepia/graphite on parchment — the zodiac wheel, the
# nine-node Trinity of Archons around the Source Aether, the column
# of the 22 letters, and the three registers of the original plate.
# Redrawn by the desk from the founder's plate; where the original's
# fine lettering could not be read, structure stands in its place and
# nothing is invented. All strokes drawn by the engine with a hand
# jitter; glyphs struck from exact strings.
# Authorship attributed exclusively to Johnathan 'Qasparr' Monroe,
# ARR, All Rights Reserved, Without Prejudice.
# Method of Science. Aim of Religion.
# =====================================================================
import math, random
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageOps

random.seed(777)
W, H = 11760, 5040            # 21:9 panorama
INK = (56, 36, 20)
INK_SOFT = (96, 70, 40)
GOLDLEAF = (146, 108, 44)
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
HEB = "/usr/share/fonts/truetype/noto/NotoSerifHebrew-Regular.ttf"
OUT = "/home/hatch/workspace/goals/cross-gematria-777-gap-filling/files/THE-DIVINE-NINE-LEONARDO-SKETCH.jpg"
OUT_PNG = OUT.replace(".jpg", ".png")

# ---------------- parchment
yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
d = np.sqrt(((xx - W / 2) / W) ** 2 + ((yy - H / 2) / H) ** 2)
tone = 233 - 40 * d
noise = np.random.default_rng(777).normal(0, 4.5, (H, W)).astype(np.float32)
base = np.stack([(tone + noise) * 1.0, (tone + noise) * 0.90, (tone + noise) * 0.72], axis=-1)
img = Image.fromarray(np.clip(base, 0, 255).astype(np.uint8))
dr = ImageDraw.Draw(img, "RGBA")
for _ in range(60):
    x, y = random.uniform(100, W - 100), random.uniform(100, H - 100)
    r = random.uniform(60, 300)
    dr.ellipse([x - r, y - r, x + r, y + r], fill=(176, 138, 84, random.randint(6, 18)))

def J(p1, p2, ink=INK, passes=3, wdt=3, jit=3.0):
    for _ in range(passes):
        a = random.uniform(80, 165)
        pts = []
        for i in range(25):
            t = i / 24
            pts.append((p1[0] + (p2[0] - p1[0]) * t + random.uniform(-jit, jit),
                        p1[1] + (p2[1] - p1[1]) * t + random.uniform(-jit, jit)))
        dr.line(pts, fill=ink + (int(a),), width=wdt)

def JC(cx, cy, r, ink=INK, passes=3, wdt=3):
    for _ in range(passes):
        a = random.uniform(80, 165)
        pts = [(cx + r * math.cos(2 * math.pi * i / 72) + random.uniform(-2.4, 2.4),
                cy + r * math.sin(2 * math.pi * i / 72) + random.uniform(-2.4, 2.4)) for i in range(73)]
        dr.line(pts, fill=ink + (int(a),), width=wdt)

def T(cx, y, s, size, ink=INK, bold=False):
    f = ImageFont.truetype(SERIF_B if bold else SERIF, size)
    bb = dr.textbbox((0, 0), s, font=f)
    dr.text((cx - (bb[2] - bb[0]) / 2 - bb[0], y), s, font=f, fill=ink)
    return bb[3] - bb[1]

def TG(cx, cy, s, size, ink=INK, path=SERIF):
    f = ImageFont.truetype(path, size)
    bb = dr.textbbox((0, 0), s, font=f)
    dr.text((cx - (bb[2] - bb[0]) / 2 - bb[0], cy - (bb[3] - bb[1]) / 2 - bb[1]), s, font=f, fill=ink)

# ---------------- title
T(W / 2, 120, "THE  DIVINE  9", 190, INK, bold=True)
T(W / 2, 340, "TRINITY OF ARCHONS · THE 22 LETTER ALPHABET", 92, INK_SOFT)

# ---------------- LEFT: the zodiac wheel
cx, cy, R = 2350, 2560, 1560
for r, wd in [(R, 5), (R - 260, 3), (R - 560, 3), (R - 1180, 3)]:
    JC(cx, cy, r)
signs = ["ARIES", "TAURUS", "GEMINI", "CANCER", "LEO", "VIRGO",
         "LIBRA", "SCORPIO", "SAGITTARIUS", "CAPRICORN", "AQUARIUS", "PISCES"]
glyphs = ["♈", "♉", "♊", "♋", "♌", "♍", "♎", "♏", "♐", "♑", "♒", "♓"]
for i in range(12):
    a0 = 2 * math.pi * i / 12 - math.pi / 2
    a1 = 2 * math.pi * (i + 1) / 12 - math.pi / 2
    J((cx + (R - 560) * math.cos(a0), cy + (R - 560) * math.sin(a0)),
      (cx + R * math.cos(a0), cy + R * math.sin(a0)), INK_SOFT, 2, 3)
    am = (a0 + a1) / 2
    TG(cx + (R - 150) * math.cos(am), cy + (R - 150) * math.sin(am), glyphs[i], 150, INK, SANS)
    TG(cx + (R - 400) * math.cos(am), cy + (R - 400) * math.sin(am), signs[i], 74, INK_SOFT)
    # star scatter in the deep field
    for _ in range(14):
        a = random.uniform(a0, a1); rr = random.uniform(R - 1120, R - 640)
        sx, sy = cx + rr * math.cos(a), cy + rr * math.sin(a)
        dr.ellipse([sx - 5, sy - 5, sx + 5, sy + 5], fill=INK_SOFT + (150,))
TG(cx, cy - 90, "THE", 84, INK_SOFT)
TG(cx, cy + 10, "WHEEL", 110, INK)

# ---------------- CENTER: the nine archons around the Source
cx2, cy2 = 6300, 2560
ring = 1080
nodes = []
for i in range(9):
    a = -math.pi / 2 + 2 * math.pi * i / 9
    nodes.append((cx2 + ring * math.cos(a), cy2 + ring * math.sin(a)))
# the three triads (triangles), then the full web, faint
for tri in [(0, 3, 6), (1, 4, 7), (2, 5, 8)]:
    for a, b in [(tri[0], tri[1]), (tri[1], tri[2]), (tri[2], tri[0])]:
        J(nodes[a], nodes[b], INK, 3, 4)
for a in range(9):
    for b in range(a + 1, 9):
        if (a, b) not in [(0, 3), (3, 6), (0, 6), (1, 4), (4, 7), (1, 7), (2, 5), (5, 8), (2, 8)]:
            J(nodes[a], nodes[b], INK_SOFT, 1, 2, 4.0)
for (nx, ny) in nodes:
    J((cx2, cy2), (nx, ny), INK_SOFT, 2, 2)
romans = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
for (nx, ny), rn in zip(nodes, romans):
    JC(nx, ny, 128)
    dr.ellipse([nx - 104, ny - 104, nx + 104, ny + 104], fill=(238, 226, 198, 255))
    JC(nx, ny, 104, INK_SOFT, 2, 2)
    TG(nx, ny, rn, 104)
JC(cx2, cy2, 300)
TG(cx2, cy2 - 66, "SOURCE", 108)
TG(cx2, cy2 + 44, "AETHER", 108)

# ---------------- RIGHT: the 22 letters
letters = ["א", "ב", "ג", "ד", "ה", "ו", "ז", "ח", "ט", "י", "כ",
           "ל", "מ", "נ", "ס", "ע", "פ", "צ", "ק", "ר", "ש", "ת"]
names = ["ALEPH", "BETH", "GIMEL", "DALETH", "HE", "VAV", "ZAYIN", "HETH", "TETH", "YOD", "KAPH",
         "LAMED", "MEM", "NUN", "SAMEKH", "AYIN", "PE", "TSADDE", "QOPH", "RESH", "SHIN", "TAV"]
x0, y0 = 9050, 980
T(x0 + 1080, 700, "THE 22 LETTERS", 96, INK, bold=True)
for i, (g, nm) in enumerate(zip(letters, names)):
    col, row = divmod(i, 11)
    gx = x0 + col * 1150; gy = y0 + row * 300
    TG(gx + 130, gy + 92, g, 168, INK, HEB)
    T(gx + 330, gy + 44, nm, 64, INK_SOFT)
    T(gx + 330, gy + 122, str(i + 1), 54, INK_SOFT)

# ---------------- BOTTOM REGISTERS (three sketch panels)
def panel(x, w, title):
    for a, b in [((x, 4420), (x + w, 4420)), ((x + w, 4420), (x + w, 4900)),
                 ((x + w, 4900), (x, 4900)), ((x, 4900), (x, 4420))]:
        J(a, b, INK, 2, 3)
    T(x + w / 2, 4280, title, 72, INK, bold=True)
panel(300, 3500, "ELEMENTAL & CHEMICAL ORIGINS")
panel(4130, 3500, "ASTROLOGICAL REMAPPING")
panel(7960, 3500, "COSMIC SCALE & LEGEND")
# panel 1: the four elemental triangles + letters
for i, (dx, up, lab) in enumerate([(500, True, "FIRE"), (1250, False, "WATER"), (2000, True, "AIR"), (2750, False, "EARTH")]):
    px_, py_ = 300 + dx, 4620
    if up:
        J((px_, py_ - 110), (px_ + 190, py_ + 110)); J((px_ + 190, py_ + 110), (px_ - 190, py_ + 110)); J((px_ - 190, py_ + 110), (px_, py_ - 110))
    else:
        J((px_, py_ + 110), (px_ + 190, py_ - 110)); J((px_ + 190, py_ - 110), (px_ - 190, py_ - 110)); J((px_ - 190, py_ - 110), (px_, py_ + 110))
        if lab == "EARTH": J((px_ - 120, py_ - 40), (px_ + 120, py_ - 40), INK, 2, 3)
    T(px_ + 300, py_ + 130, lab, 52, INK_SOFT)
# panel 2: sun, moon, star
JC(4800, 4660, 120); dr.ellipse([4792, 4652, 4808, 4668], fill=INK + (220,))
for i in range(12):
    a = 2 * math.pi * i / 12
    J((4800 + 150 * math.cos(a), 4660 + 150 * math.sin(a)), (4800 + 210 * math.cos(a), 4660 + 210 * math.sin(a)), INK, 2, 3)
for k in range(3):
    JC(5650 + k * 30, 4660, 150 - k * 30, INK_SOFT, 2, 3)
dr.ellipse([5740, 4490, 5960, 4830], fill=(233, 214, 176, 255))
for i in range(5):
    a = -math.pi / 2 + 2 * math.pi * i / 5
    a2 = a + 2 * math.pi * 2 / 5
    J((6700 + 170 * math.cos(a), 4660 + 170 * math.sin(a)), (6700 + 170 * math.cos(a2), 4660 + 170 * math.sin(a2)), INK, 2, 3)
T(4800, 4860 - 130, "", 10)
# panel 3: three spiral galaxies
for gi, gx in enumerate([8650, 9750, 10850]):
    for t_i in range(300):
        t = t_i / 300 * 5.2 * math.pi
        r = 12 + t * 16
        sx, sy = gx + r * math.cos(t + gi), 4660 + r * math.sin(t + gi) * 0.62
        if random.random() < 0.75:
            dr.ellipse([sx - 4, sy - 4, sx + 4, sy + 4], fill=INK_SOFT + (170,))

# ---------------- mirror marginalia + credit
strip = Image.new("RGBA", (3400, 110), (0, 0, 0, 0))
sd = ImageDraw.Draw(strip)
sd.text((0, 8), "redrawn in pencil after the founder's plate — the Divine Nine, the Wheel, the Letters",
        font=ImageFont.truetype(SERIF, 62), fill=INK_SOFT + (190,))
img.paste(ImageOps.mirror(strip), (W - 3560, 4920), strip)
T(300 + 1750, 4928, "", 10)
img.save(OUT_PNG)
img.convert("RGB").save(OUT, quality=92)
print("SKETCH:", OUT, img.size)
# 93 — Live, Love, and let Love, Live.
