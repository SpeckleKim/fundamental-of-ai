#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""본문의 아스키 다이어그램들을 통일 Drawing Style의 그림 다이어그램으로 재작도.
대상: 에이전트 고리(24-01), 파스 트리(23-04), 의미망(14-01),
     전문가 시스템 구조(16-01), 퍼셉트론(19-01), 유전 알고리즘 사이클(20-02)."""
import os
A=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"pages","assets")
INK="#2A2A2A";ACC="#B5651D";BLU="#3B6EA5";GRN="#4E7A51";PAPER="#FBF7EF";BORD="#E7DFCB";GRAY="#7A7268";BAND="#F3E7D6";WHT="#FFFFFF"
F="'Helvetica Neue', Arial, 'AppleSDGothicNeo', sans-serif"
DEF='<defs><marker id="ar" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#2A2A2A"/></marker><marker id="arb" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#3B6EA5"/></marker></defs>'
def head(W,H,sub):
    return [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="{F}">',DEF,
            f'<rect x="2" y="2" width="{W-4}" height="{H-4}" rx="14" fill="{PAPER}" stroke="{BORD}"/>',
            f'<text x="{W/2}" y="34" text-anchor="middle" font-size="14" fill="{GRAY}" font-style="italic">{sub}</text>']
def box(x,y,w,h,txt,fill=WHT,st=INK,fs=13.5,tc=INK,bold=True,rx=8,sw=1.6):
    fw=' font-weight="bold"' if bold else ''
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{st}" stroke-width="{sw}"/>'
            f'<text x="{x+w/2:.0f}" y="{y+h/2+5:.0f}" text-anchor="middle" font-size="{fs}" fill="{tc}"{fw}>{txt}</text>')
def line(x1,y1,x2,y2,col=INK,w=1.8,arrow=True,dash=None):
    d=f' stroke-dasharray="{dash}"' if dash else ''
    m=' marker-end="url(#ar)"' if arrow else ''
    return f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" stroke="{col}" stroke-width="{w}"{d}{m}/>'
def save(name,parts):
    parts.append('</svg>'); open(os.path.join(A,name),"w",encoding="utf-8").write("\n".join(parts)); print(name)

# ───────────────────────── 1. 에이전트 고리 (24-01) ─────────────────────────
W,H=760,260; s=head(W,H,"센서로 인식하고, 두뇌로 판단하고, 액추에이터로 행동한다 — 환경과의 끝없는 고리")
# 환경 좌우 라벨
s.append(f'<rect x="34" y="96" width="120" height="70" rx="10" fill="{BAND}" stroke="{INK}" stroke-width="1.5"/>')
s.append(f'<text x="94" y="137" text-anchor="middle" font-size="15" fill="{INK}" font-weight="bold">환경</text>')
# 에이전트 큰 박스
s.append(f'<rect x="214" y="74" width="412" height="114" rx="12" fill="{WHT}" stroke="{ACC}" stroke-width="2"/>')
s.append(f'<text x="420" y="98" text-anchor="middle" font-size="13" fill="{ACC}" font-weight="bold">에이전트</text>')
s+= [box(238,118,108,46,"센서",fill="#E9EEF5",st=BLU,tc=INK),
     box(366,118,108,46,"두뇌",fill=BAND,st=ACC,tc=INK),
     box(494,118,108,46,"액추에이터",fill="#E9EEF5",st=BLU,tc=INK)]
s.append(line(346,141,366,141)); s.append(line(474,141,494,141))
s.append(f'<text x="356" y="132" text-anchor="middle" font-size="10.5" fill="{GRAY}">판단</text>')
s.append(f'<text x="484" y="132" text-anchor="middle" font-size="10.5" fill="{GRAY}">행동</text>')
# 환경 → 센서 (인식)
s.append(line(154,131,238,131,BLU,2)); s.append(f'<text x="196" y="122" text-anchor="middle" font-size="11.5" fill="{BLU}">인식</text>')
# 액추에이터 → 환경(오른쪽) → 다시 환경(왼쪽)로 피드백
s.append(f'<rect x="686" y="96" width="40" height="70" rx="8" fill="{BAND}" stroke="{INK}" stroke-width="1.5"/>')
s.append(f'<text x="706" y="125" text-anchor="middle" font-size="12" fill="{INK}" font-weight="bold">환</text><text x="706" y="143" text-anchor="middle" font-size="12" fill="{INK}" font-weight="bold">경</text>')
s.append(line(602,131,686,131,BLU,2)); s.append(f'<text x="644" y="122" text-anchor="middle" font-size="11.5" fill="{BLU}">영향</text>')
# 피드백 곡선: 오른쪽 환경 아래 → 왼쪽 환경 아래
s.append(f'<path d="M706,166 L706,212 L94,212 L94,166" fill="none" stroke="{GRAY}" stroke-width="1.4" stroke-dasharray="5,4" marker-end="url(#ar)"/>')
s.append(f'<text x="400" y="228" text-anchor="middle" font-size="11.5" fill="{GRAY}">행동이 환경을 바꾸고, 바뀐 환경을 다시 인식한다</text>')
save("agent-loop.svg",s)

# ───────────────────────── 2. 파스 트리 (23-04) ─────────────────────────
W,H=760,360; s=head(W,H,'"the man hit the ball" — 문장이 규칙을 따라 부품으로 쪼개진다')
def nd(x,y,t,fill=BAND,st=ACC,w=64,tc=INK,fs=13.5):
    return box(x-w/2,y,w,30,t,fill=fill,st=st,tc=tc,fs=fs,rx=7,sw=1.5)
def leaf(x,y,t,w=58):
    return box(x-w/2,y,w,28,t,fill=WHT,st=GRAY,tc=INK,fs=12.5,bold=False,rx=6,sw=1.3)
# 좌표
S=(380,58); NP=(210,128); VP=(540,128)
T1=(140,200); N1=(280,200); V=(450,200); NP2=(620,200)
T2=(560,272); N2=(680,272)
the1=(140,330); man=(280,330); hit=(450,330); the2=(560,330); ball=(680,330)
def conn(p,c): return line(p[0],p[1]+30,c[0],c[1],INK,1.4,arrow=False)
for a,b in [(S,NP),(S,VP),(NP,T1),(NP,N1),(VP,V),(VP,NP2),(NP2,T2),(NP2,N2),
            (T1,the1),(N1,man),(V,hit),(T2,the2),(N2,ball)]:
    s.append(conn(a,b))
s.append(nd(*S,"Sentence",fill=ACC,st=INK,w=110,tc=WHT))
for p,t in [(NP,"NP"),(VP,"VP"),(NP2,"NP")]: s.append(nd(*p,t,w=56))
for p,t in [(T1,"T"),(N1,"N"),(V,"Verb"),(T2,"T"),(N2,"N")]:
    s.append(nd(*p,t,fill="#E9EEF5",st=BLU,w=56))
for p,t in [(the1,"the"),(man,"man"),(hit,"hit"),(the2,"the"),(ball,"ball")]:
    s.append(leaf(*p,t))
save("parse-tree.svg",s)

# ───────────────────────── 3. 의미망 (14-01) ─────────────────────────
W,H=760,310; s=head(W,H,"개념을 점으로, 관계를 화살표로 — 지식이 그물처럼 이어진다")
def cnode(x,y,t,fill=WHT,st=INK):
    return (f'<ellipse cx="{x}" cy="{y}" rx="56" ry="28" fill="{fill}" stroke="{st}" stroke-width="1.7"/>'
            f'<text x="{x}" y="{y+5}" text-anchor="middle" font-size="14" fill="{INK}" font-weight="bold">{t}</text>')
def rlabel(mx,my,lab,col):
    s.append(f'<rect x="{mx-28}" y="{my-10}" width="56" height="18" rx="6" fill="{PAPER}"/>')
    s.append(f'<text x="{mx}" y="{my+4}" text-anchor="middle" font-size="11.5" fill="{col}" font-weight="bold">{lab}</text>')
참새=(118,170); 새=(380,170); 동물=(640,170); 날개=(380,268); 날다_=(580,82)
# 가로 스파인 참새 → 새 → 동물 (is-a)
s.append(line(174,170,322,170,ACC,1.9)); rlabel(248,160,"is-a",ACC)
s.append(line(438,170,582,170,ACC,1.9)); rlabel(510,160,"is-a",ACC)
# 새 → 날개 (has-a, 아래)
s.append(line(380,198,380,238,BLU,1.8)); rlabel(380,218,"has-a",BLU)
# 새 → 날다 (can, 위 대각)
s.append(line(414,150,536,98,GRN,1.8)); rlabel(478,118,"can",GRN)
s.append(cnode(*참새,"참새")); s.append(cnode(*새,"새",fill=BAND)); s.append(cnode(*동물,"동물"))
s.append(cnode(*날개,"날개",fill="#E9EEF5")); s.append(cnode(*날다_,"날다",fill="#EAF1EA"))
s.append(f'<text x="{W/2}" y="300" text-anchor="middle" font-size="11.5" fill="{GRAY}">상속: \'참새\'는 \'새\'라서, 새의 \'날개\'와 \'날다\'를 묻지 않아도 물려받는다</text>')
save("semantic-net.svg",s)

# ───────────────────────── 4. 전문가 시스템 구조 (16-01) ─────────────────────────
W,H=760,300; s=head(W,H,"아는 것(지식베이스)과 굴리는 법(추론엔진)을 나눈 두 기둥")
s+=[box(290,64,180,42,"사용자 질문 / 사실",fill=BAND,st=INK,fs=13,tc=INK)]
s.append(line(380,106,380,134,INK,1.8))
s+=[box(180,134,200,86,"",fill=WHT,st=ACC,sw=2)]
s.append(f'<text x="280" y="170" text-anchor="middle" font-size="14.5" fill="{INK}" font-weight="bold">추론엔진</text>')
s.append(f'<text x="280" y="194" text-anchor="middle" font-size="12" fill="{GRAY}">전향 / 후향 추론</text>')
s+=[box(480,134,200,86,"",fill="#E9EEF5",st=BLU,sw=2)]
s.append(f'<text x="580" y="170" text-anchor="middle" font-size="14.5" fill="{INK}" font-weight="bold">지식베이스</text>')
s.append(f'<text x="580" y="194" text-anchor="middle" font-size="12" fill="{GRAY}">사실 + 규칙(IF–THEN)</text>')
# 양방향 참조
s.append(f'<line x1="380" y1="166" x2="480" y2="166" stroke="{INK}" stroke-width="1.8" marker-end="url(#ar)" marker-start="url(#ar)"/>')
s.append(f'<text x="430" y="156" text-anchor="middle" font-size="11.5" fill="{ACC}">참조</text>')
# 결론 출력
s.append(line(280,220,280,252,INK,1.8))
s+=[box(190,252,180,36,"결론 / 설명",fill=BAND,st=INK,fs=12.5,tc=INK)]
s.append(f'<text x="580" y="266" text-anchor="middle" font-size="11.5" fill="{GRAY}">전문가의 머릿속을 둘로 갈라 기계에 옮긴 꼴</text>')
save("expert-system.svg",s)

# ───────────────────────── 5. 퍼셉트론 (19-01) ─────────────────────────
W,H=760,300; s=head(W,H,"입력에 가중치를 곱해 더하고, 문턱을 넘으면 1을 낸다 — 뉴런 한 개의 흉내")
ins=[("x₁","w₁",90),("x₂","w₂",150),("x₃","w₃",210)]
sumc=(420,150)
for name,w,y in ins:
    s.append(f'<circle cx="120" cy="{y}" r="22" fill="{WHT}" stroke="{INK}" stroke-width="1.6"/>')
    s.append(f'<text x="120" y="{y+5}" text-anchor="middle" font-size="14" fill="{INK}" font-weight="bold">{name}</text>')
    s.append(line(142,y,sumc[0]-34,sumc[1],INK,1.7))
    mx=(142+sumc[0]-34)/2; my=(y+sumc[1])/2
    s.append(f'<rect x="{mx-16}" y="{my-22}" width="34" height="17" rx="5" fill="{PAPER}"/><text x="{mx+1}" y="{my-9}" text-anchor="middle" font-size="11.5" fill="{ACC}" font-weight="bold">{w}</text>')
# 합산 노드
s.append(f'<circle cx="{sumc[0]}" cy="{sumc[1]}" r="34" fill="{BAND}" stroke="{ACC}" stroke-width="1.9"/>')
s.append(f'<text x="{sumc[0]}" y="{sumc[1]+8}" text-anchor="middle" font-size="22" fill="{ACC}" font-weight="bold">Σ</text>')
s.append(f'<text x="{sumc[0]}" y="{sumc[1]+54}" text-anchor="middle" font-size="11.5" fill="{GRAY}">가중합</text>')
# 문턱
s+=[box(510,124,120,52,"문턱 넘으면 1",fill="#E9EEF5",st=BLU,fs=12.5,tc=INK)]
s.append(line(454,150,510,150,INK,1.8))
# 출력
s.append(f'<circle cx="690" cy="150" r="22" fill="{WHT}" stroke="{INK}" stroke-width="1.6"/>')
s.append(f'<text x="690" y="155" text-anchor="middle" font-size="13" fill="{INK}" font-weight="bold">출력</text>')
s.append(line(630,150,668,150,INK,1.8))
s.append(f'<text x="{W/2}" y="248" text-anchor="middle" font-size="12" fill="{GRAY}">학습 = 답이 틀리면 가중치 w를 조금씩 고쳐 문턱을 다시 맞추는 일</text>')
s.append(f'<text x="{W/2}" y="270" text-anchor="middle" font-size="11.5" fill="{GRAY}">한계: 직선 하나로 가르는 것만 가능 — XOR는 풀지 못한다</text>')
save("perceptron.svg",s)

# ───────────────────────── 6. 유전 알고리즘 사이클 (20-02) ─────────────────────────
W,H=760,300; s=head(W,H,"한 세대의 손놀림 — 평가·선택·교차·돌연변이를 돌고 또 돈다")
# 시작 박스(맨 위 왼쪽)
s+=[box(60,64,200,40,"초기 개체군 (무작위)",fill=BAND,st=INK,fs=12.5,tc=INK)]
# 가로 파이프라인 5단계
steps=[("① 적합도 평가","얼마나 잘났나",ACC),
       ("② 선택","잘난 것 고름",ACC),
       ("③ 교차","섞어 자식 생성",BLU),
       ("④ 돌연변이","가끔 변형",GRN),
       ("새 세대","→ 다음 세대",GRAY)]
bw,bh,gap=128,56,18; x0=50; y=150
xs=[x0+i*(bw+gap) for i in range(5)]
for (name,sub,col),x in zip(steps,xs):
    s.append(box(x,y,bw,bh,"",fill=WHT,st=col,sw=1.8))
    s.append(f'<text x="{x+bw/2:.0f}" y="{y+24:.0f}" text-anchor="middle" font-size="13" fill="{INK}" font-weight="bold">{name}</text>')
    s.append(f'<text x="{x+bw/2:.0f}" y="{y+43:.0f}" text-anchor="middle" font-size="10.5" fill="{GRAY}">{sub}</text>')
# 단계 사이 화살표
for i in range(4):
    s.append(line(xs[i]+bw,y+bh/2,xs[i+1],y+bh/2,INK,1.7))
# 시작 → ① (꺾인 화살표)
s.append(f'<path d="M160,104 L160,128 L{xs[0]+bw/2:.0f},128 L{xs[0]+bw/2:.0f},{y}" fill="none" stroke="{INK}" stroke-width="1.7" marker-end="url(#ar)"/>')
# 새 세대 → ① 피드백(아래로 크게 돌아)
lastx=xs[4]+bw/2; firstx=xs[0]+bw/2
s.append(f'<path d="M{lastx:.0f},{y+bh} L{lastx:.0f},250 L{firstx:.0f},250 L{firstx:.0f},{y+bh}" fill="none" stroke="{ACC}" stroke-width="1.8" stroke-dasharray="6,4" marker-end="url(#ar)"/>')
s.append(f'<text x="{W/2}" y="244" text-anchor="middle" font-size="12" fill="{ACC}" font-style="italic">목표에 닿을 때까지 세대를 거듭 반복</text>')
save("ga-cycle.svg",s)
print("done")
