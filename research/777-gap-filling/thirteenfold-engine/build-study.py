#!/usr/bin/env python3
"""
THE THIRTEENFOLD ENGINE — study builder.
--------------------------------------------------------------------------------
Epigraph: "In the beginning was the Word... and the Word was the Law."
Date: 2026-10-18.
93.

Authorship: Johnathan 'Qasparr' (KASPARR) Monroe, Keeper of the Secret
Treasure — All Rights Reserved, Without Prejudice. Built by the Scribe
at his order.

Method: Scientific Illuminism — hypothesis, method, observation, result.
--------------------------------------------------------------------------------
MECHANISM: This script assembles the complete study from three sources:
  (1) thirteenfold-prose.md — the author's teaching, the wells, the audit;
  (2) /tmp/fillings.json — the 135 PONTIFEX fillings parsed from
      777-REVISED.md (cell, proposal, banks, tiers, bridge, reasoning);
  (3) charts/*.png — matplotlib figures rendered from the same data.
  It injects generated tables at the <!-- NODES -->, <!-- TABLES --> and
  <!-- CHARTS --> markers, converts Markdown to HTML, and renders the PDF
  with fpdf2's write_html (which natively embeds <img> PNGs and breaks
  long <table>s across pages).
DOCTRINE: Nothing in the assembly invents data. Every number in the
  charts is counted from the ledger; every table row is quoted from
  777-REVISED.md; every tier label is the worker's own. The thirteenfold
  circle itself is the scribe's construction (mod-13, mechanical) and is
  labeled as such in the prose — findings, never doctrine.
--------------------------------------------------------------------------------
Closing: Live, Love, and let Love, Live.
"""

import json
import re
from collections import defaultdict

import markdown
from fpdf import FPDF

# --- MECHANISM: load the parsed ledger ---------------------------------------
DATA = json.load(open('/tmp/fillings.json'))
FILLED = DATA['filled']

# --- MECHANISM: node assignment, node = ((row-1) mod 13) + 1 -----------------
# DOCTRINE: thirteen is the author's load-bearing number (his ruling);
# theosophical reduction is his method; the assignment is mechanical and
# reversible, offices are NOT invented for the nodes.
NODES = defaultdict(list)
for f in FILLED:
    m = re.match(r'(\d+)', f['row'])
    node = ((int(m.group(1)) - 1) % 13) + 1
    NODES[node].append(f)


def esc(s):
    """MECHANISM: minimal HTML escaping for table text."""
    return (s.replace('&', '&amp;').replace('<', '&lt;')
             .replace('>', '&gt;'))


def brief(s, n=160):
    """MECHANISM: one-line reasoning summary for the node tables."""
    s = ' '.join(s.split())
    return s[:n] + '…' if len(s) > n else s


def build_nodes():
    """DOCTRINE: per-node tables; reasoning kept brief, full text in Part III."""
    out = []
    for node in range(1, 14):
        rows = NODES[node]
        out.append(f'<h3>Node {node} — {len(rows)} fillings</h3>')
        out.append('<table border="1" cellpadding="4">')
        out.append('<tr><th>Cell</th><th>Proposal</th><th>Tiers</th>'
                   '<th>Reasoning (brief)</th></tr>')
        for f in rows:
            tiers = ', '.join(sorted({t for _, _, t in f['banks']}))
            out.append('<tr><td>' + esc(f"{f['col']}/{f['row']}") + '</td><td>'
                       + esc(brief(f['proposal'], 60)) + '</td><td>'
                       + esc(tiers) + '</td><td>'
                       + esc(brief(f['notes'])) + '</td></tr>')
        out.append('</table>')
    return '\n'.join(out)


def build_tables():
    """DOCTRINE: the full 135 — every filling with banks, tiers, reasoning."""
    out = ['<table border="1" cellpadding="4">',
           '<tr><th>Cell</th><th>Proposal</th><th>Banks (value [tier])</th>'
           '<th>Bridge</th><th>Reasoning</th></tr>']
    for f in FILLED:
        banks = '; '.join(f'{bk}: {v} [{t}]' for bk, v, t in f['banks'])
        out.append('<tr><td>' + esc(f"{f['col']}/{f['row']}<br/>" + f['title'][:60])
                   + '</td><td>' + esc(brief(f['proposal'], 80)) + '</td><td>'
                   + esc(banks) + '</td><td>' + esc(brief(f['bridge'], 40))
                   + '</td><td>' + esc(brief(f['notes'], 420)) + '</td></tr>')
    out.append('</table>')
    return '\n'.join(out)


def build_charts():
    """MECHANISM: the four figures, with captions stating what was counted."""
    figs = [
        ('charts/pie_status.png',
         'Figure 1 — 221 ledger cells: 135 filled, 85 certified intentionally '
         'empty, 1 transcription gap left open.'),
        ('charts/pie_tiers.png',
         'Figure 2 — Provenance of the 105 bank-weighings: 19 attested, '
         '15 derived, 71 constructed.'),
        ('charts/bar_banks.png',
         'Figure 3 — Weighings by bank: every candidate word weighed in its '
         'own tongue; Agrippa and Latin lead because the cells demanded them.'),
        ('charts/circle_13.png',
         'Figure 4 — The thirteenfold engine: 135 fillings on 13 nodes, '
         'node = ((row − 1) mod 13) + 1. Node size shows fillings per node.'),
    ]
    out = []
    for src, cap in figs:
        out.append(f'<p><img src="{src}" width="520"/></p>')
        out.append(f'<p><i>{esc(cap)}</i></p>')
    return '\n'.join(out)


# --- MECHANISM: assemble ------------------------------------------------------
prose = open('thirteenfold-prose.md').read()
prose = prose.replace('<!-- NODES -->', build_nodes())
prose = prose.replace('<!-- TABLES -->', build_tables())
prose = prose.replace('<!-- CHARTS -->', build_charts())
open('thirteenfold-study.md', 'w').write(prose)

html_body = markdown.markdown(prose, extensions=['tables'])
html = ('<html><body>' + html_body + '</body></html>')
open('thirteenfold-study.html', 'w').write(html)

# --- MECHANISM: render PDF; write_html embeds imgs, breaks tables -------------
# DOCTRINE: DejaVu Sans is registered because the study carries Greek
# (THELEMA), Hebrew (transliterations), and em-dashes — all outside the
# core-font range. fpdf2 raises rather than silently dropping glyphs, so
# the Unicode font is load-bearing, not cosmetic.
pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.set_auto_page_break(True, margin=20)
pdf.set_margins(18, 18, 18)
pdf.add_font('DejaVu', '', '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf')
pdf.add_font('DejaVu', 'B', '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf')
# MECHANISM: no Sans Oblique ships on this host; the regular face stands in
# for italic so <i> captions render instead of raising. Cosmetic only.
pdf.add_font('DejaVu', 'I', '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf')
pdf.add_font('DejaVu', 'BI', '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf')
pdf.add_page()
pdf.set_font('DejaVu', '', 11)
pdf.write_html(html)
pdf.output('thirteenfold-study.pdf')

print('wrote thirteenfold-study.md')
print('wrote thirteenfold-study.html')
print('wrote thirteenfold-study.pdf')
