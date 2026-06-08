#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""이해도 보강 그림 묶음 4: 튜링기계·P/NP·IDDFS 노드수·온톨로지·추론 세 방향·
분류기 경계(SVM 여백)·지각의 역문제·재귀 전개·나비효과."""
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

# ── 1. 튜링 기계 (09-01) ──
W,H=760,300
s=head(W,H,"무한한 테이프 · 한 칸을 읽는 머리 · 규칙표 — 이것이 \'계산\'의 전부다")
# 테이프
cells=["…","1","0","1","1","0","…"]; cw=58; x0=(W-cw*len(cells))/2; ty=110
for i,v in enumerate(cells):
    x=x0+i*cw
    fill=BAND if i==3 else WHT
    s.append(f'<rect x="{x}" y="{ty}" width="{cw}" height="{cw}" fill="{fill}" stroke="{INK}" stroke-width="1.4"/>')
    s.append(f'<text x="{x+cw/2:.0f}" y="{ty+cw/2+7:.0f}" text-anchor="middle" font-size="20" fill="{INK}">{v}</text>')
# 머리(헤드) 표시 — 가운데 칸(index3)
hx=x0+3*cw+cw/2
s.append(f'<path d="M{hx-12:.0f},{ty+cw+30:.0f} L{hx+12:.0f},{ty+cw+30:.0f} L{hx:.0f},{ty+cw+8:.0f} z" fill="{ACC}"/>')
s.append(f'<text x="{hx:.0f}" y="{ty+cw+48:.0f}" text-anchor="middle" font-size="12" fill="{ACC}" font-weight="bold">머리(현재 위치)</text>')
# 상태 박스
s.append(box(60,ty,110,40,"상태: q₁",fill="#E9EEF5",st=BLU,fs=13))
# 규칙표
s.append(f'<rect x="170" y="232" width="420" height="44" rx="8" fill="{WHT}" stroke="{GRAY}" stroke-width="1.3"/>')
s.append(f'<text x="380" y="252" text-anchor="middle" font-size="12.5" fill="{INK}" font-weight="bold">규칙: (상태 q₁, 읽은 1) → 0을 쓰고 · 오른쪽 이동 · 상태 q₂로</text>')
s.append(f'<text x="380" y="270" text-anchor="middle" font-size="11" fill="{GRAY}">이런 규칙을 한 줄씩 따라가는 단순한 동작의 반복이 곧 계산이다</text>')
save("turing-machine.svg",s)

# ── 2. P / NP / NP-완전 (09-04) ──
W,H=760,360
s=head(W,H,"빠르게 푸는 문제(P) · 답을 받으면 빠르게 검산하는 문제(NP), 그리고 그 안의 가장 어려운 핵")
# 큰 타원 NP
s.append(f'<ellipse cx="360" cy="200" rx="300" ry="130" fill="#EAF1EA" stroke="{GRN}" stroke-width="2"/>')
s.append(f'<text x="360" y="92" text-anchor="middle" font-size="15" fill="{GRN}" font-weight="bold">NP — 답을 주면 빠르게 \'검산\'되는 문제</text>')
# P 안쪽
s.append(f'<ellipse cx="250" cy="210" rx="140" ry="86" fill="#E9EEF5" stroke="{BLU}" stroke-width="2"/>')
s.append(f'<text x="250" y="180" text-anchor="middle" font-size="14" fill="{BLU}" font-weight="bold">P</text>')
s.append(f'<text x="250" y="202" text-anchor="middle" font-size="11" fill="{INK}">빠르게 \'푸는\' 문제</text>')
s.append(f'<text x="250" y="222" text-anchor="middle" font-size="10.5" fill="{GRAY}">정렬 · 최단경로</text>')
# NP-완전 (오른쪽 가장 어려운 핵)
s.append(f'<ellipse cx="520" cy="210" rx="110" ry="76" fill="#F3DADE" stroke="{RED}" stroke-width="2"/>')
s.append(f'<text x="540" y="186" text-anchor="middle" font-size="13" fill="{RED}" font-weight="bold">NP-완전</text>')
s.append(f'<text x="540" y="206" text-anchor="middle" font-size="10.5" fill="{INK}">가장 어려운 무리</text>')
s.append(f'<text x="540" y="224" text-anchor="middle" font-size="10.5" fill="{GRAY}">외판원 · SAT · 배낭</text>')
s.append(f'<text x="360" y="342" text-anchor="middle" font-size="12" fill="{GRAY}">P ⊆ NP는 분명하지만, \'P = NP인가\'(빨리 검산되면 빨리 풀리기도 하나?)는 아직 미해결</text>')
save("pnp-venn.svg",s)

# ── 3. IDDFS 깊이별 노드 수 (11-03) ──
W,H=760,330
s=head(W,H,"트리의 노드는 마지막 한 겹에 거의 다 몰린다 — 그래서 다시 훑어도 손해가 적다")
depths=[1,2,4,8,16,32]; maxv=max(depths)
bx0=90; bw=82; gap=20; baseY=270; maxh=180
for i,v in enumerate(depths):
    x=bx0+i*(bw+gap); h=v/maxv*maxh
    s.append(f'<rect x="{x}" y="{baseY-h:.0f}" width="{bw}" height="{h:.0f}" rx="4" fill="{ACC if i==len(depths)-1 else BLU}" opacity="{1 if i==len(depths)-1 else 0.55}"/>')
    s.append(f'<text x="{x+bw/2:.0f}" y="{baseY-h-8:.0f}" text-anchor="middle" font-size="12" fill="{INK}" font-weight="bold">{v}</text>')
    s.append(f'<text x="{x+bw/2:.0f}" y="{baseY+18:.0f}" text-anchor="middle" font-size="11" fill="{GRAY}">깊이 {i+1}</text>')
s.append(f'<text x="{bx0+5*(bw+gap)+bw/2:.0f}" y="80" text-anchor="middle" font-size="11.5" fill="{ACC}" font-weight="bold">이 한 겹(32)이</text>')
s.append(f'<text x="{bx0+5*(bw+gap)+bw/2:.0f}" y="96" text-anchor="middle" font-size="11.5" fill="{ACC}" font-weight="bold">윗겹 전부(31)보다 많다</text>')
s.append(f'<text x="{W/2}" y="{H-14}" text-anchor="middle" font-size="11.5" fill="{GRAY}">가지가 2개씩 갈리면 1·2·4·8·16·32… 깊어질수록 두 배 — 윗겹 재방문은 거의 공짜인 셈</text>')
save("iddfs-bars.svg",s)

# ── 4. 온톨로지 (14-03) ──
W,H=760,330
s=head(W,H,"말이 다른 두 시스템도, 같은 \'개념 사전\'에 연결되면 서로 통한다")
# 상위 개념 계층(왼쪽)
s+=[box(60,70,150,38,"질병",fill=BAND,st=INK,fs=13)]
s+=[box(60,140,150,38,"심장질환",fill=WHT,st=INK,fs=12.5)]
s+=[box(60,210,150,38,"심근경색",fill="#E9EEF5",st=BLU,fs=12.5)]
s.append(line(135,108,135,140,GRAY,1.4)); s.append(line(135,178,135,210,GRAY,1.4))
s.append(f'<text x="222" y="130" font-size="10.5" fill="{GRAY}">상위-하위</text>')
s.append(f'<text x="222" y="146" font-size="10.5" fill="{GRAY}">(is-a)</text>')
# 두 병원 시스템(오른쪽)
s+=[box(470,110,220,46,"A 병원:  \'심근경색\'",fill=WHT,st=ACC,fs=12.5)]
s+=[box(470,200,220,46,"B 병원:  \'heart attack\'",fill=WHT,st=GRN,fs=12.5)]
# 온톨로지 연결
s.append(f'<ellipse cx="350" cy="178" rx="70" ry="40" fill="{BAND}" stroke="{INK}" stroke-width="1.6"/>')
s.append(f'<text x="350" y="174" text-anchor="middle" font-size="12.5" fill="{INK}" font-weight="bold">온톨로지</text>')
s.append(f'<text x="350" y="192" text-anchor="middle" font-size="10" fill="{GRAY}">공유 개념 사전</text>')
s.append(line(210,229,285,190,BLU,1.5))  # 심근경색→온톨로지
s.append(line(420,178,470,133,ACC,1.5,arrow=True)); s.append(f'<text x="450" y="150" font-size="10" fill="{ACC}">sameAs</text>')
s.append(line(420,178,470,223,GRN,1.5,arrow=True)); s.append(f'<text x="450" y="214" font-size="10" fill="{GRN}">sameAs</text>')
s.append(f'<text x="{W/2}" y="{H-14}" text-anchor="middle" font-size="11.5" fill="{GRAY}">의미망이 \'한 시스템 안\'의 지식이라면, 온톨로지는 \'여러 시스템이 함께 쓰는\' 공식 약속이다</text>')
save("ontology.svg",s)

# ── 5. 추론 세 방향 (15-02) ──
W,H=760,330
s=head(W,H,"같은 재료(규칙·사례·결과)를 어느 방향으로 잇느냐 — 연역·귀납·가추")
panels=[("연역 (deduction)",ACC,"규칙: 사람은 죽는다","사실: 소크라테스는 사람","∴ 소크라테스는 죽는다","확실 ↓ 좁혀 감"),
        ("귀납 (induction)",BLU,"백조1 희다 · 백조2 희다 …","수많은 사례","∴ 백조는 (아마) 희다","사례 ↑ 일반화"),
        ("가추 (abduction)",GRN,"결과: 땅이 젖었다","규칙: 비 오면 젖는다","∴ (아마) 비가 왔다","결과 ↩ 원인 추측")]
pw=226; gap=12; x0=24; y0=66
for i,(t,col,a,b,c,note) in enumerate(panels):
    x=x0+i*(pw+gap)
    s.append(box(x,y0,pw,200,"",fill=WHT,st=col,sw=1.8))
    s.append(f'<text x="{x+pw/2:.0f}" y="{y0+26}" text-anchor="middle" font-size="13.5" fill="{col}" font-weight="bold">{t}</text>')
    s.append(f'<text x="{x+pw/2:.0f}" y="{y0+62}" text-anchor="middle" font-size="11.5" fill="{INK}">{a}</text>')
    s.append(f'<text x="{x+pw/2:.0f}" y="{y0+86}" text-anchor="middle" font-size="11.5" fill="{INK}">{b}</text>')
    s.append(line(x+pw/2,y0+98,x+pw/2,y0+126,col,1.8,arrow=True))
    s.append(f'<text x="{x+pw/2:.0f}" y="{y0+148}" text-anchor="middle" font-size="11.5" fill="{col}" font-weight="bold">{c}</text>')
    s.append(f'<text x="{x+pw/2:.0f}" y="{y0+182}" text-anchor="middle" font-size="11" fill="{GRAY}">{note}</text>')
s.append(f'<text x="{W/2}" y="{H-12}" text-anchor="middle" font-size="11" fill="{GRAY}">연역만 \'반드시 참\'이고, 귀납·가추는 \'그럴듯함\' — 새 지식을 얻는 대신 틀릴 수 있다</text>')
save("inference-directions.svg",s)

# ── 6. 분류기 경계(SVM 여백) (22-01) ──
W,H=760,320
s=head(W,H,"특징 공간에 흩어진 점들을, 어떤 \'경계선\'으로 가를 것인가")
red=[(0.15,0.30),(0.25,0.45),(0.20,0.6),(0.32,0.35),(0.18,0.5),(0.3,0.62)]
blu=[(0.7,0.4),(0.8,0.55),(0.72,0.7),(0.85,0.42),(0.78,0.3),(0.66,0.55)]
def panel(x0,title,col):
    s.append(box(x0,64,226,200,"",fill=WHT,st=col,sw=1.6))
    s.append(f'<text x="{x0+113}" y="86" text-anchor="middle" font-size="13" fill="{col}" font-weight="bold">{title}</text>')
    ax0,ay0,ax1,ay1=x0+24,236,x0+206,104
    def m(p): return (ax0+p[0]*(ax1-ax0), ay0-p[1]*(ay0-ay1))
    for p in red:
        x,y=m(p); s.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="4.2" fill="{RED}"/>')
    for p in blu:
        x,y=m(p); s.append(f'<rect x="{x-4:.0f}" y="{y-4:.0f}" width="8" height="8" fill="{BLU}"/>')
    return m
# k-NN: 구불구불 경계
m1=panel(20,"k-NN: 가까운 이웃 따라",ACC)
pts=[(0.48,0.15),(0.45,0.4),(0.55,0.6),(0.48,0.85)]
d=" ".join(f"{m1(p)[0]:.0f},{m1(p)[1]:.0f}" for p in pts)
s.append(f'<polyline points="{d}" fill="none" stroke="{ACC}" stroke-width="2.2"/>')
s.append(f'<text x="133" y="256" text-anchor="middle" font-size="10" fill="{GRAY}">들쭉날쭉</text>')
# 결정트리: 계단(축 정렬)
m2=panel(267,"결정 트리: 축 따라 계단",GRN)
step=[(0.5,0.15),(0.5,0.5),(0.62,0.5),(0.62,0.85)]
d=" ".join(f"{m2(p)[0]:.0f},{m2(p)[1]:.0f}" for p in step)
s.append(f'<polyline points="{d}" fill="none" stroke="{GRN}" stroke-width="2.2"/>')
s.append(f'<text x="380" y="256" text-anchor="middle" font-size="10" fill="{GRAY}">수직·수평만</text>')
# SVM: 직선 + 여백
m3=panel(514,"SVM: 가장 넓은 길",BLU)
a=m3((0.5,0.05)); b=m3((0.5,0.95))
s.append(line(a[0],a[1],b[0],b[1],BLU,2.4))
# 여백(평행 점선)
la=m3((0.4,0.05)); lb=m3((0.4,0.95)); ra=m3((0.6,0.05)); rb=m3((0.6,0.95))
s.append(line(la[0],la[1],lb[0],lb[1],GRAY,1.2,dash="4,3")); s.append(line(ra[0],ra[1],rb[0],rb[1],GRAY,1.2,dash="4,3"))
s.append(f'<text x="627" y="256" text-anchor="middle" font-size="10" fill="{GRAY}">여백 최대</text>')
s.append(f'<text x="{W/2}" y="{H-10}" text-anchor="middle" font-size="11" fill="{GRAY}">SVM은 두 무리 사이에 \'가장 넓은 길\'이 나도록 경계를 그어, 새 점에도 잘 견딘다</text>')
save("classifiers.svg",s)

# ── 7. 지각의 역문제 (25-01) ──
W,H=760,320
s=head(W,H,"3차원 세상이 2차원 그림으로 눌리며 정보가 사라진다 — 그걸 거꾸로 푸는 일")
# 정방향: 3D 컵 → 2D
s.append(f'<ellipse cx="120" cy="150" rx="34" ry="16" fill="none" stroke="{INK}" stroke-width="1.6"/>')
s.append(f'<path d="M86,150 L92,210 a28,10 0 0 0 56,0 L154,150" fill="{BAND}" stroke="{INK}" stroke-width="1.6"/>')
s.append(f'<ellipse cx="120" cy="150" rx="34" ry="16" fill="{PAPER}" stroke="{INK}" stroke-width="1.6"/>')
s.append(f'<text x="120" y="244" text-anchor="middle" font-size="12" fill="{INK}">3D 실제 물체</text>')
s.append(line(166,170,250,170,INK,2,arrow=True)); s.append(f'<text x="208" y="160" text-anchor="middle" font-size="11" fill="{GRAY}">눈/카메라</text>')
# 2D 그림자
s.append(f'<rect x="262" y="120" width="96" height="100" rx="4" fill="#2b2b30" stroke="{INK}"/>')
s.append(f'<rect x="286" y="140" width="48" height="64" rx="3" fill="#9a9a9a"/>')
s.append(f'<text x="310" y="244" text-anchor="middle" font-size="12" fill="{INK}">2D 이미지(납작)</text>')
# 역방향: 2D → 여러 3D 후보
s.append(line(372,170,452,170,RED,2,arrow=True,mk="arr")); s.append(f'<text x="412" y="160" text-anchor="middle" font-size="11" fill="{RED}">거꾸로?</text>')
cands=[("컵",490),("원기둥",578),("물통",666)]
for name,cx in cands:
    s.append(f'<ellipse cx="{cx}" cy="135" rx="24" ry="10" fill="none" stroke="{GRAY}" stroke-width="1.3"/>')
    s.append(f'<path d="M{cx-24},135 L{cx-20},200 a20,7 0 0 0 40,0 L{cx+24},135" fill="{WHT}" stroke="{GRAY}" stroke-width="1.3"/>')
    s.append(f'<text x="{cx}" y="222" text-anchor="middle" font-size="11" fill="{GRAY}">{name}?</text>')
s.append(f'<text x="578" y="244" text-anchor="middle" font-size="12" fill="{RED}" font-weight="bold">후보가 여럿!</text>')
s.append(f'<text x="{W/2}" y="{H-12}" text-anchor="middle" font-size="11.5" fill="{GRAY}">같은 2D 그림을 만들 수 있는 3D는 여럿 — 그래서 \'보는 일\'은 답이 하나로 정해지지 않는 역문제다</text>')
save("inverse-problem.svg",s)

# ── 8. 재귀 전개 (26-02) ──
W,H=760,340
s=head(W,H,"재귀는 \'더 작은 자신\'을 부르며 내려갔다가, 바닥에서 되짚어 올라온다")
steps=[("(길이 '(a b c))","= 1 + (길이 '(b c))"),
       ("(길이 '(b c))","= 1 + (길이 '(c))"),
       ("(길이 '(c))","= 1 + (길이 '())"),
       ("(길이 '())","= 0  ← 기저 사례(멈춤)")]
for i,(a,b) in enumerate(steps):
    x=70+i*40; y=70+i*42
    s.append(box(x,y,260,32,"",fill=WHT,st=(RED if i==3 else BLU),fs=12,sw=1.5))
    s.append(f'<text x="{x+12}" y="{y+21}" font-size="12" fill="{INK}" font-weight="bold">{a}</text>')
    s.append(f'<text x="{x+135}" y="{y+21}" font-size="11.5" fill="{GRAY}">{b}</text>')
    if i<3: s.append(line(x+20,y+32,x+40,y+42,INK,1.5,arrow=True))
# 되짚어 올라오기(오른쪽)
ups=[("→ 0",70+3*40+280,70+3*42+16),
     ("→ 1",70+2*40+280,70+2*42+16),
     ("→ 2",70+1*40+280,70+1*42+16),
     ("→ 3  (정답!)",70+0*40+280,70+0*42+16)]
for i,(t,x,y) in enumerate(ups):
    col=ACC if "정답" in t else GRN
    s.append(f'<text x="{x}" y="{y}" font-size="12.5" fill="{col}" font-weight="bold">{t}</text>')
    if i<3: s.append(line(x+8,y-12,x-2,y-30,GRN,1.4,arrow=True))
s.append(f'<text x="200" y="{H-40}" text-anchor="middle" font-size="11.5" fill="{BLU}">내려갈 땐 문제를 잘게 쪼개고…</text>')
s.append(f'<text x="560" y="{H-40}" text-anchor="middle" font-size="11.5" fill="{GRN}">올라올 땐 답을 하나씩 합친다</text>')
s.append(f'<text x="{W/2}" y="{H-16}" text-anchor="middle" font-size="11" fill="{GRAY}">반드시 \'더 작아진 입력\'과 \'멈출 기저 사례\'가 있어야 무한 반복에 빠지지 않는다</text>')
save("recursion-unfold.svg",s)

# ── 9. 나비효과 (29-02) ──
W,H=760,320; OX,RX,TOP,BOT=70,700,80,250
s=head(W,H,"거의 같은 두 시작이, 시간이 흐르며 전혀 다른 결말로 갈라진다 — 나비효과")
s+=[line(OX,BOT,RX,BOT,INK,1.2),line(OX,TOP-6,OX,BOT,INK,1.2),
    f'<text x="{OX-8}" y="{TOP+4}" text-anchor="end" font-size="11" fill="{GRAY}">상태</text>',
    f'<text x="{RX}" y="{BOT+20}" text-anchor="end" font-size="11" fill="{GRAY}">시간 →</text>']
import math
def curve(seed,col,phase):
    pts=[]
    for i in range(0,101):
        t=i/100
        # 초기엔 거의 같다가 점점 증폭되어 갈라짐
        base=0.5+0.18*math.sin(3*t)
        div=phase*0.5*t*t*math.sin(9*t+seed)
        y=base+div
        pts.append((OX+t*(RX-OX), BOT-(y)*(BOT-TOP)*0.9))
    return pts
for seed,col,ph in [(0.0,BLU,1),(0.25,ACC,-1)]:
    pts=curve(seed,col,ph)
    s.append(f'<polyline points="{" ".join(f"{x:.0f},{y:.0f}" for x,y in pts)}" fill="none" stroke="{col}" stroke-width="2.4"/>')
# 시작점 거의 겹침 강조
s.append(f'<circle cx="{OX:.0f}" cy="{BOT-0.5*(BOT-TOP)*0.9-(0):.0f}" r="0"/>')
s.append(f'<text x="{OX+70}" y="{TOP+30}" font-size="11.5" fill="{GRAY}">시작은 거의 똑같다</text>')
s.append(f'<line x1="{OX+50}" y1="{TOP+40}" x2="{OX+20}" y2="155" stroke="{GRAY}" stroke-width="1" stroke-dasharray="3,3"/>')
s.append(f'<text x="{RX-40}" y="{TOP+50}" text-anchor="end" font-size="11.5" fill="{ACC}" font-weight="bold">→ 전혀 다른 결말</text>')
s.append(f'<text x="{W/2}" y="{H-12}" text-anchor="middle" font-size="11.5" fill="{GRAY}">소수점 아래 작은 차이가 증폭돼 예측을 무너뜨린다 — 날씨를 길게 못 맞히는 이유</text>')
save("butterfly-effect.svg",s)
print("batch4 done")
