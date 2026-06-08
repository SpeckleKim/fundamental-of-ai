#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""7장 도식: 기억의 세 단계, 두 갈래 사고(직관 vs 추론)."""
import os
A=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"pages","assets")
INK="#2A2A2A";ACC="#B5651D";BLU="#3B6EA5";PAPER="#FBF7EF";BORD="#E7DFCB";GRAY="#7A7268";BAND="#F3E7D6"
F="'Helvetica Neue', Arial, 'AppleSDGothicNeo', sans-serif"
def ar(x1,y1,x2,y2,col=INK):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{col}" stroke-width="1.8" marker-end="url(#a7)"/>'

# 기억의 세 단계
W,H=760,300
s=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="{F}">',
   '<defs><marker id="a7" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#2A2A2A"/></marker></defs>',
   f'<rect x="2" y="2" width="{W-4}" height="{H-4}" rx="14" fill="{PAPER}" stroke="{BORD}"/>',
   f'<text x="{W/2}" y="36" text-anchor="middle" font-size="14" fill="{GRAY}" font-style="italic">감각이 들어와 잠깐 머물고, 주의를 받으면 다루어지고, 되새기면 오래 남는다</text>']
boxes=[("감각 기억","약 1초, 순식간",60),("단기·작업 기억","7±2개 · 금방 사라짐",290),("장기 기억","거의 무한 · 오래",520)]
for name,sub,x in boxes:
    s.append(f'<rect x="{x}" y="110" width="180" height="70" rx="9" fill="#FFFFFF" stroke="{INK}" stroke-width="1.6"/>')
    s.append(f'<text x="{x+90}" y="142" text-anchor="middle" font-size="13.5" fill="{INK}" font-weight="bold">{name}</text>')
    s.append(f'<text x="{x+90}" y="164" text-anchor="middle" font-size="11.5" fill="{GRAY}">{sub}</text>')
s.append(ar(240,138,288,138)); s.append(f'<text x="264" y="128" text-anchor="middle" font-size="11" fill="{ACC}">주의</text>')
s.append(ar(470,138,518,138)); s.append(f'<text x="494" y="128" text-anchor="middle" font-size="11" fill="{ACC}">되새김</text>')
s.append(f'<line x1="518" y1="158" x2="470" y2="158" stroke="{GRAY}" stroke-width="1.3" marker-end="url(#a7)"/><text x="494" y="174" text-anchor="middle" font-size="10.5" fill="{GRAY}">인출</text>')
s.append(f'<text x="380" y="220" text-anchor="middle" font-size="12.5" fill="{INK}">좁은 작업 기억은 <tspan fill="{ACC}" font-weight="bold">묶음(청킹)</tspan>으로 한계를 넘는다 — \'바\'\'다\' → \'바다\'</text>')
s.append(f'<text x="380" y="252" text-anchor="middle" font-size="12" fill="{GRAY}">학습 = 연결의 변화(헵: 함께 발화하면 함께 연결된다) → 신경망 가중치의 뿌리</text>')
s.append('</svg>')
open(os.path.join(A,"memory-model.svg"),"w",encoding="utf-8").write("\n".join(s))

# 두 갈래 사고
W2,H2=760,300
t=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W2} {H2}" font-family="{F}">',
   f'<rect x="2" y="2" width="{W2-4}" height="{H2-4}" rx="14" fill="{PAPER}" stroke="{BORD}"/>',
   f'<text x="{W2/2}" y="36" text-anchor="middle" font-size="14" fill="{GRAY}" font-style="italic">사람의 사고에는 결이 다른 두 가지가 있다</text>']
t+=[f'<rect x="40" y="64" width="320" height="200" rx="10" fill="#E9EEF5" stroke="{BLU}" stroke-width="1.8"/>',
    f'<text x="200" y="98" text-anchor="middle" font-size="15" fill="{INK}" font-weight="bold">빠른 직관</text>',
    f'<text x="64" y="132" font-size="12.5" fill="{INK}">· 얼굴을 알아본다</text>',
    f'<text x="64" y="158" font-size="12.5" fill="{INK}">· 모국어를 알아듣는다</text>',
    f'<text x="64" y="184" font-size="12.5" fill="{INK}">· 노력 없이 즉각</text>',
    f'<text x="200" y="232" text-anchor="middle" font-size="12" fill="{BLU}">≈ 연결주의(신경망)가 잘함</text>']
t+=[f'<rect x="400" y="64" width="320" height="200" rx="10" fill="#FFFFFF" stroke="{ACC}" stroke-width="1.8"/>',
    f'<text x="560" y="98" text-anchor="middle" font-size="15" fill="{INK}" font-weight="bold">느린 추론</text>',
    f'<text x="424" y="132" font-size="12.5" fill="{INK}">· 17 × 23 암산</text>',
    f'<text x="424" y="158" font-size="12.5" fill="{INK}">· 논리를 따진다</text>',
    f'<text x="424" y="184" font-size="12.5" fill="{INK}">· 집중과 단계가 필요</text>',
    f'<text x="560" y="232" text-anchor="middle" font-size="12" fill="{ACC}">≈ 기호주의(논리)가 잘함</text>']
t.append('</svg>')
open(os.path.join(A,"dual-process.svg"),"w",encoding="utf-8").write("\n".join(t))
print("memory-model.svg, dual-process.svg")
