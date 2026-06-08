#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""4장 도식: AI 분야 지도 — 기초 체력 위에 다섯 능력, 그것이 모여 에이전트."""
import os
A=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"pages","assets")
INK="#2A2A2A";ACC="#B5651D";BLU="#3B6EA5";PAPER="#FBF7EF";BORD="#E7DFCB";GRAY="#7A7268";BAND="#F3E7D6"
F="'Helvetica Neue', Arial, 'AppleSDGothicNeo', sans-serif"
W,H=760,400
s=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="{F}">',
   f'<rect x="2" y="2" width="{W-4}" height="{H-4}" rx="14" fill="{PAPER}" stroke="{BORD}"/>',
   f'<text x="{W/2}" y="34" text-anchor="middle" font-size="14" fill="{GRAY}" font-style="italic">기초 위에 다섯 능력이 서고, 그것이 모여 하나의 에이전트가 된다</text>']
# 맨 위: 에이전트
s+=[f'<rect x="250" y="58" width="260" height="46" rx="10" fill="{ACC}" stroke="{INK}" stroke-width="2"/>',
    f'<text x="380" y="86" text-anchor="middle" font-size="14" fill="#fff" font-weight="bold">지능형 에이전트 (통합 주체)</text>']
# 가운데: 다섯 능력
abil=[("탐색",ACC),("지식·추론",ACC),("학습",BLU),("언어",BLU),("지각·행동",BLU)]
bw=128; gap=10; x0=(W-(bw*5+gap*4))/2; ay=180
for i,(name,c) in enumerate(abil):
    x=x0+i*(bw+gap)
    s.append(f'<rect x="{x:.0f}" y="{ay}" width="{bw}" height="50" rx="8" fill="#FFFFFF" stroke="{c}" stroke-width="1.8"/>')
    s.append(f'<text x="{x+bw/2:.0f}" y="{ay+30}" text-anchor="middle" font-size="13.5" fill="{INK}">{name}</text>')
    # 능력→에이전트
    s.append(f'<line x1="{x+bw/2:.0f}" y1="{ay}" x2="380" y2="104" stroke="#C9BFA8" stroke-width="1.3"/>')
# 맨 아래: 기초 체력
s+=[f'<rect x="60" y="300" width="640" height="56" rx="10" fill="{BAND}" stroke="{INK}" stroke-width="1.6"/>',
    f'<text x="380" y="326" text-anchor="middle" font-size="14" fill="{INK}" font-weight="bold">기초 체력</text>',
    f'<text x="380" y="346" text-anchor="middle" font-size="12.5" fill="{GRAY}">수학 · 논리 · 인지심리 · 뇌와 신경 · 계산</text>']
# 기초→능력
for i in range(5):
    x=x0+i*(bw+gap)+bw/2
    s.append(f'<line x1="{x:.0f}" y1="300" x2="{x:.0f}" y2="{ay+50}" stroke="#C9BFA8" stroke-width="1.3"/>')
# 양 옆 흐름 표시
s.append(f'<text x="125" y="166" text-anchor="middle" font-size="11.5" fill="{ACC}">기호주의</text>')
s.append(f'<text x="600" y="166" text-anchor="middle" font-size="11.5" fill="{BLU}">연결주의</text>')
s.append(f'<text x="{W/2}" y="384" text-anchor="middle" font-size="12" fill="{GRAY}">그리고 7부의 도구(LISP·Prolog)로 이 개념들을 직접 손에 쥔다</text>')
s.append('</svg>')
open(os.path.join(A,"ai-map.svg"),"w",encoding="utf-8").write("\n".join(s))
print("ai-map.svg")
