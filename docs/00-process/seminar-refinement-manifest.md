# Seminar Refinement Manifest

`docs/02-seminar/prose/`의 live sync 파일이다. 실제 seminar 문서는 `02-seminar`에 두고, 편집 상태 추적은 여기서 관리한다.

초기 스냅샷 날짜: `2026-04-19`

| file | role | gate | current drift | next loop focus |
| --- | --- | --- | --- | --- |
| `prose/00-coding-disappear.md` | 역할 이동의 도입부 | `PASS` | 경미함. 일부 원본 보존 문장이 길지만 도입 흐름은 유지됨 | 후속 장이 추상적으로 흐를 때 기준선으로 사용 |
| `prose/01-stop-fighting-chatbots.md` | 프롬프트 한계에서 Harness 필요성으로 넘기는 장 | `PASS` | 없음. 독자 경험에서 환경 문제로 넘어가는 흐름이 선명함 | 03장이 체감 예시를 반복하지 않도록 경계 기준으로 사용 |
| `prose/02-what-is-harness.md` | Harness 정의와 구성요소 설명 | `REVISE` | 제목과 파일명은 반영됨. 본문 일부는 `환경` 표현과 구성요소 설명이 다소 설명문에 가까움 | 03장 이후 톤이 잡히면 02장 문장 압력을 한 번 더 맞춤 |
| `prose/03-this-is-how-it-fails.md` | 긴 작업과 긴 컨텍스트의 실패 구조 | `REVISE` | 초안 작성 완료. 자연스러운 구어체와 source 용어 사이의 균형은 사용자 리뷰 필요 | 다음 대화에서 제목별 문장 리듬과 04장 handoff를 조정 |
| `prose/04-fix-direction-first.md` | 빠른 생성 전에 방향을 잡는 장 | `PENDING` | 새 구조 기준 원고 미작성 | 03장 확정 뒤 `SDD`, `Plan-Critic-Build`, 제작 사례를 연결 |
| `prose/05-move-deterministic-gates-left.md` | 검증과 권한 경계의 장 | `PENDING` | 새 구조 기준 원고 미작성 | 03장의 실패 구조를 결정론적 게이트로 이어 받음 |
| `prose/06-do-not-give-one-ai-everything.md` | 역할, 컨텍스트, 검증 책임 분리 | `PENDING` | 새 구조 기준 원고 미작성 | 생성자와 평가자 분리, subagent 패턴의 필요성을 정리 |
| `prose/07-practical-harness-as-files-and-commands.md` | 원칙을 파일과 명령어로 고정하는 실전 장 | `PENDING` | 새 구조 기준 원고 미작성 | `AGENTS.md`, `Skills`, `Hooks`, `MCP`, issue/worktree 운영으로 구체화 |
| `prose/08-this-presentation-was-harness.md` | 발표 제작 자체를 Harness 사례로 보여 주는 장 | `PENDING` | 새 구조 기준 원고 미작성 | source에서 prose, outline, HTML, PDF까지 이어지는 제작 사례를 정리 |
| `prose/09-harness-engineer.md` | 개인과 팀의 실천 결론 | `PENDING` | 새 구조 기준 원고 미작성 | 08장 case를 받아 실제 행동 원칙으로 닫음 |

## Update Rule

- 각 file 패스 후 `gate`, `current drift`, `next loop focus`를 즉시 갱신한다.
- `PASS`가 나온 file도 후반부 shell reference로 계속 사용한다.
- 새 구조에 포함되었지만 아직 원고가 없는 file은 `PENDING`으로 둔다.
- 같은 drift가 반복되면 file 문제로만 닫지 말고 `seminar-refinement-plan.md`와 skill prompt 보정 항목으로 올린다.
