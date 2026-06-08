#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SVG → PNG 변환 (macOS qlmanage 렌더 + PIL 여백 트림).
사용: python3 svg2png.py a.svg b.svg ...  (각 X.svg → 같은 폴더 X.png)
WikiDocs 등 어디서나 확실히 보이도록 벡터 SVG를 PNG로 굳힌다."""
import sys, os, subprocess, tempfile
from PIL import Image, ImageChops

def convert(svg):
    svg = os.path.abspath(svg)
    base = os.path.splitext(svg)[0]
    outdir = os.path.dirname(svg)
    with tempfile.TemporaryDirectory() as td:
        subprocess.run(["qlmanage", "-t", "-s", "2400", "-o", td, svg],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        cand = os.path.join(td, os.path.basename(svg) + ".png")
        if not os.path.exists(cand):
            print("FAIL(render):", svg); return False
        im = Image.open(cand).convert("RGBA")
        # 흰 배경 위에 합성(투명 → 흰색)
        bg = Image.new("RGBA", im.size, (255, 255, 255, 255))
        comp = Image.alpha_composite(bg, im).convert("RGB")
        # 흰 여백 트림 (qlmanage 정사각 패딩 제거 → 도식 패널만 남김)
        white = Image.new("RGB", comp.size, (255, 255, 255))
        bbox = ImageChops.difference(comp, white).getbbox()
        if bbox:
            pad = 16
            l, t, r, b = bbox
            comp = comp.crop((max(0, l - pad), max(0, t - pad),
                              min(comp.width, r + pad), min(comp.height, b + pad)))
        comp.save(base + ".png", "PNG")
    print("OK:", base + ".png", Image.open(base + ".png").size)
    return True

if __name__ == "__main__":
    ok = sum(convert(s) for s in sys.argv[1:] if s.lower().endswith(".svg"))
    print(f"변환 완료 {ok}/{len(sys.argv)-1}")
