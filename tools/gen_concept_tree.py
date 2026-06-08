#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""서문용 개념 트리(세로 척추형). 계층:
인공지능 → 휴리스틱 → 머신러닝 → 신경망 → 자연어처리 → 어텐션 → LLM (강조 척추),
각 단계에서 곁가지가 오른쪽으로 뻗는다. 겹침 없도록 좌표 직접 배치."""
import os
A = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "pages", "assets")
INK="#2A2A2A"; ACC="#B5651D"; PAPER="#FBF7EF"; BORD="#E7DFCB"; GRAY="#7A7268"; BAND="#F3E7D6"
FONT="'Helvetica Neue', Arial, 'AppleSDGothicNeo', sans-serif"
W,H=760,730
SX=150   # 척추 x 중심

# 척추(위→아래)
spine=[("인공지능",60),("휴리스틱",150),("머신러닝",240),("신경망 (NN)",330),
       ("자연어처리 (NLP)",420),("어텐션 (Attention)",510),("LLM",600)]
# 곁가지: (라벨, x, y, 부모척추index)
branch=[("탐색",350,52,0),("BFS",520,30,None),("DFS",520,74,None),("지식·추론",350,100,0),
        ("그리디",355,150,1),("A*",470,150,1),
        ("결정트리",360,240,2),
        ("CNN",355,330,3)]
# 곁가지 간선 (부모좌표, 자식좌표) — 부모가 척추면 (SX,spine_y), 아니면 좌표
bedges=[("ai0","탐색"),("탐색","BFS"),("탐색","DFS"),("ai0","지식·추론"),
        ("h1","그리디"),("h1","A*"),("m2","결정트리"),("n3","CNN")]

def w_of(label): return max(56, len(label)*15+24)

# 좌표 조회
pos={}
for i,(lab,y) in enumerate(spine): pos["spine%d"%i]=(SX,y)
bpos={lab:(x,y) for (lab,x,y,_) in branch}
ref={"ai0":pos["spine0"],"h1":pos["spine1"],"m2":pos["spine2"],"n3":pos["spine3"]}
ref.update({lab:(x,y) for lab,x,y in [(b[0],b[1],b[2]) for b in branch]})

s=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="{FONT}">']
s.append(f'<rect x="2" y="2" width="{W-4}" height="{H-4}" rx="16" fill="{PAPER}" stroke="{BORD}"/>')

# 척추 간선(굵은 강조)
for i in range(len(spine)-1):
    _,y1=pos["spine%d"%i]; _,y2=pos["spine%d"%(i+1)]
    s.append(f'<line x1="{SX}" y1="{y1+16}" x2="{SX}" y2="{y2-16}" stroke="{ACC}" stroke-width="3.6"/>')
# 곁가지 간선(가는 회색)
for a,b in bedges:
    ax,ay=ref[a]; bx,by=ref[b]
    s.append(f'<line x1="{ax}" y1="{ay}" x2="{bx-w_of(b)/2}" y2="{by}" stroke="#C9BFA8" stroke-width="1.6"/>')

def node(label,x,y,kind):
    w=w_of(label); h=32
    if kind=="llm": fill,tc,st,sw=ACC,"#fff",INK,2
    elif kind=="spine": fill,tc,st,sw=BAND,INK,ACC,2
    else: fill,tc,st,sw="#FFFFFF",GRAY,"#C9BFA8",1.4
    fw=' font-weight="bold"' if kind in("spine","llm") else ''
    return (f'<rect x="{x-w/2}" y="{y-h/2}" width="{w}" height="{h}" rx="8" fill="{fill}" stroke="{st}" stroke-width="{sw}"/>'
            f'<text x="{x}" y="{y+5}" text-anchor="middle" font-size="13" fill="{tc}"{fw}>{label}</text>')

# 곁가지 노드
for lab,x,y,_ in branch: s.append(node(lab,x,y,"leaf"))
# 척추 노드
for i,(lab,y) in enumerate(spine):
    s.append(node(lab,SX,y,"llm" if lab=="LLM" else "spine"))
# LLM 하위 모델들 (잎새 끝의 실제 제품들)
models=[("ChatGPT",165,688),("Claude",300,688),("Gemini",420,688),("Grok",525,688)]
lx,ly=pos["spine6"]
for lab,x,y in models:
    s.append(f'<line x1="{lx}" y1="{ly+16}" x2="{x}" y2="{y-16}" stroke="#C9BFA8" stroke-width="1.6"/>')
for lab,x,y in models:
    s.append(node(lab,x,y,"leaf"))
s.append('</svg>')
open(os.path.join(A,"concept-tree.svg"),"w",encoding="utf-8").write("\n".join(s))
print("concept-tree.svg (세로 척추형, 계층 수정)")
