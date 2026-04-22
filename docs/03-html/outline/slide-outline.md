# Slide Outline

- status: 00/01/02/03/04 45-slide make-slide rebuild
- canonical source: `docs/02-seminar/harness-rebuilt-md/00-overview.md`, `docs/02-seminar/harness-rebuilt-md/01-코딩은 사라지는가.md`, `docs/02-seminar/harness-rebuilt-md/02-왜 Claude Code인가, 그리고 왜 Harness 인가.md`, `docs/02-seminar/harness-rebuilt-md/03-AI 시대의 개발 방법론.md`, `docs/02-seminar/harness-rebuilt-md/04-프롬프트를 넘어서: 에이전트를 움직이는 기술, Harness.md`
- output deck: `docs/03-html/deck/index.html`
- output script: `docs/03-html/deck/script.md`
- theme: `minimal-light`
- runtime policy: single-file deck, keyboard navigation, touch/swipe, active slide switching, print CSS
- rejected chrome: progress bar, fullscreen UI, slide counter UI, notes UI, keyboard hint

## Section Targets

| section | source | target slides |
| --- | --- | --- |
| 00 | `docs/02-seminar/harness-rebuilt-md/00-overview.md` | 3 |
| 01 | `docs/02-seminar/harness-rebuilt-md/01-코딩은 사라지는가.md` | 11 |
| 02 | `docs/02-seminar/harness-rebuilt-md/02-왜 Claude Code인가, 그리고 왜 Harness 인가.md` | 13 |
| 03 | `docs/02-seminar/harness-rebuilt-md/03-AI 시대의 개발 방법론.md` | 6 |
| 04 | `docs/02-seminar/harness-rebuilt-md/04-프롬프트를 넘어서: 에이전트를 움직이는 기술, Harness.md` | 12 |

## Slide Registry

### S001. Harness 잘 사용하기
- file: `docs/03-html/slides/slide-001.html`
- slide type: `title`
- layout: `centered`
- shell: `title-hero-shell`
- source section: `00`
- source paragraph block: `00-00`
- key claim: 에이전트가 일할 환경 설계
- notes intent: 첫 장에서 제목, 부제, 발표자만 고정
- notes status: `ready`

### S002. 시작하며
- file: `docs/03-html/slides/slide-002.html`
- slide type: `process`
- layout: `wide`
- shell: `process-flow-shell`
- source section: `00`
- source paragraph block: `00-01`
- key claim: AI에게 무엇을 말할까에서 AI가 일할 환경 설계로 이동
- notes intent: 챗봇 사용 경험과 도구 수렴을 Harness 문제로 연결
- notes status: `ready`

### S003. 전체 목차
- file: `docs/03-html/slides/slide-003.html`
- slide type: `agenda`
- layout: `wide`
- shell: `agenda-list-shell`
- source section: `00`
- source paragraph block: `00-03`
- key claim: Harness 관점으로 읽는 9개 장
- notes intent: 00-overview의 목차 표를 한 장에 압축
- notes status: `ready`

### S004. 코딩은 사라지는가
- file: `docs/03-html/slides/slide-004.html`
- slide type: `section`
- layout: `centered`
- shell: `section-divider-shell`
- source section: `01`
- source paragraph block: `01-00`
- key claim: 개발의 추상화 수준 상승
- notes intent: 01장의 질문을 챕터 단위로 고정
- notes status: `ready`

### S005. 기계어 → 어셈블리
- file: `docs/03-html/slides/slide-005.html`
- slide type: `comparison`
- layout: `split`
- shell: `split-compare-shell`
- source section: `01`
- source paragraph block: `01-01`
- key claim: 이진 코드 직접 작성 부담의 감소
- notes intent: source code block 기반 첫 전환 사례
- notes status: `ready`

### S006. 어셈블리 → C/Pascal
- file: `docs/03-html/slides/slide-006.html`
- slide type: `comparison`
- layout: `split`
- shell: `split-compare-shell`
- source section: `01`
- source paragraph block: `01-01`
- key claim: 어셈블리 표현량에서 C 함수 표현으로
- notes intent: source code block 기반 두 번째 전환 사례
- notes status: `ready`

### S007. C → Java
- file: `docs/03-html/slides/slide-007.html`
- slide type: `comparison`
- layout: `split`
- shell: `split-compare-shell`
- source section: `01`
- source paragraph block: `01-01`
- key claim: 수동 메모리 관리에서 GC로
- notes intent: source code block 기반 세 번째 전환 사례
- notes status: `ready`

### S008. Java → Python
- file: `docs/03-html/slides/slide-008.html`
- slide type: `comparison`
- layout: `split`
- shell: `split-compare-shell`
- source section: `01`
- source paragraph block: `01-01`
- key claim: 같은 출력과 더 짧은 표현
- notes intent: source code block 기반 네 번째 전환 사례
- notes status: `ready`

### S009. AI 개발
- file: `docs/03-html/slides/slide-009.html`
- slide type: `statement`
- layout: `editorial`
- shell: `statement-editorial-shell`
- source section: `01`
- source paragraph block: `01-01`
- key claim: 개발의 추상화 수준 상승
- notes intent: source prompt와 quote 기반 AI 개발 사례
- notes status: `ready`

### S010. 직접 하던 일의 감소
- file: `docs/03-html/slides/slide-010.html`
- slide type: `table`
- layout: `wide`
- shell: `evidence-table-shell`
- source section: `01`
- source paragraph block: `01-02`
- key claim: 직접 작성 부담의 지속적 위임
- notes intent: 시대별 위임 표와 질문 반전
- notes status: `ready`

### S011. 숫자로 보는 변화
- file: `docs/03-html/slides/slide-011.html`
- slide type: `table`
- layout: `wide`
- shell: `evidence-table-shell`
- source section: `01`
- source paragraph block: `01-03`
- key claim: 수동 코드 작성 비중 감소의 현장 신호
- notes intent: source 숫자 사실만 압축
- notes status: `ready`

### S012. 문서가 코드
- file: `docs/03-html/slides/slide-012.html`
- slide type: `process`
- layout: `wide`
- shell: `process-flow-shell`
- source section: `01`
- source paragraph block: `01-04`
- key claim: 에이전트가 매 세션 읽고 따라야 할 운영 규칙
- notes intent: page-011 reference 기반 문서 card layout
- notes status: `ready`

### S013. 개발자의 새로운 역할
- file: `docs/03-html/slides/slide-013.html`
- slide type: `process`
- layout: `wide`
- shell: `process-flow-shell`
- source section: `01`
- source paragraph block: `01-05`
- key claim: 환경 설계와 결과 판단
- notes intent: reference layout 기반 evolution and analogy blocks
- notes status: `ready`

### S014. 그래도 기초가 중요하다
- file: `docs/03-html/slides/slide-014.html`
- slide type: `statement`
- layout: `editorial`
- shell: `statement-editorial-shell`
- source section: `01`
- source paragraph block: `01-06`
- key claim: AI 코딩은 에이전트가 일할 환경을 설계하고 검증하는 영역
- notes intent: reference layout 기반 quote and summary cards
- notes status: `ready`

### S015. 왜 Claude Code인가
- file: `docs/03-html/slides/slide-015.html`
- slide type: `section`
- layout: `centered`
- shell: `section-divider-shell`
- source section: `02`
- source paragraph block: `02-00`
- key claim: AI 코딩 도구 흐름의 대표 사례
- notes intent: 02장 진입과 제품 리뷰가 아닌 흐름 분석 고정
- notes status: `ready`

### S016. 에이전틱 코딩의 실제 성과
- file: `docs/03-html/slides/slide-016.html`
- slide type: `table`
- layout: `wide`
- shell: `evidence-table-shell`
- source section: `02`
- source paragraph block: `02-01`
- key claim: 속도, 온보딩, 불가능하던 작업의 변화
- notes intent: page-017 reference 기반 성과 metric cards
- notes status: `ready`

### S017. 1막: Copilot과 ChatGPT, 프롬프트의 시대
- file: `docs/03-html/slides/slide-017.html`
- slide type: `process`
- layout: `wide`
- shell: `process-flow-shell`
- source section: `02`
- source paragraph block: `02-02`
- key claim: 자동완성에서 자연어 지시 인터페이스로
- notes intent: 프롬프트 시대의 출발점 비교
- notes status: `ready`

### S018. CoT / ReAct / ToT
- file: `docs/03-html/slides/slide-018.html`
- slide type: `process`
- layout: `wide`
- shell: `process-flow-shell`
- source section: `02`
- source paragraph block: `02-03`
- key claim: 세 추론 패턴의 구조 차이
- notes intent: CoT / ReAct / ToT native three-card comparison
- notes status: `ready`

### S019. ReAct / Tree-of-Thought
- file: `docs/03-html/slides/slide-019.html`
- slide type: `process`
- layout: `wide`
- shell: `process-flow-shell`
- source section: `02`
- source paragraph block: `02-03`
- key claim: 행동 루프와 경로 탐색
- notes intent: ReAct / Tree-of-Thought native diagrams
- notes status: `ready`

### S020. Self-Refine / Reflexion
- file: `docs/03-html/slides/slide-020.html`
- slide type: `process`
- layout: `wide`
- shell: `process-flow-shell`
- source section: `02`
- source paragraph block: `02-03`
- key claim: 출력 이후의 피드백 루프
- notes intent: Self-Refine / Reflexion native feedback-loop diagrams
- notes status: `ready`

### S021. 네 가지 에이전틱 패턴
- file: `docs/03-html/slides/slide-021.html`
- slide type: `table`
- layout: `wide`
- shell: `evidence-table-shell`
- source section: `02`
- source paragraph block: `02-04`
- key claim: 모델 바깥 구조가 성능을 좌우
- notes intent: Andrew Ng four patterns native quadrant
- notes status: `ready`

### S022. 프롬프트 시대의 벽
- file: `docs/03-html/slides/slide-022.html`
- slide type: `statement`
- layout: `editorial`
- shell: `statement-editorial-shell`
- source section: `02`
- source paragraph block: `02-05`
- key claim: 모델은 보지 못한 것을 알 수 없음
- notes intent: 프롬프트 시대의 한계
- notes status: `ready`

### S023. 2막: Cursor와 컨텍스트의 시대
- file: `docs/03-html/slides/slide-023.html`
- slide type: `process`
- layout: `wide`
- shell: `process-flow-shell`
- source section: `02`
- source paragraph block: `02-06`
- key claim: 현재 파일에서 전체 코드베이스로
- notes intent: 초기 Copilot과 Cursor 계열 도구 비교
- notes status: `ready`

### S024. Cursor 아키텍처
- file: `docs/03-html/slides/slide-024.html`
- slide type: `process`
- layout: `wide`
- shell: `process-flow-shell`
- source section: `02`
- source paragraph block: `02-07`
- key claim: 긴 프롬프트가 아니라 검색기와 편집기
- notes intent: Cursor architecture native system map
- notes status: `ready`

### S025. 컨텍스트 시대의 벽
- file: `docs/03-html/slides/slide-025.html`
- slide type: `process`
- layout: `wide`
- shell: `process-flow-shell`
- source section: `02`
- source paragraph block: `02-08`
- key claim: 좋은 입력만으로는 루프 통제 불가
- notes intent: 컨텍스트 시대의 한계와 에이전트 루프
- notes status: `ready`

### S026. 3막: 하네스의 시대
- file: `docs/03-html/slides/slide-026.html`
- slide type: `process`
- layout: `wide`
- shell: `process-flow-shell`
- source section: `02`
- source paragraph block: `02-09`
- key claim: 작업 환경 전체를 품기 시작한 코딩 도구
- notes intent: Harness era signs without chapter 4 mechanics
- notes status: `ready`

### S027. 시대의 흐름
- file: `docs/03-html/slides/slide-027.html`
- slide type: `table`
- layout: `wide`
- shell: `evidence-table-shell`
- source section: `02`
- source paragraph block: `02-11`
- key claim: Agent = Model + Harness
- notes intent: final relationship page
- notes status: `ready`

### S028. AI 시대의 개발 방법론
- file: `docs/03-html/slides/slide-028.html`
- slide type: `section`
- layout: `centered`
- shell: `section-divider-shell`
- source section: `03`
- source paragraph block: `03-00`
- key claim: TDD·SDD·Spec-first 재부상
- notes intent: 03장 진입을 알리는 section divider
- notes status: `ready`

### S029. 왜 지금 방법론
- file: `docs/03-html/slides/slide-029.html`
- slide type: `table`
- layout: `wide`
- shell: `evidence-table-shell`
- source section: `03`
- source paragraph block: `03-01`
- key claim: AI에게 무엇을 시킬지, 어떻게 검증할 것인지
- notes intent: AI 코딩 방법론 재부상 연대기
- notes status: `ready`

### S030. SDD
- file: `docs/03-html/slides/slide-030.html`
- slide type: `process`
- layout: `wide`
- shell: `process-flow-shell`
- source section: `03`
- source paragraph block: `03-02`
- key claim: 스펙이 진실의 원천
- notes intent: GitHub Spec Kit의 세 단계와 멈춤 장치
- notes status: `ready`

### S031. TDD (Test-Driven Development)
- file: `docs/03-html/slides/slide-031.html`
- slide type: `statement`
- layout: `editorial`
- shell: `statement-editorial-shell`
- source section: `03`
- source paragraph block: `03-03`
- key claim: 테스트를 먼저 쓰고, 통과하는 코드를 나중에 쓴다
- notes intent: Page 028 TDD lead와 anti-cheat 규칙
- notes status: `ready`

### S032. Waterfall vs SDD
- file: `docs/03-html/slides/slide-032.html`
- slide type: `comparison`
- layout: `split`
- shell: `split-compare-shell`
- source section: `03`
- source paragraph block: `03-04`
- key claim: Waterfall은 순차적으로 진행되고, SDD는 스펙을 실행 기준으로 둔다
- notes intent: Royce 1970과 spec-driven.md evidence로 Waterfall vs SDD 비교
- notes status: `ready`

### S033. SDD + TDD가 Harness로 이어지는 이유
- file: `docs/03-html/slides/slide-033.html`
- slide type: `statement`
- layout: `editorial`
- shell: `statement-editorial-shell`
- source section: `03`
- source paragraph block: `03-05`
- key claim: 이 시스템이 곧 하네스 엔지니어링
- notes intent: 03장에서 04장 Harness 구조로 넘어가는 bridge
- notes status: `ready`

### S034. 프롬프트를 넘어서
- file: `docs/03-html/slides/slide-034.html`
- slide type: `section`
- layout: `centered`
- shell: `section-divider-shell`
- source section: `04`
- source paragraph block: `04-00`
- key claim: Prompt, Context, Harness
- notes intent: 04장 진입을 알리는 section divider
- notes status: `ready`

### S035. Prompt, Context, Harness
- file: `docs/03-html/slides/slide-035.html`
- slide type: `table`
- layout: `wide`
- shell: `evidence-table-shell`
- source section: `04`
- source paragraph block: `04-01`
- key claim: Prompt ⊂ Context ⊂ Harness
- notes intent: source page 36/37 의미를 한 장의 hierarchy로 압축
- notes status: `ready`

### S036. Agent = Model + Harness
- file: `docs/03-html/slides/slide-036.html`
- slide type: `table`
- layout: `wide`
- shell: `evidence-table-shell`
- source section: `04`
- source paragraph block: `04-02`
- key claim: 모델이 아닌 것은 전부 하네스입니다.
- notes intent: 공식, 인용구, 여섯 구성 요소를 한 장에 배치
- notes status: `ready`

### S037. 에이전트 루프: 하네스의 심장
- file: `docs/03-html/slides/slide-037.html`
- slide type: `process`
- layout: `wide`
- shell: `process-flow-shell`
- source section: `04`
- source paragraph block: `04-03`
- key claim: 네 지점을 신뢰성 있게 만드는 일
- notes intent: gather context, take action, verify work, repeat loop
- notes status: `ready`

### S038. 하네스의 책임
- file: `docs/03-html/slides/slide-038.html`
- slide type: `process`
- layout: `wide`
- shell: `process-flow-shell`
- source section: `04`
- source paragraph block: `04-04`
- key claim: 다섯 개 기능 블록
- notes intent: 5 responsibility cards와 설계 순서 rail
- notes status: `ready`

### S039. 하네스의 도구
- file: `docs/03-html/slides/slide-039.html`
- slide type: `table`
- layout: `wide`
- shell: `evidence-table-shell`
- source section: `04`
- source paragraph block: `04-05`
- key claim: 책임과 도구는 1:1이 아니다
- notes intent: 책임 anchor와 도구 node의 다대다 관계 지도
- notes status: `ready`

### S040. Context Engineering
- file: `docs/03-html/slides/slide-040.html`
- slide type: `process`
- layout: `wide`
- shell: `process-flow-shell`
- source section: `04`
- source paragraph block: `04-06`
- key claim: smallest set of high-signal tokens
- notes intent: Write, Select, Compress, Isolate 네 전략
- notes status: `ready`

### S041. MCP와 Context Hub
- file: `docs/03-html/slides/slide-041.html`
- slide type: `process`
- layout: `wide`
- shell: `process-flow-shell`
- source section: `04`
- source paragraph block: `04-07`
- key claim: 연결 방식을 표준화
- notes intent: MCP native architecture와 Context Hub 연결 의미
- notes status: `ready`

### S042. RAG vs Context Hub
- file: `docs/03-html/slides/slide-042.html`
- slide type: `table`
- layout: `wide`
- shell: `evidence-table-shell`
- source section: `04`
- source paragraph block: `04-08`
- key claim: 넓게 찾는가, 지금 맞는 문서를 지정하는가
- notes intent: RAG 논문과 MCP/Context Hub 문서 조사 기반 비교
- notes status: `ready`

### S043. Memory: 세션을 넘어서는 기억
- file: `docs/03-html/slides/slide-043.html`
- slide type: `table`
- layout: `wide`
- shell: `evidence-table-shell`
- source section: `04`
- source paragraph block: `04-09`
- key claim: 대화창을 기억 저장소로 착각하지 않는다
- notes intent: 외부 artifact map과 memory claim
- notes status: `ready`

### S044. Stable Prefix와 Variable Suffix
- file: `docs/03-html/slides/slide-044.html`
- slide type: `comparison`
- layout: `split`
- shell: `split-compare-shell`
- source section: `04`
- source paragraph block: `04-10`
- key claim: 잘 쓰는 것 못지않게 안 바꾸는 것도 능력
- notes intent: prefix/suffix diagram
- notes status: `ready`

### S045. 하네스는 환경 그 자체다
- file: `docs/03-html/slides/slide-045.html`
- slide type: `process`
- layout: `wide`
- shell: `process-flow-shell`
- source section: `04`
- source paragraph block: `04-11`
- key claim: 필요한 파일, 필요한 도구, 필요한 규칙
- notes intent: chapter 04 closing statement
- notes status: `ready`
