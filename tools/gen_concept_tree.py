#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""서문 개념 트리 — 위→아래, '왼쪽 척추 + 오른쪽 가지' 공간 절약형.
척추 자식을 항상 맨 왼쪽에 두어 척추(휴리스틱→머신러닝→신경망→NLP→어텐션→LLM)는
왼쪽 세로로 곧게 내려가고, 곁가지·잎은 오른쪽으로 편다(깊이가 달라 가로 공간을 공유 → 폭 절약).
사전순(pre-order)·깊이별 x커서로 배치 → 노드 겹침 없음."""
import os
A = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "pages", "assets")
INK="#2A2A2A"; ACC="#B5651D"; PAPER="#FBF7EF"; BORD="#E7DFCB"; GRAY="#7A7268"; BAND="#F3E7D6"
FONT="'Helvetica Neue', Arial, 'AppleSDGothicNeo', sans-serif"
OX=70; OY=48; COLW=104; ROW=92; BH=30

T=("인공지능","path",[
   ("휴리스틱","path",[
       ("머신러닝","path",[
           ("신경망(NN)","path",[
               ("NLP","path",[
                   ("어텐션","path",[
                       ("LLM","llm",[("ChatGPT","model",[]),("Claude","model",[]),("Gemini","model",[]),("Grok","model",[])])])]),
               ("CNN","leaf",[]),("RNN","leaf",[]),("GAN","leaf",[])]),
           ("회귀·분류","leaf",[]),("결정트리","leaf",[]),("SVM","leaf",[]),("군집화","leaf",[]),("강화학습","leaf",[])]),
       ("Greedy","leaf",[]),("A*","leaf",[])]),
   ("탐색","node",[("BFS","leaf",[]),("DFS","leaf",[]),("DP","leaf",[])]),
   ("지식·추론","node",[("논리","leaf",[]),("추론","leaf",[])])])

cur={}; nodes=[]; edges=[]
def place(node,depth,parent):
    label,kind,ch=node
    c=cur.get(depth,0); cur[depth]=c+1
    x=OX+c*COLW; y=OY+depth*ROW
    nodes.append((label,kind,x,y))
    if parent is not None: edges.append((parent,(x,y),kind))
    for c2 in ch: place(c2,depth+1,(x,y))
place(T,0,None)

maxx=max(x for _,_,x,_ in nodes); maxy=max(y for _,_,_,y in nodes)
W=int(maxx+OX); H=int(maxy+OY)
def wof(label):
    return max(48, sum(8.6 if ch.isascii() else 14 for ch in label)+18)

s=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="{FONT}">']
s.append(f'<rect x="2" y="2" width="{W-4}" height="{H-4}" rx="14" fill="{PAPER}" stroke="{BORD}"/>')
# 간선(직선): 부모 아래 → 자식 위
for (px,py),(cx,cy),kind in edges:
    col = ACC if kind in("path","llm") else "#C9BFA8"
    sw = 3 if kind in("path","llm") else 1.5
    s.append(f'<line x1="{px:.0f}" y1="{py+BH/2:.0f}" x2="{cx:.0f}" y2="{cy-BH/2:.0f}" stroke="{col}" stroke-width="{sw}"/>')
# 노드
for label,kind,x,y in nodes:
    w=wof(label)
    if kind=="llm": fill,tc,st,sw=ACC,"#fff",INK,2
    elif kind=="path": fill,tc,st,sw=BAND,INK,ACC,2
    elif kind=="model": fill,tc,st,sw="#E9EEF5",INK,"#3B6EA5",1.5
    elif kind=="node": fill,tc,st,sw="#FFFFFF",INK,INK,1.6
    else: fill,tc,st,sw="#FFFFFF",GRAY,"#C9BFA8",1.4
    fw=' font-weight="bold"' if kind in("path","llm") else ''
    s.append(f'<rect x="{x-w/2:.1f}" y="{y-BH/2:.0f}" width="{w:.1f}" height="{BH}" rx="7" fill="{fill}" stroke="{st}" stroke-width="{sw}"/>')
    s.append(f'<text x="{x:.0f}" y="{y+5:.0f}" text-anchor="middle" font-size="13" fill="{tc}"{fw}>{label}</text>')
s.append('</svg>')
open(os.path.join(A,"concept-tree.svg"),"w",encoding="utf-8").write("\n".join(s))
print(f"concept-tree.svg (left-spine, {W}x{H})")
