#!/usr/bin/env python3
# =====================================================================
# 93 — BUILD-LEONARDO-SHEET.PY
# A da Vinci notebook sheet for the Sphinx cascade of 2026-11-09:
# sepia ink and graphite on parchment — studies of the Cube Line,
# the Black-holed Sun (ANNVLLVS), and the Register of 91, with
# mirror-written marginalia in Leonardo's manner. Lines are struck
# with a hand jitter and hatched shading; nothing is generated.
# Authorship attributed exclusively to Johnathan 'Qasparr' Monroe,
# ARR, All Rights Reserved, Without Prejudice.
# Method of Science. Aim of Religion.
# =====================================================================
import math, random
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageOps

random.seed(93)
W, H = 2400, 3200
INK = (58, 38, 22)
INK_SOFT = (92, 66, 38)
RED = (128, 52, 30)
FONT = "/home/hatch/workspace/templates/UnifrakturMaguntia.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SERIF_I = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
OUT = "/home/hatch/workspace/goals/cross-gematria-777-gap-filling/files/LEONARDO-SHEET-THE-CASCADE.png"

# --- parchment: warm cream, aged blotches, fine grain
base = np.zeros((H, W, 3), dtype=np.float32)
yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
d = np.sqrt(((xx - W / 2) / W) ** 2 + ((yy - H / 2) / H) ** 2)
tone = 232 - 46 * d
noise = np.random.default_rng(93).normal(0, 5, (H, W)).astype(np.float32)
for c, k in enumerate((1.0, 0.90, 0.72)):
    base[..., c] = (tone + noise) * k
img = Image.fromarray(np.clip(base, 0, 255).astype(np.uint8))
dr = ImageDraw.Draw(img, "RGBA")
for _ in range(26):  # age spots
    x, y = random.uniform(80, W - 80), random.uniform(80, H - 80)
    r = random.uniform(30, 130)
    dr.ellipse([x - r, y - r, x + r, y + r], fill=(176, 138, 84, random.randint(8, 22)))

def jline(p1, p2, ink=INK, passes=3, wdt=2, jit=2.2):
    for _ in range(passes):
        a = random.uniform(90, 170)
        pts = []
        steps = 24
        for i in range(steps + 1):
            t = i / steps
            x = p1[0] + (p2[0] - p1[0]) * t + random.uniform(-jit, jit)
            y = p1[1] + (p2[1] - p1[1]) * t + random.uniform(-jit, jit)
            pts.append((x, y))
        dr.line(pts, fill=ink + (int(a),), width=wdt)

def hatch(x0, y0, x1, y1, gap=13, angle=0.7, ink=INK_SOFT):
    # parallel hatching clipped to a box (used sparingly, faces drawn as polys separately)
    L = math.hypot(x1 - x0, y1 - y0)
    n = int(L / gap) + 1
    for i in range(n):
        t = i / max(n, 1)
        sx = x0 + (x1 - x0) * t; sy = y0 + (y1 - y0) * t
        ex = sx + 60 * math.cos(angle); ey = sy + 60 * math.sin(angle)
        dr.line([(sx, sy), (ex, ey)], fill=ink + (110,), width=2)

def tc(y, s, font, fill=INK, cx=W / 2):
    bb = dr.textbbox((0, 0), s, font=font)
    dr.text((cx - (bb[2] - bb[0]) / 2 - bb[0], y), s, font=font, fill=fill)
    return bb[3] - bb[1]

def bl(s): return ImageFont.truetype(FONT, s)
def sf(s): return ImageFont.truetype(SERIF, s)

def iso_cube(cx, cy, s, label):
    dx, dy = s * 0.866, s * 0.5
    top = [(cx, cy - s), (cx + dx, cy - s + dy), (cx, cy - s + 2 * dy), (cx - dx, cy - s + dy)]
    left = [(cx - dx, cy - s + dy), (cx, cy - s + 2 * dy), (cx, cy + dy), (cx - dx, cy)]
    right = [(cx, cy - s + 2 * dy), (cx + dx, cy - s + dy), (cx + dx, cy), (cx, cy + dy)]
    for poly in (top, left, right):
        for a, b in zip(poly, poly[1:] + poly[:1]): jline(a, b)
    # construction circle + hatch on the left face
    dr.ellipse([cx - s, cy - s, cx + s, cy + s], outline=INK_SOFT + (70,), width=2)
    for i in range(6):
        t = i / 6
        jline((left[0][0] + 14, left[0][1] + t * s * 0.9),
              (left[3][0] + 14, left[3][1] + t * s * 0.9), ink=INK_SOFT, passes=1, wdt=1, jit=1.2)
    tc(cy + s * 0.95, label, sf(44), cx=cx)

# --- title, in a notebook hand (serif caps, letterspaced by the engine)
tc(130, "STUDIES OF THE NIGHT SUN", sf(64))
tc(215, "being figures of the Cube Line, the Ring, and the Register", sf(42), INK_SOFT)

# --- the cube studies
iso_cube(420, 700, 210, "5³ = 125 · BRIGHTMOOR")
iso_cube(1200, 700, 260, "6³ = 216 · GEBURAH")
iso_cube(1990, 700, 320, "9³ = 729 · DESTROY")
tc(1150, "and the palindromic cube — 1331 = XI × XI × XI — which readeth the same from either side", sf(44), cx=W / 2)

# --- the Black-holed Sun: black disc, ring, tridecagram, radial hatch
cx, cy, R = 1200, 1980, 560
pts = [(cx + 700 * math.cos(-math.pi / 2 + 2 * math.pi * i / 13),
        cy + 700 * math.sin(-math.pi / 2 + 2 * math.pi * i / 13)) for i in range(13)]
order = [(i * 5) % 13 for i in range(14)]
for a, b in zip(order, order[1:]):
    jline(pts[a], pts[b], ink=INK_SOFT, passes=2, wdt=2)
# radial rays (the etching's sunburst)
for i in range(72):
    a = 2 * math.pi * i / 72
    r0, r1 = R + 26, R + random.uniform(70, 130)
    jline((cx + r0 * math.cos(a), cy + r0 * math.sin(a)),
          (cx + r1 * math.cos(a), cy + r1 * math.sin(a)), ink=INK_SOFT, passes=1, wdt=2)
for r, wd in [(R, 10), (R - 34, 3), (R + 40, 3)]:
    dr.ellipse([cx - r, cy - r, cx + r, cy + r], outline=INK + (230,), width=wd)
dr.ellipse([cx - R + 44, cy - R + 44, cx + R - 44, cy + R - 44], fill=(16, 10, 6))
tc(cy - 78, "ANNVLLVS", bl(140), fill=(222, 196, 130))
tc(cy + R + 190, "the Black-holed Sun — the Event Horizon is Set", sf(46))
tc(cy + R + 258, "a light from within the Darkness, not against it", sf(42), INK_SOFT)

# --- register studies: four small medallions
for i, (n, name) in enumerate([("91", "DETROIT"), ("91", "LIBERTY"), ("91", "PHOENIX"), ("91", "DARKNESS")]):
    mx = 360 + i * 560; my = 2960
    dr.ellipse([mx - 150, my - 150, mx + 150, my + 150], outline=INK + (220,), width=3)
    dr.ellipse([mx - 132, my - 132, mx + 132, my + 132], outline=INK_SOFT + (160,), width=2)
    tc(my - 108, n, bl(110), cx=mx)
    tc(my + 26, name, sf(36), cx=mx)

# --- Leonardo marginalia: mirror writing at the foot
strip = Image.new("RGBA", (1900, 80), (0, 0, 0, 0))
sd = ImageDraw.Draw(strip)
sd.text((0, 6), "the Earth is the Ear of the Heart — J. Qasparr Monroe, in the manner of Leonardo",
        font=sf(44), fill=INK_SOFT + (190,))
img.paste(ImageOps.mirror(strip), ((W - 1900) // 2, 3136), strip)
# small red-chalk accent: the hermit's lamp point at the disc's rim
dr.ellipse([cx + R - 66, cy - 150, cx + R - 30, cy - 114], fill=RED + (200,))
img.save(OUT)
print("SHEET:", OUT, img.size)
# 93 — Live, Love, and let Love, Live.
