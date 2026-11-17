#!/usr/bin/env python3
"""Skrip OPSIONAL untuk membuat ulang logo ATMOS GYM di folder brand/.

Tidak diperlukan untuk menjalankan website — file logo SVG/PNG sudah tersedia.
Butuh: pip install fonttools cairosvg

Jalankan dari root repo:
    python3 tools/build_logo.py
"""
"""Logo ATMOS GYM — meniru logo pada banner promosi.
Komponen: shield biru gelap, dumbbell krom, tulisan ATMOS metalik,
GYM cyan, sparkle. Teks dijadikan outline path (font Anton) agar identik
di semua browser tanpa perlu install font.

Output (folder assets/):
  logo-atmosgym.svg        logo utama (teks + ikon)
  logo-mark.svg            ikon saja (shield + dumbbell)
  logo-atmosgym-1024.png   PNG transparan
  logo-mark-512.png        PNG transparan ikon
  favicon-64.png, apple-touch-icon.png
  inline_hero.svg / inline_mark.svg / inline_mark2.svg  (untuk ditanam di HTML)
"""
import os
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen

HERE = os.path.dirname(os.path.abspath(__file__))
FONT_PATH = os.path.join(HERE, "fonts", "Anton-Regular.ttf")
OUT_DIR = os.path.join(HERE, "assets")
os.makedirs(OUT_DIR, exist_ok=True)

FONT = TTFont(FONT_PATH)
GS = FONT.getGlyphSet()
CMAP = FONT.getBestCmap()
UPEM = FONT["head"].unitsPerEm

# ------------------------------------------------------------------ geometri
W, H = 1000, 700
CX = W / 2

S_TITLE, TRACK_TITLE = 236, -1
S_SUB, TRACK_SUB = 126, 11
BASE_TITLE, BASE_SUB = 420, 548

SHIELD_D = ("M500 40 L830 122 L830 340 C830 470 690 560 500 620 "
            "C310 560 170 470 170 340 L170 122 Z")
SHIELD_IN_D = ("M500 62 L810 136 L810 338 C810 454 682 540 500 596 "
               "C318 540 190 454 190 338 L190 136 Z")


def word_path(text, size, tracking):
    scale = size / UPEM
    x, out = 0.0, []
    for ch in text:
        gn = CMAP.get(ord(ch))
        if gn:
            pen = SVGPathPen(GS)
            GS[gn].draw(pen)
            d = pen.getCommands()
            if d:
                out.append(f'<path transform="translate({x:.2f} 0) scale({scale:.5f} {-scale:.5f})" d="{d}"/>')
            x += (GS[gn].width + tracking) * scale
        else:
            x += tracking * scale
    return "".join(out), x - tracking * scale


TITLE_FRAG, TITLE_W = word_path("ATMOS", S_TITLE, TRACK_TITLE)
SUB_FRAG, SUB_W = word_path("GYM", S_SUB, TRACK_SUB)


def plate(cx, cy, rx, ry, inner=0.52):
    return (
        f'<ellipse cx="{cx:.1f}" cy="{cy:.1f}" rx="{rx:.1f}" ry="{ry:.1f}" fill="url(#gPlate)" stroke="url(#gEdge)" stroke-width="2.6"/>'
        f'<ellipse cx="{cx:.1f}" cy="{cy - ry*0.10:.1f}" rx="{rx*inner:.1f}" ry="{ry*inner*0.94:.1f}" fill="url(#gPlateIn)"/>'
        f'<ellipse cx="{cx - rx*0.20:.1f}" cy="{cy - ry*0.36:.1f}" rx="{rx*0.30:.1f}" ry="{ry*0.22:.1f}" fill="url(#gSpec)"/>'
    )


def dumbbell(cy=112):
    out = [
        f'<rect x="352" y="{cy-11}" width="296" height="22" rx="11" fill="url(#gBarMetal)" stroke="url(#gEdge)" stroke-width="2.4"/>',
        f'<rect x="356" y="{cy-9}" width="288" height="6" rx="3" fill="#ffffff" opacity=".5"/>',
        f'<rect x="330" y="{cy-27}" width="26" height="54" rx="9" fill="url(#gPlate)" stroke="url(#gEdge)" stroke-width="2.4"/>',
        f'<rect x="644" y="{cy-27}" width="26" height="54" rx="9" fill="url(#gPlate)" stroke="url(#gEdge)" stroke-width="2.4"/>',
    ]
    for cx, w, h in [(300, 31, 100), (267, 27, 86), (241, 23, 70)]:
        out.append(plate(cx, cy, w, h))
        out.append(plate(W - cx, cy, w, h))
    return "\n  ".join(out)


def sparkle(cx, cy, r, op=1.0):
    k = 0.16
    d = (f"M{cx} {cy-r} C{cx+r*k} {cy-r*k} {cx+r*k} {cy-r*k} {cx+r} {cy} "
         f"C{cx+r*k} {cy+r*k} {cx+r*k} {cy+r*k} {cx} {cy+r} "
         f"C{cx-r*k} {cy+r*k} {cx-r*k} {cy+r*k} {cx-r} {cy} "
         f"C{cx-r*k} {cy-r*k} {cx-r*k} {cy-r*k} {cx} {cy-r} Z")
    return f'<path d="{d}" fill="url(#gSpark)" opacity="{op}"/>'


DEFS = """
<defs>
  <linearGradient id="gShieldIn" x1="0" y1="0" x2=".35" y2="1">
    <stop offset="0" stop-color="#1a2942"/><stop offset=".38" stop-color="#0b1422"/>
    <stop offset=".7" stop-color="#050b14"/><stop offset="1" stop-color="#0d1a2c"/>
  </linearGradient>
  <linearGradient id="gShieldEdge" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#f2f9ff"/><stop offset=".26" stop-color="#84a9cd"/>
    <stop offset=".52" stop-color="#2a3c53"/><stop offset=".76" stop-color="#9dc0de"/>
    <stop offset="1" stop-color="#eef8ff"/>
  </linearGradient>
  <linearGradient id="gShieldRim" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#5fe3ff" stop-opacity=".85"/>
    <stop offset=".5" stop-color="#1b7fd8" stop-opacity=".5"/>
    <stop offset="1" stop-color="#5fe3ff" stop-opacity=".85"/>
  </linearGradient>
  <linearGradient id="gChrome" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#ffffff"/><stop offset=".16" stop-color="#f2f8ff"/>
    <stop offset=".40" stop-color="#a9bed2"/><stop offset=".505" stop-color="#5c7590"/>
    <stop offset=".525" stop-color="#33475d"/><stop offset=".66" stop-color="#c6dbee"/>
    <stop offset=".84" stop-color="#ffffff"/><stop offset="1" stop-color="#a8bfd4"/>
  </linearGradient>
  <linearGradient id="gCyan" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#f0feff"/><stop offset=".24" stop-color="#a6f2ff"/>
    <stop offset=".5" stop-color="#39cbf6"/><stop offset=".63" stop-color="#0b7fc6"/>
    <stop offset=".82" stop-color="#63ddff"/><stop offset="1" stop-color="#c8f8ff"/>
  </linearGradient>
  <linearGradient id="gPlate" x1="0" y1="0" x2=".3" y2="1">
    <stop offset="0" stop-color="#f8fcff"/><stop offset=".3" stop-color="#b8cee2"/>
    <stop offset=".56" stop-color="#5a7390"/><stop offset=".78" stop-color="#cfe3f4"/>
    <stop offset="1" stop-color="#8ba4bb"/>
  </linearGradient>
  <linearGradient id="gPlateIn" x1="0" y1="0" x2=".4" y2="1">
    <stop offset="0" stop-color="#93abc2"/><stop offset=".5" stop-color="#2b3e54"/>
    <stop offset="1" stop-color="#96adc2"/>
  </linearGradient>
  <linearGradient id="gBarMetal" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#ffffff"/><stop offset=".45" stop-color="#8ca4ba"/>
    <stop offset=".56" stop-color="#3e526a"/><stop offset="1" stop-color="#dbeaf6"/>
  </linearGradient>
  <linearGradient id="gEdge" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#ffffff"/><stop offset=".5" stop-color="#6d89a3"/>
    <stop offset="1" stop-color="#ffffff"/>
  </linearGradient>
  <linearGradient id="gTopShine" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#ffffff" stop-opacity=".85"/>
    <stop offset=".34" stop-color="#ffffff" stop-opacity="0"/>
  </linearGradient>
  <radialGradient id="gSpec" cx=".5" cy=".5" r=".5">
    <stop offset="0" stop-color="#ffffff" stop-opacity=".95"/>
    <stop offset="1" stop-color="#ffffff" stop-opacity="0"/>
  </radialGradient>
  <radialGradient id="gGlowCyan" cx=".5" cy=".5" r=".5">
    <stop offset="0" stop-color="#3fd3ff" stop-opacity=".5"/>
    <stop offset="1" stop-color="#3fd3ff" stop-opacity="0"/>
  </radialGradient>
  <radialGradient id="gSpark" cx=".5" cy=".5" r=".5">
    <stop offset="0" stop-color="#ffffff"/><stop offset=".5" stop-color="#b4f2ff"/>
    <stop offset="1" stop-color="#33c4ff" stop-opacity=".3"/>
  </radialGradient>
  <filter id="fDrop" x="-25%" y="-25%" width="150%" height="160%">
    <feGaussianBlur in="SourceAlpha" stdDeviation="2" result="b"/>
    <feOffset in="b" dx="0" dy="7" result="o"/>
    <feFlood flood-color="#01060d" flood-opacity=".9" result="c"/>
    <feComposite in="c" in2="o" operator="in" result="s"/>
    <feMerge><feMergeNode in="s"/><feMergeNode in="SourceGraphic"/></feMerge>
  </filter>
  <filter id="fSoft" x="-120%" y="-120%" width="340%" height="340%">
    <feGaussianBlur stdDeviation="18"/>
  </filter>
</defs>
"""

TEXT_BLOCK = f"""
<!-- ============ ATMOS ============ -->
<g filter="url(#fDrop)">
  <g transform="translate({CX - TITLE_W/2:.2f} {BASE_TITLE})">
    {TITLE_FRAG.replace('<path ', '<path fill="#04090f" stroke="#04090f" stroke-width="26" stroke-linejoin="round" paint-order="stroke" stroke-opacity=".95" ')}
  </g>
  <g transform="translate({CX - TITLE_W/2:.2f} {BASE_TITLE})">
    {TITLE_FRAG.replace('<path ', '<path fill="url(#gChrome)" stroke="url(#gChrome)" stroke-width="10" stroke-linejoin="round" paint-order="stroke" ')}
  </g>
  <g transform="translate({CX - TITLE_W/2:.2f} {BASE_TITLE})" opacity=".30">
    {TITLE_FRAG.replace('<path ', '<path fill="url(#gTopShine)" ')}
  </g>
</g>

<!-- glow cyan di belakang GYM -->
<ellipse cx="500" cy="530" rx="230" ry="90" fill="url(#gGlowCyan)" opacity=".85" filter="url(#fSoft)"/>

<!-- ============ GYM ============ -->
<g filter="url(#fDrop)">
  <g transform="translate({CX - SUB_W/2:.2f} {BASE_SUB})">
    {SUB_FRAG.replace('<path ', '<path fill="#04090f" stroke="#04090f" stroke-width="22" stroke-linejoin="round" paint-order="stroke" stroke-opacity=".95" ')}
  </g>
  <g transform="translate({CX - SUB_W/2:.2f} {BASE_SUB})">
    {SUB_FRAG.replace('<path ', '<path fill="url(#gCyan)" stroke="url(#gCyan)" stroke-width="8" stroke-linejoin="round" paint-order="stroke" ')}
  </g>
</g>
"""


def build(with_text=True, view_box=None):
    body = f"""
<!-- glow biru (tanpa filter agar tidak terlihat kotak) -->
<ellipse cx="500" cy="330" rx="470" ry="340" fill="url(#gGlowCyan)" opacity=".75"/>

<!-- shield -->
<path d="{SHIELD_D}" fill="url(#gShieldIn)" stroke="url(#gShieldEdge)" stroke-width="9"/>
<path d="{SHIELD_IN_D}" fill="none" stroke="url(#gShieldRim)" stroke-width="3.4"/>
<path d="M500 52 L818 130" fill="none" stroke="#ffffff" stroke-width="2.4" opacity=".5" stroke-linecap="round"/>
<path d="M500 52 L182 130" fill="none" stroke="#ffffff" stroke-width="2.4" opacity=".3" stroke-linecap="round"/>

<!-- dumbbell -->
  {dumbbell(112)}

<!-- sparkle -->
{sparkle(500, 178, 28)}
{sparkle(500, 596, 16, .95)}
{sparkle(462, 588, 9, .85)}
{sparkle(538, 588, 9, .85)}
""" + (TEXT_BLOCK if with_text else "")

    vb = view_box or f"0 0 {W} {H}"
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" '
            f'width="{W}" height="{H}" role="img" aria-label="ATMOS GYM">'
            + DEFS + body + "</svg>")


AG_FRAG, AG_W = word_path("AG", 196, 4)


def mark_svg():
    """Ikon: shield + dumbbell + monogram AG (crop rapat) — untuk favicon/header."""
    svg = build(with_text=False, view_box="150 18 700 618")
    ag = (f'<g filter="url(#fDrop)">'
          f'<g transform="translate({500 - AG_W/2:.2f} 448)">'
          + AG_FRAG.replace('<path ', '<path fill="#04090f" stroke="#04090f" stroke-width="26" stroke-linejoin="round" paint-order="stroke" stroke-opacity=".95" ')
          + '</g><g transform="translate({0:.0f} 0)">'.format(0)
          + f'<g transform="translate({500 - AG_W/2:.2f} 448)">'
          + AG_FRAG.replace('<path ', '<path fill="url(#gChrome)" stroke="url(#gChrome)" stroke-width="9" stroke-linejoin="round" paint-order="stroke" ')
          + '</g></g></g>'
          + sparkle(500, 300, 20))
    return svg.replace("</svg>", ag + "</svg>")


def prefix_ids(svg, p):
    for head in ("g", "f"):
        svg = svg.replace('id="%s' % head, 'id="%s%s' % (p, head))
        svg = svg.replace('url(#%s' % head, 'url(#%s%s' % (p, head))
    return svg


def render(svg, name, width, bg=None):
    import cairosvg
    cairosvg.svg2png(bytestring=svg.encode(), write_to=os.path.join(OUT_DIR, name),
                     output_width=width, background_color=bg)
    return name


if __name__ == "__main__":
    full = build()
    mark = mark_svg()

    open(os.path.join(OUT_DIR, "logo-atmosgym.svg"), "w", encoding="utf-8").write(full)
    open(os.path.join(OUT_DIR, "logo-mark.svg"), "w", encoding="utf-8").write(mark)
    open(os.path.join(OUT_DIR, "inline_hero.svg"), "w", encoding="utf-8").write(prefix_ids(full, "hero-"))
    open(os.path.join(OUT_DIR, "inline_mark.svg"), "w", encoding="utf-8").write(prefix_ids(mark, "hd-"))
    open(os.path.join(OUT_DIR, "inline_mark2.svg"), "w", encoding="utf-8").write(prefix_ids(mark, "ft-"))

    render(full, "logo-atmosgym-1024.png", 1024, None)
    render(mark, "logo-mark-512.png", 512, None)
    render(full, "logo_preview.png", 880, "#0b1220")
    render(mark, "favicon-64.png", 64, "#080d16")
    render(mark, "apple-touch-icon.png", 180, "#080d16")
    print("OK — title_w", round(TITLE_W, 1), "sub_w", round(SUB_W, 1))
    for f in sorted(os.listdir(OUT_DIR)):
        print("  ", f, round(os.path.getsize(os.path.join(OUT_DIR, f)) / 1024, 1), "KB")
