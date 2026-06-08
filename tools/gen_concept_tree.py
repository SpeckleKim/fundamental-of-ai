#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""서문용 개념 트리 — 고전적 위→아래 확장 트리(루트 위, 아래로 가지가 퍼짐).
계층: 인공지능 → (탐색/지식추론/휴리스틱) ; 휴리스틱 → 머신러닝 → 신경망 → NLP → 어텐션 → LLM → 제품들.
리프 패킹 레이아웃으로 겹침 없이 배치."""
import os
A = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "pages", "assets")
INK="#2A2A2A"; ACC="#B5651D"; PAPER="#FBF7EF"; BORD="#E7DFCB"; GRAY="#7A7268"; BAND="#F3E7D6"
FONT="'Helvetica Neue', Arial, 'AppleSDGothicNeo', sans-serif"

# (label, kind, [children]) — kind: path(척추)/llm/model/node/leaf
T=("인공지능","path",[
   ("탐색","node",[("BFS","leaf",[]),("DFS","leaf",[]),("DP","leaf",[])]),
   ("지식·추론","node",[("논리","leaf",[]),("추론","leaf",[])]),
   ("휴리스틱","path",[
      ("그리디","leaf",[]),("A*","leaf",[]),
      ("머신러닝","path",[
         ("회귀·분류","leaf",[]),("결정트리","leaf",[]),("SVM","leaf",[]),
         ("군집화","leaf",[]),("강화학습","leaf",[]),
         ("신경망(NN)","path",[
            ("CNN","leaf",[]),("RNN","leaf",[]),("GAN","leaf",[]),
            ("NLP","path",[
               ("어텐션","path",[
                  ("LLM","llm",[
                     ("ChatGPT","model",[]),("Claude","model",[]),
                     ("Gemini","model",[]),("Grok","model",[])])])])])])])])

LEAFW=92; LEVELH=98; OX=58; OY=52; BH=30
nodes=[]   # (label,kind,x,y)
edges=[]   # (px,py,cx,cy)
slot=[0]
def layout(node, depth):
    label,kind,ch=node
    y=OY+depth*LEVELH
    if not ch:
        x=OX+slot[0]*LEAFW; slot[0]+=1
    else:
        xs=[layout(c,depth+1) for c in ch]
        x=(xs[0]+xs[-1])/2
        for c,cx in zip(ch,xs):
            edges.append((x,y, cx, OY+(depth+1)*LEVELH))
    nodes.append((label,kind,x,y))
    return x
layout(T,0)

maxx=max(x for _,_,x,_ in nodes); maxy=max(y for _,_,_,y in nodes)
W=int(maxx+OX); H=int(maxy+OY)

def wof(label):
    # 한글~14px, 라틴~8.5px 근사
    wsum=sum(8.6 if c.isascii() else 14 for c in label)
    return max(48, wsum+18)

s=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="{FONT}">']
s.append(f'<rect x="2" y="2" width="{W-4}" height="{H-4}" rx="14" fill="{PAPER}" stroke="{BORD}"/>')
# 간선(부모 아래 → 자식 위) : ㄱ자 엘보
for px,py,cx,cy in edges:
    midy=(py+BH/2+cy-BH/2)/2
    s.append(f'<path d="M{px},{py+BH/2} L{px},{midy} L{cx},{midy} L{cx},{cy-BH/2}" fill="none" stroke="#C9BFA8" stroke-width="1.5"/>')
# 노드
for label,kind,x,y in nodes:
    w=wof(label)
    if kind=="llm": fill,tc,st,sw=ACC,"#fff",INK,2
    elif kind=="path": fill,tc,st,sw=BAND,INK,ACC,2
    elif kind=="model": fill,tc,st,sw="#E9EEF5",INK,"#3B6EA5",1.5
    elif kind=="node": fill,tc,st,sw="#FFFFFF",INK,INK,1.6
    else: fill,tc,st,sw="#FFFFFF",GRAY,"#C9BFA8",1.4
    fw=' font-weight="bold"' if kind in("path","llm") else ''
    s.append(f'<rect x="{x-w/2:.1f}" y="{y-BH/2}" width="{w:.1f}" height="{BH}" rx="7" fill="{fill}" stroke="{st}" stroke-width="{sw}"/>')
    s.append(f'<text x="{x:.1f}" y="{y+5}" text-anchor="middle" font-size="13" fill="{tc}"{fw}>{label}</text>')
s.append('</svg>')
open(os.path.join(A,"concept-tree.svg"),"w",encoding="utf-8").write("\n".join(s))
print(f"concept-tree.svg  (top-down, {W}x{H}, leaves={slot[0]})")
