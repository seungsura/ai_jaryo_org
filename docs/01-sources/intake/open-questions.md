# Open Questions

현재 저장소의 markdown 기준으로 사실관계가 미해결인 항목은 없습니다. 다만 이번 prose 검증 패스에서 남은 편집 판단 2건은 아래에 열어 둡니다.

## Open Editorial Audit

## Q09. Sections 06-07 example density
- 대상 섹션: `docs/02-seminar/prose/06-multi-agent-patterns.md`, `docs/02-seminar/prose/07-practical-workflow-and-tooling.md`
- 부족한 내용: 패턴과 워크플로우의 원리는 정리돼 있지만, 외부 청중 기준으로는 각 패턴을 같은 시나리오 위에서 비교하는 공통 예시가 하나 더 있으면 이해 속도가 빨라집니다.
- 왜 보류했는가: 현재 local markdown은 패턴 taxonomy와 내부 사례를 충분히 주지만, 다섯 패턴을 같은 문제 위에 나란히 얹는 단일 예시는 제공하지 않습니다.
- 사용자 확인 필요: 다음 편집 패스에서 다섯 패턴을 하나의 공통 시나리오로 다시 설명하는 보강 단락을 추가할지 확인이 필요합니다.

## Q10. Public-facing handling of internal identifiers
- 대상 섹션: `docs/02-seminar/prose/07-practical-workflow-and-tooling.md`, `docs/02-seminar/prose/90-appendix-references.md`
- 부족한 내용: `OMC`, `Linear(PIMS)`, 내부 확인 정보 같은 식별자는 provenance에는 도움이 되지만, 외부 청중에게는 배경 설명이 부족하면 몰입을 끊을 수 있습니다.
- 왜 보류했는가: local markdown은 이 식별자들의 존재와 역할을 보여 주지만, 공개 세미나 버전에서 그대로 유지할지 일반화할지에 대한 편집 방침은 따로 명시하지 않습니다.
- 사용자 확인 필요: 공개 발표 기준으로는 내부 식별자를 유지할지, 더 일반적인 설명으로 치환할지 결정이 필요합니다.

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
