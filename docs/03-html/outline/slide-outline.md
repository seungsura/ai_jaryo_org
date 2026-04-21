# Slide Outline

- status: 00/01/02 27-slide make-slide rebuild
- canonical source: `docs/02-seminar/harness-rebuilt-md/00-overview.md`, `docs/02-seminar/harness-rebuilt-md/01-코딩은 사라지는가.md`, `docs/02-seminar/harness-rebuilt-md/02-왜 Claude Code인가, 그리고 왜 Harness 인가.md`
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

### S017. 왜 Claude Code인가
- file: `docs/03-html/slides/slide-017.html`
- slide type: `statement`
- layout: `editorial`
- shell: `statement-editorial-shell`
- source section: `02`
- source paragraph block: `02-00`
- key claim: Agent = Model + Harness
- notes intent: Agent = Model + Harness thesis와 명사형 quote
- notes status: `ready`

### S018. 1막: Copilot과 ChatGPT, 프롬프트의 시대
- file: `docs/03-html/slides/slide-018.html`
- slide type: `process`
- layout: `wide`
- shell: `process-flow-shell`
- source section: `02`
- source paragraph block: `02-02`
- key claim: 자동완성에서 자연어 지시 인터페이스로
- notes intent: 프롬프트 시대의 출발점 비교
- notes status: `ready`

### S019. 프롬프트 패턴의 확장
- file: `docs/03-html/slides/slide-019.html`
- slide type: `process`
- layout: `wide`
- shell: `process-flow-shell`
- source section: `02`
- source paragraph block: `02-03`
- key claim: 프롬프트가 모델에게 추가로 맡긴 일
- notes intent: CoT/ReAct/ToT/Self-Refine/Reflexion diagram
- notes status: `ready`

### S020. 네 가지 에이전틱 패턴
- file: `docs/03-html/slides/slide-020.html`
- slide type: `table`
- layout: `wide`
- shell: `evidence-table-shell`
- source section: `02`
- source paragraph block: `02-04`
- key claim: 모델 바깥 구조가 성능을 좌우
- notes intent: Andrew Ng 4 agentic patterns
- notes status: `ready`

### S021. 프롬프트 시대의 벽
- file: `docs/03-html/slides/slide-021.html`
- slide type: `statement`
- layout: `editorial`
- shell: `statement-editorial-shell`
- source section: `02`
- source paragraph block: `02-05`
- key claim: 모델은 보지 못한 것을 알 수 없음
- notes intent: 프롬프트 시대의 한계
- notes status: `ready`

### S022. 2막: Cursor와 컨텍스트의 시대
- file: `docs/03-html/slides/slide-022.html`
- slide type: `process`
- layout: `wide`
- shell: `process-flow-shell`
- source section: `02`
- source paragraph block: `02-06`
- key claim: 현재 파일에서 전체 코드베이스로
- notes intent: 초기 Copilot과 Cursor 계열 도구 비교
- notes status: `ready`

### S023. Cursor 아키텍처
- file: `docs/03-html/slides/slide-023.html`
- slide type: `process`
- layout: `wide`
- shell: `process-flow-shell`
- source section: `02`
- source paragraph block: `02-07`
- key claim: 긴 프롬프트가 아니라 검색기와 편집기
- notes intent: Cursor architecture asset and process
- notes status: `ready`

### S024. 컨텍스트 시대의 벽
- file: `docs/03-html/slides/slide-024.html`
- slide type: `process`
- layout: `wide`
- shell: `process-flow-shell`
- source section: `02`
- source paragraph block: `02-08`
- key claim: 좋은 입력만으로는 루프 통제 불가
- notes intent: 컨텍스트 시대의 한계와 에이전트 루프
- notes status: `ready`

### S025. 3막: 하네스의 시대
- file: `docs/03-html/slides/slide-025.html`
- slide type: `process`
- layout: `wide`
- shell: `process-flow-shell`
- source section: `02`
- source paragraph block: `02-09`
- key claim: 터미널 네이티브 실행 환경
- notes intent: Claude Code harness components
- notes status: `ready`

### S026. Agent = Model + Harness
- file: `docs/03-html/slides/slide-026.html`
- slide type: `statement`
- layout: `editorial`
- shell: `statement-editorial-shell`
- source section: `02`
- source paragraph block: `02-10`
- key claim: 하네스가 결정하는 네 지점
- notes intent: 02-v05 decision points
- notes status: `ready`

### S027. 시대의 흐름
- file: `docs/03-html/slides/slide-027.html`
- slide type: `table`
- layout: `wide`
- shell: `evidence-table-shell`
- source section: `02`
- source paragraph block: `02-11`
- key claim: 프롬프트, 컨텍스트, 하네스의 포함 관계
- notes intent: three-era timeline and table
- notes status: `ready`
