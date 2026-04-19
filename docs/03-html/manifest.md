# HTML Manifest

- current status: first-ten built
- current source of truth: `docs/02-seminar/prose/`
- approved outline: `docs/03-html/outline/slide-outline.md`
- active design contract: `docs/03-html/shared/design.md`
- active theme: `theme-minimal-light`
- active shared tokens: `docs/03-html/shared/tokens.css`
- active slide set:
  - `docs/03-html/slides/slide-01.html`
  - `docs/03-html/slides/slide-02.html`
  - `docs/03-html/slides/slide-03.html`
  - `docs/03-html/slides/slide-04.html`
  - `docs/03-html/slides/slide-05.html`
  - `docs/03-html/slides/slide-06.html`
  - `docs/03-html/slides/slide-07.html`
  - `docs/03-html/slides/slide-08.html`
  - `docs/03-html/slides/slide-09.html`
  - `docs/03-html/slides/slide-10.html`
- notes:
  - 이 파일은 slide 작업 전에 골격을 만들고, 작업 중 계속 갱신합니다.
  - slide id, source section, layout family, density, html path, 상태 변경이 생기면 즉시 반영합니다.

## Update Rules

- outline이 승인되면 slide id allocation을 먼저 적습니다.
- 새 slide를 만들면 registry에 추가합니다.
- slide order가 바뀌면 order와 section 대응을 함께 수정합니다.
- slide가 draft에서 approved로 바뀌면 status를 갱신합니다.

## Section Registry

| section id | prose source | planned slide ids | status | notes |
| --- | --- | --- | --- | --- |
| 00 | `docs/02-seminar/prose/00-overview.md` | `S01`, `S02` | built | cover and agenda |
| 01 | `docs/02-seminar/prose/01-where-coding-is-going.md` | `S03`, `S04`, `S05` | built | chapter 01 opening set |
| 02 | `docs/02-seminar/prose/02-why-claude-code.md` | `S06`, `S07`, `S08`, `S09`, `S10` | built | why Claude Code and industry-wide Harness convergence |
| 03 | `docs/02-seminar/prose/03-ai-era-methodology.md` | TBD | pending | |
| 04 | `docs/02-seminar/prose/04-harness-and-context-engineering.md` | TBD | pending | |
| 05 | `docs/02-seminar/prose/05-limitations-and-failure-patterns.md` | TBD | pending | |
| 06 | `docs/02-seminar/prose/06-multi-agent-patterns.md` | TBD | pending | |
| 07 | `docs/02-seminar/prose/07-practical-workflow-and-tooling.md` | TBD | pending | |
| 08 | `docs/02-seminar/prose/08-how-this-presentation-was-made.md` | TBD | pending | |
| 09 | `docs/02-seminar/prose/09-what-we-should-do-next.md` | TBD | pending | |
| 90 | `docs/02-seminar/prose/90-appendix-references.md` | TBD | pending | |

## Slide Registry

Populate this table as soon as slide ids are assigned.

| order | slide id | title | layout family | density | reference shell | source section | html path | status | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 01 | `S01` | AI coding 시대, 왜 Harness인가 | `title` | `light` | `title-hero-shell` | `00` | `docs/03-html/slides/slide-01.html` | built | minimal opening cover |
| 02 | `S02` | 전체 세미나 전개 구조 | `agenda` | `medium` | `agenda-list-shell` | `00` | `docs/03-html/slides/slide-02.html` | built | agenda and deck map |
| 03 | `S03` | 코딩의 중심은 어디로 이동하는가 | `section` | `light` | `section-divider-shell` | `01` | `docs/03-html/slides/slide-03.html` | built | chapter divider |
| 04 | `S04` | 코딩 중심의 3단계 이동 | `content` | `medium` | `content-three-step-shell` | `01` | `docs/03-html/slides/slide-04.html` | built | standard content page |
| 05 | `S05` | 타이핑에서 설계와 검증으로 | `content` | `medium` | `content-three-card-shell` | `01` | `docs/03-html/slides/slide-05.html` | built | standard content page |
| 06 | `S06` | 왜 Claude Code인가, 왜 결국 Harness인가 | `section` | `light` | `section-divider-shell` | `02` | `docs/03-html/slides/slide-06.html` | built | chapter 02 divider |
| 07 | `S07` | 도구는 달라도 방향은 같다 | `content` | `medium` | `content-three-card-shell` | `02` | `docs/03-html/slides/slide-07.html` | built | product surfaces converge into Harness needs |
| 08 | `S08` | 코딩 도구 진화의 3단계 | `content` | `medium` | `content-three-step-shell` | `02` | `docs/03-html/slides/slide-08.html` | built | GitHub Copilot to Cursor to Claude Code |
| 09 | `S09` | 에이전트 루프와 Harness | `content` | `medium` | `content-three-step-shell` | `02` | `docs/03-html/slides/slide-09.html` | built | loop structure makes Harness necessary |
| 10 | `S10` | 산업 전체의 구조적 수렴 | `content` | `medium` | `content-three-card-shell` | `02` | `docs/03-html/slides/slide-10.html` | built | Claude Code Codex OpenCode convergence |
