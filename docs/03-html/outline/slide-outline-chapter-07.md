# Chapter 07 Slide Outline: 실전 워크플로우와 도구 세팅

### S15. 실전 워크플로우와 도구 세팅
- source section: `docs/02-seminar/prose/07-practical-workflow-and-tooling.md`
- layout family: `section`
- density: `light`
- reference shell: `section-divider-shell`
- theme: `theme-minimal-light`
- claim: 실전 워크플로우의 핵심은 도구를 늘리는 것이 아니라 운영 구조를 세우는 것이다
- supporting points:
  - Plan-Critic-Build
  - 게이트 설계
  - 세션 격리
- placeholder plan:
  - title: 실전 워크플로우와 도구 세팅
  - body: 구조 / 게이트 / 격리 keyword line
  - chapter marker: `CHAPTER 07`
  - footer-left / footer-right: `Harness 잘 사용하기` / 15
- status: draft

### S16. Plan-Critic-Build 루프
- source section: `docs/02-seminar/prose/07-practical-workflow-and-tooling.md`
- layout family: `content`
- density: `medium`
- reference shell: `content-three-step-shell`
- chapter: `CHAPTER 07`
- theme: `theme-minimal-light`
- claim: 구현 전에 계획을 분리하고 비판하는 과정을 통해 나쁜 전제를 차단한다
- supporting points:
  - Plan | 구현 전 계획 작성
  - Critic | 계획의 빈틈 비판
  - Build | 합의된 뒤에만 실행
- placeholder plan:
  - chapter: CHAPTER 07
  - title: Plan-Critic-Build 루프
  - lead: 에이전트의 실패는 나쁜 코드가 아니라 나쁜 전제에서 시작된다
  - body: three-step progression board (Plan -> Critic -> Build)
  - footer-left / footer-right: `Harness 잘 사용하기` / 16
- status: draft

### S17. 도구보다 게이트를 설계하라
- source section: `docs/02-seminar/prose/07-practical-workflow-and-tooling.md`
- layout family: `content`
- density: `medium`
- reference shell: `content-three-card-shell`
- chapter: `CHAPTER 07`
- theme: `theme-minimal-light`
- claim: 좋은 운영은 도구를 늘리는 기술보다 도구를 덜어내고 게이트를 세우는 기술이다
- supporting points:
  - Tool Curation | 필요한 도구만 정확히 선택
  - Deterministic Gates | 기계적 검증 (Lint, Test)
  - Human-in-the-loop | 위험 작업의 수동 승인
- placeholder plan:
  - chapter: CHAPTER 07
  - title: 도구보다 게이트를 설계하라
  - lead: 기계가 확인할 수 있는 것은 기계가 닫고, AI는 답을 내는 데 집중한다
  - body: three-card role-shift board (Curation / Gates / Approval)
  - footer-left / footer-right: `Harness 잘 사용하기` / 17
- status: draft

### S18. 세션 격리와 상태 관리
- source section: `docs/02-seminar/prose/07-practical-workflow-and-tooling.md`
- layout family: `content`
- density: `medium`
- reference shell: `content-three-card-shell`
- chapter: `CHAPTER 07`
- theme: `theme-minimal-light`
- claim: cmux와 Git Worktree를 통해 세션을 물리적으로 격리하고 이슈 기반으로 상태를 관리한다
- supporting points:
  - Session Isolation | cmux / Worktree 격리
  - Context Control | /compact, /clear 명령
  - Issue-based | 이슈가 세션보다 오래가는 상태 저장소
- placeholder plan:
  - chapter: CHAPTER 07
  - title: 세션 격리와 상태 관리
  - lead: 컨텍스트 드리프트를 막기 위해 물리적 경계와 외부 상태 저장소를 활용한다
  - body: three-card role-shift board (Isolation / Control / Issue)
  - footer-left / footer-right: `Harness 잘 사용하기` / 18
- status: draft
