# Claude Code Mastery Playbook 세미나 연결 맵

이 문서는 루트 supplemental markdown source인 `claude-code-mastery-playbook.md`를 현재 `docs/02-seminar/prose/` 구조에 편입할 때 사용하는 canonical source map이다. 세미나 본문과 직접 연결되는 범위는 `02`, `04`, `05`, `06`, `07`, `09`로 한정한다. 여기서 제외한 코스와 페이지는 현 세미나의 직접 source가 아니라 `docs/01-sources/provenance/` inventory용 `reference-only` 범위로 유지한다.

## Seminar-connected map

### Section 02. 왜 Claude Code인가

- Target file: `docs/02-seminar/prose/02-why-claude-code.md`
- Source markdown: `claude-code-mastery-playbook.md`
- Relevant page range or heading cluster:
  - `Page 006`~`Page 008` / `[Course 2: Claude Code 101]`
  - `Page 012`~`Page 014` / `[Course 4: Claude Code in Action]`
- Core claims to preserve:
  - `Claude Code`를 로컬 파일 시스템, 터미널, 전체 코드베이스와 상호작용하는 `agentic coding tool`로 설명하는 정의
  - `Gather Context → Take Action → Verify Results`와 `Explore → Plan → Code → Commit`으로 요약되는 에이전트 작업 루프
  - `Approval`, `Auto-accept`, `Plan Mode`로 자율성과 통제를 함께 설계해야 한다는 관점
  - `Context Window`를 `working memory`로 보고 필요한 정보만 전략적으로 불러와야 한다는 운영 감각
- Boundary note:
  - 이 섹션은 `Claude Code`의 위치와 작동 감각을 설명하는 데만 사용한다. 세부 `MCP` 구현, 클라우드 배포, 교육용 응용 트랙은 여기로 끌어오지 않는다.

### Section 04. Harness와 Context Engineering

- Target file: `docs/02-seminar/prose/04-harness-and-context-engineering.md`
- Source markdown: `claude-code-mastery-playbook.md`
- Relevant page range or heading cluster:
  - `Page 007`~`Page 008` / `CLAUDE.md`, `Subagents`, `Skills`, `MCP`, `Hooks`
  - `Page 012`~`Page 014` / `CLAUDE.md` 계층, `Hooks & SDK`, 대화 제어, 자동화
  - `Page 045`~`Page 047` / `[Course 15: Introduction to agent skills]`
- Core claims to preserve:
  - 항상 로드되는 규칙층으로서의 `CLAUDE.md`, `CLAUDE.local.md`, `~/.claude/CLAUDE.md`
  - `Skills`를 semantic matching으로 필요할 때만 로드되는 `SKILL.md` 기반 자산으로 보는 구분
  - `Hooks`를 `PreToolUse`, `PostToolUse` 같은 결정론적 guardrail로 사용하는 설계
  - 모든 규칙을 `CLAUDE.md` 하나에 밀어 넣지 말고 `Skills`, 참조 문서, 자동화 훅으로 분산하는 `progressive disclosure`
  - `MCP`를 실행 레이어 중 하나로만 위치시키고, 다른 레이어와 동일시하지 않는 구조적 구분
- Boundary note:
  - `MCP`의 SDK, client/server, `Tools`/`Resources`/`Prompts` 구현 디테일은 이 섹션이 아니라 `reference-only` 범위로 남긴다.

### Section 05. 이렇게 하면 망한다: 한계와 실패 패턴

- Target file: `docs/02-seminar/prose/05-limitations-and-failure-patterns.md`
- Source markdown: `claude-code-mastery-playbook.md`
- Relevant page range or heading cluster:
  - `Page 008` / `Claude Code` anti-patterns
  - `Page 017` / `AI Fluency` anti-patterns와 `Diligence`
  - `Page 051`~`Page 053` / `[Course 17: AI Capabilities and Limitations]`
- Core claims to preserve:
  - `Context Bloat`, 권한 우회, 유휴 `MCP` 서버 방치, 비대해진 `CLAUDE.md` 같은 운영 안티 패턴
  - 생성형 AI를 `next token prediction`, 멈춘 지식, `working memory`의 절벽, `steerability` 간극으로 설명하는 기계적 모델
  - `Calibrated Trust`를 기준으로 이름, 날짜, 통계, 인용, `URL` 같은 구체 항목을 우선 검증해야 한다는 원칙
  - 긴 문서는 청크로 나누고, 세션이 썩기 시작하면 요약 후 새 세션으로 옮긴다는 대응 전략
- Boundary note:
  - 이 섹션에서 플레이북은 외부 벤치마크가 아니라 실패 메커니즘을 설명하는 supplemental markdown source로만 사용한다.

### Section 06. 멀티 에이전트 활용

- Target file: `docs/02-seminar/prose/06-multi-agent-patterns.md`
- Source markdown: `claude-code-mastery-playbook.md`
- Relevant page range or heading cluster:
  - `Page 007` / `Subagents`의 기본 개념
  - `Page 046` / `Skills`와 `Subagents`의 연결 규칙
  - `Page 048`~`Page 050` / `[Course 16: Introduction to subagents]`
- Core claims to preserve:
  - `Subagent`의 핵심 가치를 역할 이름이 아니라 `isolated context`와 요약 반환 구조에 두는 관점
  - `Description`, 모델 선택, `proactively` 같은 호출 조건이 위임 품질을 좌우한다는 점
  - `Summary`, `Critical Issues`, `Recommendations`처럼 정지 지점이 분명한 출력 계약
  - 조사에는 읽기 전용, 리뷰에는 최소 셸, 수정에는 쓰기 권한만 주는 `least privilege`
  - “전문가라고 주장만 하는 에이전트”, 맥락 손실이 큰 순차 파이프라인, 로그를 숨기는 test runner를 anti-pattern으로 보는 판단
- Boundary note:
  - 이 섹션은 제품 사용법보다 역할 분리, 권한 설계, 출력 형식 설계라는 구조 원칙만 회수한다.

### Section 07. 실전 워크플로우와 도구 세팅

- Target file: `docs/02-seminar/prose/07-practical-workflow-and-tooling.md`
- Source markdown: `claude-code-mastery-playbook.md`
- Relevant page range or heading cluster:
  - `Page 006`~`Page 008` / 실행 모드, 컨텍스트 명령, 커스터마이징
  - `Page 012`~`Page 014` / 대화 제어, `Planning Mode`, `Thinking Mode`, `Custom Commands`, `Hooks`
  - `Page 046`~`Page 047` / 반복 작업의 `Skills` 자산화와 팀 배포
- Core claims to preserve:
  - `Approval`, `Auto-accept`, `Plan Mode`를 작업 위험도에 맞춰 운영하는 실전 hygiene
  - `/context`, `/compact`, `/clear` 같은 컨텍스트 관리 명령을 운영 습관으로 다루는 방식
  - 구현 전 계획 검토, `success criteria` 명시, 리뷰 후 반영으로 이어지는 단계적 workflow
  - 사용하지 않는 `MCP` 서버와 도구를 끄고 필요한 것만 남기는 tool curation
  - `Custom Commands`, `Hooks`, 팀 단위 `GitHub` 연동을 통해 반복 작업을 시스템으로 고정하는 사고방식
- Boundary note:
  - `Playwright`나 `MCP` 추가 예시는 workflow 보강 사례로만 남긴다. 프로토콜 자체의 상세 설명은 다른 reference 범위에서 관리한다.

### Section 09. AI 시대, 우리는 어떻게 해야 하나

- Target file: `docs/02-seminar/prose/09-what-we-should-do-next.md`
- Source markdown: `claude-code-mastery-playbook.md`
- Relevant page range or heading cluster:
  - `Page 003`~`Page 004` / `[Course 1: Claude 101]`의 `Thought Partner`, `4D`, `Delegation-Diligence Loop`, iterative mindset
  - `Page 015`~`Page 017` / `[Course 5: AI Fluency: Framework & Foundations]`
- Core claims to preserve:
  - AI를 만능 자동화 도구보다 `Thought Partner`로 보고, 인간이 위임 범위와 판단 책임을 유지해야 한다는 framing
  - `Delegation`, `Description`, `Discernment`, `Diligence`를 인간 책임의 핵심 프레임으로 정리하는 방식
  - iterative loop, `fact-checking`, 투명성, 배포 책임을 실전 태도로 묶는 관점
  - 성공적인 협업의 핵심을 모델 이름보다 인간의 설명력과 판별력에 둔다는 메시지
- Boundary note:
  - 교육자, 학생, 비영리용 `4D` 변주들은 같은 어휘를 쓰더라도 audience-specific track이므로 이 섹션의 직접 source로 올리지 않는다.

## Reference-only ranges

### Cowork

- Relevant page range or heading cluster:
  - `Page 009`~`Page 011` / `[Course 3: Introduction to Claude Cowork]`
- Reference-only 판단:
  - `Cowork`는 세미나의 현재 `00`~`09` 구조 안에서 직접 대응되는 장이 없다.
  - 협업형 파일 생성, `Projects`, `Scheduled Tasks` 같은 기능은 흥미롭지만 현재 세미나 narrative를 넓히는 대신 별도 inventory 항목으로 남기는 편이 정확하다.

### API와 MCP detail

- Relevant page range or heading cluster:
  - `Page 018`~`Page 023` / `[Course 6: Building with the Claude API]`, `[Course 7: Introduction to Model Context Protocol]`
  - `Page 030`~`Page 032` / `[Course 10: Model Context Protocol: Advanced Topics]`
- Reference-only 판단:
  - 이 범위는 `stateless` API, `tool_use` loop, `RAG`, `MCP` SDK, `Roots`, transport, sampling 같은 구현 디테일이 중심이다.
  - 현 세미나에서는 `MCP`를 하네스 레이어 중 하나로 소개하는 수준이면 충분하므로, 프로토콜과 SDK 설명은 reference 문서로만 유지한다.

### Bedrock와 Vertex

- Relevant page range or heading cluster:
  - `Page 033`~`Page 035` / `[Course 11: Claude with Amazon Bedrock]`
  - `Page 036`~`Page 038` / `[Course 12: Claude with Google Cloud's Vertex AI]`
- Reference-only 판단:
  - 두 범위는 클라우드별 배포, 평가, `RAG`, `tool_use` 운영을 다루는 플랫폼 트랙이다.
  - 현재 세미나는 특정 cloud vendor 도입 가이드가 아니므로, 이 범위는 inventory용 참고 자료로만 남긴다.

### Education, Student, Nonprofit tracks

- Relevant page range or heading cluster:
  - `Page 024`~`Page 026` / `[Course 8: AI Fluency for educators]`
  - `Page 027`~`Page 029` / `[Course 9: AI Fluency for students]`
  - `Page 039`~`Page 041` / `[Course 13: Teaching AI Fluency]`
  - `Page 042`~`Page 044` / `[Course 14: AI Fluency for nonprofits]`
- Reference-only 판단:
  - 이 범위는 `4D` 프레임워크를 교육자, 학생, 비영리 조직에 맞게 재서술한 audience-specific track이다.
  - 현재 세미나의 핵심은 개발자와 AI 에이전트 운영 구조이므로, 이 범위는 직접 편입보다 비교 참조용 보조 자료로 두는 편이 맞다.

## Canonical boundary rules

- `Course 5`의 `4D` 프레임워크는 `Section 09`의 primary source로 사용하고, `Course 1`은 framing support로만 사용한다.
- `MCP`는 `Section 04`에서 레이어 구분을 설명하는 수준으로만 사용한다. SDK와 protocol detail은 `reference-only`로 고정한다.
- `Course 15`는 `Skills`를 설명할 때 `Section 04`의 primary support이고, 반복 작업의 표준화라는 맥락에서만 `Section 07`의 secondary support로 사용한다.
- `Course 16`은 `Section 06`의 primary source다. 같은 페이지의 product-specific usage tip보다 컨텍스트 격리, 최소 권한, 출력 계약 원칙을 우선 보존한다.

## 확인이 필요한 모호성

- `Page 013`에는 일부 command와 문장이 OCR 파손 상태로 남아 있다. 따라서 exact command spelling은 canonical source로 승격하지 않는다.
- `Page 053`의 마지막 문단은 끝부분이 잘려 있다. 다만 `Calibrated Trust`, 긴 대화 표류, 핵심 컨텍스트 재공급이라는 이미 회수 가능한 요지만 사용한다.
- `Course 1`과 `Course 5`는 모두 `4D`를 다루므로 중복이 있다. 이 문서에서는 `Course 5`를 실질적 primary source로, `Course 1`을 개념 framing용 보조 source로 고정한다.
