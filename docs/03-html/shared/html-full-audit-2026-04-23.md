# HTML 전수조사 보고서 (2026-04-23)

## 조사 범위
- 대상: `docs/03-html/`, `scripts/jaryo_html_deck/`, `docs/03-html/data/slide-specs.json`
- 기준 시점: 2026-04-23
- 전체 슬라이드 수: 94장

## 전체 분포
### 챕터별 장수
- OPENING: 3장
- CHAPTER 01: 11장
- CHAPTER 02: 13장
- CHAPTER 03: 6장
- CHAPTER 04: 12장
- CHAPTER 05: 10장
- CHAPTER 06: 13장
- CHAPTER 07: 13장
- CHAPTER 08: 9장
- CHAPTER 09: 4장

### Shell 분포
- agenda-list-shell: 1장
- evidence-table-shell: 27장
- process-flow-shell: 33장
- section-divider-shell: 7장
- split-compare-shell: 10장
- statement-editorial-shell: 15장
- title-hero-shell: 1장

## 사용자 선호 페이지 고정 baseline
- 고정 페이지: `1-18`, `21`, `24`, `37`, `39`, `40`, `52`, `53`
- 이 묶음은 이후 피드백 루프에서 디자인/작업 규칙의 우선 비교군으로 유지한다.

### 선호 페이지 목록
| Page | Slide ID | Chapter | Title | Shell |
| --- | --- | --- | --- | --- |
| 1 | S001 | OPENING | Harness 잘 사용하기 | title-hero-shell |
| 2 | S002 | OPENING | 시작하며 | process-flow-shell |
| 3 | S003 | OPENING | 전체 목차 | agenda-list-shell |
| 4 | S004 | CHAPTER 01 | 코딩은 사라지는가 | section-divider-shell |
| 5 | S005 | CHAPTER 01 | 기계어 → 어셈블리 | split-compare-shell |
| 6 | S006 | CHAPTER 01 | 어셈블리 → C/Pascal | split-compare-shell |
| 7 | S007 | CHAPTER 01 | C → Java | split-compare-shell |
| 8 | S008 | CHAPTER 01 | Java → Python | split-compare-shell |
| 9 | S009 | CHAPTER 01 | AI 개발 | statement-editorial-shell |
| 10 | S010 | CHAPTER 01 | 직접 하던 일의 감소 | evidence-table-shell |
| 11 | S011 | CHAPTER 01 | 숫자로 보는 변화 | evidence-table-shell |
| 12 | S012 | CHAPTER 01 | 문서가 코드 | process-flow-shell |
| 13 | S013 | CHAPTER 01 | 개발자의 새로운 역할 | process-flow-shell |
| 14 | S014 | CHAPTER 01 | 그래도 기초가 중요하다 | statement-editorial-shell |
| 15 | S015 | CHAPTER 02 | 왜 Claude Code인가 | section-divider-shell |
| 16 | S016 | CHAPTER 02 | 에이전틱 코딩의 실제 성과 | evidence-table-shell |
| 17 | S017 | CHAPTER 02 | 1막: Copilot과 ChatGPT, 프롬프트의 시대 | process-flow-shell |
| 18 | S018 | CHAPTER 02 | CoT / ReAct / ToT | process-flow-shell |
| 21 | S021 | CHAPTER 02 | 네 가지 에이전틱 패턴 | evidence-table-shell |
| 24 | S024 | CHAPTER 02 | Cursor 아키텍처 | process-flow-shell |
| 37 | S037 | CHAPTER 04 | 에이전트 루프: 하네스의 심장 | process-flow-shell |
| 39 | S039 | CHAPTER 04 | 하네스의 도구 | evidence-table-shell |
| 40 | S040 | CHAPTER 04 | Context Engineering | process-flow-shell |
| 52 | S052 | CHAPTER 05 | Context Rot: 길어진 기억은 조용히 썩는다 | statement-editorial-shell |
| 53 | S053 | CHAPTER 05 | 신뢰는 조율되어야 한다 | statement-editorial-shell |

## 핵심 확인 결과
- `docs/03-html/slides/slide-001.html`부터 `slide-094.html`까지 생성 artifact가 연속으로 존재한다.
- 구현 source는 `scripts/jaryo_html_deck/slides/chapter_XX/slide_YYY.py` chapter folder 기준으로 정렬했다.
- 번호 drift/충돌 리스크를 줄이기 위해 chapter folder 분리와 전역 one-pass 렌더링 파이프라인을 함께 유지한다.
