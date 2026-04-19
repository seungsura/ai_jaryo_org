# Slide Outline

- status: first-five draft
- canonical prose source: `docs/02-seminar/prose/`
- design contract: `docs/03-html/shared/design.md`
- active manifest: `docs/03-html/manifest.md`
- active theme: `theme-minimal-light`
- note:
  - 이 파일은 HTML 제작 전 승인 게이트입니다.
  - slide 제목, 핵심 주장, source section, visual need가 먼저 정해져야 합니다.

## Section Inventory

| section id | source file | intended slide span | key point | visual need | status |
| --- | --- | --- | --- | --- | --- |
| 00 | `docs/02-seminar/prose/00-overview.md` | `S01-S02` | 발표의 문제의식과 전체 흐름 제시 | none | draft |
| 01 | `docs/02-seminar/prose/01-where-coding-is-going.md` | `S03-S05` | 코딩의 중심이 Harness로 이동하는 흐름 제시 | none | draft |
| 02 | `docs/02-seminar/prose/02-why-claude-code.md` | `S06-S10` | 특정 제품이 아니라 도구 경쟁이 Harness로 수렴하는 흐름 제시 | none | draft |
| 03 | `docs/02-seminar/prose/03-ai-era-methodology.md` | TBD | TBD | TBD | pending |
| 04 | `docs/02-seminar/prose/04-harness-and-context-engineering.md` | TBD | TBD | TBD | pending |
| 05 | `docs/02-seminar/prose/05-limitations-and-failure-patterns.md` | TBD | TBD | TBD | pending |
| 06 | `docs/02-seminar/prose/06-multi-agent-patterns.md` | TBD | TBD | TBD | pending |
| 07 | `docs/02-seminar/prose/07-practical-workflow-and-tooling.md` | TBD | TBD | TBD | pending |
| 08 | `docs/02-seminar/prose/08-how-this-presentation-was-made.md` | TBD | TBD | TBD | pending |
| 09 | `docs/02-seminar/prose/09-what-we-should-do-next.md` | TBD | TBD | TBD | pending |
| 90 | `docs/02-seminar/prose/90-appendix-references.md` | TBD | TBD | TBD | pending |

## Slide Planning Template

Use one block per planned slide after the section inventory is reviewed.

```md
### SXX. Slide title
- source section: `docs/02-seminar/prose/XX-...md`
- layout family: TBD
- density: TBD
- reference shell: TBD
- claim: TBD
- supporting points: TBD
- placeholder plan: TBD
- citation or asset need: TBD
- status: pending
```

## Sample Slides

### S01. AI coding 시대, 왜 Harness인가
- source section: `docs/02-seminar/prose/00-overview.md`
- layout family: `title`
- density: `light`
- reference shell: `title-hero-shell`
- theme: `theme-minimal-light`
- claim: 이 발표는 특정 제품 소개가 아니라 AI coding 시대의 Harness 중심 개발론을 설명한다
- supporting points:
  - 구조와 운영의 문제
- placeholder plan:
  - title: cover title
  - lead: cover subtitle
  - body: none
  - footer-left / footer-right: `Harness 잘 사용하기` / page number
- citation or asset need: none
- status: draft

### S02. 전체 세미나 전개 구조
- source section: `docs/02-seminar/prose/00-overview.md`
- layout family: `agenda`
- density: `medium`
- reference shell: `agenda-list-shell`
- theme: `theme-minimal-light`
- claim: 발표는 흐름 파악부터 실제 적용까지 다섯 단계 구조로 읽힌다
- supporting points:
  - 코딩의 중심 이동
  - 왜 Harness인가
  - 어떻게 운영할 것인가
  - workflow와 사례
  - 지금 무엇부터
- placeholder plan:
  - title: agenda title
  - body: five-part agenda list
  - footer-left / footer-right: `Harness 잘 사용하기` / page number
- citation or asset need: none
- status: draft

### S03. 코딩의 중심은 어디로 이동하는가
- source section: `docs/02-seminar/prose/01-where-coding-is-going.md`
- layout family: `section`
- density: `light`
- reference shell: `section-divider-shell`
- theme: `theme-minimal-light`
- claim: 첫 챕터는 코딩의 중심 이동을 설명한다
- supporting points:
  - Prompt
  - Context
  - Harness
- placeholder plan:
  - title: chapter question
  - body: Prompt / Context / Harness keyword line
  - chapter marker: `CHAPTER 01`
  - footer-left / footer-right: `Harness 잘 사용하기` / page number
- citation or asset need: none
- status: draft

### S04. 코딩 중심의 3단계 이동
- source section: `docs/02-seminar/prose/01-where-coding-is-going.md`
- layout family: `content`
- density: `medium`
- reference shell: `content-three-step-shell`
- chapter: `CHAPTER 01`
 - theme: `theme-minimal-light`
- claim: 코딩의 중심은 Prompt에서 Context를 거쳐 Harness로 이동하고 있다
- supporting points:
  - Prompt | 무엇을 말할지
  - Context | 무엇을 보여 줄지
  - Harness | 어떻게 운영할지
  - 도구 · 권한 · 검증 · 상태
- placeholder plan:
  - chapter: fixed top-band label
  - title: fixed top-band title, no wrap
  - lead: one-sentence progression line
  - body: three-step progression board
  - footer-left / footer-right: `Harness 잘 사용하기` / page number
- citation or asset need: source note only
- status: draft

### S05. 타이핑에서 설계와 검증으로
- source section: `docs/02-seminar/prose/01-where-coding-is-going.md`
- layout family: `content`
- density: `medium`
- reference shell: `content-three-card-shell`
- chapter: `CHAPTER 01`
 - theme: `theme-minimal-light`
- claim: 직접 타이핑의 비중은 줄고, 설계와 검증의 비중은 커진다
- supporting points:
  - 타이핑 감소 | 직접 작성 축소
  - 설계 증가 | 문맥 · 규칙 · 기준
  - 검증 강화 | 결과 확인
- placeholder plan:
  - chapter: fixed top-band label
  - title: fixed top-band title, no wrap
  - lead: role-shift framing line
  - body: three-part role-shift board
  - footer-left / footer-right: `Harness 잘 사용하기` / page number
- citation or asset need: source note only
- status: draft

### S06. 왜 Claude Code인가, 왜 결국 Harness인가
- source section: `docs/02-seminar/prose/02-why-claude-code.md`
- layout family: `section`
- density: `light`
- reference shell: `section-divider-shell`
- theme: `theme-minimal-light`
- claim: 이 챕터는 특정 제품 리뷰가 아니라 도구 경쟁이 결국 Harness로 수렴하는 흐름을 본다
- supporting points:
  - 단일 제품이 아닌 흐름 읽기
  - Claude Code는 대표 사례
  - 핵심 경쟁 축은 Harness
- placeholder plan:
  - title: chapter question
  - body: 제품 / 흐름 / Harness keyword line
  - chapter marker: `CHAPTER 02`
  - footer-left / footer-right: `Harness 잘 사용하기` / page number
- citation or asset need: none
- status: draft

### S07. 도구는 달라도 방향은 같다
- source section: `docs/02-seminar/prose/02-why-claude-code.md`
- layout family: `content`
- density: `medium`
- reference shell: `content-three-card-shell`
- chapter: `CHAPTER 02`
- theme: `theme-minimal-light`
- claim: 모든 modern coding tool은 결국 더 두꺼운 Harness를 요구하는 방향으로 수렴한다
- supporting points:
  - 출발점의 차이 | IDE · terminal · chat
  - 요구의 확장 | Context · tool use · permission · verification
  - 경쟁 축 이동 | 모델보다 Harness 구조
- placeholder plan:
  - chapter: fixed top-band label
  - title: fixed top-band title, no wrap
  - lead: one-sentence framing line
  - body: three-card comparison board
  - footer-left / footer-right: `Harness 잘 사용하기` / page number
- citation or asset need: source note only
- status: draft

### S08. 코딩 도구 진화의 3단계
- source section: `docs/02-seminar/prose/02-why-claude-code.md`
- layout family: `content`
- density: `medium`
- reference shell: `content-three-step-shell`
- chapter: `CHAPTER 02`
- theme: `theme-minimal-light`
- claim: GitHub Copilot 이후의 도구 진화는 Prompt, Context, Harness의 세 단계로 읽을 수 있다
- supporting points:
  - GitHub Copilot | Prompt 중심
  - Cursor | Context 중심
  - Claude Code | Harness 중심
- placeholder plan:
  - chapter: fixed top-band label
  - title: fixed top-band title, no wrap
  - lead: one-sentence progression line
  - body: three-step progression board
  - footer-left / footer-right: `Harness 잘 사용하기` / page number
- citation or asset need: source note only
- status: draft

### S09. 에이전트 루프와 Harness
- source section: `docs/02-seminar/prose/02-why-claude-code.md`
- layout family: `content`
- density: `medium`
- reference shell: `content-three-step-shell`
- chapter: `CHAPTER 02`
- theme: `theme-minimal-light`
- claim: agent loop가 시작되면 핵심은 답변 품질보다 루프를 어떤 구조로 운영하는가로 이동한다
- supporting points:
  - Gather Context | 읽을 범위 결정
  - Take Action | 수정과 실행 통제
  - Verify Work | 실패 확산 차단
- placeholder plan:
  - chapter: fixed top-band label
  - title: fixed top-band title, no wrap
  - lead: one-sentence progression line
  - body: three-step progression board
  - footer-left / footer-right: `Harness 잘 사용하기` / page number
- citation or asset need: source note only
- status: draft

### S10. 산업 전체의 구조적 수렴
- source section: `docs/02-seminar/prose/02-why-claude-code.md`
- layout family: `content`
- density: `medium`
- reference shell: `content-three-card-shell`
- chapter: `CHAPTER 02`
- theme: `theme-minimal-light`
- claim: Claude Code, Codex, OpenCode는 서로 다른 진영에서도 같은 Harness 방향으로 수렴하고 있음을 보여 준다
- supporting points:
  - Claude Code | workflow layers를 드러낸다
  - Codex | agent-first workspace로 확장된다
  - OpenCode | planner · subagent · permission 경계를 둔다
- placeholder plan:
  - chapter: fixed top-band label
  - title: fixed top-band title, no wrap
  - lead: one-sentence framing line
  - body: three-card comparison board
  - footer-left / footer-right: `Harness 잘 사용하기` / page number
- citation or asset need: source note only
- status: draft
