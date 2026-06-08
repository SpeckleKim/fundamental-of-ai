#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""서문 개념 트리 — 위→아래, '왼쪽 척추 + 오른쪽 가지' 공간 절약형.
척추(휴리스틱→머신러닝→신경망→NLP→어텐션→LLM)는 왼쪽 세로로 곧게,
곁가지·잎은 오른쪽으로. 단, 일반 분기 노드(탐색·지식추론)는 자식 가운데로 정렬."""
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

cur={}; N=[]
def place(node,depth,parent):
    label,kind,ch=node
    c=cur.get(depth,0); cur[depth]=c+1
    idx=len(N)
    N.append({"l":label,"k":kind,"x":OX+c*COLW,"y":OY+depth*ROW,"kids":[]})
    if parent is not None: N[parent]["kids"].append(idx)
    for c2 in ch: place(c2,depth+1,idx)
    return idx
place(T,0,None)
# 일반 분기 노드는 자식 가운데로 정렬(탐색·지식추론)
for n in N:
    if n["k"]=="node" and n["kids"]:
        xs=[N[k]["x"] for k in n["kids"]]
        n["x"]=(min(xs)+max(xs))/2

maxx=max(n["x"] for n in N); maxy=max(n["y"] for n in N)
W=int(maxx+OX); H=int(maxy+OY)
def wof(l): return max(48, sum(8.6 if c.isascii() else 14 for c in l)+18)

s=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="{FONT}">']
s.append(f'<rect x="2" y="2" width="{W-4}" height="{H-4}" rx="14" fill="{PAPER}" stroke="{BORD}"/>')
for n in N:
    for k in n["kids"]:
        ck=N[k]; col=ACC if ck["k"] in("path","llm") else "#C9BFA8"; sw=3 if ck["k"] in("path","llm") else 1.5
        s.append(f'<line x1="{n["x"]:.0f}" y1="{n["y"]+BH/2:.0f}" x2="{ck["x"]:.0f}" y2="{ck["y"]-BH/2:.0f}" stroke="{col}" stroke-width="{sw}"/>')
for n in N:
    l,k,x,y=n["l"],n["k"],n["x"],n["y"]; w=wof(l)
    if k=="llm": fill,tc,st,sw=ACC,"#fff",INK,2
    elif k=="path": fill,tc,st,sw=BAND,INK,ACC,2
    elif k=="model": fill,tc,st,sw="#E9EEF5",INK,"#3B6EA5",1.5
    elif k=="node": fill,tc,st,sw="#FFFFFF",INK,INK,1.6
    else: fill,tc,st,sw="#FFFFFF",GRAY,"#C9BFA8",1.4
    fw=' font-weight="bold"' if k in("path","llm") else ''
    s.append(f'<rect x="{x-w/2:.1f}" y="{y-BH/2:.0f}" width="{w:.1f}" height="{BH}" rx="7" fill="{fill}" stroke="{st}" stroke-width="{sw}"/>')
    s.append(f'<text x="{x:.0f}" y="{y+5:.0f}" text-anchor="middle" font-size="13" fill="{tc}"{fw}>{l}</text>')
s.append('</svg>')
open(os.path.join(A,"concept-tree.svg"),"w",encoding="utf-8").write("\n".join(s))
print(f"concept-tree.svg ({W}x{H})")
