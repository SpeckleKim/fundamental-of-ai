#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Declarative builder for "Fundamental of AI".

- Chapter numbers & section codes are derived from order, so inserting a
  chapter renumbers everything automatically (incl. NN-NN section codes).
- Hand-written pages listed in PROTECTED are never overwritten.
- A section may carry a slug:
    slug=None  -> listed as plain text in TOC; its content lives in the
                  chapter overview page (for now).
    slug="..." -> gets its own page pages/NN-MM-slug.md (a stub is created
                  only if missing) and is linked from the chapter overview
                  and TOC.
"""
import os

ROOT  = os.path.dirname(os.path.abspath(__file__))
PAGES = os.path.join(ROOT, "pages")

# Files we authored by hand — never regenerate/overwrite these.
PROTECTED = {
    "00-preface.md",
    "01-what-is-ai.md", "02-history.md",
    "01-01-intelligence.md", "01-02-definition.md",
    "01-03-turing-test.md", "01-04-strong-weak-ai.md",
    "02-01-dartmouth.md", "02-02-golden-age-winter.md",
    "02-03-expert-systems-winter.md", "02-04-connectionism-today.md",
    "A1-pioneers.md", "B1-glossary.md",
}

# Each chapter: (slug, title, summary, [ (sec_title, sec_summary, sec_slug|None), ... ])
# Each part:    (part_title, [chapters])
BOOK = [
 ("Part 1. 인공지능이란 무엇인가", [
   ("what-is-ai","인공지능이란 무엇인가","'지능'이라는 말부터 차근차근 풀며, 인공지능이 어떤 질문에 답하려는 학문인지 그림을 그린다.",[
     ("지능이란 무엇인가","사람의 지능을 어떻게 정의할 수 있는지, 그 정의가 왜 어려운지 살펴본다.","intelligence"),
     ("인공지능의 정의와 목표","'생각하는 기계'라는 목표를 네 갈래(사람처럼 생각/행동, 합리적으로 생각/행동)로 나눠 이해한다.","definition"),
     ("튜링 테스트","앨런 튜링이 던진 '기계가 생각할 수 있는가'라는 질문과 그 판별법을 들여다본다.","turing-test"),
     ("강한 AI와 약한 AI","'정말 마음을 갖는 기계'와 '지능처럼 행동하는 도구'의 구분을 정리한다.","strong-weak-ai"),
   ]),
   ("history","인공지능의 역사","꿈에서 현실로 — 인공지능이 어떤 부침을 거쳐 오늘에 이르렀는지 시대순으로 짚는다.",[
     ("태동: 다트머스 회의","1956년, '인공지능'이라는 이름이 처음 붙은 순간과 그 배경.","dartmouth"),
     ("황금기와 첫 번째 겨울","초기의 낙관, 그리고 과장된 기대가 식으며 찾아온 첫 침체.","golden-age-winter"),
     ("전문가 시스템과 두 번째 겨울","규칙 기반 시스템의 상업적 성공과 그 한계가 부른 두 번째 침체.","expert-systems-winter"),
     ("연결주의의 부활과 오늘","신경망의 재등장, 데이터와 연산의 시대가 열리기까지.","connectionism-today"),
   ]),
   ("philosophy","인공지능을 둘러싼 철학","기계가 정말 '이해'할 수 있는가? 기술 이전에 던져야 할 질문들을 다룬다.",[
     ("마음과 기계: 심신 문제","마음이란 무엇이며 물질인 기계가 그것을 가질 수 있는가.","mind-body"),
     ("중국어 방 논변","존 설의 사고실험으로 '계산이 곧 이해인가'를 따져 본다.","chinese-room"),
     ("기호주의와 연결주의","지능을 기호 조작으로 보는 관점과 연결망으로 보는 관점의 대립.","symbolism-connectionism"),
   ]),
   ("branches","인공지능의 분야 지도","탐색·추론·학습·언어·지각 — AI의 하위 분야를 한눈에 보고 이 책의 길을 안내한다.",[
     ("AI의 하위 분야 한눈에 보기","이 책이 다룰 분야들이 서로 어떻게 연결되는지 지도를 그린다.","map"),
     ("이 책의 길찾기","어떤 순서로 읽고, 어디서 멈춰 직접 해보면 좋은지 안내한다.","how-to-read"),
   ]),
 ]),
 ("Part 2. 기초 체력 — AI를 떠받치는 토대", [
   ("mathematics","AI를 위한 수학","겁먹지 않고 꼭 필요한 만큼만 — AI를 이해하는 데 쓰이는 수학의 언어를 다진다.",[
     ("선형대수: 벡터와 행렬","데이터와 변환을 표현하는 가장 기본적인 도구.","linear-algebra"),
     ("확률과 통계","불확실한 세계를 다루기 위한 사고의 틀.","probability"),
     ("미적분과 최적화","'더 나은 값을 찾아가는' 학습의 수학적 바탕.","calculus-optimization"),
   ]),
   ("logic","논리","참과 거짓, 그리고 그로부터 새로운 사실을 이끌어내는 추론의 규칙을 배운다.",[
     ("명제 논리","참/거짓을 다루는 가장 단순한 논리 체계.","propositional-logic"),
     ("술어 논리","대상과 관계를 표현해 더 풍부한 지식을 담는 논리.","predicate-logic"),
     ("추론 규칙","전제로부터 결론을 타당하게 이끌어내는 방법.","inference-rules"),
   ]),
   ("psychology","인지심리학","AI는 사람의 사고를 흉내 내며 출발했다. 사람은 어떻게 생각하는지를 들여다본다.",[
     ("사람은 어떻게 사고하는가","문제 해결과 의사결정의 인지 과정.","how-people-think"),
     ("기억과 학습","사람의 기억 구조와 학습 방식, 그 계산적 시사점.","memory-learning"),
     ("인지의 계산 모형","마음을 정보처리로 보는 관점.","computational-mind"),
   ]),
   ("brain","뇌와 신경","인공신경망의 원형 — 뇌가 정보를 처리하는 방식에서 영감을 얻고, 그것을 칩으로까지 옮기는 흐름을 따라간다.",[
     ("뉴런의 구조와 신호","뇌의 기본 단위인 뉴런이 신호를 주고받는 방식.","neuron"),
     ("뇌의 정보처리와 시각피질","수많은 뉴런이 만드는 처리, 그리고 휴벨-비셀이 밝힌 시각피질의 계층적 에지 검출.","visual-cortex"),
     ("생물학적 영감에서 인공신경망으로","뇌의 원리가 어떻게 인공신경망으로 옮겨졌는가.","to-neural-network"),
     ("뇌를 본뜬 하드웨어: 뉴로모픽","폰 노이만 병목을 넘어, 뉴런을 직접 본뜬 칩(스파이킹 신경망·뉴런 칩).","neuromorphic"),
   ]),
   ("computation","계산과 알고리즘","'계산한다'는 것의 의미와, 문제를 푸는 절차로서의 알고리즘을 정리한다.",[
     ("계산이란 무엇인가: 튜링 기계","계산의 본질을 규정한 추상 기계.","turing-machine"),
     ("자료구조 기초","정보를 담는 그릇 — 리스트·트리·그래프.","data-structures"),
     ("복잡도와 알고리즘","'얼마나 빨리, 얼마나 많은 자원으로' 푸는가.","complexity"),
   ]),
 ]),
 ("Part 3. 탐색과 문제해결", [
   ("state-space","문제를 상태공간으로 보기","많은 AI 문제는 '상태들의 공간에서 길찾기'로 바꿀 수 있다. 그 사고법을 익힌다.",[
     ("상태·연산자·목표","문제를 상태공간으로 정식화하는 3요소.","state-operator-goal"),
     ("문제 정의의 예","퍼즐과 길찾기로 보는 상태공간 모델링.","problem-examples"),
   ]),
   ("blind-search","맹목적 탐색 — BFS와 DFS","목표까지의 정보 없이 공간을 훑는 기본 탐색 전략들.",[
     ("너비 우선 탐색(BFS)","가까운 곳부터 차례로 넓혀가는 탐색.","bfs"),
     ("깊이 우선 탐색(DFS)","한 길을 끝까지 파고드는 탐색.","dfs"),
     ("반복적 깊이심화","BFS의 최적성과 DFS의 적은 메모리를 결합한다.","iterative-deepening"),
   ]),
   ("heuristic-search","휴리스틱 탐색 — A*","'어림짐작'으로 탐색을 똑똑하게 만드는 방법.",[
     ("휴리스틱이란","목표까지의 거리를 추정하는 경험적 어림값.","heuristic"),
     ("탐욕적 최선 우선 탐색","추정값만 믿고 나아가는 탐색과 그 함정.","greedy-search"),
     ("A* 알고리즘","지나온 비용과 추정 비용을 함께 보는 최적 탐색.","astar"),
   ]),
   ("game-playing","게임과 적대적 탐색","상대가 있는 게임에서 최선의 수를 찾는 방법.",[
     ("게임 트리","수의 흐름을 트리로 펼쳐 보기.","game-tree"),
     ("미니맥스","최악을 가정하고 최선을 고르는 전략.","minimax"),
     ("알파-베타 가지치기","불필요한 가지를 잘라 탐색을 줄인다.","alpha-beta"),
   ]),
 ]),
 ("Part 4. 지식 표현과 추론", [
   ("representation","지식을 표현하는 방법","기계가 다룰 수 있도록 지식을 담는 여러 형식을 살펴본다.",[
     ("의미망과 프레임","개념과 관계를 그래프·틀로 표현하기.","semantic-net-frame"),
     ("규칙과 논리","'만약 ~라면 ~이다' 형태의 지식 표현.","rules-logic"),
     ("온톨로지","개념 체계를 정교하게 정의하기.","ontology"),
   ]),
   ("reasoning","추론","표현된 지식으로부터 새로운 결론을 이끌어내는 과정.",[
     ("전향 추론과 후향 추론","사실에서 출발할까, 목표에서 거슬러 올라갈까.","forward-backward"),
     ("연역·귀납·가추","세 가지 추론의 방식과 쓰임.","deduction-induction-abduction"),
   ]),
   ("expert-systems","전문가 시스템","규칙으로 전문가의 지식을 담아낸 고전 AI의 대표 성과.",[
     ("구조: 지식베이스와 추론엔진","전문가 시스템을 이루는 두 축.","structure"),
     ("대표 사례 (MYCIN 등)","의료 진단 등 실제로 쓰인 시스템들.","cases"),
     ("한계와 교훈","규칙 기반 접근이 부딪힌 벽과 그 시사점.","limits"),
   ]),
   ("fuzzy","불확실성과 퍼지 논리","'참/거짓' 사이의 회색지대를 다루는 방법.",[
     ("확실성 요인","결론에 신뢰도를 매기는 방식.","certainty-factor"),
     ("퍼지 집합과 퍼지 논리","'어느 정도 참'을 수학으로 다루기.","fuzzy-logic"),
   ]),
 ]),
 ("Part 5. 학습하는 기계", [
   ("machine-learning","기계학습의 기초","데이터로부터 스스로 규칙을 찾아내는 학습의 기본 개념.",[
     ("학습이란: 지도·비지도·강화","세 가지 학습 패러다임.","learning-paradigms"),
     ("회귀와 분류","연속값을 예측할까, 범주를 가를까.","regression-classification"),
     ("과적합과 일반화","외운 것과 이해한 것의 차이.","overfitting"),
   ]),
   ("neural-network","신경망의 원리","뇌에서 영감을 얻은 학습 모델의 작동 원리, 그리고 시각을 다루는 합성곱 신경망까지.",[
     ("퍼셉트론","가장 단순한 인공뉴런.","perceptron"),
     ("다층 신경망과 역전파","층을 쌓고 오차를 거슬러 학습시키기.","backpropagation"),
     ("합성곱 신경망(CNN): 고양이 실험에서 영상 인식까지","CNN 이전의 합성곱(Sobel·Gabor), 휴벨-비셀, 그리고 학습된 필터가 Gabor·V1과 일치하는 놀라움.","cnn"),
     ("딥러닝으로 가는 길","고전 신경망에서 오늘의 딥러닝까지.","deep-learning"),
     ("어텐션의 천장과 논리의 귀환","현 LLM은 어텐션 기반의 통계적 예측이라 본질적 한계(천장)가 있고, 이를 넘으려면 논리·추론(기호주의)과의 결합이 필요하다.","attention-ceiling"),
   ]),
   ("genetic","유전 알고리즘","진화의 원리를 빌려 좋은 해를 찾아가는 방법.",[
     ("진화에서 배우기","자연선택을 최적화에 적용하기.","learning-from-evolution"),
     ("선택·교차·돌연변이","유전 알고리즘의 핵심 연산.","selection-crossover-mutation"),
   ]),
   ("artificial-life","인공생명(Artificial Life)","'있을 수 있는 생명'을 기계로 빚는다 — 세포 자동자에서 예쁜꼬마선충의 커넥톰까지, 구조에서 행동이 창발하는 현장.",[
     ("인공생명이란","랭턴의 'life-as-it-could-be', 생명을 만들며 이해하기.","what-is-alife"),
     ("세포 자동자와 생명 게임","폰 노이만의 자기복제와 콘웨이의 생명 게임 — 단순 규칙에서 솟는 복잡성.","cellular-automata"),
     ("떼 지능과 디지털 진화","Boids의 새 떼, Tierra·Avida의 디지털 진화.","swarm-evolution"),
     ("커넥톰: 예쁜꼬마선충에서 OpenWorm·커넥톰 로봇까지","뉴런 302개의 배선도를 옮겼더니 똑같이 움직였다 — 구조가 곧 행동인가.","connectome"),
   ]),
   ("pattern-recognition","패턴 인식","데이터 속의 규칙과 무리를 알아보는 기술.",[
     ("특징과 분류","무엇을 보고 어떻게 나눌 것인가.","features-classification"),
     ("군집화","비슷한 것끼리 묶기.","clustering"),
   ]),
 ]),
 ("Part 6. 언어와 지각", [
   ("nlp","자연어 처리의 기초","사람의 말을 기계가 다루게 만드는 일의 어려움과 기본 기법.",[
     ("언어를 다루는 어려움","모호성·문맥 등 자연어의 까다로움.","difficulty-of-language"),
     ("형태소 분석과 구문 분석","문장을 단위로 쪼개고 구조를 파악하기.","morphology-syntax"),
     ("통계적 언어 모델","확률로 다음에 올 말을 예측하기.","statistical-language-model"),
   ]),
   ("agent","지능형 에이전트","인식하고 판단하고 행동하는 자율 시스템의 개념.",[
     ("에이전트란 무엇인가","환경 속에서 행동하는 주체.","what-is-agent"),
     ("환경과 합리성","무엇이 '합리적' 행동인가.","environment-rationality"),
     ("에이전트의 구조","단순 반사부터 학습 에이전트까지.","agent-architecture"),
   ]),
   ("robotics","로봇공학과 지각","현실 세계에서 보고 움직이는 지능.",[
     ("지각: 보고 듣기","센서로 세상을 받아들이기.","perception"),
     ("계획과 행동","지각을 행동으로 잇기.","planning-action"),
   ]),
 ]),
 ("Part 7. 고전 AI의 도구", [
   ("lisp","LISP — 생각을 코드로","고전 AI의 언어 LISP로 개념을 직접 손으로 다뤄 본다.",[
     ("왜 LISP인가","AI 연구가 LISP를 택한 이유.","why-lisp"),
     ("리스트와 재귀","LISP의 심장 — 리스트 처리와 재귀.","lists-recursion"),
     ("작은 예제","간단한 프로그램을 직접 만들어 보기.","lisp-example"),
   ]),
   ("prolog","Prolog — 논리로 프로그래밍하기","'무엇을'만 적으면 컴퓨터가 '어떻게'를 찾는 논리 프로그래밍.",[
     ("왜 Prolog인가","선언적 프로그래밍의 매력.","why-prolog"),
     ("사실·규칙·질의","Prolog 프로그램의 세 요소.","facts-rules-queries"),
     ("작은 예제","가계도·추론을 Prolog로 풀어 보기.","prolog-example"),
   ]),
 ]),
]

APPENDIX = [
  ("A1","pioneers","부록 A. 인공지능의 선구자들","튜링·매카시·민스키·힌튼… 이 분야를 만든 사람들과 그들의 생각."),
  ("B1","glossary","부록 B. 용어집","책에 나온 핵심 용어를 한자리에 모아 정리한다."),
]


def w(path, text):
    """Write unless the file is protected (hand-authored)."""
    if os.path.basename(path) in PROTECTED:
        return "protected"
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return "written"


def stub_section(path, code, title, summary):
    """Create a section stub only if it does not already exist."""
    if os.path.exists(path) or os.path.basename(path) in PROTECTED:
        return
    text = f"# {code}. {title}\n\n> {summary}\n\n---\n\n_본문은 준비 중입니다._\n"
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def main():
    os.makedirs(PAGES, exist_ok=True)
    toc = ["# 목차 — 인공지능의 기초 (Fundamental of AI)", "",
           "* [00. 들어가며 — 왜 지금 '기초'인가](pages/00-preface.md)", ""]
    chap = 0
    for part_title, chapters in BOOK:
        toc.append(f"### {part_title}")
        toc.append("")
        for slug, title, summary, sections in chapters:
            chap += 1
            cc = f"{chap:02d}"
            overview_name = f"{cc}-{slug}.md"
            # chapter overview page
            lines = [f"# {cc}. {title}", "", f"> {summary}", "", "## 이 장에서 다루는 것", ""]
            toc.append(f"* [{cc}. {title}](pages/{overview_name})")
            has_written = False
            for i, (st, ssum, sslug) in enumerate(sections, 1):
                code = f"{cc}-{i:02d}"
                if sslug:
                    has_written = True
                    sec_name = f"{code}-{sslug}.md"
                    lines.append(f"- [**{code} {st}**]({sec_name}) — {ssum}")
                    toc.append(f"  * [{code} {st}](pages/{sec_name})")
                    stub_section(os.path.join(PAGES, sec_name), code, st, ssum)
                else:
                    lines.append(f"- **{code} {st}** — {ssum}")
                    toc.append(f"  * {code} {st}")
            if has_written:
                lines += ["", "---", "", "위 목록의 각 절을 순서대로 따라가며 읽어 보세요.", ""]
            else:
                lines += ["", "---", "", "_본문은 준비 중입니다._", ""]
            w(os.path.join(PAGES, overview_name), "\n".join(lines))
        toc.append("")
    toc.append("### 부록")
    toc.append("")
    for prefix, slug, title, summary in APPENDIX:
        name = f"{prefix}-{slug}.md"
        toc.append(f"* [{title}](pages/{name})")
        w(os.path.join(PAGES, name),
          f"# {title}\n\n> {summary}\n\n---\n\n_본문은 준비 중입니다._\n")
    toc.append("")
    with open(os.path.join(ROOT, "TOC.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(toc))
    print(f"done. {chap} chapters. protected files preserved.")


if __name__ == "__main__":
    main()
