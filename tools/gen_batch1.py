#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""개념 도식 묶음 1: 빅오, 상태공간, 미니맥스, 추론 방향, 퍼지 멤버십, 회귀/분류, 과적합, 군집화."""
import os, math
A=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"pages","assets")
INK="#2A2A2A";ACC="#B5651D";BLU="#3B6EA5";GRN="#4E7A51";RED="#B5495B";PAPER="#FBF7EF";BORD="#E7DFCB";GRAY="#7A7268";BAND="#F3E7D6";WHT="#FFFFFF"
F="'Helvetica Neue', Arial, 'AppleSDGothicNeo', sans-serif"
DEF='<defs><marker id="ar" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#2A2A2A"/></marker></defs>'
def head(W,H,sub):
    return [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="{F}">',DEF,
            f'<rect x="2" y="2" width="{W-4}" height="{H-4}" rx="14" fill="{PAPER}" stroke="{BORD}"/>',
            f'<text x="{W/2}" y="34" text-anchor="middle" font-size="14" fill="{GRAY}" font-style="italic">{sub}</text>']
def box(x,y,w,h,txt,fill=WHT,st=INK,fs=13.5,tc=INK,bold=True,rx=8,sw=1.6):
    fw=' font-weight="bold"' if bold else ''
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{st}" stroke-width="{sw}"/>'
            f'<text x="{x+w/2:.0f}" y="{y+h/2+5:.0f}" text-anchor="middle" font-size="{fs}" fill="{tc}"{fw}>{txt}</text>')
def line(x1,y1,x2,y2,col=INK,w=1.8,arrow=False,dash=None):
    d=f' stroke-dasharray="{dash}"' if dash else ''; m=' marker-end="url(#ar)"' if arrow else ''
    return f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" stroke="{col}" stroke-width="{w}"{d}{m}/>'
def save(name,parts): parts.append('</svg>'); open(os.path.join(A,name),"w",encoding="utf-8").write("\n".join(parts)); print(name)

# ── 1. 빅오 증가 곡선 (09-03) ──
W,H=760,360; OX,RX,TOP,BOT=70,710,70,300
s=head(W,H,"입력이 커질 때 비용이 얼마나 빨리 자라는가 — 같은 문제도 절차에 따라 천지차이")
s+=[line(OX,BOT,RX,BOT,INK,1.2),line(OX,TOP-6,OX,BOT,INK,1.2),
    f'<text x="{OX-8}" y="{TOP+4}" text-anchor="end" font-size="11" fill="{GRAY}">비용(시간)</text>',
    f'<text x="{RX}" y="{BOT+20}" text-anchor="end" font-size="11" fill="{GRAY}">입력 크기 n →</text>']
def curve(fn,col,lab,ly):
    pts=[]
    for i in range(0,101):
        x=i/100; v=fn(x)
        if v>1.02:
            pts.append((OX+x*(RX-OX), TOP)); break
        pts.append((OX+x*(RX-OX), BOT-v*(BOT-TOP)))
    d=" ".join(f"{x:.0f},{y:.0f}" for x,y in pts)
    s.append(f'<polyline points="{d}" fill="none" stroke="{col}" stroke-width="2.4"/>')
    lx,lyy=pts[-1]; s.append(f'<text x="{min(lx+6,RX-4):.0f}" y="{ly}" font-size="12" fill="{col}" font-weight="bold">{lab}</text>')
curve(lambda x:0.08, GRAY, "O(1) 상수", BOT-0.08*(BOT-TOP)-6)
curve(lambda x:0.10+0.16*math.log(1+9*x)/math.log(10), GRN, "O(log n)", 250)
curve(lambda x:0.12+0.7*x, BLU, "O(n) 선형", 150)
curve(lambda x:0.12+0.9*x*x, ACC, "O(n²)", 96)
curve(lambda x:0.12+0.0009*(math.exp(7*x)-1), RED, "O(2ⁿ) 지수", 74)
s.append(f'<text x="{W/2}" y="{H-18}" text-anchor="middle" font-size="12" fill="{GRAY}">지수(붉은 선)는 조금만 커져도 폭발한다 — 그래서 휴리스틱으로 비껴간다</text>')
save("complexity-bigo.svg",s)

# ── 2. 상태공간/탐색 트리 (10-01) ──
W,H=760,330
s=head(W,H,"문제를 \'상태\'와 \'연산자\'로 바꾸면, 푸는 일은 곧 길찾기가 된다")
# 8-퍼즐 미니 보드 그리기
def puzzle(cx,cy,grid,cell=22,hl=False):
    out=[]; n=3; x0=cx-n*cell/2; y0=cy-n*cell/2
    out.append(f'<rect x="{x0-3}" y="{y0-3}" width="{n*cell+6}" height="{n*cell+6}" rx="5" fill="{BAND if hl else WHT}" stroke="{ACC if hl else INK}" stroke-width="{1.8 if hl else 1.2}"/>')
    for r in range(n):
        for c in range(n):
            v=grid[r*n+c]; x=x0+c*cell; y=y0+r*cell
            if v:
                out.append(f'<rect x="{x+1}" y="{y+1}" width="{cell-2}" height="{cell-2}" rx="3" fill="#fff" stroke="{GRAY}" stroke-width="0.8"/>')
                out.append(f'<text x="{x+cell/2:.0f}" y="{y+cell/2+4:.0f}" text-anchor="middle" font-size="11" fill="{INK}">{v}</text>')
    return out
start=[1,2,3,4,0,5,6,7,8]
ch1=[1,2,3,0,4,5,6,7,8]; ch2=[1,2,3,4,7,5,6,0,8]; ch3=[1,2,3,4,5,0,6,7,8]
s+=puzzle(140,150,start,hl=True); s.append(f'<text x="140" y="210" text-anchor="middle" font-size="11.5" fill="{ACC}" font-weight="bold">시작 상태</text>')
for (g,cx) in [(ch1,360),(ch2,400),(ch3,440)]:
    pass
# 가지 3개
kids=[(330,90,ch1,"빈칸 ←"),(330,150,ch2,"빈칸 ↓"),(330,235,ch3,"빈칸 →")]
for cx,cy,g,lab in kids:
    s.append(line(178,150,cx-44,cy,GRAY,1.4))
    s+=puzzle(cx,cy,g)
    s.append(f'<text x="{cx}" y="{cy+44}" text-anchor="middle" font-size="10.5" fill="{GRAY}">{lab}</text>')
# 목표 표시(오른쪽)
goal=[1,2,3,4,5,6,7,8,0]
s+=puzzle(620,150,goal,hl=True); s.append(f'<text x="620" y="210" text-anchor="middle" font-size="11.5" fill="{GRN}" font-weight="bold">목표 상태</text>')
s.append(line(452,90,560,150,GRAY,1.2,dash="4,4")); s.append(line(452,235,560,150,GRAY,1.2,dash="4,4"))
s.append(f'<text x="490" y="120" text-anchor="middle" font-size="11" fill="{GRAY}">…연산자를 거듭 적용…</text>')
s.append(f'<text x="{W/2}" y="{H-16}" text-anchor="middle" font-size="12" fill="{GRAY}">상태(보드 배치) · 연산자(빈칸 밀기) · 목표(정렬). 시작에서 목표까지의 경로를 찾는 일</text>')
save("state-space.svg",s)

# ── 3. 미니맥스 트리 (13-02) ──
W,H=760,340
s=head(W,H,"나는 최선을, 상대는 나에게 최악을 둔다 — 값이 잎에서 위로 거슬러 오른다")
def nodec(x,y,t,col,r=20):
    s.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{WHT}" stroke="{col}" stroke-width="2"/>')
    s.append(f'<text x="{x}" y="{y+5}" text-anchor="middle" font-size="13" fill="{INK}" font-weight="bold">{t}</text>')
root=(380,80); mids=[(190,170),(380,170),(570,170)]
leaves=[(110,270,"3"),(190,270,"5"),(270,270,"2"),(330,270,"9"),(380,270,"1"),(430,270,"8"),(500,270,"4"),(570,270,"6"),(640,270,"7")]
# 잎-중간 연결
groups=[leaves[0:3],leaves[3:6],leaves[6:9]]
midvals=[]
for (mx,my),grp in zip(mids,groups):
    vals=[int(l[2]) for l in grp]; mv=min(vals); midvals.append(mv)
    for lx,ly,_ in grp: s.append(line(mx,my+20,lx,ly-20,GRAY,1.4))
    s.append(line(root[0],root[1]+20,mx,my-20,GRAY,1.4))
for (mx,my),mv in zip(mids,midvals): nodec(mx,my,str(mv),BLU)
nodec(*root,str(max(midvals)),ACC,r=22)
for lx,ly,v in leaves:
    s.append(f'<rect x="{lx-16}" y="{ly-16}" width="32" height="32" rx="6" fill="{BAND}" stroke="{GRAY}" stroke-width="1.2"/>')
    s.append(f'<text x="{lx}" y="{ly+5}" text-anchor="middle" font-size="13" fill="{INK}">{v}</text>')
s.append(f'<text x="{root[0]+34}" y="84" font-size="12" fill="{ACC}" font-weight="bold">MAX (나: 큰 값 선택)</text>')
s.append(f'<text x="120" y="150" font-size="12" fill="{BLU}" font-weight="bold">MIN (상대: 작은 값 선택)</text>')
s.append(f'<text x="{W/2}" y="{H-14}" text-anchor="middle" font-size="11.5" fill="{GRAY}">잎 = 판 평가 점수. MIN은 자식 중 최소를, MAX는 그 결과 중 최대를 고른다</text>')
save("minimax-tree.svg",s)

# ── 4. 전향/후향 추론 (15-01) ──
W,H=760,300
s=head(W,H,"같은 규칙망을 두 방향으로 — 사실에서 앞으로(전향), 목표에서 거슬러(후향)")
# 좌: 전향
s+=[box(40,70,300,200,"",fill="#F7F2E8",st=ACC,sw=1.6)]
s.append(f'<text x="190" y="96" text-anchor="middle" font-size="14" fill="{ACC}" font-weight="bold">전향 추론 (자료 주도)</text>')
s+=[box(70,116,110,34,"사실",fill=BAND,st=INK,fs=12),box(70,164,110,34,"규칙 적용",fill=WHT,st=INK,fs=12),box(70,212,110,34,"새 사실…",fill=WHT,st=INK,fs=12)]
s.append(line(125,150,125,164,INK,1.6,arrow=True)); s.append(line(125,198,125,212,INK,1.6,arrow=True))
s.append(f'<text x="250" y="180" text-anchor="middle" font-size="11.5" fill="{GRAY}">아는 것에서</text>')
s.append(f'<text x="250" y="198" text-anchor="middle" font-size="11.5" fill="{GRAY}">결론으로 →</text>')
# 우: 후향
s+=[box(420,70,300,200,"",fill="#EAF1EA",st=GRN,sw=1.6)]
s.append(f'<text x="570" y="96" text-anchor="middle" font-size="14" fill="{GRN}" font-weight="bold">후향 추론 (목표 주도)</text>')
s+=[box(580,116,110,34,"목표",fill="#DDEBDD",st=INK,fs=12),box(580,164,110,34,"필요 조건",fill=WHT,st=INK,fs=12),box(580,212,110,34,"사실로 확인",fill=WHT,st=INK,fs=12)]
s.append(line(635,150,635,164,INK,1.6,arrow=True)); s.append(line(635,198,635,212,INK,1.6,arrow=True))
s.append(f'<text x="500" y="180" text-anchor="middle" font-size="11.5" fill="{GRAY}">← 묻고 싶은</text>')
s.append(f'<text x="500" y="198" text-anchor="middle" font-size="11.5" fill="{GRAY}">것에서 거꾸로</text>')
s.append(f'<text x="{W/2}" y="{H-14}" text-anchor="middle" font-size="11.5" fill="{GRAY}">진단(증상→병)은 후향이, 모니터링(센서→경보)은 전향이 어울린다</text>')
save("chaining.svg",s)

# ── 5. 퍼지 멤버십 함수 (17-02) ──
W,H=760,330; OX,RX,TOP,BOT=70,710,80,260
s=head(W,H,"\'차갑다\'와 \'뜨겁다\' 사이엔 칼금이 없다 — 0과 1 사이의 정도로 표현한다")
s+=[line(OX,BOT,RX,BOT,INK,1.2),line(OX,TOP-6,OX,BOT,INK,1.2),
    f'<text x="{OX-8}" y="{TOP+4}" text-anchor="end" font-size="11" fill="{GRAY}">소속도</text>',
    f'<text x="{OX-8}" y="{BOT+4}" text-anchor="end" font-size="10" fill="{GRAY}">0</text>',
    f'<text x="{OX-8}" y="{TOP+10}" text-anchor="end" font-size="10" fill="{GRAY}">1</text>',
    f'<text x="{RX}" y="{BOT+20}" text-anchor="end" font-size="11" fill="{GRAY}">온도 →</text>']
def tri(pts,col,lab,lx):
    d=" ".join(f"{OX+px*(RX-OX):.0f},{BOT-py*(BOT-TOP):.0f}" for px,py in pts)
    s.append(f'<polyline points="{d}" fill="none" stroke="{col}" stroke-width="2.6"/>')
    s.append(f'<text x="{lx}" y="{TOP-12}" text-anchor="middle" font-size="12.5" fill="{col}" font-weight="bold">{lab}</text>')
tri([(0,1),(0.30,1),(0.45,0)], BLU, "차갑다", OX+0.15*(RX-OX))
tri([(0.30,0),(0.50,1),(0.70,0)], GRN, "적당", OX+0.50*(RX-OX))
tri([(0.55,0),(0.70,1),(1,1)], RED, "뜨겁다", OX+0.85*(RX-OX))
# 예시 점선: 특정 온도
xv=0.40; px=OX+xv*(RX-OX)
s.append(line(px,TOP,px,BOT,GRAY,1.2,dash="4,4"))
s.append(f'<text x="{px:.0f}" y="{BOT+20}" text-anchor="middle" font-size="10.5" fill="{GRAY}">이 온도</text>')
s.append(f'<text x="{W/2}" y="{H-16}" text-anchor="middle" font-size="11.5" fill="{GRAY}">한 온도가 \'차갑다 0.3·적당 0.5\'처럼 여러 집합에 동시에, 정도껏 속한다</text>')
save("fuzzy-membership.svg",s)

# ── 6. 회귀 vs 분류 (18-02) ──
W,H=760,340
s=head(W,H,"숫자를 맞히면 회귀, 무리를 가르면 분류 — 지도학습의 두 얼굴")
pts_l=[(0.12,0.78),(0.22,0.66),(0.33,0.60),(0.45,0.50),(0.55,0.46),(0.66,0.36),(0.78,0.28),(0.88,0.22)]
def panel(x0,y0,w,h,title,col):
    s.append(box(x0,y0,w,h,"",fill=WHT,st=col,sw=1.6))
    s.append(f'<text x="{x0+w/2:.0f}" y="{y0+24}" text-anchor="middle" font-size="13.5" fill="{col}" font-weight="bold">{title}</text>')
# 좌: 회귀
px0,py0,pw,ph=40,64,330,240; panel(px0,py0,pw,ph,"회귀: 선을 긋는다",ACC)
ax0,ay0,ax1,ay1=px0+40,py0+200,px0+pw-20,py0+50
def mapxy(p,bx0,by0,bx1,by1): return (bx0+p[0]*(bx1-bx0), by0+(1-p[1])*(by1-by0))
s.append(line(ax0,ay0,ax1,ay0,GRAY,1)); s.append(line(ax0,ay0,ax0,ay1,GRAY,1))
for p in pts_l:
    x,y=mapxy(p,ax0,py0+200,ax1,py0+50); s.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="4.5" fill="{BLU}"/>')
x1,y1=mapxy((0.05,0.82),ax0,py0+200,ax1,py0+50); x2,y2=mapxy((0.95,0.18),ax0,py0+200,ax1,py0+50)
s.append(line(x1,y1,x2,y2,ACC,2.4))
s.append(f'<text x="{px0+pw/2:.0f}" y="{py0+ph-12}" text-anchor="middle" font-size="11" fill="{GRAY}">예: 평수 → 집값</text>')
# 우: 분류
qx0=400; panel(qx0,py0,pw,ph,"분류: 경계를 긋는다",GRN)
bx0,by0,bx1,by1=qx0+40,py0+200,qx0+pw-20,py0+50
s.append(line(bx0,by0,bx1,by0,GRAY,1)); s.append(line(bx0,by0,bx0,by1,GRAY,1))
red=[(0.2,0.7),(0.3,0.8),(0.25,0.55),(0.4,0.72),(0.18,0.85)]
blu=[(0.7,0.3),(0.8,0.45),(0.65,0.2),(0.85,0.35),(0.75,0.5)]
for p in red:
    x,y=mapxy(p,bx0,py0+200,bx1,py0+50); s.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="4.5" fill="{RED}"/>')
for p in blu:
    x,y=mapxy(p,bx0,py0+200,bx1,py0+50); s.append(f'<rect x="{x-4:.0f}" y="{y-4:.0f}" width="8" height="8" fill="{BLU}"/>')
lx1,ly1=mapxy((0.15,0.25),bx0,py0+200,bx1,py0+50); lx2,ly2=mapxy((0.9,0.95),bx0,py0+200,bx1,py0+50)
s.append(line(lx1,ly1,lx2,ly2,GRN,2.4,dash="6,4"))
s.append(f'<text x="{qx0+pw/2:.0f}" y="{py0+ph-12}" text-anchor="middle" font-size="11" fill="{GRAY}">예: 메일 → 스팸/정상</text>')
save("regression-classification.svg",s)

# ── 7. 과적합 (18-03) ──
W,H=760,320
s=head(W,H,"덜 배워도(과소), 외워 버려도(과적합) 탈 난다 — 사이의 \'적당함\'이 목표")
import random
base=[(0.10,0.30),(0.20,0.42),(0.30,0.40),(0.40,0.55),(0.50,0.52),(0.60,0.66),(0.72,0.64),(0.85,0.78)]
titles=[("과소적합","직선 하나로 뭉갬",RED,"underfit"),("적당함(일반화)","흐름을 잡음",GRN,"good"),("과적합","점을 다 외움",RED,"overfit")]
pw=226; gap=12; x0=24; y0=70; ph=180
for i,(t,sub,col,kind) in enumerate(titles):
    bx=x0+i*(pw+gap)
    s.append(box(bx,y0,pw,ph,"",fill=WHT,st=col,sw=1.6))
    s.append(f'<text x="{bx+pw/2:.0f}" y="{y0+22}" text-anchor="middle" font-size="13" fill="{col}" font-weight="bold">{t}</text>')
    ax0,ay0,ax1,ay1=bx+24,y0+150,bx+pw-16,y0+40
    s.append(line(ax0,ay0,ax1,ay0,GRAY,1)); s.append(line(ax0,ay0,ax0,ay1,GRAY,1))
    for p in base:
        x=ax0+p[0]*(ax1-ax0); y=ay0-p[1]*(ay0-ay1); s.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="3.6" fill="{BLU}"/>')
    if kind=="underfit":
        s.append(line(ax0+0.05*(ax1-ax0),ay0-0.34*(ay0-ay1),ax1,ay0-0.74*(ay0-ay1),col,2.4))
    elif kind=="good":
        pts=[(p[0],p[1]) for p in [(0.05,0.30),(0.3,0.45),(0.55,0.58),(0.8,0.72),(0.95,0.80)]]
        d=" ".join(f"{ax0+px*(ax1-ax0):.0f},{ay0-py*(ay0-ay1):.0f}" for px,py in pts)
        s.append(f'<polyline points="{d}" fill="none" stroke="{col}" stroke-width="2.4"/>')
    else:
        d=" ".join(f"{ax0+p[0]*(ax1-ax0):.0f},{ay0-p[1]*(ay0-ay1):.0f}" for p in base)
        s.append(f'<polyline points="{d}" fill="none" stroke="{col}" stroke-width="2.2"/>')
    s.append(f'<text x="{bx+pw/2:.0f}" y="{y0+ph-10}" text-anchor="middle" font-size="10.5" fill="{GRAY}">{sub}</text>')
s.append(f'<text x="{W/2}" y="{H-14}" text-anchor="middle" font-size="11.5" fill="{GRAY}">과적합은 훈련 데이터의 잡음까지 외워, 처음 보는 데이터에서 헛디딘다</text>')
save("overfitting.svg",s)

# ── 8. 군집화 k-means (22-02) ──
W,H=760,320
s=head(W,H,"정답표 없이, 가까운 것끼리 스스로 무리를 이룬다")
clusters=[((0.22,0.30),RED,[(0.16,0.22),(0.24,0.28),(0.20,0.38),(0.30,0.32),(0.14,0.34)]),
          ((0.55,0.70),GRN,[(0.50,0.62),(0.58,0.72),(0.52,0.78),(0.62,0.66),(0.56,0.60)]),
          ((0.80,0.28),BLU,[(0.74,0.22),(0.84,0.30),(0.78,0.36),(0.86,0.20),(0.82,0.40)])]
ax0,ay0,ax1,ay1=80,270,690,70
s.append(line(ax0,ay0,ax1,ay0,GRAY,1)); s.append(line(ax0,ay0,ax0,ay1,GRAY,1))
def m(p): return (ax0+p[0]*(ax1-ax0), ay0-p[1]*(ay0-ay1))
for (cen,col,pts) in clusters:
    cx,cy=m(cen)
    s.append(f'<ellipse cx="{cx:.0f}" cy="{cy:.0f}" rx="62" ry="50" fill="{col}" opacity="0.07"/>')
    for p in pts:
        x,y=m(p); s.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="4.5" fill="{col}"/>')
    s.append(f'<path d="M{cx-7:.0f},{cy:.0f} L{cx+7:.0f},{cy:.0f} M{cx:.0f},{cy-7:.0f} L{cx:.0f},{cy+7:.0f}" stroke="{INK}" stroke-width="2"/>')
    s.append(f'<text x="{cx:.0f}" y="{cy-14:.0f}" text-anchor="middle" font-size="11" fill="{col}" font-weight="bold">중심</text>')
s.append(f'<text x="{W/2}" y="{H-14}" text-anchor="middle" font-size="11.5" fill="{GRAY}">k-평균: 중심을 정하고 → 가까운 점을 모으고 → 중심을 다시 계산, 반복</text>')
save("clustering.svg",s)
print("batch1 done")
