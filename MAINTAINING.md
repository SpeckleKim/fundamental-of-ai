# 리포지토리 관리 안내 (maintainers)

이 저장소는 WikiDocs 책 『인공지능의 기초』와 연동된다. (이 파일은 관리용이며 책 본문이 아니다.)

## 구조
- `TOC.md` — 목차 정의
- `pages/` — 본문 마크다운 (제목 번호 `NN-`, `NN-MM-`로 정렬을 맞춘다)
- `pages/assets/` — 도식 이미지(PNG) + 원본 SVG + `STYLE.md`(Drawing Style)
- `tools/` — 도식 생성/변환 스크립트
  - `svg2png.py` — SVG → PNG(qlmanage 렌더 + PIL 여백 트림, 폭 1100 제한)
  - `gen_*.py` — 복잡한 도식의 파이썬 생성기

## 워크플로
1. `TOC.md`/`pages/` 수정
2. 도식은 SVG로 그린 뒤 `python3 tools/svg2png.py pages/assets/X.svg` 로 PNG 생성, 본문에서 `![설명](assets/X.png)` 참조
3. `git push` → WikiDocs에 자동 반영

## 주의
- 그림은 **원본 SVG로 직접 작도**(외부 이미지 직접 사용 금지, 저작권). Drawing Style은 `pages/assets/STYLE.md` 준수.
- `build_skeleton.py`는 초기 스캐폴딩용 — 본문이 채워진 지금은 실행 시 덮어쓸 수 있으니 주의.
