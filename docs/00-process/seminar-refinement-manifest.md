# Seminar Refinement Manifest

`docs/02-seminar/prose/`의 live sync 파일이다. 실제 seminar 문서는 `02-seminar`에 두고, 편집 상태 추적은 여기서 관리한다.

초기 스냅샷 날짜: `2026-04-19`

| file | role | gate | current drift | next loop focus |
| --- | --- | --- | --- | --- |
| `prose/00-코딩은-사라지는가.md` | 역할 이동의 도입부 | `REVISE` | slide-first 형식으로 재작성함. 목적지를 먼저 제시하고, `추상화의 역사` 구간은 이미 만들어 둔 자료를 연속 장면으로 살림. 숫자 사례 3개는 적절하므로 모두 유지하고 역할 이동의 증거로 회수함 | 추상화 역사 자료의 길이, 숫자 slide의 layout family 조정 |
| `prose/01-챗봇과-싸우지-않기.md` | 프롬프트 한계에서 Harness 필요성으로 넘기는 장 | `REVISE` | 02장 첫 슬라이드의 agent loop와 겹치지 않도록 `파일/명령/검증/다음 판단` 설명을 걷어내고, `챗봇처럼 쓰면서 작업 결과를 기대한 착각`과 `프롬프트는 부탁, 환경은 구조`라는 전환에 집중시킴 | 사용자 리뷰 후 01-3의 Harness 정의가 02장 정의부와 겹치는지 조정 |
| `prose/02-하네스는-무엇인가.md` | 챗봇과 agent를 가르는 루프/환경 정의 장 | `REVISE` | slide-first 틀을 제거하고 발표체 본문으로 재작성함. agent loop, context curation, `Agent = Model + Harness`, 실행 환경으로서의 Harness에 집중시켜 01의 문제 제기와 03의 실패 구조 사이에 놓음 | 00/01 통합 뒤 챗봇 대비 문장이 반복되는지 확인 |
| `prose/03-이렇게-하면-망한다.md` | 긴 작업과 긴 컨텍스트의 실패 구조 | `REVISE` | slide-first 틀을 제거하고 긴 작업을 통째로 맡겼을 때의 누적 실패를 발표체로 정리함. `95%` 성공률이 20단계에서 `36%`가 되는 source-backed 수치만 남기고 과한 확장 계산은 제거함 | 실패 패턴 용어 수와 `AI Slop/Doom Loop/Shadow Agent`의 필요성 조정 |
| `prose/04-먼저-방향을-잡는다.md` | 빠른 생성 전에 방향을 잡는 장 | `REVISE` | slide-first 틀을 제거하고 방향, 기준, spec을 먼저 세우는 장으로 재작성함. Waterfall 오해를 풀고 SDD, TDD, Plan-Critic-Build를 생성 전 기준 설계로 묶음 | 07장 실전 파일/명령어 설명과 `Plan-Critic-Build` 반복 정도 확인 |
| `prose/05-기계가-막을-수-있는-것은-앞에서-막는다.md` | 검증과 권한 경계의 장 | `REVISE` | slide-first 틀을 제거하고 검증, gate, 권한 경계, `Keep Quality Left`를 발표체로 재정렬함. 04가 방향을 잡는 장이라면 05는 잘못된 실행을 앞에서 멈추는 장으로 둠 | `TDD`, permission, gate 예시의 밀도 조정 |
| `prose/06-하나의-AI에게-다-맡기지-않는다.md` | 역할, 컨텍스트, 검증 책임 분리 | `REVISE` | slide-first 틀을 제거하고 한 창에 모든 일을 밀어 넣는 문제에서 역할 분리로 이동함. Sub-Agent, Orchestrator, 생성/검증 분리, Agent Team을 실무 구조로 압축함 | `SOLID` 재해석을 남길지 줄일지 사용자 판단 |
| `prose/07-실전-하네스는-파일과-명령어로-남는다.md` | 원칙을 파일과 명령어로 고정하는 실전 장 | `REVISE` | slide-first 틀을 제거하고 파일, 명령어, Hook, 이슈, Worktree, 최소 워크플로우를 실제 적용 흐름으로 재작성함. 04~06의 원칙을 실행 환경으로 내리는 장으로 정리함 | Hook, manifest, worktree 예시의 구체성 조정 |
| `prose/08-이-발표-자체가-하네스였다.md` | 발표 제작 자체를 Harness 사례로 보여 주는 장 | `REVISE` | slide-first 틀을 제거하고 source, prose, outline, manifest, design, validation layer로 이어지는 proof 장으로 재작성함. 00장의 `이 발표 자료 또한 전부 Harness로 만들었습니다`를 사례로 회수함 | 실제 파일 경로 증거와 source line mapping을 얼마나 넣을지 판단 |
| `prose/09-하네스-엔지니어.md` | 개인과 팀의 실천 결론 | `REVISE` | slide-first 틀을 제거하고 FOMO, 경험 증폭, 팀 성숙도, Harness Engineer, 다음 행동으로 닫는 발표체 결론으로 재작성함. 내부 공유 사례는 일반화하지 않도록 qualifier를 유지함 | 결론 문장 압력과 내부 공유 사례 노출 강도 조정 |

## Update Rule

- 각 file 패스 후 `gate`, `current drift`, `next loop focus`를 즉시 갱신한다.
- `PASS`가 나온 file도 후반부 shell reference로 계속 사용한다.
- 새 구조에 포함되었지만 아직 원고가 없는 file은 `PENDING`으로 둔다.
- 같은 drift가 반복되면 file 문제로만 닫지 말고 `seminar-refinement-plan.md`와 skill prompt 보정 항목으로 올린다.
