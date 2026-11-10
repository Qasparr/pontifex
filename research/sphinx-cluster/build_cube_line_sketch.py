#!/usr/bin/env python3
# =====================================================================
# 93 — BUILD-CUBE-LINE-SKETCH.PY
# The Cube Line as a Leonardo pencil study, 21:9 panorama, same
# press and specs as the Divine Nine strike: sepia/graphite on
# parchment — four cube studies (RENDER 4^3, BRIGHTMOOR 5^3, GEBURAH
# 6^3, DESTROY 9^3) and the two OPEN seats (7^3, 8^3) drawn as ghost
# frames, marked open, never filled. Mirror marginalia at the foot.
# Authorship attributed exclusively to Johnathan 'Qasparr' Monroe,
# ARR, All Rights Reserved, Without Prejudice.
# Method of Science. Aim of Religion.
# =====================================================================
import math, random
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageOps

random.seed(64)
W, H = 11760, 5040
INK = (56, 36, 20)
INK_SOFT = (96, 70, 40)
RED = (128, 52, 30)
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
OUT = "/home/hatch/workspace/goals/cross-gematria-777-gap-filling/files/THE-CUBE-LINE-LEONARDO-SKETCH.jpg"
OUT_PNG = OUT.replace(".jpg", ".png")

yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
d = np.sqrt(((xx - W / 2) / W) ** 2 + ((yy - H / 2) / H) ** 2)
tone = 233 - 40 * d
noise = np.random.default_rng(64).normal(0, 4.5, (H, W)).astype(np.float32)
base = np.stack([(tone + noise), (tone + noise) * 0.90, (tone + noise) * 0.72], axis=-1)
img = Image.fromarray(np.clip(base, 0, 255).astype(np.uint8))
dr = ImageDraw.Draw(img, "RGBA")
for _ in range(60):
    x, y = random.uniform(100, W - 100), random.uniform(100, H - 100)
    r = random.uniform(60, 300)
    dr.ellipse([x - r, y - r, x + r, y + r], fill=(176, 138, 84, random.randint(6, 18)))

def J(p1, p2, ink=INK, passes=3, wdt=3, jit=3.0):
    for _ in range(passes):
        a = random.uniform(80, 165)
        pts = [(p1[0] + (p2[0] - p1[0]) * (i / 24) + random.uniform(-jit, jit),
                p1[1] + (p2[1] - p1[1]) * (i / 24) + random.uniform(-jit, jit)) for i in range(25)]
        dr.line(pts, fill=ink + (int(a),), width=wdt)

def JDASH(p1, p2, ink=INK_SOFT):
    # a broken, ghosted edge: short dashes with gaps — an unfilled seat
    steps = 26
    for i in range(steps):
        if i % 3 == 2: continue
        t0, t1 = i / steps, (i + 0.8) / steps
        a = (p1[0] + (p2[0] - p1[0]) * t0, p1[1] + (p2[1] - p1[1]) * t0)
        b = (p1[0] + (p2[0] - p1[0]) * t1, p1[1] + (p2[1] - p1[1]) * t1)
        dr.line([a, b], fill=ink + (120,), width=3)

def T(cx, y, s, size, ink=INK, bold=False):
    f = ImageFont.truetype(SERIF_B if bold else SERIF, size)
    bb = dr.textbbox((0, 0), s, font=f)
    dr.text((cx - (bb[2] - bb[0]) / 2 - bb[0], y), s, font=f, fill=ink)
    return bb[3] - bb[1]

def cube_pts(cx, cy, s):
    dx, dy = s * 0.866, s * 0.5
    top = [(cx, cy - s), (cx + dx, cy - s + dy), (cx, cy - s + 2 * dy), (cx - dx, cy - s + dy)]
    left = [(cx - dx, cy - s + dy), (cx, cy - s + 2 * dy), (cx, cy + dy), (cx - dx, cy)]
    right = [(cx, cy - s + 2 * dy), (cx + dx, cy - s + dy), (cx + dx, cy), (cx, cy + dy)]
    return top, left, right

def cube(cx, cy, s, ghost=False):
    top, left, right = cube_pts(cx, cy, s)
    for poly in (top, left, right):
        for a, b in zip(poly, poly[1:] + poly[:1]):
            if ghost: JDASH(a, b)
            else: J(a, b)
    if not ghost:
        dr.ellipse([cx - s, cy - s, cx + s, cy + s], outline=INK_SOFT + (64,), width=2)
        for i in range(7):  # hatch the left face
            t = i / 7
            J((left[0][0] + 26, left[0][1] + t * s * 0.92), (left[3][0] + 26, left[3][1] + t * s * 0.92),
              INK_SOFT, 1, 2, 1.6)

T(W / 2, 130, "THE  CUBE  LINE", 190, INK, bold=True)
T(W / 2, 350, "four cubes weighed · two seats standing open · studies in the manner of Leonardo", 88, INK_SOFT)

CY = 2500
stations = [
    (1250, 480, False, "4³ = 64", "RENDER", True),
    (3100, 600, False, "5³ = 125", "BRIGHTMOOR", False),
    (5100, 720, False, "6³ = 216", "GEBURAH", False),
    (7000, 820, True, "7³ = 343", "THE SEAT STANDS OPEN", False),
    (8900, 920, True, "8³ = 512", "THE SEAT STANDS OPEN", False),
    (10700, 1020, False, "9³ = 729", "DESTROY · in Agrippa", False),
]
for cx, s, ghost, powval, name, is_new in stations:
    cube(cx, CY, s, ghost)
    ink_lab = INK_SOFT if ghost else INK
    T(cx, CY + s * 0.62 + 130, powval, 96, ink_lab, bold=True)
    T(cx, CY + s * 0.62 + 268, name, 72, INK_SOFT)
    if is_new:
        dr.ellipse([cx - 26, CY - s - 120, cx + 26, CY - s - 68], fill=RED + (215,))
        T(cx, CY - s - 320, "the new find", 66, RED)

# the palindromic cube, a small study at the foot
cube(2100, 4420, 200)
T(2100, 4760, "1331 = XI × XI × XI", 76, INK, bold=True)
T(3500, 4400, "the Palindromic Cube — readeth the same from either side;", 68, INK_SOFT)
T(3500, 4496, "the mirror breaketh at 11⁵, where the coefficients first carry", 68, INK_SOFT)

strip = Image.new("RGBA", (3600, 110), (0, 0, 0, 0))
sd = ImageDraw.Draw(strip)
sd.text((0, 8), "render · brightmoor · geburah · destroy — the line of cubes, and the gaps kept honest",
        font=ImageFont.truetype(SERIF, 62), fill=INK_SOFT + (190,))
img.paste(ImageOps.mirror(strip), (W - 3760, 4880), strip)
img.save(OUT_PNG)
img.convert("RGB").save(OUT, quality=92)
print("SKETCH:", OUT, img.size)
# 93 — Live, Love, and let Love, Live.
