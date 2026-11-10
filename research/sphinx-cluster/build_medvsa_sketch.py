#!/usr/bin/env python3
# =====================================================================
# 93 — BUILD-MEDVSA-SKETCH.PY
# The Sphinx with a MEDVSA head, as a Leonardo pencil study, 21:9,
# same press as the Divine Nine and Cube Line strikes: sepia and
# graphite on parchment — the great profile study, a front-face
# study of the gaze, and a serpent study. Mirror marginalia.
# Authorship attributed exclusively to Johnathan 'Qasparr' Monroe,
# ARR, All Rights Reserved, Without Prejudice.
# Method of Science. Aim of Religion.
# =====================================================================
import math, random
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageOps

random.seed(93)
W, H = 11760, 5040
INK = (54, 34, 18)
INK_SOFT = (98, 72, 42)
RED = (130, 52, 30)
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
OUT = "/home/hatch/workspace/goals/cross-gematria-777-gap-filling/files/SPHINX-MEDVSA-LEONARDO-SKETCH.jpg"
OUT_PNG = OUT.replace(".jpg", ".png")

yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
d = np.sqrt(((xx - W / 2) / W) ** 2 + ((yy - H / 2) / H) ** 2)
tone = 233 - 40 * d
noise = np.random.default_rng(93).normal(0, 4.5, (H, W)).astype(np.float32)
base = np.stack([(tone + noise), (tone + noise) * 0.90, (tone + noise) * 0.72], axis=-1)
img = Image.fromarray(np.clip(base, 0, 255).astype(np.uint8))
dr = ImageDraw.Draw(img, "RGBA")
for _ in range(60):
    x, y = random.uniform(100, W - 100), random.uniform(100, H - 100)
    r = random.uniform(60, 300)
    dr.ellipse([x - r, y - r, x + r, y + r], fill=(176, 138, 84, random.randint(6, 18)))

def J(pts, ink=INK, passes=3, wdt=4, jit=2.6, alpha=170):
    if len(pts) < 2: return
    for _ in range(passes):
        pp = [(x + random.uniform(-jit, jit), y + random.uniform(-jit, jit)) for x, y in pts]
        dr.line(pp, fill=ink + (int(alpha * random.uniform(0.55, 1.0)),), width=wdt)

def curve(pts, n=90):
    # Catmull-Rom through control points
    p = [pts[0]] + pts + [pts[-1]]
    out = []
    for i in range(len(p) - 3):
        for t_i in range(n // (len(p) - 3) + 1):
            t = t_i / (n // (len(p) - 3))
            out.append(tuple(0.5 * ((2 * p[i + 1][k]) + (-p[i][k] + p[i + 2][k]) * t +
                             (2 * p[i][k] - 5 * p[i + 1][k] + 4 * p[i + 2][k] - p[i + 3][k]) * t * t +
                             (-p[i][k] + 3 * p[i + 1][k] - 3 * p[i + 2][k] + p[i + 3][k]) * t * t * t)
                             for k in (0, 1)))
    return out

def T(cx, y, s, size, ink=INK, bold=False):
    f = ImageFont.truetype(SERIF_B if bold else SERIF, size)
    bb = dr.textbbox((0, 0), s, font=f)
    dr.text((cx - (bb[2] - bb[0]) / 2 - bb[0], y), s, font=f, fill=ink)

def snake(x0, y0, ang, length, amp, wl, curl, scale=1.0):
    pts, x, y, a = [], x0, y0, ang
    steps = 46
    for i in range(steps + 1):
        t = i / steps
        pts.append((x + math.sin(t * wl * 6.28) * amp * math.cos(a + 1.57),
                    y + math.sin(t * wl * 6.28) * amp * math.sin(a + 1.57)))
        step = length / steps
        a += curl / steps
        x += math.cos(a) * step; y += math.sin(a) * step
    J(pts, INK, 3, max(3, int(7 * scale)))
    ex, ey = pts[-1]
    dr.ellipse([ex - 26 * scale, ey - 15 * scale, ex + 30 * scale, ey + 15 * scale],
               outline=INK + (190,), width=max(2, int(4 * scale)))
    tx, ty = ex + 34 * scale, ey
    J([(tx, ty), (tx + 34 * scale, ty - 12 * scale)], RED, 1, 3, 1.2)
    J([(tx, ty), (tx + 34 * scale, ty + 12 * scale)], RED, 1, 3, 1.2)
    return pts

def hatch(pts_top, pts_bot, step, ink=INK_SOFT):
    for a, b in zip(pts_top, pts_bot):
        J([a, b], ink, 1, 2, 1.4, 90)

# ------------------------------------------------------------- title
T(3000, 150, "LA  SPHINGE  MEDVSA", 185, INK, bold=True)
T(3000, 372, "the Sphinx of the strait, crowned with serpents — studies in the manner of Leonardo", 84, INK_SOFT)

# ------------------------------------------------- the great profile
GROUND = 3960
body = [(1560, 3380), (1700, 2880), (2250, 2560), (3300, 2460), (4700, 2520),
        (5900, 2560), (6650, 2480), (7250, 2680), (7560, 3160), (7580, 3620)]
J(curve(body), INK, 3, 5)
# forepaws, lying forward along the ground
J(curve([(7580, 3560), (8300, 3620), (9050, 3660), (9380, 3760), (9360, 3880),
         (9050, 3920), (8200, 3920), (7620, 3880)]), INK, 3, 5)
J(curve([(7700, 3720), (8400, 3760), (9080, 3800)]), INK_SOFT, 2, 3)  # the farther paw
for tx in (8960, 9080, 9200):  # toe divisions at the paw's front
    J([(tx, 3760), (tx + 26, 3900)], INK, 2, 3)
J(curve([(7160, 2760), (7300, 3160), (7340, 3620)]), INK, 2, 4)          # shoulder / foreleg front
# belly and ground line
J(curve([(7580, 3860), (6200, 3920), (4600, 3940), (3300, 3900), (2450, 3920),
         (1900, 3800), (1680, 3560)]), INK, 3, 5)
J([(700, GROUND), (9700, GROUND)], INK_SOFT, 2, 3)
# folded hind leg — the haunch arc and a hind paw
J(curve([(2150, 2820), (2650, 3280), (3050, 3840)]), INK, 2, 4)
J(curve([(1980, 2960), (2380, 3360), (2720, 3860)]), INK, 2, 4)
J(curve([(2560, 2620), (2900, 3060), (3150, 3560)]), INK_SOFT, 2, 3)
J(curve([(2380, 3860), (2850, 3800), (3180, 3860), (3120, 3940), (2480, 3940)]), INK_SOFT, 2, 3)
# the tail, lying along the haunch, tuft at its end
J(curve([(1620, 3050), (1420, 3350), (1500, 3620), (1720, 3700)]), INK, 2, 4)
dr.ellipse([1640, 3620, 1800, 3780], outline=INK + (170,), width=3)
# haunch and belly shading
for k in range(9):
    t = k / 9
    J(curve([(2050 + 130 * k, 2860 + 60 * k), (2350 + 120 * k, 3300), (2650 + 110 * k, 3820 - 40 * k)]),
      INK_SOFT, 1, 2, 1.6, 80)
for k in range(12):
    x = 800 + 720 * k
    J([(x, GROUND + 26), (x + 260, GROUND + 150)], INK_SOFT, 1, 2, 1.5, 60)

# neck rising to the head
J(curve([(7080, 2620), (7380, 2280), (7620, 2080)]), INK, 3, 5)          # throat
J(curve([(6760, 2600), (7050, 2180), (7260, 1880)]), INK, 3, 5)          # mane-side of neck
for k in range(6):  # neck shading
    J(curve([(6920 + 60 * k, 2520 - 40 * k), (7150 + 55 * k, 2240), (7380 + 50 * k, 2040)]),
      INK_SOFT, 1, 2, 1.5, 75)

# the head in profile, facing right (east)
face = [(7330, 1900), (7420, 1620), (7620, 1420), (7900, 1330), (8120, 1420),
        (8240, 1560), (8400, 1700), (8520, 1840), (8460, 1960), (8380, 2030),
        (8410, 2140), (8330, 2260), (8200, 2400), (7960, 2500), (7680, 2440),
        (7480, 2240)]
J(curve(face), INK, 3, 5)
J(curve([(8240, 1560), (8300, 1730)]), INK_SOFT, 2, 3)                   # brow fall
J(curve([(7720, 1560), (7790, 1660), (7740, 1780), (7660, 1680), (7720, 1560)]), INK, 2, 4)  # the ear
for k in range(5):  # jaw and cheek shading
    J(curve([(7760 + 46 * k, 2260 - 26 * k), (7960 + 40 * k, 2380), (8180 + 30 * k, 2400 - 30 * k)]),
      INK_SOFT, 1, 2, 1.5, 70)
J(curve([(7480, 2240), (7560, 2400), (7720, 2520)]), INK, 2, 4)          # throat to neck
# the eye — the gaze that stoneth
J(curve([(8060, 1810), (8160, 1770), (8260, 1810), (8160, 1850), (8060, 1810)]), INK, 2, 4)
dr.ellipse([8136, 1792, 8184, 1840], fill=INK + (220,))
J(curve([(8030, 1720), (8160, 1680), (8290, 1720)]), INK, 2, 4)          # brow
J(curve([(8360, 2030), (8300, 2080)]), INK_SOFT, 1, 3)
dr.ellipse([7960, 1310, 7960 + 1500, 1310 + 1500], outline=INK_SOFT + (60,), width=2)  # construction circle

# the serpent crown — nine snakes from the crown of the head
crown = [(7560, 1470), (7760, 1360), (7980, 1300), (8180, 1360)]
starts = [(7620, 1470, 3.55, 1050, 52, 2.2, -1.5), (7760, 1370, 3.95, 980, 48, 2.4, -1.1),
          (7920, 1315, 4.35, 1020, 55, 2.1, -0.7), (8060, 1325, 4.75, 940, 46, 2.5, -0.4),
          (8200, 1400, 5.20, 860, 44, 2.3, 0.1), (8280, 1520, 5.75, 780, 40, 2.2, 0.5),
          (7700, 1420, 3.15, 900, 50, 2.0, -2.0), (8000, 1300, 4.55, 1180, 60, 1.9, -0.9),
          (7860, 1340, 4.05, 1120, 58, 2.0, -1.3)]
for sx, sy, ang, ln, amp, wl, cu in starts:
    snake(sx, sy, ang, ln, amp, wl, cu, 1.0)
# two serpents as the brow band
snake(8180, 1470, 0.5, 420, 22, 2.6, 0.7, 0.62)
snake(8060, 1420, 2.7, 430, 22, 2.6, -2.4, 0.62)
T(4900, 4240, "the body of the lion · the head of the woman · the serpents for her hair", 76, INK_SOFT)
dr.ellipse([8236, 1568, 8292, 1624], fill=RED + (215,))

# -------------------------------------------- the front-face study
FX, FY = 10650, 1560
dr.ellipse([FX - 470, FY - 640, FX + 470, FY + 640], outline=INK + (200,), width=4)
J(curve([(FX - 470, FY - 200), (FX - 520, FY + 260), (FX - 300, FY + 560), (FX, FY + 640),
         (FX + 300, FY + 560), (FX + 520, FY + 260), (FX + 470, FY - 200)]), INK, 2, 4)
for sgn in (-1, 1):
    ex = FX + sgn * 195
    J(curve([(ex - 105, FY - 60), (ex, FY - 105), (ex + 105, FY - 60), (ex, FY - 18), (ex - 105, FY - 60)]), INK, 2, 4)
    dr.ellipse([ex - 26, FY - 82, ex + 26, FY - 30], fill=INK + (220,))
    J(curve([(ex - 120, FY - 165), (ex, FY - 205), (ex + 120, FY - 165)]), INK, 2, 4)
J(curve([(FX, FY - 20), (FX - 28, FY + 130), (FX + 6, FY + 175)]), INK, 2, 3)
J(curve([(FX - 62, FY + 185), (FX, FY + 205), (FX + 62, FY + 185)]), INK, 2, 3)
J(curve([(FX - 130, FY + 330), (FX, FY + 300), (FX + 130, FY + 330), (FX, FY + 385), (FX - 130, FY + 330)]), INK, 2, 4)
for k in range(7):  # sfumato hatch on the shadow side
    J([(FX + 190 + 34 * k, FY - 420 + 60 * k), (FX + 300 + 30 * k, FY + 120 + 40 * k)], INK_SOFT, 1, 2, 1.5, 65)
for i, ang in enumerate([3.5, 4.1, 4.7, 5.3, 5.9, 0.35, 0.95, 1.55, 2.15, 2.75]):
    sx = FX + math.cos(ang) * 430; sy = FY - 480 + math.sin(ang) * 180
    snake(sx, sy, ang + 3.14, 560, 34, 2.2, (1 if i % 2 else -1) * 0.9, 0.72)
T(FX, 2420, "the face, front — the gaze that stoneth", 72, INK_SOFT)

# -------------------------------------------- the serpent study
snake(9650, 3450, 0.12, 1750, 120, 3.0, 0.55, 1.35)
for k in range(16):
    x = 9750 + 105 * k
    J([(x, 3300 + 60 * math.sin(k)), (x + 44, 3380 + 60 * math.sin(k))], INK_SOFT, 1, 2, 1.3, 80)
T(10550, 3860, "one serpent, enlarged — the lock of hair that biteth", 72, INK_SOFT)

strip = Image.new("RGBA", (3500, 110), (0, 0, 0, 0))
sd = ImageDraw.Draw(strip)
sd.text((0, 8), "sphinx medvsa — she asketh the riddle with a crown of serpents",
        font=ImageFont.truetype(SERIF, 62), fill=INK_SOFT + (190,))
img.paste(ImageOps.mirror(strip), (W - 3660, 4880), strip)
img.save(OUT_PNG)
img.convert("RGB").save(OUT, quality=92)
print("SKETCH:", OUT, img.size)
# 93 — Live, Love, and let Love, Live.
