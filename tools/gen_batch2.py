#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""개념 도식 묶음 2: DFS, 알파-베타 가지치기, 역전파, 딥러닝 계층 특징,
어텐션 천장·신경기호, 뉴로모픽(폰노이만 병목), 로봇 지각-계획-행동, 사이버네틱스 피드백."""
import os, math
A=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"pages","assets")
INK="#2A2A2A";ACC="#B5651D";BLU="#3B6EA5";GRN="#4E7A51";RED="#B5495B";PAPER="#FBF7EF";BORD="#E7DFCB";GRAY="#7A7268";BAND="#F3E7D6";WHT="#FFFFFF"
F="'Helvetica Neue', Arial, 'AppleSDGothicNeo', sans-serif"
DEF='<defs><marker id="ar" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#2A2A2A"/></marker><marker id="arr" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#B5495B"/></marker></defs>'
def head(W,H,sub):
    return [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="{F}">',DEF,
            f'<rect x="2" y="2" width="{W-4}" height="{H-4}" rx="14" fill="{PAPER}" stroke="{BORD}"/>',
            f'<text x="{W/2}" y="34" text-anchor="middle" font-size="14" fill="{GRAY}" font-style="italic">{sub}</text>']
def box(x,y,w,h,txt,fill=WHT,st=INK,fs=13.5,tc=INK,bold=True,rx=8,sw=1.6):
    fw=' font-weight="bold"' if bold else ''
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{st}" stroke-width="{sw}"/>'
            f'<text x="{x+w/2:.0f}" y="{y+h/2+5:.0f}" text-anchor="middle" font-size="{fs}" fill="{tc}"{fw}>{txt}</text>')
def line(x1,y1,x2,y2,col=INK,w=1.8,arrow=False,dash=None,mk="ar"):
    d=f' stroke-dasharray="{dash}"' if dash else ''; m=f' marker-end="url(#{mk})"' if arrow else ''
    return f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" stroke="{col}" stroke-width="{w}"{d}{m}/>'
def save(name,parts): parts.append('</svg>'); open(os.path.join(A,name),"w",encoding="utf-8").write("\n".join(parts)); print(name)

# ── 1. DFS (11-02) ── 깊이 우선 방문 순서
W,H=760,330
s=head(W,H,"한 길을 끝까지 파고들었다가, 막히면 되돌아 나온다 — 깊이 우선")
# 이진 트리 좌표
pos={'A':(380,70),'B':(230,150),'C':(530,150),'D':(150,240),'E':(310,240),'F':(450,240),'G':(610,240)}
edges=[('A','B'),('A','C'),('B','D'),('B','E'),('C','F'),('C','G')]
for a,b in edges:
    s.append(line(*pos[a],pos[b][0],pos[b][1],GRAY,1.5))
order={'A':1,'B':2,'D':3,'E':4,'C':5,'F':6,'G':7}  # DFS preorder
for n,(x,y) in pos.items():
    s.append(f'<circle cx="{x}" cy="{y}" r="22" fill="{WHT}" stroke="{ACC}" stroke-width="2"/>')
    s.append(f'<text x="{x}" y="{y+5}" text-anchor="middle" font-size="14" fill="{INK}" font-weight="bold">{n}</text>')
    s.append(f'<circle cx="{x+20}" cy="{y-18}" r="11" fill="{ACC}"/>')
    s.append(f'<text x="{x+20}" y="{y-14}" text-anchor="middle" font-size="11" fill="#fff" font-weight="bold">{order[n]}</text>')
s.append(f'<text x="{W/2}" y="295" text-anchor="middle" font-size="12" fill="{GRAY}">방문 순서 A→B→D→(되돌아)→E→(되돌아)→C→F→G  ·  스택(또는 재귀)으로 \'가장 최근 갈림길\'부터</text>')
s.append(f'<text x="{W/2}" y="{H-12}" text-anchor="middle" font-size="11.5" fill="{BLU}">장점: 메모리 적음(현재 경로만) · 단점: 최단경로 보장 못 함, 무한히 깊으면 못 빠져나옴</text>')
save("dfs-tree.svg",s)

# ── 2. 알파-베타 가지치기 (13-03) ──
W,H=760,330
s=head(W,H,"이미 진 가지는 끝까지 볼 필요가 없다 — 결과는 같고 속도는 빠르다")
root=(380,72); mids=[(210,160),(550,160)]
leaves=[(120,255,"3",False),(210,255,"5",False),(300,255,"6",False),
        (470,255,"2",False),(550,255,"×",True),(630,255,"×",True)]
for (mx,my) in mids: s.append(line(root[0],root[1]+22,mx,my-20,GRAY,1.5))
groups=[leaves[0:3],leaves[3:6]]
for (mx,my),grp in zip(mids,groups):
    for lx,ly,_,pr in grp: s.append(line(mx,my+20,lx,ly-18,(RED if pr else GRAY),1.5,dash="4,3" if pr else None))
# 노드
for (x,y,t,col) in [(root[0],root[1],"3",ACC),(mids[0][0],mids[0][1],"3",BLU),(mids[1][0],mids[1][1],"≤2",BLU)]:
    s.append(f'<circle cx="{x}" cy="{y}" r="21" fill="{WHT}" stroke="{col}" stroke-width="2"/>')
    s.append(f'<text x="{x}" y="{y+5}" text-anchor="middle" font-size="13" fill="{INK}" font-weight="bold">{t}</text>')
for lx,ly,v,pr in leaves:
    s.append(f'<rect x="{lx-15}" y="{ly-15}" width="30" height="30" rx="6" fill="{("#F3DADE" if pr else BAND)}" stroke="{(RED if pr else GRAY)}" stroke-width="1.3"/>')
    s.append(f'<text x="{lx}" y="{ly+5}" text-anchor="middle" font-size="13" fill="{(RED if pr else INK)}">{v}</text>')
s.append(f'<text x="{root[0]+30}" y="76" font-size="11.5" fill="{ACC}" font-weight="bold">MAX</text>')
s.append(f'<text x="150" y="150" font-size="11.5" fill="{BLU}" font-weight="bold">MIN</text>')
s.append(f'<text x="640" y="200" font-size="11" fill="{RED}" font-weight="bold">가지치기!</text>')
s.append(f'<text x="{W/2}" y="{H-12}" text-anchor="middle" font-size="11.5" fill="{GRAY}">오른쪽 MIN이 이미 2를 봤다 → 왼쪽 결과 3보다 작을 게 뻔하니 나머지(×)는 안 본다</text>')
save("alpha-beta.svg",s)

# ── 3. 역전파 (19-02) ──
W,H=760,320
s=head(W,H,"앞으로 답을 내고(순전파), 오차를 거꾸로 흘려보내 가중치를 고친다(역전파)")
layers=[("입력",3,120),("은닉",4,330),("출력",2,540)]
coords={}
for li,(name,cnt,x) in enumerate(layers):
    for j in range(cnt):
        y=90+ (j+ (0 if cnt==4 else (0.5 if cnt==3 else 1)) )*44
        coords[(li,j)]=(x,y)
# 연결
for li in range(len(layers)-1):
    for j in range(layers[li][1]):
        for k in range(layers[li+1][1]):
            s.append(line(*coords[(li,j)],coords[(li+1,k)][0],coords[(li+1,k)][1],"#D8CDB4",1))
# 노드
for (li,j),(x,y) in coords.items():
    col=[GRAY,BLU,ACC][li]
    s.append(f'<circle cx="{x}" cy="{y}" r="15" fill="{WHT}" stroke="{col}" stroke-width="1.8"/>')
for name,cnt,x in layers:
    s.append(f'<text x="{x}" y="78" text-anchor="middle" font-size="12" fill="{GRAY}">{name}층</text>')
# 순전파/역전파 화살표
s.append(line(120,275,540,275,GRN,2,arrow=True)); s.append(f'<text x="330" y="268" text-anchor="middle" font-size="12" fill="{GRN}" font-weight="bold">순전파: 입력 → 예측</text>')
s.append(line(560,298,140,298,RED,2,arrow=True,mk="arr")); s.append(f'<text x="350" y="312" text-anchor="middle" font-size="12" fill="{RED}" font-weight="bold">역전파: 오차를 거슬러 보내 가중치 수정</text>')
save("backprop.svg",s)

# ── 4. 딥러닝 계층 특징 (19-04) ──
W,H=760,320
s=head(W,H,"층이 깊어질수록 점·선에서 부분으로, 부분에서 사물로 — 특징이 저절로 쌓인다")
stages=[("픽셀/입력","원본 이미지",GRAY),("모서리·점","낮은 층",BLU),("눈·코·바퀴","중간 층",GRN),("얼굴·자동차","높은 층",ACC),("\"고양이\"","출력",RED)]
bw=120; gap=20; x0=30; y=120; h=90
for i,(t,sub,col) in enumerate(stages):
    x=x0+i*(bw+gap)
    s.append(box(x,y,bw,h,"",fill=WHT,st=col,sw=1.8))
    s.append(f'<text x="{x+bw/2:.0f}" y="{y+38}" text-anchor="middle" font-size="13" fill="{INK}" font-weight="bold">{t}</text>')
    s.append(f'<text x="{x+bw/2:.0f}" y="{y+62}" text-anchor="middle" font-size="11" fill="{GRAY}">{sub}</text>')
    if i<len(stages)-1: s.append(line(x+bw,y+h/2,x+bw+gap,y+h/2,INK,1.8,arrow=True))
s.append(f'<text x="{W/2}" y="{H-22}" text-anchor="middle" font-size="11.5" fill="{GRAY}">사람이 특징을 일일이 정해 주던 일을, 깊은 층들이 데이터로부터 스스로 알아낸다</text>')
save("deep-features.svg",s)

# ── 5. 어텐션 천장 & 신경-기호 (19-05) ──
W,H=760,330; OX,RX,TOP,BOT=70,690,90,250
s=head(W,H,"데이터를 키울수록 좋아지지만 천장에 부딪힌다 — 논리(기호)와 손잡아 넘어선다")
s+=[line(OX,BOT,RX,BOT,INK,1.2),line(OX,TOP-6,OX,BOT,INK,1.2),
    f'<text x="{OX-8}" y="{TOP+4}" text-anchor="end" font-size="11" fill="{GRAY}">능력</text>',
    f'<text x="{RX}" y="{BOT+20}" text-anchor="end" font-size="11" fill="{GRAY}">데이터·크기 →</text>']
# 천장선
s.append(line(OX,TOP+30,RX,TOP+30,GRAY,1.3,dash="6,4"))
s.append(f'<text x="{RX-6}" y="{TOP+24}" text-anchor="end" font-size="11" fill="{GRAY}">논리·일관성의 천장</text>')
# 어텐션 곡선(천장에 점근)
pts=[]
for i in range(0,71):
    x=i/100; v=TOP+30+ (BOT-TOP-30)*math.exp(-2.6*x)
    pts.append((OX+x*(RX-OX),v))
s.append(f'<polyline points="{" ".join(f"{x:.0f},{y:.0f}" for x,y in pts)}" fill="none" stroke="{BLU}" stroke-width="2.6"/>')
s.append(f'<text x="{pts[-1][0]:.0f}" y="{pts[-1][1]-10:.0f}" font-size="11.5" fill="{BLU}" font-weight="bold">어텐션(LLM)</text>')
# 신경-기호 돌파(천장 위로)
bx,by=pts[-1]
brk=[(bx,by),(bx+30,by-6),(bx+55,TOP+30),(bx+80,TOP-2)]
s.append(f'<polyline points="{" ".join(f"{x:.0f},{y:.0f}" for x,y in brk)}" fill="none" stroke="{ACC}" stroke-width="2.8" stroke-dasharray="2,0"/>')
s.append(f'<text x="{bx+30:.0f}" y="{TOP-8:.0f}" font-size="11.5" fill="{ACC}" font-weight="bold">+ 논리(신경-기호)</text>')
s.append(f'<text x="{W/2}" y="{H-16}" text-anchor="middle" font-size="11.5" fill="{GRAY}">통계적 패턴만으론 못 넘는 \'추론·일관성\'의 벽 — 기호 추론과의 결합이 다음 문을 연다</text>')
save("attention-ceiling.svg",s)

# ── 6. 뉴로모픽: 폰 노이만 병목 (08-04) ──
W,H=760,320
s=head(W,H,"연산과 기억을 따로 둔 컴퓨터 vs 한데 둔 뇌 — 병목을 없앤 칩")
# 좌: 폰 노이만
s.append(box(40,70,330,200,"",fill=WHT,st=GRAY,sw=1.6))
s.append(f'<text x="205" y="94" text-anchor="middle" font-size="13.5" fill="{INK}" font-weight="bold">폰 노이만 구조</text>')
s+=[box(70,120,110,50,"연산(CPU)",fill=BAND,st=INK,fs=12),box(230,120,110,50,"기억(메모리)",fill="#E9EEF5",st=BLU,fs=12)]
s.append(line(180,135,230,135,RED,2,arrow=True,mk="arr")); s.append(line(230,155,180,155,RED,2,arrow=True,mk="arr"))
s.append(f'<text x="205" y="200" text-anchor="middle" font-size="11.5" fill="{RED}" font-weight="bold">좁은 통로로 끊임없이 오감 = 병목</text>')
s.append(f'<text x="205" y="222" text-anchor="middle" font-size="11" fill="{GRAY}">데이터가 많을수록 막힌다</text>')
# 우: 뉴로모픽
s.append(box(400,70,330,200,"",fill="#EAF1EA",st=GRN,sw=1.6))
s.append(f'<text x="565" y="94" text-anchor="middle" font-size="13.5" fill="{INK}" font-weight="bold">뉴로모픽(뇌 모방)</text>')
# 뉴런 격자(연산=기억)
import math
for i in range(4):
    for j in range(3):
        x=455+i*55; y=130+j*40
        s.append(f'<circle cx="{x}" cy="{y}" r="9" fill="{WHT}" stroke="{GRN}" stroke-width="1.5"/>')
        if i<3: s.append(line(x+9,y,x+46,y,"#BcCcBc" if False else "#AFC4AF",1))
        if j<2: s.append(line(x,y+9,x,y+31,"#AFC4AF",1))
s.append(f'<text x="565" y="232" text-anchor="middle" font-size="11.5" fill="{GRN}" font-weight="bold">시냅스마다 연산+기억이 한자리</text>')
s.append(f'<text x="{W/2}" y="{H-12}" text-anchor="middle" font-size="11.5" fill="{GRAY}">스파이크로 드문드문 계산 → 저전력 · 대표 칩: TrueNorth, Loihi</text>')
save("neuromorphic.svg",s)

# ── 7. 로봇: 지각-계획-행동 + 모라벡 역설 (25-02) ──
W,H=760,300
s=head(W,H,"보고(지각) → 짜고(계획) → 움직인다(행동) — 그런데 쉬운 게 가장 어렵다")
steps=[("지각","센서로 세상을 읽기",BLU),("계획","행동 순서를 짜기",ACC),("행동","모터로 움직이기",GRN)]
bw=170; gap=40; x0=80; y=90; h=70
xs=[x0+i*(bw+gap) for i in range(3)]
for (t,sub,col),x in zip(steps,xs):
    s.append(box(x,y,bw,h,"",fill=WHT,st=col,sw=1.8))
    s.append(f'<text x="{x+bw/2:.0f}" y="{y+30}" text-anchor="middle" font-size="14" fill="{INK}" font-weight="bold">{t}</text>')
    s.append(f'<text x="{x+bw/2:.0f}" y="{y+52}" text-anchor="middle" font-size="11" fill="{GRAY}">{sub}</text>')
for i in range(2): s.append(line(xs[i]+bw,y+h/2,xs[i+1],y+h/2,INK,1.8,arrow=True))
# 피드백
s.append(f'<path d="M{xs[2]+bw/2:.0f},{y+h} L{xs[2]+bw/2:.0f},200 L{xs[0]+bw/2:.0f},200 L{xs[0]+bw/2:.0f},{y+h}" fill="none" stroke="{GRAY}" stroke-width="1.5" stroke-dasharray="5,4" marker-end="url(#ar)"/>')
s.append(f'<text x="{W/2}" y="194" text-anchor="middle" font-size="11" fill="{GRAY}">움직인 결과를 다시 지각</text>')
s.append(box(150,232,460,40,"모라벡의 역설: 어른의 체스보다 아기의 걷기·잡기가 더 어렵다",fill=BAND,st=ACC,fs=12,tc=INK))
save("sense-plan-act.svg",s)

# ── 8. 사이버네틱스 피드백 루프 (29-01) ──
W,H=760,290
s=head(W,H,"목표와 현재의 \'차이\'를 재서 스스로 바로잡는다 — 모든 자동 제어의 뿌리")
s+=[box(60,120,120,56,"목표값",fill=BAND,st=INK,fs=12.5)]
s.append(f'<circle cx="250" cy="148" r="22" fill="{WHT}" stroke="{ACC}" stroke-width="2"/>')
s.append(f'<text x="250" y="153" text-anchor="middle" font-size="18" fill="{ACC}" font-weight="bold">−</text>')
s.append(f'<text x="250" y="110" text-anchor="middle" font-size="11" fill="{GRAY}">오차 = 목표 − 현재</text>')
s+=[box(310,120,130,56,"제어기",fill=WHT,st=BLU,fs=12.5),box(490,120,130,56,"대상(시스템)",fill=WHT,st=GRN,fs=12.5)]
s.append(line(180,148,228,148,INK,1.8,arrow=True))
s.append(line(272,148,310,148,INK,1.8,arrow=True))
s.append(line(440,148,490,148,INK,1.8,arrow=True))
s.append(line(620,148,680,148,INK,1.8,arrow=True)); s.append(f'<text x="676" y="138" text-anchor="end" font-size="11" fill="{GRAY}">출력</text>')
# 피드백(센서로 현재값 되돌림)
s.append(f'<path d="M650,176 L650,240 L250,240 L250,170" fill="none" stroke="{RED}" stroke-width="1.8" stroke-dasharray="5,4" marker-end="url(#arr)"/>')
s.append(f'<text x="450" y="234" text-anchor="middle" font-size="11.5" fill="{RED}" font-weight="bold">센서로 현재값을 되먹임(feedback)</text>')
s.append(f'<text x="{W/2}" y="{H-10}" text-anchor="middle" font-size="11" fill="{GRAY}">에어컨·자동운전·항법장치… AI의 \'목표를 향해 스스로 조정\'이라는 발상의 조상</text>')
save("feedback-loop.svg",s)
print("batch2 done")
