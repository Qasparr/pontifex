#!/usr/bin/env python3
# =====================================================================
# 93 — BUILD-CASCADE-PLATES.PY
# Renders the three plates of the Sphinx cascade of 2026-11-09:
#   I.  THE CUBE LINE      — 5^3 Brightmoor, 6^3 Geburah, 9^3 Destroy,
#                            enthroned over the palindromic cube 1331.
#   II. THE SEATS          — the 91 register four-wide, the 74 beauty
#                            bridge three-wide, the 57s and the 194s.
#   III. THE BLACK-HOLED SUN — the Annvllvs ring, horizon set.
# All lettering struck from exact strings by the engine; all geometry
# drawn, not generated. House livery: purple and gold, blackletter.
# Authorship attributed exclusively to Johnathan 'Qasparr' Monroe,
# ARR, All Rights Reserved, Without Prejudice.
# Method of Science. Aim of Religion.
# =====================================================================
import math
from PIL import Image, ImageDraw, ImageFont

GOLD = (232, 184, 75)
GOLD_DIM = (168, 128, 52)
CREAM = (240, 226, 190)
FONT = "/home/hatch/workspace/templates/UnifrakturMaguntia.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
OUTDIR = "/home/hatch/workspace/goals/cross-gematria-777-gap-filling/files"

def ground(W, H):
    img = Image.new("RGB", (W, H), (24, 4, 40))
    px = img.load(); cx, cy = W / 2, H / 2
    for y in range(H):
        for x in range(0, W, 4):
            d = math.hypot(x - cx, y - cy) / (W * 0.72)
            f = max(0.0, 1.0 - d)
            r = int(24 + 38 * f); g = int(4 + 8 * f); b = int(40 + 46 * f)
            for dx in range(4):
                if x + dx < W: px[x + dx, y] = (r, g, b)
    return img

class Plate:
    def __init__(self, W, H):
        self.W, self.H = W, H
        self.img = ground(W, H)
        self.dr = ImageDraw.Draw(self.img, "RGBA")
        self.dr.rectangle([70, 70, W - 70, H - 70], outline=GOLD, width=6)
        self.dr.rectangle([100, 100, W - 100, H - 100], outline=GOLD_DIM, width=2)
    def bl(self, s): return ImageFont.truetype(FONT, s)
    def sf(self, s, bold=False): return ImageFont.truetype(SERIF_B if bold else SERIF, s)
    def fit(self, s, maxw, start, blackletter=False, bold=False):
        size = start
        while size > 18:
            f = self.bl(size) if blackletter else self.sf(size, bold)
            if self.dr.textlength(s, font=f) <= maxw: return f
            size -= 2
        return self.bl(size) if blackletter else self.sf(size, bold)
    def tc(self, y, s, font, fill):
        bb = self.dr.textbbox((0, 0), s, font=font)
        self.dr.text(((self.W - (bb[2] - bb[0])) / 2 - bb[0], y), s, font=font, fill=fill)
        return bb[3] - bb[1]
    def save(self, name):
        self.img.save(f"{OUTDIR}/{name}")
        print("PLATE:", name, self.img.size)

def iso_cube(p: Plate, cx, cy, s, edge=GOLD):
    # isometric cube: top rhombus, left and right faces; s = edge length px
    dx = s * 0.866; dy = s * 0.5
    top = [(cx, cy - s), (cx + dx, cy - s + dy), (cx, cy - s + 2 * dy), (cx - dx, cy - s + dy)]
    left = [(cx - dx, cy - s + dy), (cx, cy - s + 2 * dy), (cx, cy + dy), (cx - dx, cy)]
    right = [(cx, cy - s + 2 * dy), (cx + dx, cy - s + dy), (cx + dx, cy), (cx, cy + dy)]
    p.dr.polygon(top, fill=(90, 40, 130, 200), outline=edge)
    p.dr.polygon(left, fill=(52, 14, 84, 220), outline=edge)
    p.dr.polygon(right, fill=(68, 24, 104, 220), outline=edge)
    for poly in (top, left, right):
        p.dr.line(poly + [poly[0]], fill=edge, width=5)

# ---------------------------------------------------------------- I. CUBES
p = Plate(2400, 3200)
p.tc(180, "The Cube Line", p.bl(290), GOLD)
p.tc(540, "what the banks keep in three dimensions", p.sf(50), CREAM)
cubes = [(260, "5³", "125", "BRIGHTMOOR"),
         (320, "6³", "216", "GEBURAH — Strength"),
         (380, "9³", "729", "DESTROY — in Agrippa")]
for i, (s, pow_, val, name) in enumerate(cubes):
    cx = [400, 1180, 1960][i]; cy = 1560
    iso_cube(p, cx, cy, s)
    p.tc(0, "", p.sf(10), GOLD)  # no-op keeps draw state simple
    seg_y = 1830
    f1 = p.fit(pow_, 700, 150, blackletter=True)
    bb = p.dr.textbbox((0, 0), pow_, font=f1)
    p.dr.text((cx - (bb[2] - bb[0]) / 2 - bb[0], seg_y), pow_, font=f1, fill=GOLD)
    f2 = p.fit("= " + val, 700, 120, blackletter=True)
    bb = p.dr.textbbox((0, 0), "= " + val, font=f2)
    p.dr.text((cx - (bb[2] - bb[0]) / 2 - bb[0], seg_y + 190), "= " + val, font=f2, fill=CREAM)
    f3 = p.fit(name, 760, 52, bold=True)
    bb = p.dr.textbbox((0, 0), name, font=f3)
    p.dr.text((cx - (bb[2] - bb[0]) / 2 - bb[0], seg_y + 360), name, font=f3, fill=GOLD_DIM)
p.dr.line([300, 2420, 2100, 2420], fill=GOLD_DIM, width=3)
p.tc(2500, "and the cube that reads the same from either side", p.sf(50), CREAM)
p.tc(2600, "1331", p.bl(300), GOLD)
p.tc(2880, "XI × XI × XI — the Palindromic Cube", p.sf(54, True), CREAM)
p.tc(2965, "BRIGHT alone is 64 = 4³ · the mirror breaks at 11⁵, the first carry", p.fit("BRIGHT alone is 64 = 4³ · the mirror breaks at 11⁵, the first carry", 2000, 40), GOLD_DIM)
p.tc(3026, "Flagpole of Claim and Coinage — Johnathan 'Qasparr' Monroe, ARR", p.fit("Flagpole of Claim and Coinage — Johnathan 'Qasparr' Monroe, ARR", 2000, 38, bold=True), GOLD_DIM)
p.save("PLATE-I-THE-CUBE-LINE.png")

# ---------------------------------------------------------------- II. SEATS
p = Plate(2400, 3200)
p.tc(180, "The Seats", p.bl(290), GOLD)
p.tc(545, "THE REGISTER OF 91 — four-wide", p.sf(56, True), CREAM)
def medallion(p, cx, cy, r, big, name):
    p.dr.ellipse([cx - r, cy - r, cx + r, cy + r], outline=GOLD, width=6)
    p.dr.ellipse([cx - r + 18, cy - r + 18, cx + r - 18, cy + r - 18], outline=GOLD_DIM, width=2)
    f1 = p.fit(big, 2 * r - 90, 190, blackletter=True)
    bb = p.dr.textbbox((0, 0), big, font=f1)
    p.dr.text((cx - (bb[2] - bb[0]) / 2 - bb[0], cy - 150), big, font=f1, fill=GOLD)
    f2 = p.fit(name, 2 * r - 40, 56, bold=True)
    bb = p.dr.textbbox((0, 0), name, font=f2)
    p.dr.text((cx - (bb[2] - bb[0]) / 2 - bb[0], cy + 60), name, font=f2, fill=CREAM)
for i, name in enumerate(["DETROIT", "LIBERTY", "PHOENIX", "DARKNESS"]):
    medallion(p, 390 + i * 540, 1010, 250, "91", name)
p.tc(1400, "FER keeps the same seat in Agrippa — the Carrier at 91", p.fit("FER keeps the same seat in Agrippa — the Carrier at 91", 1900, 48), GOLD_DIM)
p.dr.line([300, 1560, 2100, 1560], fill=GOLD_DIM, width=3)
p.tc(1640, "THE BEAUTY BRIDGE — 74, three tongues", p.sf(56, True), CREAM)
for i, name in enumerate(["BEAUTY", "JAMĀL", "LUCIFER"]):
    medallion(p, 500 + i * 700, 2080, 250, "74", name)
p.dr.line([300, 2480, 2100, 2480], fill=GOLD_DIM, width=3)
p.tc(2560, "PRICK · ROSE · LUX — 57, and what they weigh is Light", p.fit("PRICK · ROSE · LUX — 57, and what they weigh is Light", 2000, 52, bold=True), CREAM)
p.tc(2680, "ASHES · TIRE · EARTH · HEART — 194 in Agrippa", p.fit("ASHES · TIRE · EARTH · HEART — 194 in Agrippa", 2000, 52, bold=True), CREAM)
p.tc(2820, "the ashes, the rim, the ground, and the heart — one seat in the old bank", p.fit("the ashes, the rim, the ground, and the heart — one seat in the old bank", 2000, 46), GOLD_DIM)
p.tc(2940, "CATALYST · CINERIBVS — 101 · the catalyst weighs the ashes", p.fit("CATALYST · CINERIBVS — 101 · the catalyst weighs the ashes", 2000, 46), GOLD_DIM)
p.tc(3026, "Flagpole of Claim and Coinage — Johnathan 'Qasparr' Monroe, ARR", p.fit("Flagpole of Claim and Coinage — Johnathan 'Qasparr' Monroe, ARR", 2000, 38, bold=True), GOLD_DIM)
p.save("PLATE-II-THE-SEATS.png")

# ---------------------------------------------------------------- III. SUN
p = Plate(2400, 3200)
p.tc(180, "The Black-Holed Sun", p.bl(240), GOLD)
p.tc(500, "the Event Horizon is Set", p.sf(56, True), CREAM)
cx, cy = 1200, 1560
# tridecagram, faint
R = 760
pts = [(cx + R * math.cos(-math.pi / 2 + 2 * math.pi * i / 13),
        cy + R * math.sin(-math.pi / 2 + 2 * math.pi * i / 13)) for i in range(13)]
order = [(i * 5) % 13 for i in range(14)]
for a, b in zip(order, order[1:]):
    p.dr.line([pts[a], pts[b]], fill=(232, 184, 75, 40), width=4)
# the annulus: ring of light
for r, wdt, col in [(560, 26, GOLD), (520, 8, GOLD_DIM), (600, 6, GOLD_DIM)]:
    p.dr.ellipse([cx - r, cy - r, cx + r, cy + r], outline=col, width=wdt)
# the black disc
p.dr.ellipse([cx - 500, cy - 500, cx + 500, cy + 500], fill=(0, 0, 0))
p.dr.ellipse([cx - 500, cy - 500, cx + 500, cy + 500], outline=(10, 2, 16), width=2)
p.tc(1470, "ANNVLLVS", p.bl(150), GOLD)
p.tc(2400, "DARK STARR — 110, the seat of SPARROW", p.fit("DARK STARR — 110, the seat of SPARROW", 2000, 54, bold=True), CREAM)
p.tc(2540, "GLOW-WYRM — the Glow weighs 77 in Agrippa; the Wyrm is 79, the gold seat", p.fit("GLOW-WYRM — the Glow weighs 77 in Agrippa; the Wyrm is 79, the gold seat", 2000, 48), CREAM)
p.tc(2680, "BLACK HOLE weighs the RIM in Agrippa — 119 to 119", p.fit("BLACK HOLE weighs the RIM in Agrippa — 119 to 119", 2000, 48), CREAM)
p.tc(2880, "a light from within the Darkness — not against it", p.sf(48), GOLD_DIM)
p.tc(3020, "Flagpole of Claim and Coinage — Johnathan 'Qasparr' Monroe, ARR", p.fit("Flagpole of Claim and Coinage — Johnathan 'Qasparr' Monroe, ARR", 2000, 40, bold=True), GOLD_DIM)
p.save("PLATE-III-THE-BLACK-HOLED-SUN.png")
# 93 — Live, Love, and let Love, Live.
