        # Korean Copy Packet

        - batch id: `batch-03`
        - active theme: `theme-minimal-light`
        - approved slide ids: `S19`, `S20`, `S21`, `S22`, `S23`, `S24`

        ### S19. 실패 패턴을 먼저 봐야 한다
- family: `section`
- shell: `section-divider-shell`
- chapter marker: CHAPTER 05
- line: 실패는 부작용이 아니라 운영 설계의 본문이다
- keywords: Long Context, Context Rot, Trust

### S20. Long Context의 적은 길이가 아니다
- family: `content`
- shell: `content-three-card-shell`
- chapter label: CHAPTER 05
- lead: 길이가 아니라 조성
- cards:
  - TOO MUCH | 과다 주입 | 많이 넣는다고 더 정확해지지 않는다 | 관련 없는 문장이 늘수록 판단 비용만 커짐
  - CONFLICT | 기준 충돌 | 서로 다른 기준이 같이 들어오면 루프가 흔들린다 | 긴 문맥의 적은 길이가 아니라 조성 [focus]
  - NOISE | 노이즈 | 핵심과 주변이 구분되지 않으면 드리프트가 시작된다 | 좋은 컨텍스트는 선별과 압축

### S21. Context Rot는 조용히 누적된다
- family: `content`
- shell: `content-three-step-shell`
- chapter label: CHAPTER 05
- lead: 기준은 조용히 흐려진다
- steps:
  - START | 기준선 | 처음에는 목적과 범위가 또렷하다 | 무엇을 해야 하고 말아야 하는지 또렷
  - DRIFT | 누적 | 중간 노동이 쌓이며 기준이 조금씩 흐려진다 | 관련 없는 수정과 설명이 섞이는 순간 시작 [focus]
  - FAIL | 확신 | 마지막에는 틀린 방향을 자신 있게 민다 | 실패 신호는 대개 하네스 공백의 이름

### S22. Calibrated Trust
- family: `content`
- shell: `content-three-card-shell`
- chapter label: CHAPTER 05
- lead: 어디를 맡기고 어디서 멈출지
- cards:
  - HUMAN | 인간 승인 | 고위험 수정은 사람이 마지막 문을 쥔다 | 권한이 큰 행동일수록 승인선이 더 앞
  - AUTO | 자동 검증 | 기계적 테스트가 자신감을 잘라낸다 | 좋은 trust는 자동 필터 위에 쌓임 [focus]
  - ISOLATE | 격리 | 샌드박스와 worktree가 실패 범위를 좁힌다 | 신뢰는 능력보다 반경 설계에 가깝다

### S23. 멀티 에이전트는 운영 해법이다
- family: `section`
- shell: `section-divider-shell`
- chapter marker: CHAPTER 06
- line: Context Rot와 trust 문제를 풀려면 격리와 handoff가 먼저다
- keywords: 격리, handoff, 평가

### S24. 병렬화보다 격리와 handoff
- family: `content`
- shell: `content-three-card-shell`
- chapter label: CHAPTER 06
- lead: 더 많은 AI보다 더 좁은 책임
- cards:
  - ISOLATE | 격리 | Sub-Agent는 중간 노동을 메인 밖으로 밀어낸다 | 메인 컨텍스트는 방향과 판단을 붙듦
  - HANDOFF | handoff | Orchestrator는 입력과 출력 경계를 먼저 설계한다 | 좋은 분업은 메시지보다 handoff에서 갈림 [focus]
  - EVAL | 평가 | 평가 분리가 blind spot을 줄인다 | 생성자와 평가자를 같은 손에 두지 않음
