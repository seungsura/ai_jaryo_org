# Seminar Refinement Manifest

`docs/02-seminar/prose/`의 live sync 파일이다. 실제 seminar 문서는 `02-seminar`에 두고, 편집 상태 추적은 여기서 관리한다.

초기 스냅샷 날짜: `2026-04-19`

| file | role | gate | current drift | next loop focus |
| --- | --- | --- | --- | --- |
| `prose/00-overview.md` | 전체 thesis와 독서 지도 | `PASS` | 없음. 현재 tone과 압력의 기준선 역할 | 후반부 pass에서 baseline shell로 계속 참조 |
| `prose/01-where-coding-is-going.md` | 시대 전환과 역할 이동의 도입부 | `PASS` | 없음. 역사 서사와 현재 논지의 연결이 안정적 | 후반부 chapter가 너무 설명적으로 흐를 때 비교 기준으로 사용 |
| `prose/02-why-claude-code.md` | tool genealogy와 harness 수렴의 대표 사례 | `PASS` | 없음. 사례와 논지의 결합이 선명함 | later chapter가 vendor 설명으로 미끄러질 때 기준 shell로 사용 |
| `prose/03-ai-era-methodology.md` | 방법론 재부상과 `SDD`/`TDD`의 필요성 | `PASS` | 없음. 앞 장과 뒤 장 사이의 bridge가 비교적 안정적 | 후반부 workflow chapter의 기준 chapter로 사용 |
| `prose/04-harness-and-context-engineering.md` | `Prompt`/`Context`/`Harness` 층위 구분 | `PASS` | 없음. 5대 기능 블록과 도구 레이어 구분, 05장 handoff가 안정적 | 후반부에서 `State Management`/`Observability`를 반복할 때 기준 chapter로 사용 |
| `prose/05-limitations-and-failure-patterns.md` | 실패 누적 구조와 `Calibrated Trust` | `PASS` | 없음. 실패 증상보다 구조 공백과 검증 배치가 앞에 선다 | 06장 이후 drift를 점검할 때 `failure -> response` 전환 기준으로 사용 |
| `prose/06-multi-agent-patterns.md` | 패턴 분해와 선택 기준 | `PASS` | 없음. 공통 비교 시나리오가 들어와 패턴 선택 축이 선명함 | slide planning 단계에서 패턴 비교 슬라이드의 prose source로 사용 |
| `prose/07-practical-workflow-and-tooling.md` | 원리를 command와 gate로 고정하는 운영 장 | `PASS` | 경미함. 특정 tool 사례 밀도가 약간 높지만 workflow spine은 안정적 | 다음 후반부 pass에서 사례 밀도가 다시 늘어날 때 비교 기준으로 사용 |
| `prose/08-how-this-presentation-was-made.md` | 이 저장소의 실제 제작 경로 설명 | `PASS` | 없음. 단계 나열보다 파이프라인의 이유와 경계가 앞선다 | slide pipeline 설명이나 speaker notes 작성 시 canonical case study로 사용 |
| `prose/09-what-we-should-do-next.md` | 개인과 팀의 실천 원칙 정리 | `PASS` | 없음. closing chapter의 압축도와 추진력이 안정적 | deck closing section과 notes tone의 기준 shell로 사용 |
| `prose/90-appendix-references.md` | 근거층 정리와 후속 읽기 가이드 | `PASS` | 경미함. public source 인덱스는 후속 패스에서 더 세밀화 가능 | appendix utility를 높이는 후속 reference 정리 때 기준판으로 사용 |

## Update Rule

- 각 file 패스 후 `gate`, `current drift`, `next loop focus`를 즉시 갱신한다.
- `PASS`가 나온 file도 후반부 shell reference로 계속 사용한다.
- 같은 drift가 반복되면 file 문제로만 닫지 말고 `seminar-refinement-plan.md`와 skill prompt 보정 항목으로 올린다.
