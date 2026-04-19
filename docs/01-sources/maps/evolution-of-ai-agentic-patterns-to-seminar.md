# AI 에이전틱 패턴 진화 세미나 연결 맵

이 문서는 `evolution-of-ai-agentic-patterns.md`를 현재 `docs/02-seminar/prose/` 구조에 편입할 때 사용하는 canonical source map이다. 이 source의 직접 연결 범위는 `02`, `04`, `05`, `06`, `07`, `90`으로 유지한다. 핵심 역할은 `GitHub Copilot` 이후의 genealogy, `Prompt → Context → Harness` 시대 구분, 컨텍스트 격리와 `Observability`, 보안 경계 프레임을 세미나 본문에 어떤 밀도로 반영할지 정하는 데 있다.

## Seminar-connected map

### Section 02. 왜 Claude Code인가, 그리고 왜 코딩 도구는 결국 Harness로 수렴하는가

- Target file: `docs/02-seminar/prose/02-why-claude-code.md`
- Source markdown: `evolution-of-ai-agentic-patterns.md`
- Relevant heading cluster:
  - `세 시대 타임라인`
  - `GitHub Copilot이 문을 열다`
  - `Copilot Chat`, `Cursor`, `Harness Engineering` 시대
- Core claims to preserve:
  - `Prompt → Context → Harness`라는 세 시대 구분
  - `GitHub Copilot`에서 `Copilot Chat`, `Cursor`, `Claude Code`, `Codex`로 이어지는 form factor 변화
  - 도구 경쟁의 핵심이 단일 모델보다 더 두꺼운 실행 환경으로 이동했다는 convergence framing
- Boundary note:
  - growth 수치, valuation, adoption 속도 같은 외부 사례는 genealogy의 배경으로만 읽고 본문 핵심 claim으로 과도하게 끌어오지 않는다.

### Section 04. Harness와 Context Engineering

- Target file: `docs/02-seminar/prose/04-harness-and-context-engineering.md`
- Source markdown: `evolution-of-ai-agentic-patterns.md`
- Relevant heading cluster:
  - `그래도 부족했다 — 컨텍스트의 벽`
  - `하네스 엔지니어링의 시대`
  - `에이전트 = 모델 + 하네스`
- Core claims to preserve:
  - `Context`만으로는 장기 실행, 에러 복구, 보안, 비용 제어를 설명할 수 없다는 점
  - `Agent = Model + Harness`라는 정의
  - 하네스를 모델 바깥의 운영 시스템으로 이해해야 한다는 framing
- Boundary note:
  - benchmark나 비용 수치보다 개념 전환과 구조 원리를 우선 보존한다.

### Section 05. 이렇게 하면 망한다: 한계와 실패 패턴

- Target file: `docs/02-seminar/prose/05-limitations-and-failure-patterns.md`
- Source markdown: `evolution-of-ai-agentic-patterns.md`
- Relevant heading cluster:
  - `Write / Select / Compress / Isolate`
  - `컨텍스트의 벽`
  - `Lethal Trifecta와 2인 규칙`
- Core claims to preserve:
  - long context 문제를 길이보다 `signal-to-noise`와 운영 구조의 실패로 읽는 관점
  - 필요한 것만 선택하고 요약하고 격리해야 한다는 context hygiene 원리
  - 외부 입력, 민감 정보, 상태 변경이 한곳에 모일 때 위험이 커진다는 보안 경계 프레임
- Boundary note:
  - 보안 예시는 일반 원리 설명용으로만 사용하고, 세미나 본문을 별도 security deep dive로 넓히지 않는다.

### Section 06. 멀티 에이전트 활용

- Target file: `docs/02-seminar/prose/06-multi-agent-patterns.md`
- Source markdown: `evolution-of-ai-agentic-patterns.md`
- Relevant heading cluster:
  - `Isolate`
  - `서브에이전트(Sub-agent)`
  - `Anthropic의 3-에이전트 아키텍처`
- Core claims to preserve:
  - 멀티 에이전트의 출발점은 병렬성보다 컨텍스트 격리라는 점
  - 서브 에이전트에는 필요한 파일과 맥락만 넘기는 `least privilege`의 컨텍스트 버전
  - `planner`, `generator`, `evaluator`처럼 생성과 평가를 분리해야 자기평가 착시를 줄일 수 있다는 점
- Boundary note:
  - 프레임워크 역사나 구현 디테일보다 역할 분리 원칙과 handoff 구조를 우선 회수한다.

### Section 07. 실전 워크플로우와 도구 세팅

- Target file: `docs/02-seminar/prose/07-practical-workflow-and-tooling.md`
- Source markdown: `evolution-of-ai-agentic-patterns.md`
- Relevant heading cluster:
  - `Write / Select / Compress / Isolate`
  - `OpenAI Codex 하네스의 관찰성(observability) 스택`
  - `Ralph 패턴`
- Core claims to preserve:
  - workflow 운영은 무엇을 쓰고, 선택하고, 압축하고, 격리할지 정하는 실무 절차라는 점
  - 검증 루프에는 pass/fail뿐 아니라 로그, 실행 흔적, 대기 상태를 보는 `Observability`가 필요하다는 점
  - 장기 작업은 세션 기억보다 파일 시스템과 외부 아티팩트에 상태를 남겨야 한다는 점
- Boundary note:
  - `Ralph` 같은 사례는 workflow 원리를 보여 주는 보조 사례로만 사용하고, 특정 커뮤니티 도구 사용법으로 확장하지 않는다.

### Section 90. 부록: 출처와 후속 읽기

- Target file: `docs/02-seminar/prose/90-appendix-references.md`
- Source markdown: `evolution-of-ai-agentic-patterns.md`
- Role in appendix:
  - genealogy, harness convergence, context isolation, `Observability`, 보안 경계 프레임을 보강하는 supplemental markdown source로 위치시킨다.
  - `claude-code-seminar-kakao.md`와 달리 narrative spine이 아니라, public source와 세미나 본문 사이를 두껍게 연결하는 conceptual support로 기록한다.

## Reference-only ranges

### MCP, A2A, Context Hub 세부 구현

- Relevant heading cluster:
  - `MCP: 도구 연결의 표준이 되다`
  - `Context Hub: 에이전트의 기억상실증을 치료하다`
- Reference-only 판단:
  - 현재 세미나는 `MCP`와 external knowledge injection의 구현 가이드를 직접 다루지 않는다.
  - 본문에서는 구조적 의미만 회수하고, 세부 아키텍처와 숫자, 구현 디테일은 reference-only로 남긴다.

### 세부 benchmark와 비용 수치

- Relevant heading cluster:
  - `OpenAI Codex 실험`
  - `Anthropic의 3-에이전트 아키텍처`
- Reference-only 판단:
  - 비용, 시간, 속도 배수 같은 수치는 세미나의 구조 논지를 돕는 맥락으로만 유지한다.
  - 본문에서는 수치 그 자체보다 왜 그런 구조가 필요했는지를 우선 보존한다.
