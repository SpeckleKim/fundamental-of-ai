#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2장 도식: AI의 부침 곡선(기대·투자 vs 시대) — 겨울과 봄의 반복."""
import os
A=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"pages","assets")
INK="#2A2A2A";ACC="#B5651D";BLU="#3B6EA5";PAPER="#FBF7EF";BORD="#E7DFCB";GRAY="#7A7268"
FONT="'Helvetica Neue', Arial, 'AppleSDGothicNeo', sans-serif"
W,H=940,420; OX=60; RX=W-40; TOP=80; BOT=330
def fx(yr): return OX+(yr-1950)/(2025-1950)*(RX-OX)
def fy(h): return BOT-(h/100)*(BOT-TOP)
pts=[(1956,18,"다트머스 회의 (1956)","s"),(1965,82,"황금기","up"),
     (1974,22,"첫 번째 겨울","dn"),(1985,80,"전문가 시스템 붐","up"),
     (1992,20,"두 번째 겨울","dn"),(2005,48,"통계적 학습","up"),
     (2012,72,"딥러닝 (2012)","up"),(2023,96,"LLM","up")]
s=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="{FONT}">']
s.append(f'<rect x="2" y="2" width="{W-4}" height="{H-4}" rx="14" fill="{PAPER}" stroke="{BORD}"/>')
s.append(f'<text x="{W/2:.0f}" y="38" text-anchor="middle" font-size="15" fill="{INK}" font-weight="bold">인공지능의 부침 — 기대와 겨울의 반복</text>')
# 축
s.append(f'<line x1="{OX}" y1="{BOT}" x2="{RX}" y2="{BOT}" stroke="{INK}" stroke-width="1.4"/>')
s.append(f'<line x1="{OX}" y1="{TOP-10}" x2="{OX}" y2="{BOT}" stroke="{INK}" stroke-width="1.4"/>')
s.append(f'<text x="{OX-8}" y="{TOP}" text-anchor="end" font-size="11" fill="{GRAY}">기대·투자</text>')
for yr in (1960,1970,1980,1990,2000,2010,2020):
    s.append(f'<text x="{fx(yr):.0f}" y="{BOT+18}" text-anchor="middle" font-size="11" fill="{GRAY}">{yr}</text>')
# 곡선
path="M "+" L ".join(f"{fx(y):.0f},{fy(h):.0f}" for y,h,_,_ in pts)
s.append(f'<path d="{path}" fill="none" stroke="{ACC}" stroke-width="3" stroke-linejoin="round"/>')
# 마커 + 라벨
for y,h,lab,kind in pts:
    x,yy=fx(y),fy(h)
    col= BLU if kind=="dn" else ACC
    s.append(f'<circle cx="{x:.0f}" cy="{yy:.0f}" r="5" fill="{col}" stroke="#fff" stroke-width="1.4"/>')
    if kind=="dn":
        s.append(f'<text x="{x:.0f}" y="{yy+22:.0f}" text-anchor="middle" font-size="12" fill="{BLU}" font-weight="bold">{lab}</text>')
    elif kind=="s":
        s.append(f'<text x="{x:.0f}" y="{yy+22:.0f}" text-anchor="middle" font-size="11.5" fill="{GRAY}">{lab}</text>')
    else:
        s.append(f'<text x="{x:.0f}" y="{yy-12:.0f}" text-anchor="middle" font-size="12" fill="{INK}">{lab}</text>')
s.append(f'<text x="{W/2:.0f}" y="{H-16:.0f}" text-anchor="middle" font-size="12" fill="{GRAY}">과장된 기대 → 한계 → 겨울 → 새로운 접근으로 부활 … 그 반복 속에서도 기초는 남았다</text>')
s.append('</svg>')
open(os.path.join(A,"ai-winters.svg"),"w",encoding="utf-8").write("\n".join(s))
print("ai-winters.svg")
