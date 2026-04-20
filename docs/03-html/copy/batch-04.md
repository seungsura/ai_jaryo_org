        # Korean Copy Packet

        - batch id: `batch-04`
        - active theme: `theme-minimal-light`
        - approved slide ids: `S25`, `S26`, `S27`, `S28`, `S29`, `S30`, `S31`, `S32`, `S33`

        ### S25. 실전 워크플로우와 도구
- family: `section`
- shell: `section-divider-shell`
- chapter marker: CHAPTER 07
- line: 격리와 handoff와 평가가 실전 습관으로 내려오면 workflow가 된다
- keywords: Handoff, Gate, Workflow

### S26. 네 동사로 굴러간다
- family: `content`
- shell: `content-three-card-shell`
- chapter label: CHAPTER 07
- lead: 네 동사로 남기는 workflow
- cards:
  - WRITE | Write + Select | 무엇을 남기고 무엇을 읽힐지 먼저 고른다 | 좋은 workflow는 기록과 선별로 시작
  - COMPRESS | Compress | 긴 세션 대신 결론을 짧은 아티팩트로 남긴다 | 압축 없는 컨텍스트는 곧바로 rot [focus]
  - ISOLATE | Isolate | 위험한 작업과 중간 노동을 따로 격리한다 | 격리가 있어야 메인 컨텍스트가 살아남음

### S27. Plan-Critic-Build
- family: `content`
- shell: `content-three-step-shell`
- chapter label: CHAPTER 07
- lead: 생산보다 먼저 사고 분리
- steps:
  - PLAN | Plan | 목표, 범위, 성공 조건을 먼저 고정한다 | 판단이 흐린 채 구현으로 뛰지 않음
  - CRITIC | Critic | 다른 시야로 계획의 구멍을 먼저 건드린다 | 자기최면을 끊는 가장 싼 순간
  - BUILD | Build | 생산은 마지막에만 몰아넣는다 | 좋은 build는 좋은 plan과 critic 뒤 [focus]

### S28. gate와 observability
- family: `content`
- shell: `content-three-card-shell`
- chapter label: CHAPTER 07
- lead: 어디서 멈출지 먼저 정한다
- cards:
  - PRE | pre gate | 생산 전에 방향과 톤을 먼저 막는다 | storyline과 tone gate가 여기에 섬
  - POST | post gate | 생산 뒤에는 구조와 렌더를 따로 본다 | deck consistency와 slide validation 분리 [focus]
  - TRACE | trace | 로그와 체크포인트가 흔들린 지점을 보여 준다 | Observability가 있어야 재작업 범위도 좁아짐

### S29. 메인 컨텍스트를 지키는 운영
- family: `content`
- shell: `content-three-card-shell`
- chapter label: CHAPTER 07
- lead: 세션 안 기억보다 바깥 흔적
- cards:
  - MUX | cmux | 작업 채널을 분리해 메인 시야를 덜 더럽힌다 | 같은 터미널 안에서도 역할 경계를 분명히 만듦
  - TREE | Git Worktree | 실험과 본선을 물리적으로 갈라 놓는다 | 격리는 추상 규칙보다 물리적 경계에서 강함 [focus]
  - STATE | issue와 PR | 상태를 세션 밖 아티팩트에 남긴다 | 실전에서 신뢰할 것은 대화보다 바깥 흔적

### S30. 이 발표는 이렇게 만들었다
- family: `content`
- shell: `content-three-step-shell`
- chapter label: CHAPTER 08
- lead: 이 경로가 drift를 막았다
- steps:
  - INPUT | source | 입력층을 먼저 잠가 근거와 해석을 분리 | source boundary가 흔들리면 뒤 단계도 함께 흐려짐
  - CANON | prose | prose를 기준 문장으로 세워 논지 축을 고정 | slide는 본문을 압축할 뿐 논지 밖으로 못 튐
  - BUILD | outline → HTML | outline과 manifest gate 뒤에만 HTML build | 그래서 제작 과정 자체가 발표 논지를 증명 [focus]

### S31. 우리가 다음에 해야 할 일
- family: `section`
- shell: `section-divider-shell`
- chapter marker: CHAPTER 09
- line: 새 모델 소식보다 먼저 작업 환경의 원칙을 고정해야 한다
- keywords: rules, gates, harness

### S32. 암묵지를 밖으로 꺼내라
- family: `content`
- shell: `content-three-card-shell`
- chapter label: CHAPTER 09
- lead: 잘하는 사람 머릿속 밖으로
- cards:
  - RULES | 규칙 파일 | 반복해서 말하는 기준부터 문서로 뺀다 | 좋은 암묵지는 먼저 규칙 파일이 됨
  - GATES | 결정론적 gate | AI의 자신감과 무관하게 통과 문을 세운다 | test, review, hook이 이 층을 맡음 [focus]
  - STATE | 세션 밖 상태 | 결론과 다음 행동을 파일에 남긴다 | 상태를 대화 밖으로 밀어낼수록 안전

### S33. Harness Engineer가 새 역할이다
- family: `title`
- shell: `title-hero-shell`
- lead: 숙련은 사라지지 않는다. 하네스를 설계하고 운영하는 쪽으로 옮겨 갈 뿐이다
- body:
  - 반복 규칙 세 가지부터 파일로 빼라
  - 검증 문 하나를 추가해 기준을 잠가라
  - 세션 결론을 밖에 남겨 컨텍스트를 가볍게 하라
