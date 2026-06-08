#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""일러스트형 그림(장면 재현): 휴벨-비셀 고양이 실험, 합성곱, 예쁜꼬마선충 코넥톰, 생명 게임.
인터넷 참고 이미지의 '형태'만 빌려 통일 Drawing Style로 새로 작도(저작권 안전)."""
import os, math
A=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"pages","assets")
INK="#2A2A2A";ACC="#B5651D";BLU="#3B6EA5";GRN="#4E7A51";RED="#B5495B";PAPER="#FBF7EF";BORD="#E7DFCB";GRAY="#7A7268";BAND="#F3E7D6";WHT="#FFFFFF"
F="'Helvetica Neue', Arial, 'AppleSDGothicNeo', sans-serif"
DEF='<defs><marker id="ar" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#2A2A2A"/></marker></defs>'
def head(W,H,sub):
    return [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="{F}">',DEF,
            f'<rect x="2" y="2" width="{W-4}" height="{H-4}" rx="14" fill="{PAPER}" stroke="{BORD}"/>',
            f'<text x="{W/2}" y="34" text-anchor="middle" font-size="14" fill="{GRAY}" font-style="italic">{sub}</text>']
def save(name,parts): parts.append('</svg>'); open(os.path.join(A,name),"w",encoding="utf-8").write("\n".join(parts)); print(name)
def spikes(x0,y,w,n,seed,big):
    """스파이크 트레인 그리기."""
    out=[f'<line x1="{x0}" y1="{y}" x2="{x0+w}" y2="{y}" stroke="{GRAY}" stroke-width="1"/>']
    # 의사난수(시드 기반) 위치
    v=seed; xs=[]
    for i in range(40):
        v=(v*1103515245+12345)&0x7fffffff; xs.append(v/0x7fffffff)
    cnt=0
    for i,r in enumerate(xs):
        if big and r<0.55 or (not big and r<0.10):
            px=x0+8+ (i/40)*(w-12)
            out.append(f'<line x1="{px:.0f}" y1="{y}" x2="{px:.0f}" y2="{y-26}" stroke="{ACC if big else GRAY}" stroke-width="1.8"/>')
            cnt+=1
    return out

# ── 1. 휴벨-비셀 고양이 실험 ──
W,H=760,360
s=head(W,H,"고양이에게 막대를 보여주며 시각피질의 한 세포를 엿듣다 — 방향이 맞을 때만 터진다")
# 스크린(자극)
s.append(f'<rect x="40" y="120" width="120" height="120" rx="6" fill="#1c1c22" stroke="{INK}" stroke-width="2"/>')
s.append(f'<line x1="70" y1="225" x2="130" y2="135" stroke="#FBE7A0" stroke-width="9" stroke-linecap="round"/>')
s.append(f'<text x="100" y="262" text-anchor="middle" font-size="11.5" fill="{GRAY}">기울어진 빛 막대</text>')
s.append(f'<text x="100" y="278" text-anchor="middle" font-size="10.5" fill="{GRAY}">(스크린에 투사)</text>')
# 빛 → 눈
s.append(f'<line x1="162" y1="180" x2="214" y2="180" stroke="{ACC}" stroke-width="1.6" stroke-dasharray="5,4" marker-end="url(#ar)"/>')
# 고양이(측면, 단순 선화) — 오른쪽 보게? 스크린이 왼쪽이니 왼쪽 보게
cx,cy=300,190
# 몸통
s.append(f'<ellipse cx="{cx+30}" cy="{cy+34}" rx="62" ry="34" fill="{BAND}" stroke="{INK}" stroke-width="1.8"/>')
# 머리
s.append(f'<circle cx="{cx-26}" cy="{cy}" r="30" fill="{BAND}" stroke="{INK}" stroke-width="1.8"/>')
# 귀
s.append(f'<path d="M{cx-44},{cy-22} l-6,-22 l20,10 z" fill="{BAND}" stroke="{INK}" stroke-width="1.6"/>')
s.append(f'<path d="M{cx-12},{cy-26} l4,-22 l-18,12 z" fill="{BAND}" stroke="{INK}" stroke-width="1.6"/>')
# 눈, 코, 수염
s.append(f'<circle cx="{cx-38}" cy="{cy-4}" r="3.5" fill="{INK}"/>')
s.append(f'<path d="M{cx-52},{cy+6} l-14,-3 M{cx-52},{cy+10} l-14,2 M{cx-52},{cy+2} l-13,-7" stroke="{GRAY}" stroke-width="0.9"/>')
# 꼬리
s.append(f'<path d="M{cx+88},{cy+34} q40,-6 30,-40" fill="none" stroke="{INK}" stroke-width="1.8"/>')
# 다리
for dx in (4,40): s.append(f'<line x1="{cx+dx}" y1="{cy+62}" x2="{cx+dx}" y2="{cy+82}" stroke="{INK}" stroke-width="1.8"/>')
s.append(f'<text x="{cx+20}" y="{cy+100}" text-anchor="middle" font-size="11.5" fill="{GRAY}">마취된 고양이</text>')
# 전극(머리 위 → 시각피질)
s.append(f'<line x1="{cx-22}" y1="{cy-30}" x2="{cx-10}" y2="{cy-70}" stroke="{RED}" stroke-width="2.2"/>')
s.append(f'<circle cx="{cx-22}" cy="{cy-30}" r="3" fill="{RED}"/>')
s.append(f'<text x="{cx-10}" y="{cy-76}" text-anchor="middle" font-size="11" fill="{RED}" font-weight="bold">전극</text>')
# 전극 → 오실로스코프
s.append(f'<line x1="{cx-2}" y1="{cy-70}" x2="500" y2="120" stroke="{RED}" stroke-width="1.6"/>')
# 오실로스코프 패널
s.append(f'<rect x="500" y="96" width="228" height="184" rx="8" fill="{WHT}" stroke="{INK}" stroke-width="1.6"/>')
s.append(f'<text x="614" y="118" text-anchor="middle" font-size="12.5" fill="{INK}" font-weight="bold">세포의 반응(스파이크)</text>')
s+=spikes(516,160,196,40,12345,True)
s.append(f'<text x="516" y="178" font-size="11" fill="{ACC}" font-weight="bold">선호 방향 → 격렬히 발화</text>')
s+=spikes(516,236,196,40,999,False)
s.append(f'<text x="516" y="254" font-size="11" fill="{GRAY}">다른 방향 → 거의 잠잠</text>')
s.append(f'<text x="{W/2}" y="{H-14}" text-anchor="middle" font-size="11.5" fill="{GRAY}">어떤 세포는 \'특정 기울기의 모서리\'에만 반응한다 — 훗날 CNN 필터의 원형</text>')
save("cat-experiment.svg",s)

# ── 2. 합성곱(convolution) ──
W,H=760,360
s=head(W,H,"작은 필터를 이미지 위로 미끄러뜨려 \'모서리\' 같은 특징을 뽑아낸다")
# 입력 이미지 그리드 6x6
def grid(x0,y0,cell,vals,stroke=INK):
    out=[]
    n=len(vals)
    for r in range(n):
        for c in range(len(vals[0])):
            v=vals[r][c]; col= "#3a3a44" if v else "#EFE7D5"
            out.append(f'<rect x="{x0+c*cell}" y="{y0+r*cell}" width="{cell}" height="{cell}" fill="{col}" stroke="{stroke}" stroke-width="0.7"/>')
    return out
img=[[0,0,1,1,0,0],[0,0,1,1,0,0],[0,0,1,1,0,0],[0,0,1,1,0,0],[0,0,1,1,0,0],[0,0,1,1,0,0]]
s+=grid(60,90,32,img)
s.append(f'<text x="156" y="312" text-anchor="middle" font-size="11.5" fill="{GRAY}">입력 이미지(세로 모서리)</text>')
# 필터 3x3 강조 (좌상단 위치)
s.append(f'<rect x="60" y="90" width="96" height="96" fill="none" stroke="{ACC}" stroke-width="3"/>')
s.append(f'<text x="108" y="84" text-anchor="middle" font-size="11" fill="{ACC}" font-weight="bold">3×3 필터</text>')
# 화살표
s.append(f'<line x1="270" y1="186" x2="340" y2="186" stroke="{INK}" stroke-width="2" marker-end="url(#ar)"/>')
s.append(f'<text x="305" y="176" text-anchor="middle" font-size="11" fill="{GRAY}">미끄러뜨림</text>')
# 특징 맵 (모서리 검출 결과)
fm=[[0,1,0,0],[0,1,0,0],[0,1,0,0],[0,1,0,0]]
s+=grid(360,122,32,fm,stroke=BLU)
s.append(f'<text x="424" y="270" text-anchor="middle" font-size="11.5" fill="{GRAY}">특징 맵(모서리 위치가 켜짐)</text>')
# 오른쪽: 학습된 1층 필터들 = 손으로 만든 패치와 닮음
s.append(f'<rect x="540" y="96" width="190" height="150" rx="8" fill="{WHT}" stroke="{GRN}" stroke-width="1.5"/>')
s.append(f'<text x="635" y="116" text-anchor="middle" font-size="11.5" fill="{GRN}" font-weight="bold">학습된 첫 층 필터</text>')
# 작은 oriented gabor-like 패치 6개
import math
def gabor(cx,cy,ang):
    out=[f'<rect x="{cx-22}" y="{cy-22}" width="44" height="44" fill="#EFE7D5" stroke="{GRAY}" stroke-width="0.8"/>']
    dx=20*math.cos(math.radians(ang)); dy=20*math.sin(math.radians(ang))
    out.append(f'<line x1="{cx-dx:.0f}" y1="{cy-dy:.0f}" x2="{cx+dx:.0f}" y2="{cy+dy:.0f}" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>')
    return out
angs=[0,45,90,135,20,160]
for i,a in enumerate(angs):
    gx=565+ (i%3)*58; gy=150+ (i//3)*52
    s+=gabor(gx,gy,a)
s.append(f'<text x="635" y="238" text-anchor="middle" font-size="10.5" fill="{GRAY}">제각각 방향의 모서리</text>')
s.append(f'<text x="{W/2}" y="{H-14}" text-anchor="middle" font-size="11.5" fill="{GRAY}">놀랍게도 — 스스로 학습한 필터가 사람이 손으로 깎던 모서리 검출기, 그리고 고양이 시각세포와 닮았다</text>')
save("convolution.svg",s)

# ── 3. 예쁜꼬마선충 코넥톰 → 로봇 ──
W,H=760,330
s=head(W,H,"뇌 전체의 배선도를 아는 유일한 동물 — 그 배선만 옮겼더니 똑같이 움직였다")
# 벌레 몸통(길쭉하게 휜 관 모양, 양끝 가늘게)
import math
spine=[(60,170),(110,150),(165,140),(225,148),(285,165),(330,150)]
def smooth(pts):
    d=f"M{pts[0][0]},{pts[0][1]}"
    for i in range(1,len(pts)):
        x0,y0=pts[i-1]; x1,y1=pts[i]; mx=(x0+x1)/2
        d+=f" Q{x0},{y0} {mx},{(y0+y1)/2}"
    d+=f" T{pts[-1][0]},{pts[-1][1]}"
    return d
# 두꺼운 몸 + 가는 윤곽
s.append(f'<path d="{smooth(spine)}" fill="none" stroke="{BAND}" stroke-width="30" stroke-linecap="round"/>')
s.append(f'<path d="{smooth(spine)}" fill="none" stroke="{INK}" stroke-width="1.2" opacity="0.4"/>')
# 머리쪽 살짝 굵게
s.append(f'<circle cx="60" cy="170" r="13" fill="{BAND}" stroke="{INK}" stroke-width="1.1" opacity="0.6"/>')
# 신경 노드(302개 중 일부 표현) + 연결 — 척추선 따라
nodes=[]
for i in range(14):
    t=i/13
    # spine 보간
    seg=t*(len(spine)-1); k=min(int(seg),len(spine)-2); f=seg-k
    x=spine[k][0]*(1-f)+spine[k+1][0]*f
    y=spine[k][1]*(1-f)+spine[k+1][1]*f + 7*math.sin(i*1.3)
    nodes.append((x,y))
for i in range(len(nodes)-1):
    x1,y1=nodes[i]; x2,y2=nodes[i+1]
    s.append(f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" stroke="{BLU}" stroke-width="1"/>')
    if i%2==0 and i+2<len(nodes):
        x3,y3=nodes[i+2]; s.append(f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x3:.0f}" y2="{y3:.0f}" stroke="{BLU}" stroke-width="0.7" opacity="0.6"/>')
for x,y in nodes:
    s.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="3.4" fill="{ACC}"/>')
s.append(f'<text x="165" y="225" text-anchor="middle" font-size="12" fill="{INK}" font-weight="bold">예쁜꼬마선충 (C. elegans)</text>')
s.append(f'<text x="165" y="243" text-anchor="middle" font-size="10.5" fill="{GRAY}">신경 302개 · 시냅스 ~7000개</text>')
# 화살표
s.append(f'<line x1="350" y1="160" x2="430" y2="160" stroke="{INK}" stroke-width="2" marker-end="url(#ar)"/>')
s.append(f'<text x="390" y="150" text-anchor="middle" font-size="11" fill="{GRAY}">배선도를</text>')
s.append(f'<text x="390" y="180" text-anchor="middle" font-size="11" fill="{GRAY}">그대로 이식</text>')
# 로봇(레고풍)
rx,ry=540,140
s.append(f'<rect x="{rx}" y="{ry}" width="120" height="86" rx="8" fill="{WHT}" stroke="{INK}" stroke-width="1.8"/>')
# 눈/소나
s.append(f'<circle cx="{rx+60}" cy="{ry-6}" r="8" fill="{BLU}" stroke="{INK}" stroke-width="1.4"/>')
s.append(f'<line x1="{rx+60}" y1="{ry-14}" x2="{rx+60}" y2="{ry}" stroke="{INK}" stroke-width="1.4"/>')
s.append(f'<text x="{rx+60}" y="{ry-22}" text-anchor="middle" font-size="10" fill="{GRAY}">소나(코)</text>')
# 표시
s.append(f'<rect x="{rx+16}" y="{ry+18}" width="88" height="26" rx="4" fill="{BAND}" stroke="{GRAY}" stroke-width="1"/>')
s.append(f'<text x="{rx+60}" y="{ry+36}" text-anchor="middle" font-size="10.5" fill="{INK}">connectome</text>')
# 바퀴
for wx in (rx+24,rx+96):
    s.append(f'<circle cx="{wx}" cy="{ry+86}" r="13" fill="{GRAY}" stroke="{INK}" stroke-width="1.6"/>')
s.append(f'<text x="{rx+60}" y="{ry+120}" text-anchor="middle" font-size="12" fill="{INK}" font-weight="bold">레고 로봇</text>')
s.append(f'<text x="{W/2}" y="{H-14}" text-anchor="middle" font-size="11.5" fill="{GRAY}">코를 건드리면 멈추고, 뒤를 건드리면 앞으로 — 프로그램한 적 없는 행동이 \'배선\'에서 저절로 나왔다</text>')
save("connectome-worm.svg",s)

# ── 4. 콘웨이 생명 게임 (글라이더) ──
W,H=760,330
s=head(W,H,"단순한 규칙 몇 줄에서 \'움직이는\' 패턴이 태어난다 — 콘웨이의 생명 게임")
def board(x0,y0,cell,live,n=7,hl=None):
    out=[]
    for r in range(n):
        for c in range(n):
            on=(r,c) in live
            col=ACC if on else WHT
            out.append(f'<rect x="{x0+c*cell}" y="{y0+r*cell}" width="{cell}" height="{cell}" fill="{col}" stroke="{BORD}" stroke-width="1"/>')
    return out
# 글라이더 3세대
g0={(0,1),(1,2),(2,0),(2,1),(2,2)}
g1={(1,0),(1,2),(2,1),(2,2),(3,1)}
g2={(1,2),(2,0),(2,2),(3,1),(3,2)}
cell=26
gens=[("세대 1",g0,60),("세대 2",g1,300),("세대 3",g2,540)]
for lab,g,x0 in gens:
    s+=board(x0,80,cell,g)
    s.append(f'<text x="{x0+ 3.5*cell:.0f}" y="290" text-anchor="middle" font-size="12" fill="{INK}" font-weight="bold">{lab}</text>')
# 화살표 사이
for x in (262,502):
    s.append(f'<line x1="{x}" y1="170" x2="{x+34}" y2="170" stroke="{GRAY}" stroke-width="2" marker-end="url(#ar)"/>')
s.append(f'<text x="{W/2}" y="{H-12}" text-anchor="middle" font-size="11.5" fill="{GRAY}">규칙: 이웃이 적으면 죽고(고립), 많으면 죽고(과밀), 알맞으면 산다 — 그뿐인데 패턴이 기어간다</text>')
save("game-of-life.svg",s)
print("illus done")
