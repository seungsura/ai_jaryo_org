# Seminar Refinement Manifest

`docs/02-seminar/prose/`의 live sync 파일이다. 실제 seminar 문서는 `02-seminar`에 두고, 편집 상태 추적은 여기서 관리한다.

초기 스냅샷 날짜: `2026-04-19`

| file | role | gate | current drift | next loop focus |
| --- | --- | --- | --- | --- |
| `prose/00-코딩은-사라지는가.md` | 역할 이동의 도입부 | `REVISE` | slide-first 형식으로 재작성함. 목적지를 먼저 제시하고, `추상화의 역사` 구간은 이미 만들어 둔 자료를 연속 장면으로 살림. 숫자 사례 3개는 적절하므로 모두 유지하고 역할 이동의 증거로 회수함 | 추상화 역사 자료의 길이, 숫자 slide의 layout family 조정 |
| `prose/01-챗봇과-싸우지-않기.md` | 프롬프트 한계에서 Harness 필요성으로 넘기는 장 | `REVISE` | slide-first 형식으로 재작성함. `AI를 채팅창/챗봇처럼 쓰면서 실무 결과를 기대했다`는 문제를 명시함 | `챗봇처럼 쓰고 에이전트 결과를 기대한다`는 문장을 더 앞당길지 조정 |
| `prose/02-하네스는-무엇인가.md` | Harness 정의와 구성요소 설명 | `REVISE` | slide-first 형식으로 재작성함. loop, Prompt/Context/Harness, Agent=Model+Harness, 구성요소/책임/도구 흐름으로 정렬함 | 정의 장이 너무 교과서처럼 보이지 않는지 사용자 리뷰 |
| `prose/03-이렇게-하면-망한다.md` | 긴 작업과 긴 컨텍스트의 실패 구조 | `REVISE` | slide-first 형식으로 재작성함. 큰 작업을 통째로 맡겼다가 이상한 수정이 누적되는 장면을 루프 실패와 연결함 | 실패 패턴 용어 수와 `AI Slop/Doom Loop/Shadow Agent`의 필요성 조정 |
| `prose/04-먼저-방향을-잡는다.md` | 빠른 생성 전에 방향을 잡는 장 | `REVISE` | slide-first 형식으로 재작성함. 병목 이동, SDD, Plan-Critic-Build, 파일로 남는 방향으로 압축함 | 08장과 겹치는 발표 제작 예시를 더 줄일지 판단 |
| `prose/05-기계가-막을-수-있는-것은-앞에서-막는다.md` | 검증과 권한 경계의 장 | `REVISE` | slide-first 형식으로 재작성함. 검증 없는 사용이 위험하다는 감정과 `Keep Quality Left`를 연결함 | `TDD`와 권한 표의 밀도 조정 |
| `prose/06-하나의-AI에게-다-맡기지-않는다.md` | 역할, 컨텍스트, 검증 책임 분리 | `REVISE` | slide-first 형식으로 재작성함. 병렬화보다 분해, Sub-Agent, Orchestrator, 생성/검증 분리로 정렬함 | `SOLID` 재해석을 남길지 줄일지 사용자 판단 |
| `prose/07-실전-하네스는-파일과-명령어로-남는다.md` | 원칙을 파일과 명령어로 고정하는 실전 장 | `REVISE` | slide-first 형식으로 재작성함. 파일, 명령어, Hook, 이슈, Worktree, 최소 워크플로우로 행동 가능성을 높임 | `Plan-Critic-Build` 반복 설명과 `Ralph Loop` 비중 조정 |
| `prose/08-이-발표-자체가-하네스였다.md` | 발표 제작 자체를 Harness 사례로 보여 주는 장 | `REVISE` | slide-first 형식으로 재작성함. 00장의 `이 발표 자료 또한 전부 Harness로 만들었습니다`를 `기억하시나요?`로 회수하는 구조를 반영함 | 실제 파일 경로 증거를 얼마나 넣을지 판단 |
| `prose/09-하네스-엔지니어.md` | 개인과 팀의 실천 결론 | `REVISE` | slide-first 형식으로 재작성함. FOMO, 경험 증폭, 팀 성숙도, Harness Engineer, 다음 행동으로 닫음 | 결론 문장 압력과 내부 공유 사례 노출 강도 조정 |

## Update Rule

- 각 file 패스 후 `gate`, `current drift`, `next loop focus`를 즉시 갱신한다.
- `PASS`가 나온 file도 후반부 shell reference로 계속 사용한다.
- 새 구조에 포함되었지만 아직 원고가 없는 file은 `PENDING`으로 둔다.
- 같은 drift가 반복되면 file 문제로만 닫지 말고 `seminar-refinement-plan.md`와 skill prompt 보정 항목으로 올린다.
