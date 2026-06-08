#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""6장 도식: 추론 규칙(타당 vs 오류), 단일화·분해."""
import os
A=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"pages","assets")
INK="#2A2A2A";ACC="#B5651D";BLU="#3B6EA5";GRN="#4E7A51";RED="#B5495B";PAPER="#FBF7EF";BORD="#E7DFCB";GRAY="#7A7268";BAND="#F3E7D6"
F="'Helvetica Neue', Arial, 'AppleSDGothicNeo', sans-serif"

# 추론 규칙
W,H=760,330
rows=[("모더스 포넨스","P → Q,  그리고 P  ⟹  Q","비 오면 젖는다 · 비 온다  ⟹  젖었다","✓",GRN),
      ("모더스 톨렌스","P → Q,  그리고 ¬Q  ⟹  ¬P","비 오면 젖는다 · 안 젖었다  ⟹  비 안 왔다","✓",GRN),
      ("후건 긍정의 오류","P → Q,  그리고 Q  ⟹  P (?)","젖었다고 비가 왔다는 보장은 없다 — 스프링클러일 수도","✗",RED)]
s=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="{F}">',
   f'<rect x="2" y="2" width="{W-4}" height="{H-4}" rx="14" fill="{PAPER}" stroke="{BORD}"/>',
   f'<text x="{W/2}" y="36" text-anchor="middle" font-size="14" fill="{GRAY}" font-style="italic">전제가 참이면 결론도 반드시 참인가? — 타당한 규칙과 닮은꼴 오류</text>']
for i,(name,formal,ex,mark,col) in enumerate(rows):
    y=64+i*84
    s.append(f'<rect x="40" y="{y}" width="680" height="70" rx="9" fill="#FFFFFF" stroke="{BORD}" stroke-width="1.2"/>')
    s.append(f'<rect x="40" y="{y}" width="8" height="70" rx="3" fill="{col}"/>')
    s.append(f'<text x="68" y="{y+28}" font-size="14" fill="{INK}" font-weight="bold">{name}</text>')
    s.append(f'<text x="68" y="{y+50}" font-size="13" fill="{INK}">{formal}</text>')
    s.append(f'<text x="320" y="{y+28}" font-size="12" fill="{GRAY}">{ex}</text>')
    s.append(f'<text x="694" y="{y+44}" text-anchor="middle" font-size="26" fill="{col}">{mark}</text>')
s.append('</svg>')
open(os.path.join(A,"inference-rules.svg"),"w",encoding="utf-8").write("\n".join(s))

# 단일화·분해
W2,H2=760,330
t=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W2} {H2}" font-family="{F}">',
   f'<rect x="2" y="2" width="{W2-4}" height="{H2-4}" rx="14" fill="{PAPER}" stroke="{BORD}"/>',
   f'<text x="{W2/2}" y="36" text-anchor="middle" font-size="14" fill="{GRAY}" font-style="italic">변수의 짝을 맞춰(단일화) 새 결론을 길어 올린다 — 기계가 스스로 추론하는 엔진</text>']
def box(x,y,w,h,txt,fill="#FFFFFF",st=INK,fs=13,tc=INK):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{fill}" stroke="{st}" stroke-width="1.5"/>'
            f'<text x="{x+w/2}" y="{y+h/2+5}" text-anchor="middle" font-size="{fs}" fill="{tc}">{txt}</text>')
t.append(box(120,70,300,44,"규칙:  죽는다(X) :- 사람(X)",BAND,ACC))
t.append(box(440,70,200,44,"사실:  사람(소크라테스)"))
t.append(f'<text x="380" y="150" text-anchor="middle" font-size="13.5" fill="{BLU}" font-weight="bold">단일화(unification): X = 소크라테스</text>')
t.append(f'<line x1="380" y1="160" x2="380" y2="196" stroke="{INK}" stroke-width="1.6"/><path d="M374,190 L380,200 L386,190 z" fill="{INK}"/>')
t.append(box(250,206,260,46,"결론:  죽는다(소크라테스)  ✓","#E9EEF5",BLU,13.5))
t.append(f'<text x="{W2/2}" y="296" text-anchor="middle" font-size="12" fill="{GRAY}">이렇게 반복해 거짓을 이끌어내 반박하는 방식이 분해(resolution) — 7부 Prolog의 심장</text>')
t.append('</svg>')
open(os.path.join(A,"unification.svg"),"w",encoding="utf-8").write("\n".join(t))
print("inference-rules.svg, unification.svg")
