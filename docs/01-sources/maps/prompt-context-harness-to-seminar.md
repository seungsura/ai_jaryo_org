# Harness Engineering 참고 메모

이 문서는 `prompt-context-harness-1-15.md`가 세미나 본문 중 `01`, `04`, `05`, `07`, `09`를 어떻게 보강하는지 정리한 reference다. 위치상으로는 `docs/02-seminar/prose/`의 본문을 대체하는 문서가 아니라, 본문에 이미 흡수된 논지를 다시 확인하고 편집 경계를 분명히 하기 위한 보조 문서에 가깝다. `docs/01-sources/intake/source-inbox.md`는 이 source를 `Prompt → Context → Harness` 전환, 하네스 실패 모드, 상태 외부화, tool curation, `Harness Engineer`, `Build to Delete` 원칙을 기존 섹션에 분산 편입하는 자료로 분류하고 있고, `.codex/skills/local/jaryo-doc-reconstruction/references/structure.md` 역시 이 markdown archive가 `docs/01-sources/maps/prompt-context-harness-to-seminar.md`로 정리될 수 있다고 안내한다.

중요한 점은 이 자료의 위상이다. `docs/01-sources/maps/seminar-claims-and-sources.md`가 정리하듯 `prompt-context-harness-1-15.md`는 `supplemental markdown source`다. 따라서 여기서 회수한 개념과 표현은 세미나 narrative를 두껍게 만드는 데에는 유효하지만, 별도 공개 검증이 끝난 외부 benchmark처럼 다루면 안 된다. 특히 벤더 사례, 점수 비교, 비용 절감 같은 숫자는 로컬 markdown 안에서 제시된 맥락적 예시로만 읽어야 하며, 이 reference 문서도 그 원칙을 따른다.

## 이 source가 Section 01을 지지하는 방식

`docs/02-seminar/prose/01-where-coding-is-going.md`의 핵심은 개발의 중심이 직접 타이핑에서 환경 설계와 검증으로 이동하고 있다는 주장이다. `prompt-context-harness-1-15.md`는 이 논지를 두 개의 축으로 뒷받침한다. 하나는 page 002의 `Prompt → Context → Harness` 전환이다. 이 문서는 관심사가 “어떻게 말할 것인가”에서 “무엇을 보여 줄 것인가”, 다시 “무엇을 통제하고 방지할 것인가”로 넓어졌다고 정리한다. 다른 하나는 page 003의 추상화 역사다. 어셈블리에서 고급 언어로, 메모리 수동 관리에서 `GC`로, 인프라 직접 운영에서 클라우드로 이동했던 흐름 위에 이제는 코딩 자체를 에이전트에 위임하고 인간은 환경을 설계하는 단계가 놓인다고 설명한다.

이 연결은 Section 01의 “코딩은 사라지지 않지만 중심이 손가락에서 설계와 검증으로 이동한다”는 문장을 더 또렷하게 만든다. page 014의 “타이피스트에서 지휘자로”라는 대비도 같은 방향을 보강한다. 전통적 엔지니어가 코드를 직접 쓰고 버그를 직접 고치는 사람으로 그려진다면, 현대의 `Harness Engineer`는 에이전트가 일할 환경을 설계하고 결과의 taste를 감별하는 사람으로 재정의된다. Section 01이 말하는 역할 이동은 바로 이 언어에 기대어 정리할 수 있다.

## 이 source가 Section 04를 지지하는 방식

`docs/02-seminar/prose/04-harness-and-context-engineering.md`는 `Harness Engineering`을 세미나의 중심 개념으로 세운다. `prompt-context-harness-1-15.md`는 여기서 가장 직접적인 보강 자료다. page 005는 하네스의 실무 구조를 `Guardrails`, `Specification`, `Verification`, `State Management`, `Observability`라는 다섯 블록으로 제시한다. 세미나 본문이 `Harness`를 컨텍스트 설계, 도구 오케스트레이션, 상태와 메모리, 검증 루프, 오류 복구, 인간 개입 제어까지 포괄하는 실행 환경으로 설명할 때, 이 source는 그 넓은 설명을 더 손에 잡히는 운영 어휘로 압축해 준다.

같은 자료의 page 006은 “병목은 AI의 능력이 아니라 환경에 있다”는 방향성을 강하게 밀어 준다. 다만 이 대목의 점수 비교와 향상 폭은 본 저장소의 다른 정리 문서가 경고하듯 공개 benchmark처럼 재인용할 대상은 아니다. 여기서 회수해야 할 핵심은 숫자 자체가 아니라, 하네스가 품질을 좌우하는 위치가 기능 구현 성능보다 방어적 프로그래밍과 구조 설계 강제에 가깝다는 framing이다. 즉 Section 04에서 이 source를 쓰는 가장 안전한 방식은 `Harness`의 해부학과 역할 전환을 설명하는 데 두고, 개별 수치는 맥락 예시로만 남기는 것이다.

## 이 source가 Section 05를 지지하는 방식

`docs/02-seminar/prose/05-limitations-and-failure-patterns.md`는 긴 작업에서 실패가 누적되는 구조와 컨텍스트 오염 문제를 다룬다. `prompt-context-harness-1-15.md`는 page 004에서 이를 보다 운영적인 실패 언어로 번역한다. 이 문서는 하네스가 없을 때 나타나는 징후를 `AI Slop`, `Doom Loop`, 명시적 지시 무시, 감시 없는 `Shadow Agent`로 묶는다. 세미나 본문이 컨텍스트의 `Poisoning`, `Distraction`, `Confusion`, `Clash`와 신뢰성 저하를 설명할 때, 이 source는 그러한 실패가 현장에서 어떤 체감 증상으로 보이는지 보여 주는 보조 축이 된다.

중요한 것은 이 자료가 실패를 모델 내부의 결함으로만 설명하지 않는다는 점이다. page 005의 다섯 블록과 연결해 읽으면, 실패는 대개 `Guardrails` 부재, `Verification` 부재, `Observability` 부재, 상태 관리 실패가 겹친 결과로 이해된다. 그래서 Section 05에서 이 source는 “에이전트가 왜 망가지는가”를 묻는 장이 아니라 “어떤 하네스 공백이 실패를 증폭시키는가”를 묻는 장으로 기능한다.

## 이 source가 Section 07을 지지하는 방식

`docs/02-seminar/prose/07-practical-workflow-and-tooling.md`와 가장 촘촘하게 맞물리는 대목은 page 007부터 page 011까지다. 먼저 page 007은 tool curation 원칙을 분명히 한다. 도구를 많이 주는 것이 아니라 태스크별로 필요한 도구만 좁혀 주어야 한다는 주장이다. 세미나 본문이 “좋은 운영은 도구를 늘리는 기술보다 도구를 줄이는 기술에 가깝다”고 쓰는 근거가 여기 있다. 이 문장은 `MCP` 서버와 도구를 무제한으로 붙이는 습관이 오히려 컨텍스트를 오염시킨다는 본문의 경고와도 정확히 이어진다.

page 008은 `State Management`를 에이전트의 기억을 윈도우 밖으로 빼는 일로 설명한다. 세션이 끊기면 기억도 리셋되므로, 파일 시스템과 `Git` 히스토리 같은 외부 아티팩트에 상태를 영속화해야 한다는 주장이다. 이는 Section 07의 이슈 기반 워크플로우, `git worktree`, 물리적 세션 분리와 같은 운영 방식이 왜 필요한지 설명하는 실무 언어를 제공한다. page 009와 page 011은 여기에 한 단계 더해, 결정론적 제어와 확률적 제어를 분리하고 둘을 교차시키는 하이브리드 루프를 제시한다. 기계가 확인할 수 있는 것은 기계에게 맡기고, AI는 판단과 생성에 집중해야 하며, `lint`, `type check`, `test`, 승인 게이트는 우회할 수 없는 문으로 남겨야 한다는 것이다.

page 010의 레퍼런스 아키텍처 설명도 Section 07을 받쳐 준다. OCR이 거칠어서 세부 라벨은 일부 불안정하지만, 인간 검토, `E2E` 테스트 게이트, 기계적 린트 게이트, 동적 도구 큐레이션, 격리 `VM`이 층위별 하네스로 수렴한다는 큰 구조는 분명하다. 이 정도 범위에서는 세미나 본문의 layered workflow 설명과 정합적이다. 반대로 OCR이 파손된 고유 명칭이나 세부 벤더 사례는 여기서 더 강한 문장으로 복원하지 않는 편이 안전하다.

## 이 source가 Section 09를 지지하는 방식

`docs/02-seminar/prose/09-what-we-should-do-next.md`는 AI 시대의 역할 변화와 행동 원칙을 다룬다. `prompt-context-harness-1-15.md`는 이 섹션을 두 개의 문장으로 밀어 준다. 하나는 page 014의 `Harness Engineer` 재정의다. 이제 핵심 역량은 직접 코드를 많이 쓰는 것이 아니라, 에이전트가 잘 일할 수 있도록 환경을 설계하고 결과의 품질을 판별하는 데 있다는 주장이다. 다른 하나는 page 015의 `Build to Delete`다. 오늘의 하네스는 영구히 복잡해지는 구조가 아니라, 모델이 좋아질수록 점진적으로 지워질 수 있게 만들어야 한다는 원칙이다.

이 원칙은 Section 09의 실천 조언과 잘 맞는다. 글로 규칙을 남기고, 반복 업무를 명세하고, command와 loop에 원리를 고정하되, 그것이 영구 불변의 관료적 구조가 되지 않도록 삭제 조건까지 함께 생각해야 한다는 것이다. 다시 말해 이 source는 “AI를 많이 써라”는 막연한 메시지보다 “좋은 하네스는 현재의 약점을 덮기 위해 존재하지만 미래의 개선을 가로막지 않아야 한다”는 더 성숙한 운영 원칙을 제공한다.

## 편집상 주의할 점

이 source는 세미나의 하네스 관련 서사를 선명하게 해 주지만, OCR 특성상 표현이 흔들리는 부분도 있다. page 005의 다섯 블록은 상대적으로 안정적이지만, 일부 번호 표기와 중복 라벨은 정돈이 필요하다. page 010은 구조적 방향은 읽히지만 고유 명칭과 세부 배치가 깨진 부분이 남아 있다. 따라서 이 reference를 사용할 때는 개념 축과 섹션 연결을 우선하고, OCR 파손이 남은 미세한 디테일은 본문 주장으로 승격하지 않는 것이 맞다.

정리하면 `prompt-context-harness-1-15.md`는 세미나 전체를 새로 쓰게 만드는 별도 세계관이라기보다, 이미 형성된 `01`, `04`, `05`, `07`, `09`의 논지를 더 응집력 있게 만드는 보조 source다. Section 01에는 추상화와 역할 이동의 언어를, Section 04에는 하네스 해부학의 실무 어휘를, Section 05에는 실패 징후의 운영적 표현을, Section 07에는 tool curation과 상태 외부화, 결정론적 게이트의 구조를, Section 09에는 `Harness Engineer`와 `Build to Delete`라는 결론 문장을 공급한다. 이 범위를 넘는 일반화나 외부 검증 효과는 이 문서의 역할이 아니다.
