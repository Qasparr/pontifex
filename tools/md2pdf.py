#!/usr/bin/env python3
"""Build a styled PDF from a markdown Liber edition via weasyprint.

Usage: md2pdf.py <input.md> <output.pdf> [title]
"""
import sys
import markdown
from weasyprint import HTML

MD, PDF = sys.argv[1], sys.argv[2]
TITLE = sys.argv[3] if len(sys.argv) > 3 else MD

with open(MD, encoding="utf-8") as f:
    src = f.read()

html_body = markdown.markdown(
    src,
    extensions=["tables", "sane_lists", "smarty"],
    output_format="html5",
)

CSS = """
@page {
  size: letter;
  margin: 2.4cm 2.2cm 2.6cm 2.2cm;
  @bottom-center {
    content: counter(page);
    font-family: "Noto Serif", serif;
    font-size: 9pt;
    color: #555;
  }
  @bottom-right {
    content: string(booktitle);
    font-family: "Noto Serif", serif;
    font-size: 8pt;
    font-style: italic;
    color: #888;
  }
}
@page :first { @bottom-center { content: none; } @bottom-right { content: none; } }
body {
  font-family: "Noto Serif", "Noto Sans", serif;
  font-size: 11pt;
  line-height: 1.55;
  color: #1a1a1a;
  string-set: booktitle "Liber Ma'at — Revised Edition";
}
h1 {
  font-size: 22pt; text-align: center; margin-top: 3cm;
  letter-spacing: 0.06em; page-break-before: avoid;
}
h2 { font-size: 14pt; margin-top: 1.6em; border-bottom: 1px solid #999; padding-bottom: 0.25em; }
h3 { font-size: 12pt; margin-top: 1.3em; }
blockquote {
  border-left: 3px solid #8a6d3b; margin-left: 0; padding: 0.4em 1em;
  color: #333; font-style: italic; background: #faf7f0;
}
table { border-collapse: collapse; width: 100%; font-size: 9.5pt; margin: 1em 0; }
th, td { border: 1px solid #999; padding: 6px 8px; text-align: left; vertical-align: top; }
th { background: #f0ead9; }
code { font-family: "Noto Sans Mono", monospace; font-size: 9.5pt; }
hr { border: none; border-top: 1px solid #bbb; margin: 2em auto; width: 40%; }
ul, ol { padding-left: 1.6em; }
li { margin-bottom: 0.35em; }
p { text-align: justify; }
"""

CSS = CSS.replace("Liber Ma'at — Revised Edition", TITLE)

doc = f"""<!DOCTYPE html><html><head><meta charset="utf-8"><title>{TITLE}</title>
<style>{CSS}</style></head><body>{html_body}</body></html>"""

HTML(string=doc).write_pdf(PDF)
print("wrote", PDF)
