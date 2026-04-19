# Section 01 복구용 claim matrix

이 문서는 `docs/02-seminar/prose/01-where-coding-is-going.md`를 복구할 때 참조하는 Section 01 전용 source map이다. 목적은 현재 prose를 요약문으로 다시 줄이는 것이 아니라, canonical transcript와 local supplemental source가 실제로 어떤 문장과 연결되어야 하는지 고정하는 데 있다.

## Source set

- Local canonical
  - `docs/01-sources/local-canonical/claude-code-seminar-kakao.md`의 `Page 005`~`Page 013`
- Local supplemental
  - `docs/01-sources/maps/prompt-context-harness-to-seminar.md`
- Provenance boundary
  - `docs/01-sources/maps/seminar-claims-and-sources.md`

## Section-connected matrix

### 00. 질문을 먼저 다시 세우기

- Canonical block
  - `Page 005`~`Page 013` 전체가 보여 주는 흐름
- Supplemental block
  - `prompt-context-harness-to-seminar.md`의 `이 source가 Section 01을 지지하는 방식`
- Preserve
  - Section 01의 질문은 `코딩이 사라지는가`보다 `개발자의 일이 어디로 이동하는가`에 가깝게 세운다.
  - 뒤에서 다룰 `Prompt`, `Context`, `Harness` 구분은 이 질문을 푸는 언어로만 제한해 사용한다.
- Provenance label
  - `Prompt → Context → Harness`는 supplemental framing이다.
  - 역할 이동이라는 큰 질문은 canonical 흐름으로 지지한다.
- Boundary note
  - Section 01을 `Prompt → Context → Harness` 개념사로 과도하게 확장하지 않는다.

### 01. 추상화의 역사는 늘 직접 하는 일을 줄여 왔다

- Canonical block
  - `Page 005`: 기계어, `C`, `"기계를 직접 다루지 않으면 개발자가 아니다"`
  - `Page 006`: `Java`, `GC`, `"메모리 직접 관리 안 하면 개발이 아니다"`
  - `Page 007`: `Python`, `"장난감 언어, 실제 개발에 못 쓴다"`, `Python > #1 언어`
  - `Page 008`: `"이 함수를 리팩토링하고 테스트를 작성해줘"`, `"이건 진짜 개발이 아니다"`
  - `Page 009`: `매번 틀렸다`
- Supplemental block
  - `prompt-context-harness-1-15.md`의 `Page 003`
  - `어셈블리 → 고급 언어 → 메모리 관리 → 프레임워크 → 클라우드 → AI 에이전트`
  - `코딩을 위임하고 '환경'을 설계`
- Preserve
  - `Java`와 `GC`가 등장하는 수동 메모리 관리 인식은 명시적으로 남긴다.
  - `Python`이 장난감 언어 취급을 받다가 널리 쓰이게 된 대비를 유지한다.
  - AI 장면까지 네 단계 대비 구조를 보존한다.
  - 필요할 때는 supplemental source의 계단형 도식으로 중간 단계를 보강한다.
  - `AI 에이전트` 단계의 설명은 `코딩을 위임하고 '환경'을 설계`라는 문장으로 회수한다.
  - `매번 틀렸다`는 이 대비의 결론으로 남긴다.
- Provenance label
  - 네 장면 대비와 결론은 canonical
  - 더 긴 계단 구조와 `환경` 설계 문장은 supplemental
- Boundary note
  - `메모리 관리` 같은 일반화만 남기고 `Java`/`GC`를 지우면 실패다.
  - supplemental 계단을 쓸 때도 canonical transcript의 네 장면 대비를 대체하지 않는다.

### 02. 이번 변화의 핵심은 타이핑의 독점성이 무너지는 데 있다

- Canonical block
  - `Page 010`: `25%`, `~3개월`, `100%`, `YC 2025 겨울 배치`, `Meta 엔지니어`, `AI가 짠 코드가 사람의 터치 없이 PR에 그대로 올라오는 일상`
- Preserve
  - 공개 신호와 내부 실무 신호를 한 문장으로 뭉개지지 않게 분리한다.
  - `YC W25`의 `25% / 95%`는 공개 신호로 다룬다.
  - `~3개월`, `Meta engineer`, `PR에 그대로 올라오는 일상`은 내부 관찰로만 다룬다.
- Provenance label
  - Public: `YC W25`의 `25% / 95%`
  - Internal: `~3개월`, `Meta engineer`, `사람의 터치 없이 PR에 그대로 올라오는 일상`
- Boundary note
  - 내부 신호를 외부 benchmark처럼 일반화하지 않는다.

### 03. 코드 바깥의 문서가 실제 작업을 바꾸기 시작했다

- Canonical block
  - `Page 011`: `이름은 다르지만 역할은 동일 - 마크다운으로 프로젝트 규칙을 AI에게 전달`
  - `CLAUDE.md`, `Cursor Rules`, `copilot-instructions.md`, `AGENTS.md`
- Preserve
  - `이름은 다르지만 역할은 동일`이라는 대비 문장을 살린다.
  - 각 문서명이 실제 예시로 남아야 한다.
  - 문서가 단순 설명서가 아니라 작업 규칙을 전달하는 실무 문서가 되었다는 뜻을 풀어 쓴다.
- Provenance label
  - canonical
- Boundary note
  - `입력 계층`, `생산 시스템` 같은 번역투 추상어로만 처리하지 않는다.

### 04. 개발자의 새로운 역할

- Canonical block
  - `Page 012`: `코드를 잘 짜는 능력`, `문서를 잘 쓰는 능력`, `컨텍스트를 설계하는 능력`
  - `건축가`, `오케스트라 지휘자`, `CLAUDE.md = 총보`
- Supplemental block
  - `prompt-context-harness-to-seminar.md`의 `Harness Engineer` 연결
- Preserve
  - 세 능력을 각각 분리해 보여 준다.
  - 건축가와 지휘자 비유를 둘 다 유지한다.
  - `CLAUDE.md = 총보`는 빠지면 안 된다.
- Provenance label
  - 능력 구분, 비유, `CLAUDE.md = 총보`: canonical
  - `Harness Engineer`: supplemental bridge term
- Boundary note
  - `Harness Engineer` 한 문장으로 세 능력을 다시 압축하지 않는다.

### 05. 그래도 기초는 중요하다

- Canonical block
  - `Page 013`: `"AI가 더 많이 해줄수록, 기초 지식을 가진 사람의 경쟁력이 역설적으로 올라간다"`
  - `변하는 것 / 변하지 않는 것`
  - `보안 • 동시접속 • DB 스키마 • 캐싱`
  - `기본기 없이는 질문조차 불가`
- Supplemental block
  - `prompt-context-harness-to-seminar.md`의 역할 이동 설명
- Preserve
  - 직접 타이핑 비중은 줄어도 시스템 이해는 남는다는 대비를 유지한다.
  - 데모와 실서비스의 차이를 `보안 / 동시접속 / DB 스키마 / 캐싱`으로 풀어 쓴다.
  - `기본기 없이는 질문조차 불가`는 의미상 살아 있어야 한다.
- Provenance label
  - 핵심 문장과 예시는 canonical
  - 엄밀함의 이동 같은 설명 문장은 supplemental 보강으로만 사용한다.
- Boundary note
  - 추상적인 `엄밀함 이동` 설명만 남기고 실무 예시를 잃어버리면 실패다.

### 06. 결론

- Canonical block
  - `Page 010`~`Page 013`의 종합
- Supplemental block
  - `prompt-context-harness-to-seminar.md`의 역할 이동 정리
- Preserve
  - 코딩의 소멸이 아니라 역할 이동이라는 결론
  - 규칙을 적고, 문맥을 정하고, 결과를 검증하는 책임이 커진다는 정리
- Provenance label
  - 결론의 뼈대는 canonical
  - `Prompt`, `Context`, `Harness` 연결은 supplemental
- Boundary note
  - 이 결론에서 tool genealogy나 vendor 비교로 옮겨 가지 않는다.

## Writer notes

- 먼저 canonical transcript의 대비 구조를 세우고, 그다음 supplemental source로 연결 문장만 보강한다.
- public / internal / supplemental 경계를 prose 안에서 흐리게 섞지 않는다.
- slide slogan을 그대로 옮기지 말되, slogan이 담당하던 논리 연결은 prose 안에서 복원한다.
