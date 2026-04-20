        # Chapter Batch

        - batch id: `batch-03`
        - chapter or theme: sections `05, 06`
        - approved source files: `docs/02-seminar/prose/05-limitations-and-failure-patterns.md`, `docs/02-seminar/prose/06-multi-agent-patterns.md`
        - planned slide ids: `S19`, `S20`, `S21`, `S22`, `S23`, `S24`
        - default layout families: `content`, `section`
        - approved reference shells: `content-three-card-shell`, `content-three-step-shell`, `section-divider-shell`
        - exception slides: `S19`, `S23`

        ## Slide Briefs

        ### S19. 실패 패턴을 먼저 봐야 한다
- source section: `docs/02-seminar/prose/05-limitations-and-failure-patterns.md`
- layout family: `section`
- density: `light`
- reference shell: `section-divider-shell`
- claim: 실패는 부작용이 아니라 운영 설계의 본문이다
- supporting points:
  - Long Context
  - Context Rot
  - Trust
- must-keep terms: `Long Context`, `Context Rot`, `Calibrated Trust`
- do-not-say: 실패는 모델이 멍청해서 생긴다
- evidence requirement: prose source only
- speaker intent: 실패를 예외가 아니라 구조 문제로 읽게 만든다

### S20. Long Context의 적은 길이가 아니다
- source section: `docs/02-seminar/prose/05-limitations-and-failure-patterns.md`
- layout family: `content`
- density: `medium`
- reference shell: `content-three-card-shell`
- claim: 긴 문맥의 문제는 길이보다 무엇을 어떤 조성으로 넣느냐다
- supporting points:
  - 과다 주입
  - 기준 충돌
  - 관계 없는 노이즈
- must-keep terms: `Long Context`
- do-not-say: 길기만 하면 무조건 좋다
- evidence requirement: prose source only
- speaker intent: 길이 집착을 버리고 선별 문제로 시선을 돌린다

### S21. Context Rot는 조용히 누적된다
- source section: `docs/02-seminar/prose/05-limitations-and-failure-patterns.md`
- layout family: `content`
- density: `medium`
- reference shell: `content-three-step-shell`
- claim: 세션이 길어질수록 기준은 서서히 흐려지고, 실패는 대개 조용히 누적된다
- supporting points:
  - 초기 기준선
  - 누적된 드리프트
  - 확신을 가진 잘못
- must-keep terms: `Context Rot`
- do-not-say: 조금 더 설명하면 해결된다
- evidence requirement: prose source only
- speaker intent: 긴 세션을 무작정 붙드는 습관의 위험을 보이게 한다

### S22. Calibrated Trust
- source section: `docs/02-seminar/prose/05-limitations-and-failure-patterns.md`
- layout family: `content`
- density: `medium`
- reference shell: `content-three-card-shell`
- claim: 신뢰는 감정이 아니라 배치이며, 인간 승인과 자동 검증과 물리적 격리가 함께 설계돼야 한다
- supporting points:
  - 인간 승인선
  - 자동 검증선
  - 샌드박스와 격리
- must-keep terms: `Calibrated Trust`
- do-not-say: AI를 믿지 말자, AI를 그냥 믿자
- evidence requirement: prose source only
- speaker intent: 신뢰를 정서가 아니라 설계 문제로 바꿔 놓는다

### S23. 멀티 에이전트는 운영 해법이다
- source section: `docs/02-seminar/prose/06-multi-agent-patterns.md`
- layout family: `section`
- density: `light`
- reference shell: `section-divider-shell`
- claim: 멀티 에이전트는 Context Rot와 trust 문제를 격리와 handoff와 평가로 푸는 운영 해법이다
- supporting points:
  - 격리
  - handoff
  - 평가
- must-keep terms: `Sub-Agent`, `Orchestrator`, `Parallel`
- do-not-say: AI 수가 많을수록 좋다
- evidence requirement: prose source only
- speaker intent: 병렬화 환상을 끊고 분해 설계를 앞에 놓는다

### S24. 병렬화보다 격리와 handoff
- source section: `docs/02-seminar/prose/06-multi-agent-patterns.md`
- layout family: `content`
- density: `medium`
- reference shell: `content-three-card-shell`
- claim: 좋은 멀티 에이전트는 격리, handoff, 평가를 분명히 한 구조다
- supporting points:
  - 중간 노동 격리
  - handoff 설계
  - 생성자와 평가자 분리
- must-keep terms: `handoff`, `GAN-Style`
- do-not-say: 복잡하면 일단 agent를 더 붙인다
- evidence requirement: prose source only
- speaker intent: 패턴 이름보다 책임 설계가 먼저라는 점을 압축한다

        ## Batch Risks

        - title 길이는 한 줄을 유지한다
        - 밝은 minimal-light 테마에 맞게 body copy를 더 짧게 유지한다
        - shell drift보다 copy 축약을 먼저 선택한다
