#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""5장 도식: 경사 하강(손실 골짜기), 벡터·행렬."""
import os, math
A=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"pages","assets")
INK="#2A2A2A";ACC="#B5651D";BLU="#3B6EA5";PAPER="#FBF7EF";BORD="#E7DFCB";GRAY="#7A7268";BAND="#F3E7D6"
F="'Helvetica Neue', Arial, 'AppleSDGothicNeo', sans-serif"

# ---------- 경사 하강 ----------
W,H=760,360; OX=70; RX=710; TOP=80; BOT=300
def loss(x):  # x in [0,1]
    return 1.7*(x-0.62)**2 - 0.26*math.exp(-((x-0.28)/0.05)**2) + 0.30
xs=[i/120 for i in range(121)]
ys=[loss(x) for x in xs]
lo,hi=min(ys),max(ys)
def px(x): return OX+x*(RX-OX)
def py(v): return BOT-(v-lo)/(hi-lo)*(BOT-TOP)
pathpts=" ".join(f"{px(x):.0f},{py(loss(x)):.0f}" for x in xs)
s=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="{F}">',
   f'<rect x="2" y="2" width="{W-4}" height="{H-4}" rx="14" fill="{PAPER}" stroke="{BORD}"/>',
   f'<text x="{W/2}" y="36" text-anchor="middle" font-size="14" fill="{GRAY}" font-style="italic">오차(손실)를 가장 낮추는 값을 찾아, 기울기 따라 한 걸음씩 내려간다</text>',
   f'<line x1="{OX}" y1="{BOT}" x2="{RX}" y2="{BOT}" stroke="{INK}" stroke-width="1.2"/>',
   f'<line x1="{OX}" y1="{TOP-6}" x2="{OX}" y2="{BOT}" stroke="{INK}" stroke-width="1.2"/>',
   f'<text x="{OX-8}" y="{TOP+6}" text-anchor="end" font-size="11" fill="{GRAY}">오차</text>',
   f'<text x="{RX}" y="{BOT+20}" text-anchor="end" font-size="11" fill="{GRAY}">값(가중치)</text>',
   f'<path d="M {pathpts}" fill="none" stroke="{ACC}" stroke-width="2.6"/>']
# 공이 굴러 내려가는 경로(시작 → 지역 최솟값)
for x in [0.10,0.16,0.22,0.28]:
    s.append(f'<circle cx="{px(x):.0f}" cy="{py(loss(x))-7:.0f}" r="6" fill="{BLU}" opacity="{0.35 if x<0.28 else 1}"/>')
s.append(f'<text x="{px(0.10):.0f}" y="{py(loss(0.10))-18:.0f}" text-anchor="middle" font-size="11.5" fill="{BLU}">시작</text>')
# 지역/전역 최솟값
s.append(f'<text x="{px(0.28):.0f}" y="{py(loss(0.28))+26:.0f}" text-anchor="middle" font-size="12" fill="{BLU}" font-weight="bold">지역 최솟값(갇힘 주의)</text>')
gx=min(xs,key=lambda x:loss(x))
s.append(f'<circle cx="{px(gx):.0f}" cy="{py(loss(gx))-7:.0f}" r="6" fill="{ACC}"/>')
s.append(f'<text x="{px(gx):.0f}" y="{py(loss(gx))+26:.0f}" text-anchor="middle" font-size="12" fill="{ACC}" font-weight="bold">전역 최솟값(목표)</text>')
s.append('</svg>')
open(os.path.join(A,"gradient-descent.svg"),"w",encoding="utf-8").write("\n".join(s))

# ---------- 벡터·행렬 ----------
W2,H2=760,330
t=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W2} {H2}" font-family="{F}">',
   f'<rect x="2" y="2" width="{W2-4}" height="{H2-4}" rx="14" fill="{PAPER}" stroke="{BORD}"/>',
   f'<text x="{W2/2}" y="34" text-anchor="middle" font-size="14" fill="{GRAY}" font-style="italic">데이터는 점(벡터), 변형은 손(행렬)</text>']
# 패널1: 벡터=점
t+=[f'<rect x="34" y="58" width="330" height="246" rx="10" fill="#FFFFFF" stroke="{INK}" stroke-width="1.4"/>',
    f'<text x="199" y="84" text-anchor="middle" font-size="13.5" fill="{INK}" font-weight="bold">벡터 = 공간 속 한 점</text>',
    f'<line x1="80" y1="270" x2="330" y2="270" stroke="{GRAY}" stroke-width="1"/>',
    f'<line x1="80" y1="270" x2="80" y2="110" stroke="{GRAY}" stroke-width="1"/>']
pts=[(150,160,"A",ACC),(180,185,"B",ACC),(300,140,"C",BLU)]
for x,y,n,c in pts:
    t.append(f'<circle cx="{x}" cy="{y}" r="6" fill="{c}"/><text x="{x+10}" y="{y+4}" font-size="12" fill="{INK}">{n}</text>')
t.append(f'<text x="199" y="296" text-anchor="middle" font-size="11.5" fill="{GRAY}">가까우면(A·B) 비슷, 멀면(C) 다르다</text>')
# 패널2: 행렬=변환
t+=[f'<rect x="396" y="58" width="330" height="246" rx="10" fill="#E9EEF5" stroke="{BLU}" stroke-width="1.6"/>',
    f'<text x="561" y="84" text-anchor="middle" font-size="13.5" fill="{INK}" font-weight="bold">행렬 = 벡터를 변형하는 손</text>',
    f'<rect x="430" y="150" width="80" height="40" rx="6" fill="#fff" stroke="{INK}" stroke-width="1.4"/><text x="470" y="175" text-anchor="middle" font-size="12" fill="{INK}">입력 벡터</text>',
    f'<rect x="530" y="150" width="56" height="40" rx="6" fill="{BAND}" stroke="{INK}" stroke-width="1.4"/><text x="558" y="175" text-anchor="middle" font-size="13" fill="{ACC}" font-weight="bold">×W</text>',
    f'<rect x="606" y="150" width="84" height="40" rx="6" fill="#fff" stroke="{INK}" stroke-width="1.4"/><text x="648" y="175" text-anchor="middle" font-size="12" fill="{INK}">새 벡터</text>',
    f'<line x1="510" y1="170" x2="528" y2="170" stroke="{INK}" stroke-width="1.6"/>',
    f'<line x1="586" y1="170" x2="604" y2="170" stroke="{INK}" stroke-width="1.6"/>',
    f'<text x="561" y="232" text-anchor="middle" font-size="11.5" fill="{GRAY}">신경망의 한 층 = 입력 벡터에 행렬 곱하기</text>']
t.append('</svg>')
open(os.path.join(A,"vector-matrix.svg"),"w",encoding="utf-8").write("\n".join(t))
print("gradient-descent.svg, vector-matrix.svg")
