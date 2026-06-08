#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""3장 도식: 기호주의 vs 연결주의, 심신문제 세 입장."""
import os
A=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"pages","assets")
INK="#2A2A2A";ACC="#B5651D";BLU="#3B6EA5";PAPER="#FBF7EF";BORD="#E7DFCB";GRAY="#7A7268";BAND="#F3E7D6"
F="'Helvetica Neue', Arial, 'AppleSDGothicNeo', sans-serif"

def panel(x,y,w,h,fill,stroke,sw=1.6):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'

# 1) 기호주의 vs 연결주의
W,H=760,360
s=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="{F}">',
   f'<rect x="2" y="2" width="{W-4}" height="{H-4}" rx="14" fill="{PAPER}" stroke="{BORD}"/>',
   f'<text x="{W/2}" y="36" text-anchor="middle" font-size="14" fill="{GRAY}" font-style="italic">지능을 보는 두 관점 — 위에서 설계할까, 아래서 솟게 할까</text>']
s+= [panel(40,64,320,232,"#FFFFFF",INK),
 f'<text x="200" y="96" text-anchor="middle" font-size="15" fill="{INK}" font-weight="bold">기호주의</text>',
 f'<text x="200" y="120" text-anchor="middle" font-size="12" fill="{ACC}">위에서 설계 (top-down)</text>',
 f'<text x="64" y="154" font-size="12.5" fill="{INK}">· 기호·규칙·논리로 다룬다</text>',
 f'<text x="64" y="180" font-size="12.5" fill="{INK}">· 명료하고 설명 가능</text>',
 f'<text x="64" y="206" font-size="12.5" fill="{INK}">· 약점: 상식·모호함에 약함</text>',
 f'<text x="200" y="250" text-anchor="middle" font-size="12" fill="{GRAY}">논리 · 탐색 · 전문가 시스템</text>']
s+= [panel(400,64,320,232,"#E9EEF5",BLU,1.8),
 f'<text x="560" y="96" text-anchor="middle" font-size="15" fill="{INK}" font-weight="bold">연결주의</text>',
 f'<text x="560" y="120" text-anchor="middle" font-size="12" fill="{BLU}">아래서 창발 (bottom-up)</text>',
 f'<text x="424" y="154" font-size="12.5" fill="{INK}">· 연결망·가중치로 익힌다</text>',
 f'<text x="424" y="180" font-size="12.5" fill="{INK}">· 학습·잡음에 강함</text>',
 f'<text x="424" y="206" font-size="12.5" fill="{INK}">· 약점: 설명 어려움(블랙박스)</text>',
 f'<text x="560" y="250" text-anchor="middle" font-size="12" fill="{GRAY}">신경망 · 딥러닝</text>']
s.append(f'<text x="{W/2}" y="332" text-anchor="middle" font-size="13" fill="{INK}">오늘날의 답: 경쟁이 아니라 <tspan fill="{ACC}" font-weight="bold">상호 보완</tspan> — 둘을 잇는 신경-기호(neuro-symbolic)</text>')
s.append('</svg>')
open(os.path.join(A,"symbolism-connectionism.svg"),"w",encoding="utf-8").write("\n".join(s))

# 2) 심신문제 세 입장
W2,H2=760,300
t=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W2} {H2}" font-family="{F}">',
   f'<rect x="2" y="2" width="{W2-4}" height="{H2-4}" rx="14" fill="{PAPER}" stroke="{BORD}"/>',
   f'<text x="{W2/2}" y="36" text-anchor="middle" font-size="14" fill="{GRAY}" font-style="italic">마음과 물질의 관계 — 기계가 마음을 가질 수 있는가?</text>']
cols=[("이원론","마음 ≠ 물질","(별개의 실체)","→ 기계는 마음을\n   가질 수 없다","#FFFFFF",INK),
      ("유물론","마음 = 물리 과정","(뇌에서 일어나는 일)","→ 기계도 가질\n   여지가 있다","#FFFFFF",INK),
      ("기능주의","마음 = 기능적 역할","(무엇으로 만들었든)","→ 강한 AI의\n   철학적 토대","#F3E7D6",ACC)]
bw=216; gap=18; x0=40
for i,(name,l1,l2,l3,fill,st) in enumerate(cols):
    x=x0+i*(bw+gap)
    t.append(panel(x,70,bw,170,fill,st,2 if st==ACC else 1.6))
    t.append(f'<text x="{x+bw/2}" y="104" text-anchor="middle" font-size="15" fill="{INK}" font-weight="bold">{name}</text>')
    t.append(f'<text x="{x+bw/2}" y="132" text-anchor="middle" font-size="13" fill="{st if st==ACC else INK}">{l1}</text>')
    t.append(f'<text x="{x+bw/2}" y="154" text-anchor="middle" font-size="11.5" fill="{GRAY}">{l2}</text>')
    for j,ln in enumerate(l3.split("\n")):
        t.append(f'<text x="{x+16}" y="{190+j*20}" font-size="12.5" fill="{INK}">{ln}</text>')
t.append('</svg>')
open(os.path.join(A,"mind-body.svg"),"w",encoding="utf-8").write("\n".join(t))
print("symbolism-connectionism.svg, mind-body.svg")
