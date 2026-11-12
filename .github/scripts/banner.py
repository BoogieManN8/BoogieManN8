#!/usr/bin/env python3
"""Draw assets/banner-dark.svg and assets/banner-light.svg (Matrix theme).

Static SVG with CSS animation only (transform), no scripts, no external fonts or links,
so GitHub serves it safely. The code rain is seeded, so the output never changes by itself.
Run by hand after editing: python3 .github/scripts/banner.py
"""
import os
import random

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "assets")
W, H = 880, 260
WIDE_H = 130
GLYPHS = "01ｱｲｳｴｵｶｷｸｹｺｻｼｽｾﾀﾁﾂﾃﾄﾅﾆﾇﾈﾊﾋﾌﾍﾎﾏﾐﾑﾒﾓﾔﾕﾗﾘﾜ0123456789ABCDEF"

THEMES = {
    "dark": dict(bg1="#0D1117", bg2="#0B1410", border="#1F3A2A", name="#E6EDF3", role="#C9D1D9",
                 muted="#7D8590", accent="#39D353", head="#00FF41", rain="#2EA043", rain_op=.55,
                 fade="#0D1117"),
    "light": dict(bg1="#F8FBF9", bg2="#F8FBF9", border="#C9DCCF", name="#1F2328", role="#424A53",
                  muted="#59636E", accent="#1A7F37", head="#116329", rain="#2DA44E", rain_op=.35,
                  fade="#F8FBF9"),
}


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;")


def rain(t, x0=500, x1=872, fall=620):
    rnd = random.Random(1999)
    step = 17
    cols = []
    styles = []
    for i, x in enumerate(range(x0, x1, step)):
        n = rnd.randint(14, 24)
        glyphs = "".join(rnd.choice(GLYPHS) for _ in range(n))
        dur = rnd.uniform(5.5, 11.0)
        delay = -rnd.uniform(0, dur)
        size = 13
        tspans = []
        for j, g in enumerate(glyphs):
            y = j * (size + 3)
            last = j == n - 1
            op = 1 if last else round(.15 + .85 * (j / n), 2)
            fill = t["head"] if last else t["rain"]
            tspans.append(f'<tspan x="{x}" y="{y}" fill="{fill}" fill-opacity="{op}">{esc(g)}</tspan>')
        h = n * (size + 3)
        styles.append(f".c{i}{{animation:fall {dur:.1f}s linear {delay:.1f}s infinite;}}")
        cols.append(f'<g class="c{i}" style="--h:{h}px"><text class="mono" font-size="{size}" '
                    f'opacity="{t["rain_op"]}" transform="translate(0,-{h})">{"".join(tspans)}</text></g>')
    return "\n".join(styles), "\n      ".join(cols)


def banner(t):
    rain_css, rain_cols = rain(t)
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="title desc">
  <title id="title">Tengiz Kiknadze, Senior iOS Developer</title>
  <desc id="desc">Profile banner. Tengiz Kiknadze, Senior iOS Developer. Swift, SwiftUI, UIKit, Swift Concurrency. Green code rain on the right.</desc>
  <style>
    .sans {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; }}
    .mono {{ font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, "Liberation Mono", monospace; }}
    .cur  {{ animation: blink 1.2s steps(1) infinite; }}
    @keyframes blink {{ 0%, 55% {{ opacity: 1; }} 56%, 100% {{ opacity: 0; }} }}
    @keyframes fall  {{ from {{ transform: translateY(0); }} to {{ transform: translateY(620px); }} }}
    {rain_css}
    @media (prefers-reduced-motion: reduce) {{ .cur, [class^="c"] {{ animation: none; }} }}
  </style>
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="{t['bg1']}"/>
      <stop offset="1" stop-color="{t['bg2']}"/>
    </linearGradient>
    <linearGradient id="side" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="{t['fade']}" stop-opacity="1"/>
      <stop offset=".35" stop-color="{t['fade']}" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="bottom" x1="0" y1="0" x2="0" y2="1">
      <stop offset=".7" stop-color="{t['fade']}" stop-opacity="0"/>
      <stop offset="1" stop-color="{t['fade']}" stop-opacity=".9"/>
    </linearGradient>
    <clipPath id="card"><rect width="{W}" height="{H}" rx="14"/></clipPath>
    <clipPath id="rainbox"><rect x="490" y="0" width="{W - 490}" height="{H}"/></clipPath>
  </defs>

  <g clip-path="url(#card)">
    <rect width="{W}" height="{H}" fill="url(#bg)"/>

    <!-- right: code rain -->
    <g clip-path="url(#rainbox)">
      {rain_cols}
    </g>
    <rect x="490" y="0" width="{W - 490}" height="{H}" fill="url(#side)"/>
    <rect x="490" y="0" width="{W - 490}" height="{H}" fill="url(#bottom)"/>
    <text x="846" y="236" class="mono" font-size="13" text-anchor="end" fill="{t['accent']}" fill-opacity=".85">follow the white rabbit_</text>

    <!-- left: identity -->
    <rect x="48" y="62" width="3" height="140" rx="1.5" fill="{t['accent']}"/>
    <text x="68" y="116" class="sans" font-size="54" font-weight="800" letter-spacing="-1.2" fill="{t['name']}">Tengiz Kiknadze</text>
    <text x="70" y="154" class="sans" font-size="26" font-weight="500" fill="{t['role']}">Senior iOS Developer</text>
    <rect class="cur" x="70" y="180" width="10" height="19" fill="{t['accent']}"/>
    <text x="92" y="196" class="mono" font-size="18" fill="{t['muted']}">Swift / SwiftUI / UIKit / Swift Concurrency</text>
  </g>
  <rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" rx="13.5" fill="none" stroke="{t['border']}"/>
</svg>
"""


def banner_wide(t):
    """Slim strip for desktop widths: the intro text stays above the fold."""
    W2, H2 = W, WIDE_H
    rain_css, rain_cols = rain(t, x0=560, x1=872)
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W2}" height="{H2}" viewBox="0 0 {W2} {H2}" role="img" aria-labelledby="title desc">
  <title id="title">Tengiz Kiknadze, Senior iOS Developer</title>
  <desc id="desc">Profile banner. Tengiz Kiknadze, Senior iOS Developer. Swift, SwiftUI, UIKit, Swift Concurrency. Green code rain on the right.</desc>
  <style>
    .sans {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; }}
    .mono {{ font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, "Liberation Mono", monospace; }}
    .cur  {{ animation: blink 1.2s steps(1) infinite; }}
    @keyframes blink {{ 0%, 55% {{ opacity: 1; }} 56%, 100% {{ opacity: 0; }} }}
    @keyframes fall  {{ from {{ transform: translateY(0); }} to {{ transform: translateY(520px); }} }}
    {rain_css}
    @media (prefers-reduced-motion: reduce) {{ .cur, [class^="c"] {{ animation: none; }} }}
  </style>
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="{t['bg1']}"/>
      <stop offset="1" stop-color="{t['bg2']}"/>
    </linearGradient>
    <linearGradient id="side" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="{t['fade']}" stop-opacity="1"/>
      <stop offset=".4" stop-color="{t['fade']}" stop-opacity="0"/>
    </linearGradient>
    <clipPath id="card"><rect width="{W2}" height="{H2}" rx="12"/></clipPath>
    <clipPath id="rainbox"><rect x="550" y="0" width="{W2 - 550}" height="{H2}"/></clipPath>
  </defs>
  <g clip-path="url(#card)">
    <rect width="{W2}" height="{H2}" fill="url(#bg)"/>
    <g clip-path="url(#rainbox)">
      {rain_cols}
    </g>
    <rect x="550" y="0" width="{W2 - 550}" height="{H2}" fill="url(#side)"/>
    <text x="852" y="114" class="mono" font-size="12" text-anchor="end" fill="{t['accent']}" fill-opacity=".85">follow the white rabbit_</text>
    <rect x="40" y="28" width="3" height="74" rx="1.5" fill="{t['accent']}"/>
    <text x="58" y="66" class="sans" font-size="40" font-weight="800" letter-spacing="-1" fill="{t['name']}">Tengiz Kiknadze</text>
    <rect class="cur" x="60" y="80" width="8" height="15" fill="{t['accent']}"/>
    <text x="76" y="93" class="mono" font-size="15" fill="{t['muted']}">Senior iOS Developer / Swift / SwiftUI / UIKit</text>
  </g>
  <rect x=".5" y=".5" width="{W2 - 1}" height="{H2 - 1}" rx="11.5" fill="none" stroke="{t['border']}"/>
</svg>
"""


if __name__ == "__main__":
    for name, theme in THEMES.items():
        with open(os.path.normpath(os.path.join(OUT, f"banner-{name}.svg")), "w") as f:
            f.write(banner(theme))
        with open(os.path.normpath(os.path.join(OUT, f"banner-{name}-wide.svg")), "w") as f:
            f.write(banner_wide(theme))
    print("written")
