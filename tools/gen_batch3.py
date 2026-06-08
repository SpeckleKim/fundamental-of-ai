#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""개념 도식 묶음 3: LISP 콘즈 셀(리스트 구조), Prolog 분해·역추적 트리, 인지과학 학제간 육각형."""
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

# ── 1. LISP 콘즈 셀: (A B C) 의 내부 구조 ──
W,H=760,300
s=head(W,H,"리스트 (A B C)는 사실 \'칸 두 개짜리 상자\'가 줄줄이 이어진 것 — car·cdr로 집는다")
# 셀 3개: 각 셀 [car|cdr]
cy=130; cw=92; ch=44; gap=64; x0=70
cells=[("A",70),("B",70+cw+gap),("C",70+2*(cw+gap))]
for i,(val,x) in enumerate(cells):
    # car 칸 + cdr 칸
    s.append(f'<rect x="{x}" y="{cy}" width="{cw}" height="{ch}" rx="5" fill="{WHT}" stroke="{INK}" stroke-width="1.6"/>')
    s.append(f'<line x1="{x+cw/2}" y1="{cy}" x2="{x+cw/2}" y2="{cy+ch}" stroke="{INK}" stroke-width="1.2"/>')
    s.append(f'<text x="{x+cw/4:.0f}" y="{cy-8}" text-anchor="middle" font-size="10.5" fill="{GRAY}">car</text>')
    s.append(f'<text x="{x+3*cw/4:.0f}" y="{cy-8}" text-anchor="middle" font-size="10.5" fill="{GRAY}">cdr</text>')
    # car 값
    s.append(f'<text x="{x+cw/4:.0f}" y="{cy+ch/2+6:.0f}" text-anchor="middle" font-size="15" fill="{ACC}" font-weight="bold">{val}</text>')
    # cdr: 다음 셀로 화살표 / 마지막은 nil
    cdrx=x+3*cw/4
    if i<2:
        s.append(f'<circle cx="{cdrx:.0f}" cy="{cy+ch/2:.0f}" r="3.5" fill="{INK}"/>')
        s.append(line(cdrx,cy+ch/2,x+cw+gap,cy+ch/2,INK,1.6,arrow=True))
    else:
        s.append(f'<text x="{cdrx:.0f}" y="{cy+ch/2+5:.0f}" text-anchor="middle" font-size="12" fill="{GRAY}">nil</text>')
s.append(f'<text x="{x0}" y="{cy-30}" font-size="13" fill="{INK}" font-weight="bold">(A B C)</text>')
# car/cdr 설명
s.append(f'<text x="{W/2}" y="222" text-anchor="middle" font-size="12.5" fill="{INK}">(car L) = 첫 원소 <tspan fill="{ACC}" font-weight="bold">A</tspan>  ·  (cdr L) = 나머지 리스트 <tspan fill="{BLU}" font-weight="bold">(B C)</tspan></text>')
s.append(f'<text x="{W/2}" y="{H-22}" text-anchor="middle" font-size="11.5" fill="{GRAY}">이 단순한 구조 덕에 코드도 데이터도 모두 리스트 — 재귀로 자연스럽게 훑는다</text>')
save("lisp-cons.svg",s)

# ── 2. Prolog 역추적(backtracking) 탐색 트리 ──
W,H=760,330
s=head(W,H,"질의에 답하려 Prolog는 규칙을 펼치며 탐색하고, 막히면 되돌아가 다른 길을 본다")
# 질의
s.append(box(290,56,180,38,"?- 조부모(톰, X)",fill=BAND,st=ACC,fs=12.5,tc=INK))
# 트리 노드들
def n(x,y,t,col,w=150,fail=False):
    fill="#F3DADE" if fail else WHT
    s.append(box(x-w/2,y,w,34,t,fill=fill,st=(RED if fail else col),fs=11.5,tc=INK,sw=1.5))
n(190,130,"부모(톰,밥)?",BLU)
n(380,130,"부모(톰,앤)?",BLU)
n(570,130,"…다른 사실",GRAY)
s.append(line(380,94,190,130,GRAY,1.3)); s.append(line(380,94,380,130,GRAY,1.3)); s.append(line(380,94,570,130,GRAY,1.3,dash="4,3"))
n(120,200,"부모(밥,X)?",GRN)
n(300,200,"막다른 길",RED,w=120,fail=True)
n(440,200,"부모(앤,X)?",GRN)
s.append(line(190,164,120,200,GRAY,1.3)); s.append(line(190,164,300,200,RED,1.3,dash="4,3"))
s.append(line(380,164,440,200,GRAY,1.3))
n(120,270,"X = 캐럴 ✓",ACC,w=130)
n(440,270,"X = 데이브 ✓",ACC,w=140)
s.append(line(120,234,120,270,GRN,1.5)); s.append(line(440,234,440,270,GRN,1.5))
s.append(f'<text x="300" y="250" text-anchor="middle" font-size="10.5" fill="{RED}">↩ 역추적</text>')
s.append(f'<text x="{W/2}" y="{H-12}" text-anchor="middle" font-size="11.5" fill="{GRAY}">사실·규칙을 차례로 맞춰 보다 실패하면 갈림길로 되돌아가 다음 후보를 시도(분해 + 역추적)</text>')
save("prolog-resolution.svg",s)

# ── 3. 인지과학 학제간 육각형 ──
W,H=760,390
s=head(W,H,"마음을 함께 묻는 여섯 학문이 한자리에 모였다 — 그 한가운데서 AI가 태어났다")
cx,cy,r=380,200,116
fields=[("심리학",ACC),("인공지능",RED),("언어학",BLU),("신경과학",GRN),("철학",ACC),("인류학",GRAY)]
pts=[]
for i in range(6):
    ang=-90+i*60
    x=cx+r*math.cos(math.radians(ang)); y=cy+r*math.sin(math.radians(ang)); pts.append((x,y))
# 서로 잇는 선(망)
for i in range(6):
    for j in range(i+1,6):
        s.append(line(*pts[i],pts[j][0],pts[j][1],"#D8CDB4",0.9))
# 중앙
s.append(f'<circle cx="{cx}" cy="{cy}" r="46" fill="{BAND}" stroke="{INK}" stroke-width="1.8"/>')
s.append(f'<text x="{cx}" y="{cy-2}" text-anchor="middle" font-size="14" fill="{INK}" font-weight="bold">인지과학</text>')
s.append(f'<text x="{cx}" y="{cy+16}" text-anchor="middle" font-size="10.5" fill="{GRAY}">마음의 과학</text>')
# 꼭짓점 노드
for (name,col),(x,y) in zip(fields,pts):
    s.append(f'<ellipse cx="{x:.0f}" cy="{y:.0f}" rx="52" ry="30" fill="{WHT}" stroke="{col}" stroke-width="2"/>')
    s.append(f'<text x="{x:.0f}" y="{y+5:.0f}" text-anchor="middle" font-size="13" fill="{INK}" font-weight="bold">{name}</text>')
s.append(f'<text x="{W/2}" y="{H-14}" text-anchor="middle" font-size="11.5" fill="{GRAY}">\'사람은 어떻게 생각하는가\'라는 한 물음을 여섯 갈래가 함께 파고든다</text>')
save("cognitive-hexagon.svg",s)
print("batch3 done")
