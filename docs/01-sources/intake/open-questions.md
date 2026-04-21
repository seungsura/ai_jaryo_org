# Open Questions

현재 저장소의 markdown 기준으로 사실관계가 미해결인 항목은 없습니다. 다만 `docs/02-seminar/harness-rebuilt-md` 시각물 asset 링크화 패스에서는 direct asset가 없는 합성 시각물 backlog가 열려 있습니다.

## Open Editorial Audit

### Q11. `harness-rebuilt-md` synthetic visual asset backlog
- 상태: open
- 대상 섹션: `docs/02-seminar/harness-rebuilt-md/00-overview.md`, `docs/02-seminar/harness-rebuilt-md/01-코딩은 사라지는가.md`, `docs/02-seminar/harness-rebuilt-md/02-왜 Claude Code인가, 그리고 왜 Harness 인가.md`, `docs/02-seminar/harness-rebuilt-md/04-프롬프트를 넘어서: 에이전트를 움직이는 기술, Harness.md`, `docs/02-seminar/harness-rebuilt-md/07-실전 워크플로우와 도구 세팅.md`, `docs/02-seminar/harness-rebuilt-md/08-이 글과 발표가 만들어진 과정.md`, `docs/02-seminar/harness-rebuilt-md/09-우리가 다음에 해야 할 일.md`
- 확인 내용: direct asset가 있는 17개 시각물에는 footnote link를 추가했고, 아래 9개 묶음은 exact asset가 없는 합성 시각물로 backlog에 남겼습니다.
- backlog: `00-v01` — overview 목차 표. direct asset 없음.
- backlog: `01-v01`~`01-v09` — 기계어/어셈블리/C/Java/Python/자연어 prompt 코드 예시 블록. direct asset 없음.
- backlog: `02-v03` — Cursor 비교표. candidate: [06-cursor-ai-code-editor-architecture.png](../../../assets/evolution-of-ai-agentic-patterns/06-cursor-ai-code-editor-architecture.png)
- backlog: `04-v06` — `RAG vs Context Hub` 비교표. direct asset 없음.
- backlog: `04-v07` — `LLM-as-OS` 표. source markdown 표 기반 합성 시각물.
- backlog: `07-v01` — 위험도별 `Approval / Auto-accept / Plan Mode` 표. candidate: [page-006.png](../../../assets/claude-code-mastery-playbook/page-006.png), [page-007.png](../../../assets/claude-code-mastery-playbook/page-007.png), [page-012.png](../../../assets/claude-code-mastery-playbook/page-012.png), [page-014.png](../../../assets/claude-code-mastery-playbook/page-014.png)
- backlog: `08-v01` — `source → prose → outline → html → pdf → notes` 경로 표. candidate: [page-080.png](../../../assets/claude-code-seminar-kakao/page-080.png), [page-081.png](../../../assets/claude-code-seminar-kakao/page-081.png)
- backlog: `08-v02` — 사람이 붙든 것 / 에이전트에게 맡긴 것 표. candidate: [page-081.png](../../../assets/claude-code-seminar-kakao/page-081.png), [page-082.png](../../../assets/claude-code-seminar-kakao/page-082.png)
- backlog: `09-v01` — Kent Beck / Simon Willison / Martin Fowler 표. provenance 정리표라 direct asset 없음.
- 추가 사용자 확인: 합성 시각물에도 candidate asset 연결을 허용할지, 아니면 direct asset가 새로 정리될 때까지 backlog로 유지할지 후속 대화에서 닫습니다.

## Closed Audit Records

## Q09. Sections 06-07 example density
- 상태: closed
- 대상 섹션: `docs/02-seminar/prose/06-multi-agent-patterns.md`, `docs/02-seminar/prose/07-practical-workflow-and-tooling.md`
- 확인 내용: `06`장을 저장소 변경이라는 하나의 공통 시나리오 위에서 다섯 패턴 비교로 다시 묶었고, `07`장은 그 비교를 `Write / Select / Compress / Isolate`, command, gate, state 외부화, worktree, issue 운영으로 이어 받도록 재구성했습니다.
- 왜 닫았는가: 패턴과 워크플로우가 같은 문제를 서로 다른 높이에서 다룬다는 비교 spine이 본문 안에 들어와, 추가 사용자 확인 없이도 이해 속도 저하 문제를 해소했습니다.
- 추가 사용자 확인: 없음

## Q10. Public-facing handling of internal identifiers
- 상태: closed
- 대상 섹션: `docs/02-seminar/prose/07-practical-workflow-and-tooling.md`, `docs/02-seminar/prose/90-appendix-references.md`
- 확인 내용: 공개 글 기준으로는 `OMC`는 public preset pack 예시로 설명을 덧붙여 유지하고, `Linear(PIMS)`와 특정 내부 팀 식별자는 더 일반적인 표현으로 치환했습니다. provenance 구분은 유지하되, 내부 식별자가 본문 몰입을 끊지 않도록 노출 강도를 낮췄습니다.
- 왜 닫았는가: 사용자가 seminar 전체 문서를 외부 공개 가능한 기술 블로그 수준으로 다듬는 편집 패스를 요청했으므로, 공개 독자 기준의 일반화 편집을 적용해 질문을 닫았습니다.
- 추가 사용자 확인: 없음

## Q01. OMC page 071 literal uncertainty 3건
- 상태: closed
- 대상 섹션: `docs/02-seminar/prose/07-practical-workflow-and-tooling.md`
- 확인 내용: Section 7 literal은 authoritative 기준으로 `Plan-Critic-Build` command를 `/ralplan`, 검증 루프 command를 `/ultraqa`, 모델 라우팅 수치를 `30~50%↓`로 유지합니다.
- 왜 닫았는가: 더 이상 본문에 OCR 파손 추정치를 남기지 않고, 사용자 제공 authoritative 값으로 Section 7 본문과 provenance를 일치시켰습니다.
- 추가 사용자 확인: 없음

## Q06. S02 canonical reference deliverable audit
- 상태: closed
- 대상 섹션: `docs/01-sources/intake/source-inbox.md`, `docs/01-sources/maps/claude-code-mastery-playbook-to-seminar.md`, `docs/02-seminar/prose/02-why-claude-code.md`, `docs/02-seminar/prose/04-harness-and-context-engineering.md`, `docs/02-seminar/prose/05-limitations-and-failure-patterns.md`, `docs/02-seminar/prose/06-multi-agent-patterns.md`, `docs/02-seminar/prose/07-practical-workflow-and-tooling.md`, `docs/02-seminar/prose/09-what-we-should-do-next.md`
- 확인 내용: `claude-code-mastery-playbook.md`의 보강 내용은 이미 위 세미나 섹션들에 흡수되어 있고, source-specific canonical reference deliverable은 `docs/01-sources/maps/claude-code-mastery-playbook-to-seminar.md`입니다. `docs/01-sources/maps/seminar-claims-and-sources.md`는 본문 provenance 경계를 기록하는 별도 reference로 유지합니다.
- 왜 닫았는가: 로컬 markdown만으로 세미나 편입 위치와 source-specific reference 문서 경로를 함께 확인할 수 있어 추가 사용자 확인이 필요하지 않습니다.
- 추가 사용자 확인: 없음

## Q07. S03 canonical reference deliverable audit
- 상태: closed
- 대상 섹션: `docs/01-sources/intake/source-inbox.md`, `docs/01-sources/maps/prompt-context-harness-to-seminar.md`, `docs/02-seminar/prose/01-where-coding-is-going.md`, `docs/02-seminar/prose/04-harness-and-context-engineering.md`, `docs/02-seminar/prose/05-limitations-and-failure-patterns.md`, `docs/02-seminar/prose/07-practical-workflow-and-tooling.md`, `docs/02-seminar/prose/09-what-we-should-do-next.md`
- 확인 내용: `prompt-context-harness-1-15.md`의 핵심 논지는 이미 위 세미나 섹션들에 편입되어 있고, source-specific canonical reference deliverable은 `docs/01-sources/maps/prompt-context-harness-to-seminar.md`입니다. `docs/01-sources/maps/seminar-claims-and-sources.md`는 이 source를 supplemental provenance로만 교차 참조합니다.
- 왜 닫았는가: 로컬 markdown만으로 세미나 편입 위치와 source-specific reference 문서 경로를 확인할 수 있어 추가 사용자 확인이 필요하지 않습니다.
- 추가 사용자 확인: 없음

## Q08. S01 provenance closure
- 상태: closed
- 대상 섹션: `docs/01-sources/intake/source-inbox.md`, `docs/02-seminar/prose/02-why-claude-code.md`, `docs/02-seminar/prose/03-ai-era-methodology.md`, `docs/02-seminar/prose/04-harness-and-context-engineering.md`, `docs/02-seminar/prose/05-limitations-and-failure-patterns.md`, `docs/02-seminar/prose/06-multi-agent-patterns.md`, `docs/02-seminar/prose/90-appendix-references.md`, `docs/01-sources/maps/seminar-claims-and-sources.md`
- 확인 내용: `evolution-of-ai-agentic-patterns.md`는 Section 2의 tool genealogy와 `Prompt → Context → Harness` 시대 구분, 그리고 Section 4~6의 harness convergence 논지를 보강하는 공식 supplemental markdown source로 편입했습니다. `docs/01-sources/intake/source-inbox.md` 상태를 `integrated`로 올렸고, appendix와 provenance 문서에도 이 source의 역할을 반영했습니다.
- 왜 닫았는가: local markdown과 공식 web source를 함께 대조해 이 source가 어떤 claim을 보강하는지 문서상으로 명시했으므로 provenance closure 경계가 닫혔습니다.
- 추가 사용자 확인: 없음
