#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""신설 절용 그림 묶음 5: 언덕 오르기·강화학습 고리·베이지안 네트워크·죄수의 딜레마·언어 층위·홉필드 에너지."""
import os, math
A=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"pages","assets")
INK="#2A2A2A";ACC="#B5651D";BLU="#3B6EA5";GRN="#4E7A51";RED="#B5495B";PAPER="#FBF7EF";BORD="#E7DFCB";GRAY="#7A7268";BAND="#F3E7D6";WHT="#FFFFFF"
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
def line(x1,y1,x2,y2,col=INK,w=1.8,arrow=False,dash=None,mk="ar"):
    d=f' stroke-dasharray="{dash}"' if dash else ''; m=f' marker-end="url(#{mk})"' if arrow else ''
    return f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" stroke="{col}" stroke-width="{w}"{d}{m}/>'
def save(name,parts): parts.append('</svg>'); open(os.path.join(A,name),"w",encoding="utf-8").write("\n".join(parts)); print(name)

# ── 1. 언덕 오르기와 지역 최댓값 (12-04) ──
W,H=760,330; OX,RX,TOP,BOT=70,710,80,270
s=head(W,H,"가까운 봉우리만 보고 오르면, 더 높은 봉우리를 영영 놓칠 수 있다")
def land(x): # 봉우리 둘: 왼쪽 낮음(지역), 오른쪽 높음(전역)
    return (0.10 + 0.42*math.exp(-((x-0.27)/0.11)**2)   # 지역 봉우리(낮음)
                 + 0.72*math.exp(-((x-0.72)/0.12)**2))  # 전역 봉우리(높음)
xs=[i/200 for i in range(201)]; ys=[land(x) for x in xs]
lo,hi=min(ys),max(ys)
def px(x): return OX+x*(RX-OX)
def py(v): return BOT-(v-lo)/(hi-lo)*(BOT-TOP)
pathpts=" ".join(f"{px(x):.0f},{py(land(x)):.0f}" for x in xs)
s.append(f'<polyline points="{pathpts}" fill="none" stroke="{ACC}" stroke-width="2.6"/>')
# 지역 봉우리(공이 갇힘) — 왼쪽
lx=0.27
s.append(f'<circle cx="{px(lx):.0f}" cy="{py(land(lx))-8:.0f}" r="7" fill="{BLU}"/>')
s.append(f'<text x="{px(lx):.0f}" y="{py(land(lx))-20:.0f}" text-anchor="middle" font-size="11.5" fill="{BLU}" font-weight="bold">여기서 멈춤(지역 최댓값)</text>')
# 전역 봉우리 — 오른쪽
gx=0.72
s.append(f'<circle cx="{px(gx):.0f}" cy="{py(land(gx))-8:.0f}" r="7" fill="{GRN}"/>')
s.append(f'<text x="{px(gx):.0f}" y="{py(land(gx))-18:.0f}" text-anchor="middle" font-size="11.5" fill="{GRN}" font-weight="bold">전역 최댓값(진짜 목표)</text>')
# 오르는 화살표(왼쪽 봉우리로)
s.append(line(px(0.14),py(land(0.14))-8,px(0.21),py(land(0.21))-8,BLU,1.6,arrow=True,mk="arb"))
s.append(f'<text x="{W/2}" y="{H-14}" text-anchor="middle" font-size="11.5" fill="{GRAY}">언덕 오르기는 \'지금보다 높은\' 쪽으로만 간다 — 담금질은 가끔 일부러 내려가 이 함정을 빠져나온다</text>')
save("hill-climbing.svg",s)

# ── 2. 강화학습 고리 (18-04) ──
W,H=760,300
s=head(W,H,"행동하고, 그 결과로 상태와 보상을 받고, 다시 행동한다 — 시행착오의 고리")
s+=[box(120,110,190,80,"에이전트",fill=WHT,st=ACC,fs=15,sw=2)]
s.append(f'<text x="215" y="170" text-anchor="middle" font-size="11" fill="{GRAY}">무엇을 할지 정한다</text>')
s+=[box(450,110,190,80,"환경",fill="#E9EEF5",st=BLU,fs=15,sw=2)]
s.append(f'<text x="545" y="170" text-anchor="middle" font-size="11" fill="{GRAY}">세상이 반응한다</text>')
# 행동(위쪽 화살표 →)
s.append(f'<path d="M310,135 L450,135" fill="none" stroke="{ACC}" stroke-width="2" marker-end="url(#ar)"/>')
s.append(f'<text x="380" y="126" text-anchor="middle" font-size="12.5" fill="{ACC}" font-weight="bold">행동(action)</text>')
# 상태+보상(아래쪽 화살표 ←)
s.append(f'<path d="M450,168 L310,168" fill="none" stroke="{BLU}" stroke-width="2" marker-end="url(#arb)"/>')
s.append(f'<text x="380" y="186" text-anchor="middle" font-size="12.5" fill="{BLU}" font-weight="bold">상태(state) · 보상(reward)</text>')
s.append(f'<text x="{W/2}" y="240" text-anchor="middle" font-size="12" fill="{INK}">좋은 보상을 준 행동은 더 자주, 벌을 부른 행동은 덜 — 그렇게 \'정책\'이 다듬어진다</text>')
s.append(f'<text x="{W/2}" y="{H-16}" text-anchor="middle" font-size="11.5" fill="{GRAY}">정답을 알려 주는 선생은 없다. 오직 보상이라는 점수만이 길을 가리킨다(강아지 훈련처럼)</text>')
save("rl-loop.svg",s)

# ── 3. 베이지안 네트워크 (17-03) ──
W,H=760,330
s=head(W,H,"원인과 결과를 화살표로 잇고, 증거를 받아 거꾸로 의심을 좁힌다")
def node(cx,cy,t,col=INK,fill=WHT,r=40):
    s.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{r}" ry="28" fill="{fill}" stroke="{col}" stroke-width="1.8"/>')
    s.append(f'<text x="{cx}" y="{cy+5}" text-anchor="middle" font-size="12.5" fill="{INK}" font-weight="bold">{t}</text>')
node(200,90,"비",ACC,BAND); node(520,90,"스프링클러",ACC,BAND,r=58)
node(360,220,"잔디 젖음",BLU,"#E9EEF5",r=56)
s.append(line(210,116,330,196,GRAY,1.6,arrow=True))
s.append(line(505,116,395,196,GRAY,1.6,arrow=True))
s.append(line(252,92,462,92,GRAY,1.4,arrow=True)); s.append(f'<text x="357" y="84" text-anchor="middle" font-size="10.5" fill="{GRAY}">비 오면 잘 안 켬</text>')
# CPT 작은 표
s.append(f'<rect x="540" y="200" width="180" height="86" rx="6" fill="{WHT}" stroke="{GRAY}" stroke-width="1.1"/>')
s.append(f'<text x="630" y="220" text-anchor="middle" font-size="10.5" fill="{INK}" font-weight="bold">조건부확률표(일부)</text>')
s.append(f'<text x="550" y="240" font-size="10.5" fill="{GRAY}">비O·스프O → 젖음 0.99</text>')
s.append(f'<text x="550" y="258" font-size="10.5" fill="{GRAY}">비X·스프O → 젖음 0.90</text>')
s.append(f'<text x="550" y="276" font-size="10.5" fill="{GRAY}">비X·스프X → 젖음 0.01</text>')
s.append(f'<text x="200" y="300" text-anchor="middle" font-size="11" fill="{BLU}">잔디가 젖었다(증거) →</text>')
s.append(f'<text x="200" y="316" text-anchor="middle" font-size="11" fill="{BLU}">비? 스프링클러? 거꾸로 추론</text>')
save("bayes-net.svg",s)

# ── 4. 죄수의 딜레마 (30-04) ──
W,H=760,330
s=head(W,H,"각자 똑똑하게 자기 이익을 좇은 끝에, 둘 다 더 나빠진다")
# 2x2 격자
gx,gy,cw,ch=240,90,180,90
labels=[["(0, 0)","(-2, +1)"],["(+1, -2)","(-1, -1)"]]
rowh=["내가 부인(B)","내가 자백(A)"]; colh=["상대 부인(B)","상대 자백(A)"]
for c in range(2):
    s.append(f'<text x="{gx+cw/2+c*cw:.0f}" y="{gy-10}" text-anchor="middle" font-size="12" fill="{INK}" font-weight="bold">{colh[c]}</text>')
for r in range(2):
    s.append(f'<text x="{gx-10}" y="{gy+ch/2+r*ch+5:.0f}" text-anchor="end" font-size="12" fill="{INK}" font-weight="bold">{rowh[r]}</text>')
for r in range(2):
    for c in range(2):
        x=gx+c*cw; y=gy+r*ch
        nash=(r==1 and c==1); pareto=(r==0 and c==0)
        fill="#F3DADE" if nash else ("#EAF1EA" if pareto else WHT)
        st=RED if nash else (GRN if pareto else GRAY)
        s.append(f'<rect x="{x}" y="{y}" width="{cw}" height="{ch}" fill="{fill}" stroke="{st}" stroke-width="{2 if (nash or pareto) else 1.2}"/>')
        s.append(f'<text x="{x+cw/2:.0f}" y="{y+ch/2:.0f}" text-anchor="middle" font-size="18" fill="{INK}" font-weight="bold">{labels[r][c]}</text>')
        if nash: s.append(f'<text x="{x+cw/2:.0f}" y="{y+ch-12:.0f}" text-anchor="middle" font-size="11" fill="{RED}" font-weight="bold">내시 균형(안정·둘 다 자백)</text>')
        if pareto: s.append(f'<text x="{x+cw/2:.0f}" y="{y+ch-12:.0f}" text-anchor="middle" font-size="11" fill="{GRN}" font-weight="bold">파레토 최적(둘 다 부인)</text>')
s.append(f'<text x="{gx+cw/2:.0f}" y="{gy-30}" text-anchor="middle" font-size="10.5" fill="{GRAY}">칸 = (나의 보수, 상대의 보수)</text>')
s.append(f'<text x="{W/2}" y="{H-16}" text-anchor="middle" font-size="11.5" fill="{GRAY}">안정적인 곳(내시)은 모두에게 최선이 아니고, 모두에게 최선인 곳(파레토)은 안정적이지 않다</text>')
save("prisoners-dilemma.svg",s)

# ── 5. 언어의 층위 (23-06) ──
W,H=760,330
s=head(W,H,"소리에서 뜻과 쓰임까지 — 위로 갈수록 기계에게 더 어렵다")
layers=[("음운 — 소리","p, a, n…",GRAY,False),
        ("형태소 — 단어 조각","먹-, -었-, -다",BLU,False),
        ("구문 — 문장 구조","주어+목적어+서술어",BLU,False),
        ("의미 — 뜻","무엇을 가리키나",GRN,True),
        ("화용·담화 — 쓰임","맥락이 정하는 속뜻",ACC,True)]
bw=380; bh=44; x0=(W-bw)/2; y0=70; gap=8
for i,(t,ex,col,hi) in enumerate(layers):
    y=y0+(len(layers)-1-i)*(bh+gap)  # 아래에서 위로 쌓기
    s.append(box(x0,y,bw,bh,"",fill=("#FBEFDD" if hi else WHT),st=col,sw=2 if hi else 1.5))
    s.append(f'<text x="{x0+14}" y="{y+27}" font-size="13" fill="{INK}" font-weight="bold">{t}</text>')
    s.append(f'<text x="{x0+bw-14}" y="{y+27}" text-anchor="end" font-size="11" fill="{GRAY}">{ex}</text>')
# 난이도 화살표
s.append(line(x0-26,y0+5*(bh+gap)-gap,x0-26,y0+4,RED,2,arrow=True,mk="ar"))
s.append(f'<text x="{x0-34}" y="{y0+2.4*(bh+gap)}" text-anchor="middle" font-size="11" fill="{RED}" font-weight="bold" transform="rotate(-90 {x0-34} {y0+2.4*(bh+gap):.0f})">어려움</text>')
s.append(f'<text x="{W/2}" y="{H-14}" text-anchor="middle" font-size="11.5" fill="{GRAY}">23장 앞 절은 \'뼈대\'(형태·구문)까지, 이 절은 그 위 \'뜻과 쓰임\'(의미·화용)을 다룬다</text>')
save("nlp-layers.svg",s)

# ── 6. 홉필드 에너지 풍경 (19-06) ──
W,H=760,320; OX,RX,TOP,BOT=70,710,90,250
s=head(W,H,"기억은 골짜기로 저장되고, 흐릿한 입력은 가장 가까운 기억으로 굴러내린다")
def en(x):
    return 0.55-0.30*math.exp(-((x-0.22)/0.08)**2)-0.42*math.exp(-((x-0.55)/0.07)**2)-0.33*math.exp(-((x-0.83)/0.07)**2)
xs=[i/200 for i in range(201)]; ys=[en(x) for x in xs]
lo,hi=min(ys),max(ys)
def px(x): return OX+x*(RX-OX)
def py(v): return TOP+(v-lo)/(hi-lo)*(BOT-TOP)
s.append(f'<polyline points="{" ".join(f"{px(x):.0f},{py(en(x)):.0f}" for x in xs)}" fill="none" stroke="{ACC}" stroke-width="2.6"/>')
# 저장된 기억(골짜기 바닥)
for x,lab in [(0.22,"기억 A"),(0.55,"기억 B"),(0.83,"기억 C")]:
    s.append(f'<circle cx="{px(x):.0f}" cy="{py(en(x)):.0f}" r="6" fill="{GRN}"/>')
    s.append(f'<text x="{px(x):.0f}" y="{py(en(x))+22:.0f}" text-anchor="middle" font-size="11" fill="{GRN}" font-weight="bold">{lab}</text>')
# 흐릿한 입력 공이 굴러내림
s.append(f'<circle cx="{px(0.42):.0f}" cy="{py(en(0.42))-2:.0f}" r="7" fill="{BLU}"/>')
s.append(f'<text x="{px(0.42):.0f}" y="{py(en(0.42))-14:.0f}" text-anchor="middle" font-size="11" fill="{BLU}">흐릿한 입력</text>')
s.append(line(px(0.46),py(en(0.46))-2,px(0.52),py(en(0.52))-2,BLU,1.6,arrow=True,mk="arb"))
s.append(f'<text x="{W/2}" y="{H-14}" text-anchor="middle" font-size="11.5" fill="{GRAY}">에너지가 낮아지는 쪽으로 흘러, 일부만 주어도 가장 닮은 기억 전체를 되살린다(연상기억)</text>')
save("hopfield-energy.svg",s)
print("batch5 done")
