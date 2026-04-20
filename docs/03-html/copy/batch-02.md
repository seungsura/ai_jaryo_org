        # Korean Copy Packet

        - batch id: `batch-02`
        - active theme: `theme-minimal-light`
        - approved slide ids: `S11`, `S12`, `S13`, `S14`, `S15`, `S16`, `S17`, `S18`

        ### S11. 방법론이 다시 앞에 온다
- family: `section`
- shell: `section-divider-shell`
- chapter marker: CHAPTER 03
- line: 자율성이 커질수록 무엇을 만들지와 어디서 멈출지가 먼저다
- keywords: SDD, TDD, Harness

### S12. 왜 지금 방법론인가
- family: `content`
- shell: `content-three-step-shell`
- chapter label: CHAPTER 03
- lead: 질문이 바뀌었다. 빨리 만드는가에서 무엇을 고정할 것인가로 갔다
- steps:
  - 2025.02 | 폭발 | 일단 빨리 만들어 보자는 분위기가 앞섰다 | 초기 충격은 생성 속도 그 자체였다
  - 2025 H2 | 고정 | 구현 전에 방향을 못 박으려는 움직임이 나왔다 | Spec-first와 SDD가 여기에 응답했다 [focus]
  - 2026 | 검증 | 구현 뒤 결과를 걸러내는 규율이 다시 중요해졌다 | TDD와 Context control이 함께 다시 올라왔다

### S13. Spec-first가 방향을 못 박는다
- family: `content`
- shell: `content-three-card-shell`
- chapter label: CHAPTER 03
- lead: 속도보다 먼저 고정할 것
- cards:
  - GOAL | 목적 | 무엇을 만들라고 하는지 먼저 닫는다 | 목표가 흐리면 속도는 바로 드리프트
  - SCOPE | 범위 | 무엇을 하지 말아야 하는지도 함께 적는다 | 빼야 할 범위가 없으면 에이전트가 번짐
  - DONE | 완료 기준 | 무엇을 통과로 볼지 결정론적으로 남긴다 | 좋은 스펙은 구현보다 검증 기준을 남김 [focus]

### S14. TDD가 가장 거친 가드레일
- family: `content`
- shell: `content-three-step-shell`
- chapter label: CHAPTER 03
- lead: 테스트가 자신감을 잘라낸다
- steps:
  - RED | Red | 실패하는 테스트로 기대 동작을 먼저 선언한다 | 정답 경계를 사람이 먼저 박아 넣음
  - GREEN | Green | 테스트를 통과하는 최소 구현만 허용한다 | 기준 준수가 기능 확장보다 앞
  - REVIEW | Review | 테스트 삭제와 완화 시도 차단 | AI 시대의 가장 거친 가드레일 [focus]

### S15. 프롬프트를 넘어서 Harness
- family: `section`
- shell: `section-divider-shell`
- chapter marker: CHAPTER 04
- line: 문장은 시작일 뿐이고 병목은 운영 구조로 이동했다
- keywords: Prompt, Context, Harness

### S16. Prompt, Context, Harness
- family: `content`
- shell: `content-three-card-shell`
- chapter label: CHAPTER 04
- lead: 세 층은 서로 다른 질문
- cards:
  - PROMPT | Prompt | 어떻게 말할 것인가 | 지시문과 추론 유도
  - CONTEXT | Context | 무엇을 보여 줄 것인가 | 시야를 잘못 주면 모델이 흔들림
  - HARNESS | Harness | 무엇을 통제하고 방지할 것인가 | 권한, 검증, 상태를 다루는 바깥 구조 [focus]

### S17. Agent = Model + Harness
- family: `content`
- shell: `content-three-card-shell`
- chapter label: CHAPTER 04
- lead: 좋은 모델만으로는 부족
- cards:
  - MODEL | Model | 생성과 추론의 엔진이다 | 스스로 경계를 세우지는 못함
  - TOOLS | Tools | 읽고 쓰고 실행하는 팔이 된다 | 행동 능력이 커질수록 위험도 같이 커짐
  - HARNESS | Harness | 권한, 상태, 검증을 묶는 뼈대다 | 좋은 에이전트는 하네스에서 더 크게 갈림 [focus]

### S18. 하네스의 다섯 블록
- family: `content`
- shell: `content-three-card-shell`
- chapter label: CHAPTER 04
- lead: 다섯 블록, 세 묶음
- cards:
  - CONTROL | 경계 고정 | Guardrails와 Specification이 범위를 먼저 잠근다 | 위험한 행동을 막고 기준선을 고정
  - FILTER | 결과 필터링 | Verification이 결과를 결정론적으로 거른다 | lint, test, review gate가 이 층 [focus]
  - STATE | 상태 가시화 | State와 Observability가 세션 밖 흔적을 남긴다 | 파일, 로그, 이력이 루프를 다시 읽게 만듦
