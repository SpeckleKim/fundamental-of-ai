#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""서문용 개념 트리: 책 전반 개념을 나무로, LLM까지의 깊은 경로를 강조.
메시지 = LLM은 큰 나무의 한 잎새. 뿌리(기초)를 알아야 이해된다."""
import os
A = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "pages", "assets")
INK="#2A2A2A"; ACC="#B5651D"; BLU="#3B6EA5"; PAPER="#FBF7EF"; BORD="#E7DFCB"; GRAY="#7A7268"; BAND="#F3E7D6"
FONT="'Helvetica Neue', Arial, 'AppleSDGothicNeo', sans-serif"
W,H=1000,660

# id: (label, x, y, kind)  kind: root/branch/leaf/path/llm
N = {
 "ai":("인공지능",500,46,"path"),
 "search":("탐색",165,150,"branch"),
 "know":("지식·추론",380,150,"branch"),
 "learn":("학습",660,150,"path"),
 "etc":("언어·지각·로봇 …",880,150,"leaf"),
 "bfs":("BFS",70,248,"leaf"), "dfs":("DFS",150,248,"leaf"), "heur":("휴리스틱",260,248,"branch"),
 "greedy":("그리디",215,338,"leaf"), "astar":("A*",315,338,"leaf"),
 "logic":("논리·규칙",355,248,"leaf"), "reason":("추론",460,248,"leaf"),
 "dtree":("결정트리",575,248,"leaf"), "nn":("신경망(NN)",720,248,"path"),
 "cnn":("CNN",650,340,"leaf"), "nlp":("자연어처리(NLP)",815,340,"path"),
 "attn":("어텐션(Attention)",840,438,"path"),
 "llm":("LLM",880,540,"llm"),
}
E = [("ai","search"),("ai","know"),("ai","learn"),("ai","etc"),
     ("search","bfs"),("search","dfs"),("search","heur"),("heur","greedy"),("heur","astar"),
     ("know","logic"),("know","reason"),
     ("learn","dtree"),("learn","nn"),("nn","cnn"),("nn","nlp"),("nlp","attn"),("attn","llm")]
PATH=[("ai","learn"),("learn","nn"),("nn","nlp"),("nlp","attn"),("attn","llm")]
pathset=set(PATH)

def box(id):
    label,x,y,kind=N[id]
    w=max(56,len(label)*15+22); h=32
    return x-w/2,y-h/2,w,h

s=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="{FONT}">']
s.append(f'<rect x="2" y="2" width="{W-4}" height="{H-4}" rx="16" fill="{PAPER}" stroke="{BORD}"/>')
s.append(f'<text x="{W/2}" y="34" text-anchor="middle" font-size="15" fill="{INK}" font-weight="bold">인공지능이라는 한 그루 나무</text>')
# 간선
for a,b in E:
    _,ax,ay,_=N[a]; _,bx,by,_=N[b]
    if (a,b) in pathset:
        s.append(f'<line x1="{ax}" y1="{ay+16}" x2="{bx}" y2="{by-16}" stroke="{ACC}" stroke-width="3.4"/>')
    else:
        s.append(f'<line x1="{ax}" y1="{ay+16}" x2="{bx}" y2="{by-16}" stroke="#C9BFA8" stroke-width="1.6"/>')
# 노드
for id in N:
    label,x,y,kind=N[id]; bx,by,w,h=box(id)
    if kind=="llm":
        fill=ACC; tcol="#fff"; stroke=INK; sw=2
    elif kind=="path":
        fill=BAND; tcol=INK; stroke=ACC; sw=2
    elif kind=="branch":
        fill="#FFFFFF"; tcol=INK; stroke=INK; sw=1.6
    else:
        fill="#FFFFFF"; tcol=GRAY; stroke="#C9BFA8"; sw=1.4
    s.append(f'<rect x="{bx}" y="{by}" width="{w}" height="{h}" rx="8" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')
    fw=' font-weight="bold"' if kind in("llm","path","root") else ''
    s.append(f'<text x="{x}" y="{y+5}" text-anchor="middle" font-size="13" fill="{tcol}"{fw}>{label}</text>')
# LLM 강조 주석
lx=N["llm"][1]
s.append(f'<text x="{lx+40}" y="{N["llm"][2]+5}" font-size="12" fill="{ACC}">← 우리가 흔히 보는 표면</text>')
# 하단 메시지
s.append(f'<text x="{W/2}" y="{H-26}" text-anchor="middle" font-size="13.5" fill="{INK}">LLM은 이 나무의 한 잎새다. 뿌리와 줄기(탐색·논리·학습·신경망)를 알아야 비로소 그 잎이 보인다.</text>')
s.append('</svg>')
open(os.path.join(A,"concept-tree.svg"),"w",encoding="utf-8").write("\n".join(s))
print("concept-tree.svg")
