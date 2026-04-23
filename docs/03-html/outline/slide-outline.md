# Slide Outline

- status: 00/01/02/03/04/05/06/07/08/09 92-slide make-slide rebuild
- canonical source: `docs/02-seminar/harness-rebuilt-md/00-*.md`, `docs/02-seminar/harness-rebuilt-md/01-*.md`, `docs/02-seminar/harness-rebuilt-md/02-*.md`, `docs/02-seminar/harness-rebuilt-md/03-*.md`, `docs/02-seminar/harness-rebuilt-md/04-*.md`, `docs/02-seminar/harness-rebuilt-md/05-*.md`, `docs/02-seminar/harness-rebuilt-md/06-*.md`, `docs/02-seminar/harness-rebuilt-md/07-*.md`, `docs/02-seminar/harness-rebuilt-md/08-*.md`, `docs/02-seminar/harness-rebuilt-md/09-*.md`
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

### S019. 네 가지 에이전틱 패턴
- file: `docs/03-html/slides/slide-019.html`
- slide type: `table`
- layout: `wide`
- shell: `evidence-table-shell`
- source section: `02`
- source paragraph block: `02-04`
- key claim: 모델 바깥 구조가 성능을 좌우
- notes intent: Andrew Ng four patterns node-only native quadrant
- notes status: `ready`

### S020. 프롬프트 시대의 벽
- file: `docs/03-html/slides/slide-020.html`
- slide type: `statement`
- layout: `editorial`
- shell: `statement-editorial-shell`
- source section: `02`
- source paragraph block: `02-05`
- key claim: 모델은 보지 못한 것을 알 수 없음
- notes intent: 프롬프트 시대의 한계
- notes status: `ready`

### S021. 2막: Cursor와 컨텍스트의 시대
- file: `docs/03-html/slides/slide-021.html`
- slide type: `process`
- layout: `wide`
- shell: `process-flow-shell`
- source section: `02`
- source paragraph block: `02-06`
- key claim: 현재 파일에서 전체 코드베이스로
- notes intent: 초기 Copilot과 Cursor 계열 도구 비교
- notes status: `ready`

### S022. Cursor 아키텍처
- file: `docs/03-html/slides/slide-022.html`
- slide type: `process`
- layout: `wide`
- shell: `process-flow-shell`
- source section: `02`
- source paragraph block: `02-07`
- key claim: 긴 프롬프트가 아니라 검색기와 편집기
- notes intent: Cursor architecture raw asset with source-backed arrow flow
- notes status: `ready`

### S023. 컨텍스트만으로는 부족하다
- file: `docs/03-html/slides/slide-023.html`
- slide type: `comparison`
- layout: `split`
- shell: `split-compare-shell`
- source section: `02`
- source paragraph block: `02-08`
- key claim: 멈춤 기준과 검증 경로를 먼저 설계해야 한다
- notes intent: split-compare family로 폭주 축과 통제 기준을 압축 대비
- notes status: `ready`

### S024. 3막: 하네스의 시대
- file: `docs/03-html/slides/slide-024.html`
- slide type: `process`
- layout: `wide`
- shell: `process-flow-shell`
- source section: `02`
- source paragraph block: `02-09`
- key claim: 작업 환경 전체를 품기 시작한 코딩 도구
- notes intent: Harness era minimal transition
- notes status: `ready`

### S025. 3막: Claude Code, Codex, OpenCode 와 하네스의 시대
- file: `docs/03-html/slides/slide-025.html`
- slide type: `table`
- layout: `wide`
- shell: `evidence-table-shell`
- source section: `02`
- source paragraph block: `02-11`
- key claim: Agent = Model + Harness
- notes intent: 2장 결론 관계식을 source heading 중심으로 고정
- notes status: `ready`

### S026. AI 시대의 개발 방법론
- file: `docs/03-html/slides/slide-026.html`
- slide type: `section`
- layout: `centered`
- shell: `section-divider-shell`
- source section: `03`
- source paragraph block: `03-00`
- key claim: TDD·SDD·Spec-first 재부상
- notes intent: 03장 진입을 source heading 키워드와 함께 고정
- notes status: `ready`

### S027. 왜 지금 방법론
- file: `docs/03-html/slides/slide-027.html`
- slide type: `table`
- layout: `wide`
- shell: `evidence-table-shell`
- source section: `03`
- source paragraph block: `03-01`
- key claim: AI에게 무엇을 시킬지, 어떻게 검증할 것인지
- notes intent: AI 코딩 방법론 재부상 연대기
- notes status: `ready`

### S028. SDD
- file: `docs/03-html/slides/slide-028.html`
- slide type: `process`
- layout: `wide`
- shell: `process-flow-shell`
- source section: `03`
- source paragraph block: `03-02`
- key claim: 스펙이 진실의 원천
- notes intent: GitHub Spec Kit의 세 단계와 멈춤 장치
- notes status: `ready`

### S029. TDD (Test-Driven Development)
- file: `docs/03-html/slides/slide-029.html`
- slide type: `statement`
- layout: `editorial`
- shell: `statement-editorial-shell`
- source section: `03`
- source paragraph block: `03-03`
- key claim: 테스트를 먼저 쓰고, 통과하는 코드를 나중에 쓴다
- notes intent: Page 028 TDD lead와 anti-cheat 규칙
- notes status: `ready`

### S030. Waterfall vs SDD
- file: `docs/03-html/slides/slide-030.html`
- slide type: `comparison`
- layout: `split`
- shell: `split-compare-shell`
- source section: `03`
- source paragraph block: `03-04`
- key claim: Waterfall은 순차적으로 진행되고, SDD는 스펙을 실행 기준으로 둔다
- notes intent: Royce 1970과 spec-driven.md evidence로 Waterfall vs SDD 비교
- notes status: `ready`

### S031. SDD + TDD가 Harness로 이어지는 이유
- file: `docs/03-html/slides/slide-031.html`
- slide type: `statement`
- layout: `editorial`
- shell: `statement-editorial-shell`
- source section: `03`
- source paragraph block: `03-05`
- key claim: 이 시스템이 곧 하네스 엔지니어링
- notes intent: 03장에서 04장 Harness 구조로 넘어가는 bridge
- notes status: `ready`

### S032. 프롬프트를 넘어서
- file: `docs/03-html/slides/slide-032.html`
- slide type: `section`
- layout: `centered`
- shell: `section-divider-shell`
- source section: `04`
- source paragraph block: `04-00`
- key claim: Prompt, Context, Harness
- notes intent: 04장 진입을 알리는 section divider
- notes status: `ready`

### S033. Prompt, Context, Harness
- file: `docs/03-html/slides/slide-033.html`
- slide type: `table`
- layout: `wide`
- shell: `evidence-table-shell`
- source section: `04`
- source paragraph block: `04-01`
- key claim: Prompt ⊂ Context ⊂ Harness
- notes intent: source page 36/37 의미를 한 장의 hierarchy로 압축
- notes status: `ready`

### S034. Agent = Model + Harness
- file: `docs/03-html/slides/slide-034.html`
- slide type: `table`
- layout: `wide`
- shell: `evidence-table-shell`
- source section: `04`
- source paragraph block: `04-02`
- key claim: 모델이 아닌 것은 전부 하네스입니다.
- notes intent: 공식, 인용구, 여섯 구성 요소를 한 장에 배치
- notes status: `ready`

### S035. 에이전트 루프: 하네스의 심장
- file: `docs/03-html/slides/slide-035.html`
- slide type: `process`
- layout: `wide`
- shell: `process-flow-shell`
- source section: `04`
- source paragraph block: `04-03`
- key claim: 거의 모든 에이전트가 반복하는 4단계.
- notes intent: gather context, take action, verify work, repeat loop
- notes status: `ready`

### S036. 하네스의 책임
- file: `docs/03-html/slides/slide-036.html`
- slide type: `process`
- layout: `wide`
- shell: `process-flow-shell`
- source section: `04`
- source paragraph block: `04-04`
- key claim: 다섯 개 기능 블록
- notes intent: 5 responsibility cards와 설계 순서 rail
- notes status: `ready`

### S037. 하네스의 도구
- file: `docs/03-html/slides/slide-037.html`
- slide type: `table`
- layout: `wide`
- shell: `evidence-table-shell`
- source section: `04`
- source paragraph block: `04-05`
- key claim: 책임과 도구는 1:1이 아니다
- notes intent: 책임 anchor와 도구 node의 다대다 관계 지도
- notes status: `ready`

### S038. Context Engineering
- file: `docs/03-html/slides/slide-038.html`
- slide type: `process`
- layout: `wide`
- shell: `process-flow-shell`
- source section: `04`
- source paragraph block: `04-06`
- key claim: Anthropic의 4가지 전략: 필요한 정보만 남기고 잡음은 덜어낸다.
- notes intent: Write, Select, Compress, Isolate 네 전략
- notes status: `ready`

### S039. MCP와 Context 7
- file: `docs/03-html/slides/slide-039.html`
- slide type: `process`
- layout: `wide`
- shell: `process-flow-shell`
- source section: `04`
- source paragraph block: `04-07`
- key claim: 연결 방식을 표준화
- notes intent: MCP 원리와 Context 7 MCP 서버 연결 의미
- notes status: `ready`

### S040. RAG vs Context 7
- file: `docs/03-html/slides/slide-040.html`
- slide type: `table`
- layout: `wide`
- shell: `evidence-table-shell`
- source section: `04`
- source paragraph block: `04-08`
- key claim: 검색 범위와 기준 시점의 차이
- notes intent: RAG와 Context 7의 차이를 표로 비교
- notes status: `ready`

### S041. Memory: 세션을 넘어서는 기억
- file: `docs/03-html/slides/slide-041.html`
- slide type: `table`
- layout: `wide`
- shell: `evidence-table-shell`
- source section: `04`
- source paragraph block: `04-09`
- key claim: 대화창을 기억 저장소로 착각하지 않는다
- notes intent: 외부 artifact map과 memory claim
- notes status: `ready`

### S042. Stable Prefix와 Variable Suffix
- file: `docs/03-html/slides/slide-042.html`
- slide type: `comparison`
- layout: `split`
- shell: `split-compare-shell`
- source section: `04`
- source paragraph block: `04-10`
- key claim: 잘 쓰는 것 못지않게 안 바꾸는 것도 능력
- notes intent: prefix/suffix diagram
- notes status: `ready`

### S043. 하네스는 환경 그 자체다
- file: `docs/03-html/slides/slide-043.html`
- slide type: `process`
- layout: `wide`
- shell: `process-flow-shell`
- source section: `04`
- source paragraph block: `04-11`
- key claim: 필요한 파일, 필요한 도구, 필요한 규칙
- notes intent: chapter 04 closing statement
- notes status: `ready`

### S044. 이렇게 하면 망한다
- file: `docs/03-html/slides/slide-044.html`
- slide type: `section`
- layout: `centered`
- shell: `section-divider-shell`
- source section: `05`
- source paragraph block: `05-00`
- key claim: 한계와 실패 패턴
- notes intent: chapter 05 opener
- notes status: `ready`

### S045. 오류의 나비효과
- file: `docs/03-html/slides/slide-045.html`
- slide type: `table`
- layout: `wide`
- shell: `evidence-table-shell`
- source section: `05`
- source paragraph block: `05-01`
- key claim: 작은 오류가 다음 단계로 번진다
- notes intent: 작은 오해가 루프 전체로 누적되는 구조
- notes status: `ready`

### S046. 작업이 길어질 때 특히 위험한 이유
- file: `docs/03-html/slides/slide-046.html`
- slide type: `statement`
- layout: `editorial`
- shell: `statement-editorial-shell`
- source section: `05`
- source paragraph block: `05-02`
- key claim: 작업이 길어질수록 기준이 달라진다
- notes intent: 첫 번째 결과물에서 20 단계 결과물까지의 성공률 하락
- notes status: `ready`

### S047. 컨텍스트가 길수록 항상 좋은 것은 아니다
- file: `docs/03-html/slides/slide-047.html`
- slide type: `comparison`
- layout: `split`
- shell: `split-compare-shell`
- source section: `05`
- source paragraph block: `05-03`
- key claim: 신호 대 잡음비가 핵심이다
- notes intent: 길어진 컨텍스트의 잡음 문제
- notes status: `ready`

### S048. 대표 실패 패턴 네 가지
- file: `docs/03-html/slides/slide-048.html`
- slide type: `statement`
- layout: `editorial`
- shell: `statement-editorial-shell`
- source section: `05`
- source paragraph block: `05-04`
- key claim: 기억과 잡음과 규칙이 하나의 컨텍스트 안에서 썩고 있다
- notes intent: 컨텍스트 실패 모드 네 가지 정리
- notes status: `ready`

### S049. 현실에서 보이는 증상들
- file: `docs/03-html/slides/slide-049.html`
- slide type: `statement`
- layout: `editorial`
- shell: `statement-editorial-shell`
- source section: `05`
- source paragraph block: `05-05`
- key claim: 작은 오류가 누적되면 증상으로 드러난다
- notes intent: 실전 증상 3종을 source-backed 카드로 압축
- notes status: `ready`

### S050. Context Rot: 길어진 기억은 조용히 썩는다
- file: `docs/03-html/slides/slide-050.html`
- slide type: `statement`
- layout: `editorial`
- shell: `statement-editorial-shell`
- source section: `05`
- source paragraph block: `05-06`
- key claim: 길이보다 신호 대 잡음비가 중요하다
- notes intent: Context Rot의 길이 문제와 외부 아티팩트 전환
- notes status: `ready`

### S051. 신뢰는 조율되어야 한다
- file: `docs/03-html/slides/slide-051.html`
- slide type: `statement`
- layout: `editorial`
- shell: `statement-editorial-shell`
- source section: `05`
- source paragraph block: `05-07`
- key claim: 자율성은 작업 비용에 맞춰 조절해야 한다
- notes intent: Calibrated Trust를 비용 구간으로 압축
- notes status: `ready`

### S052. 결정 제어와 확률 제어를 분리하라
- file: `docs/03-html/slides/slide-052.html`
- slide type: `comparison`
- layout: `split`
- shell: `split-compare-shell`
- source section: `05`
- source paragraph block: `05-08`
- key claim: 기계가 확인할 것은 기계에게, 유연한 판단은 AI에게
- notes intent: 결정론적 제어와 확률적 제어의 분리
- notes status: `ready`

### S053. 더 긴 컨텍스트보다 더 좋은 게이트
- file: `docs/03-html/slides/slide-053.html`
- slide type: `statement`
- layout: `editorial`
- shell: `statement-editorial-shell`
- source section: `05`
- source paragraph block: `05-09`
- key claim: 더 긴 컨텍스트보다 더 좋은 게이트
- notes intent: 05장 결론을 source-backed gate principle로 마무리
- notes status: `ready`

### S054. 왜 하나의 에이전트만으로는 부족한가
- file: `docs/03-html/slides/slide-054.html`
- slide type: `table`
- layout: `wide`
- shell: `evidence-table-shell`
- source section: `06`
- source paragraph block: `06-01`
- key claim: 멀티 에이전트는 세 가지 벽을 줄이기 위한 구조
- notes intent: 단일 에이전트의 세 가지 문제를 3-card 구조로 압축
- notes status: `ready`

### S055. 하나의 에이전트 = 하나의 역할
- file: `docs/03-html/slides/slide-055.html`
- slide type: `process`
- layout: `wide`
- shell: `process-flow-shell`
- source section: `06`
- source paragraph block: `06-02`
- key claim: 멀티 에이전트의 본질은 병렬화가 아니라 분해
- notes intent: 다섯 패턴과 Planner/Generator/Evaluator 원칙 연결
- notes status: `ready`

### S056. 1. Sub-Agent: 중간 작업을 격리하는 기본형
- file: `docs/03-html/slides/slide-056.html`
- slide type: `process`
- layout: `wide`
- shell: `process-flow-shell`
- source section: `06`
- source paragraph block: `06-03`
- key claim: 서브 에이전트는 메인 컨텍스트를 지키는 격리 패턴
- notes intent: Main -> Sub-Agent -> summary 흐름과 least privilege 원칙
- notes status: `ready`

### S057. Advisor 전략: 작은 실행자, 큰 자문
- file: `docs/03-html/slides/slide-057.html`
- slide type: `table`
- layout: `wide`
- shell: `evidence-table-shell`
- source section: `06`
- source paragraph block: `06-04`
- key claim: 막히는 순간에만 상위 판단을 빌림
- notes intent: executor와 advisor의 결정 책임 분리
- notes status: `ready`

### S058. 2. Orchestrator: 계획자 하나가 여러 실행자를 배치한다
- file: `docs/03-html/slides/slide-058.html`
- slide type: `process`
- layout: `wide`
- shell: `process-flow-shell`
- source section: `06`
- source paragraph block: `06-05`
- key claim: Orchestrator는 1:N 위임 구조
- notes intent: source numbered flow를 1:N chain으로 구현
- notes status: `ready`

### S059. 3. Parallel: 같은 목표를 평면으로 벌리고 나중에 합친다
- file: `docs/03-html/slides/slide-059.html`
- slide type: `process`
- layout: `wide`
- shell: `process-flow-shell`
- source section: `06`
- source paragraph block: `06-06`
- key claim: 좋은 병렬은 서로를 더럽히지 않는 구조
- notes intent: 독립 lane과 merge 조건을 source 예시로 압축
- notes status: `ready`

### S060. 4. GAN-Style: 생성자와 평가자를 분리한다
- file: `docs/03-html/slides/slide-060.html`
- slide type: `process`
- layout: `wide`
- shell: `process-flow-shell`
- source section: `06`
- source paragraph block: `06-07`
- key claim: 생성과 평가는 같은 손에 묶지 않음
- notes intent: Planner/Generator/Evaluator loop
- notes status: `ready`

### S061. 5. Agent Teams: 양방향 대화가 가능한 팀을 만든다
- file: `docs/03-html/slides/slide-061.html`
- slide type: `process`
- layout: `wide`
- shell: `process-flow-shell`
- source section: `06`
- source paragraph block: `06-08`
- key claim: Agent Teams는 함께 토론하고 합의하는 구조
- notes intent: team graph reference를 role cards로 재구성
- notes status: `ready`

### S062. Sub-Agent와 Agent Team은 다르다
- file: `docs/03-html/slides/slide-062.html`
- slide type: `table`
- layout: `wide`
- shell: `evidence-table-shell`
- source section: `06`
- source paragraph block: `06-09`
- key claim: 단순한 심부름은 Sub-Agent, 양방향 토론은 Agent Team
- notes intent: source table을 그대로 비교 표로 구성
- notes status: `ready`

### S063. 설계 원칙: 패턴보다 경계가 중요하다
- file: `docs/03-html/slides/slide-063.html`
- slide type: `table`
- layout: `wide`
- shell: `evidence-table-shell`
- source section: `06`
- source paragraph block: `06-10`
- key claim: 컨텍스트, 역할, 검증을 쪼개는 경계 설계
- notes intent: 다섯 설계 원칙을 source 문구로 카드화
- notes status: `ready`

### S064. 설계 원칙: 패턴보다 경계가 중요하다
- file: `docs/03-html/slides/slide-064.html`
- slide type: `table`
- layout: `wide`
- shell: `evidence-table-shell`
- source section: `06`
- source paragraph block: `06-11`
- key claim: SOLID도 에이전트 중심으로 다시 읽힘
- notes intent: SOLID reinterpretation table
- notes status: `ready`

### S065. 멀티 모델과 멀티 에이전트
- file: `docs/03-html/slides/slide-065.html`
- slide type: `table`
- layout: `wide`
- shell: `evidence-table-shell`
- source section: `06`
- source paragraph block: `06-12`
- key claim: 여러 모델 교차 사용은 독립 평가자 풀에 가까움
- notes intent: 멀티 모델 distinction과 Claude/Codex/Gemini 역할
- notes status: `ready`

### S066. 결론: 더 많은 AI가 아니라 더 좁은 역할의 AI 여럿
- file: `docs/03-html/slides/slide-066.html`
- slide type: `table`
- layout: `wide`
- shell: `evidence-table-shell`
- source section: `06`
- source paragraph block: `06-13`
- key claim: 더 좁은 역할의 AI 여럿을, 더 명확한 경계 안에서 일하게 한다
- notes intent: chapter 06 closing lines
- notes status: `ready`

### S067. 시작하며: 두 가지 막다른 길
- file: `docs/03-html/slides/slide-067.html`
- slide type: `comparison`
- layout: `split`
- shell: `split-compare-shell`
- source section: `07`
- source paragraph block: `07-01`
- key claim: 출발점은 원리를 시스템이 대신 강제하게 만드는 일
- notes intent: 두 dead-end split comparison
- notes status: `ready`

### S068. OMC(Oh My Claude Code)
- file: `docs/03-html/slides/slide-068.html`
- slide type: `process`
- layout: `wide`
- shell: `process-flow-shell`
- source section: `07`
- source paragraph block: `07-02`
- key claim: preset pack이 모드와 검증 루프를 먼저 고정
- notes intent: preset command/routing map without canonical-only claims
- notes status: `ready`

### S069. Plan-Critic-Build
- file: `docs/03-html/slides/slide-069.html`
- slide type: `process`
- layout: `wide`
- shell: `process-flow-shell`
- source section: `07`
- source paragraph block: `07-03`
- key claim: 합의된 뒤에만 실행
- notes intent: Plan/Critic/Build와 Explore/Plan/Code/Commit 연결
- notes status: `ready`

### S070. 필요없는 도구는 덜어내라
- file: `docs/03-html/slides/slide-070.html`
- slide type: `table`
- layout: `wide`
- shell: `evidence-table-shell`
- source section: `07`
- source paragraph block: `07-04`
- key claim: 도구 큐레이션은 취향이 아니라 성능 문제
- notes intent: tool curation과 gate 목록
- notes status: `ready`

### S071. Approval, Auto-accept, Plan Mode
- file: `docs/03-html/slides/slide-071.html`
- slide type: `table`
- layout: `wide`
- shell: `evidence-table-shell`
- source section: `07`
- source paragraph block: `07-05`
- key claim: 위험도에 따라 모드를 나눔
- notes intent: source table exact-mode mapping
- notes status: `ready`

### S072. 반복의 자산화
- file: `docs/03-html/slides/slide-072.html`
- slide type: `process`
- layout: `wide`
- shell: `process-flow-shell`
- source section: `07`
- source paragraph block: `07-06`
- key claim: 반복되는 지침은 시스템 바깥에 있어야 할 지식
- notes intent: /context, /compact, /clear와 Skills/Hooks/Commands/AGENTS mapping
- notes status: `ready`

### S073. Ralph Loop
- file: `docs/03-html/slides/slide-073.html`
- slide type: `process`
- layout: `wide`
- shell: `process-flow-shell`
- source section: `07`
- source paragraph block: `07-07`
- key claim: PROMPT.md 하나를 루프의 중심에 둠
- notes intent: PROMPT.md loop
- notes status: `ready`

### S074. 암묵지를 파일로 뽑아내라
- file: `docs/03-html/slides/slide-074.html`
- slide type: `table`
- layout: `wide`
- shell: `evidence-table-shell`
- source section: `07`
- source paragraph block: `07-08`
- key claim: 암묵지가 파일로 옮겨지는 순간 하네스가 됨
- notes intent: four numbered steps and closing source
- notes status: `ready`

### S075. 한 모델에만 기대지 않는다
- file: `docs/03-html/slides/slide-075.html`
- slide type: `table`
- layout: `wide`
- shell: `evidence-table-shell`
- source section: `07`
- source paragraph block: `07-09`
- key claim: 여러 모델의 응답을 합의, 불일치, 불확실로 나눔
- notes intent: Claude/Codex/Gemini cross-check roles
- notes status: `ready`

### S076. cmux와 Git Worktree
- file: `docs/03-html/slides/slide-076.html`
- slide type: `process`
- layout: `wide`
- shell: `process-flow-shell`
- source section: `07`
- source paragraph block: `07-10`
- key claim: 창과 작업 디렉터리를 나누어 메인 컨텍스트를 보호
- notes intent: four-window workspace map
- notes status: `ready`

### S077. 세션이 아니라 이슈가 상태를 들고 간다
- file: `docs/03-html/slides/slide-077.html`
- slide type: `process`
- layout: `wide`
- shell: `process-flow-shell`
- source section: `07`
- source paragraph block: `07-11`
- key claim: 이슈는 세션보다 오래가는 상태 저장소
- notes intent: issue -> worktree -> session -> PR -> verification chain
- notes status: `ready`

### S078. 첫 주에 바로 세울 수 있는 최소 워크플로우
- file: `docs/03-html/slides/slide-078.html`
- slide type: `table`
- layout: `wide`
- shell: `evidence-table-shell`
- source section: `07`
- source paragraph block: `07-12`
- key claim: 대화창의 기준을 작업 환경의 일부로 만드는 첫 단계
- notes intent: six minimal habits
- notes status: `ready`

### S079. 결론: 실전 워크플로우의 중심은 운영 구조다
- file: `docs/03-html/slides/slide-079.html`
- slide type: `table`
- layout: `wide`
- shell: `evidence-table-shell`
- source section: `07`
- source paragraph block: `07-13`
- key claim: 검증과 흔적 위에 다음 판단을 올리는 운영 구조
- notes intent: chapter 07 closing lines
- notes status: `ready`

### S080. 이 글과 발표가 만들어진 과정
- file: `docs/03-html/slides/slide-080.html`
- slide type: `section`
- layout: `centered`
- shell: `section-divider-shell`
- source section: `08`
- source paragraph block: `08-00`
- key claim: 이 글과 발표가 만들어진 과정
- notes intent: 08장 chapter divider
- notes status: `ready`

### S081. 이 글과 발표가 만들어진 과정
- file: `docs/03-html/slides/slide-081.html`
- slide type: `statement`
- layout: `editorial`
- shell: `statement-editorial-shell`
- source section: `08`
- source paragraph block: `08-01`
- key claim: 코드 한 줄, PPT 한 장도 직접 만들지 않았습니다
- notes intent: 코드/PPT 직접 제작이 아니라 하네스 설계였다는 증거 진입
- notes status: `ready`

### S082. 이 발표를 만든 방법
- file: `docs/03-html/slides/slide-082.html`
- slide type: `process`
- layout: `wide`
- shell: `process-flow-shell`
- source section: `08`
- source paragraph block: `08-02`
- key claim: source → prose → outline → html → pdf
- notes intent: source에서 pdf까지 이어지는 제작 pipeline
- notes status: `ready`

### S083. 재료 1 source 수집
- file: `docs/03-html/slides/slide-083.html`
- slide type: `table`
- layout: `wide`
- shell: `evidence-table-shell`
- source section: `08`
- source paragraph block: `08-03`
- key claim: 불확실한 부분은 억지로 메우지 않았습니다
- notes intent: source 계층과 중요도 분리
- notes status: `ready`

### S084. 재료 2 단일 진실원 만들기
- file: `docs/03-html/slides/slide-084.html`
- slide type: `process`
- layout: `wide`
- shell: `process-flow-shell`
- source section: `08`
- source paragraph block: `08-04`
- key claim: prose는 source of truth
- notes intent: prose를 기준 문장과 판단 기준으로 세운 과정
- notes status: `ready`

### S085. 재료 3- slides-grab, Skill 경계로 박힌 분리
- file: `docs/03-html/slides/slide-085.html`
- slide type: `process`
- layout: `wide`
- shell: `process-flow-shell`
- source section: `08`
- source paragraph block: `08-05`
- key claim: 단계 사이에 사용자 승인을 물리적으로 강제
- notes intent: outline, manifest, slides-grab의 단계 분리와 승인 관문
- notes status: `ready`

### S086. 재료 4 규칙 세우기
- file: `docs/03-html/slides/slide-086.html`
- slide type: `table`
- layout: `wide`
- shell: `evidence-table-shell`
- source section: `08`
- source paragraph block: `08-06`
- key claim: design contract를 먼저 고정
- notes intent: design contract와 validation contract를 한 장에 압축
- notes status: `ready`

### S087. 생성과 검증을 같은 손에 쥐지 않았다
- file: `docs/03-html/slides/slide-087.html`
- slide type: `comparison`
- layout: `split`
- shell: `split-compare-shell`
- source section: `08`
- source paragraph block: `08-07`
- key claim: 생성과 검증을 분리
- notes intent: HTML generation 이후 기계적 검증과 사람 검토 분리
- notes status: `ready`

### S088. 이 발표가 증거
- file: `docs/03-html/slides/slide-088.html`
- slide type: `process`
- layout: `wide`
- shell: `process-flow-shell`
- source section: `08`
- source paragraph block: `08-08`
- key claim: 원하는 것을 글로 작성 → 규칙을 문서로 작성 → 결과를 사람이 검증
- notes intent: 제작 과정 자체가 Harness 방식으로 만들어진 사례
- notes status: `ready`

### S089. 우리가 다음에 해야 할 일
- file: `docs/03-html/slides/slide-089.html`
- slide type: `section`
- layout: `centered`
- shell: `section-divider-shell`
- source section: `09`
- source paragraph block: `09-00`
- key claim: 우리가 다음에 해야 할 일
- notes intent: 09장 chapter divider
- notes status: `ready`

### S090. 시작하며: FOMO 와 피로
- file: `docs/03-html/slides/slide-090.html`
- slide type: `statement`
- layout: `editorial`
- shell: `statement-editorial-shell`
- source section: `09`
- source paragraph block: `09-01`
- key claim: 더 많은 정보를 읽는 일이 아니라 직접 써 보는 일
- notes intent: FOMO와 피로를 직접 써 보기로 연결
- notes status: `ready`

### S091. 증폭되는 경험 - 세 개의 증언
- file: `docs/03-html/slides/slide-091.html`
- slide type: `statement`
- layout: `editorial`
- shell: `statement-editorial-shell`
- source section: `09`
- source paragraph block: `09-02`
- key claim: AI 시대의 경험 - 축소가 아니라 증폭
- notes intent: Page 085 testimony cards and bottom support line
- notes status: `ready`

### S092. 내일부터
- file: `docs/03-html/slides/slide-092.html`
- slide type: `statement`
- layout: `editorial`
- shell: `statement-editorial-shell`
- source section: `09`
- source paragraph block: `09-03`
- key claim: 글로 먼저 · 직접 써보기 · 도구
- notes intent: Page 086 actions and source line
- notes status: `ready`
