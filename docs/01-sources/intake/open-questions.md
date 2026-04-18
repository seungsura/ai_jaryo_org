# Open Questions

현재 저장소의 markdown 기준으로 사실관계가 미해결인 항목은 없습니다. 이번 편집 패스 기준으로 열려 있던 provenance closure audit도 닫혔습니다.

## Open Editorial Audit

- 없음

## Closed Audit Records

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
