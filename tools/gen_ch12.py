#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""12장 도식 생성: A* 격자맵, 배낭(그리디). STYLE.md 팔레트 준수."""
import os
A = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "pages", "assets")
INK="#2A2A2A"; ACC="#B5651D"; BLU="#3B6EA5"; PAPER="#FBF7EF"; BORD="#E7DFCB"; GRAY="#7A7268"; BAND="#F3E7D6"
FONT="'Helvetica Neue', Arial, 'AppleSDGothicNeo', sans-serif"

def astar_grid():
    cols, rows, c, ox, oy = 9, 6, 56, 64, 72
    W, H = ox*2 + cols*c, oy + rows*c + 90
    obst = {(4,0),(4,1),(4,2),(4,3)}            # 가운데 벽(아래쪽에 틈)
    start=(1,5); goal=(7,0)
    path=[(1,5),(2,5),(3,5),(4,5),(5,4),(5,3),(6,2),(6,1),(7,1),(7,0)]
    pset=set(path)
    s=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="{FONT}">']
    s.append(f'<rect x="2" y="2" width="{W-4}" height="{H-4}" rx="14" fill="{PAPER}" stroke="{BORD}"/>')
    s.append(f'<text x="{W/2}" y="40" text-anchor="middle" font-size="14" fill="{GRAY}" font-style="italic">맵을 격자로 나누고, 칸마다 f=g+h로 최단 경로를 찾는다</text>')
    for r in range(rows):
        for col in range(cols):
            x, y = ox+col*c, oy+r*c
            if (col,r) in obst: fill=INK
            elif (col,r) in pset: fill=BAND
            else: fill="#FFFFFF"
            s.append(f'<rect x="{x}" y="{y}" width="{c}" height="{c}" fill="{fill}" stroke="#D8CEB6" stroke-width="1"/>')
    # 경로 선
    pts=" ".join(f"{ox+col*c+c/2},{oy+r*c+c/2}" for col,r in path)
    s.append(f'<polyline points="{pts}" fill="none" stroke="{ACC}" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>')
    # S, G
    sx,sy=ox+start[0]*c+c/2, oy+start[1]*c+c/2
    gx,gy=ox+goal[0]*c+c/2, oy+goal[1]*c+c/2
    s.append(f'<circle cx="{sx}" cy="{sy}" r="20" fill="{ACC}" stroke="{INK}" stroke-width="1.6"/><text x="{sx}" y="{sy+5}" text-anchor="middle" font-size="15" fill="#fff">S</text>')
    s.append(f'<circle cx="{gx}" cy="{gy}" r="20" fill="{BLU}" stroke="{INK}" stroke-width="1.6"/><text x="{gx}" y="{gy+5}" text-anchor="middle" font-size="15" fill="#fff">G</text>')
    # 범례
    ly=oy+rows*c+34
    s.append(f'<text x="{ox}" y="{ly}" font-size="13" fill="{INK}">■ 벽(못 지나감)   ■ 찾은 경로   <tspan fill="{ACC}">S</tspan> 출발   <tspan fill="{BLU}">G</tspan> 목표</text>')
    s.append(f'<text x="{ox}" y="{ly+24}" font-size="13" fill="{GRAY}">g = S에서 여기까지 온 거리 · h = 여기서 G까지 직선 어림 · f = g + h (작을수록 먼저 살핀다)</text>')
    s.append('</svg>')
    open(os.path.join(A,"astar-grid.svg"),"w",encoding="utf-8").write("\n".join(s))
    print("astar-grid.svg")

def knapsack():
    W,H=720,340
    s=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="{FONT}">']
    s.append(f'<rect x="2" y="2" width="{W-4}" height="{H-4}" rx="14" fill="{PAPER}" stroke="{BORD}"/>')
    s.append(f'<text x="{W/2}" y="40" text-anchor="middle" font-size="14" fill="{GRAY}" font-style="italic">한정된 배낭에, 단위 무게당 가치가 큰 것부터 담는다 — 그것이 그리디</text>')
    # 배낭
    s.append(f'<path d="M120,150 q-14,0 -14,16 l0,120 q0,16 16,16 l96,0 q16,0 16,-16 l0,-120 q0,-16 -14,-16 z" fill="#F3E7D6" stroke="{INK}" stroke-width="1.6"/>')
    s.append(f'<path d="M140,150 q22,-34 56,0" fill="none" stroke="{INK}" stroke-width="1.6"/>')
    s.append(f'<text x="172" y="300" text-anchor="middle" font-size="13" fill="{INK}">배낭(용량 한정)</text>')
    # 물건들
    items=[("A","가치 60 / 무게 10","→ 6","#B5651D"),("B","가치 100 / 무게 20","→ 5","#3B6EA5"),("C","가치 120 / 무게 30","→ 4","#7A7268")]
    bx=300
    for i,(name,vw,ratio,col) in enumerate(items):
        y=90+i*72
        s.append(f'<rect x="{bx}" y="{y}" width="300" height="54" rx="8" fill="#FFFFFF" stroke="{INK}" stroke-width="1.4"/>')
        s.append(f'<circle cx="{bx+28}" cy="{y+27}" r="16" fill="{col}"/><text x="{bx+28}" y="{y+32}" text-anchor="middle" font-size="14" fill="#fff">{name}</text>')
        s.append(f'<text x="{bx+56}" y="{y+24}" font-size="13" fill="{INK}">{vw}</text>')
        s.append(f'<text x="{bx+56}" y="{y+44}" font-size="12" fill="{GRAY}">무게당 가치 {ratio}</text>')
    s.append(f'<text x="{bx+150}" y="316" text-anchor="middle" font-size="12" fill="{GRAY}">쪼갤 수 있으면(분수 배낭) 그리디가 늘 최적 · 못 쪼개면(0-1 배낭) 빗나갈 수 있다</text>')
    s.append('</svg>')
    open(os.path.join(A,"knapsack.svg"),"w",encoding="utf-8").write("\n".join(s))
    print("knapsack.svg")

astar_grid(); knapsack()
