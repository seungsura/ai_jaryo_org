        # Chapter Batch

        - batch id: `batch-04`
        - chapter or theme: sections `07, 08, 09`
        - approved source files: `docs/02-seminar/prose/07-practical-workflow-and-tooling.md`, `docs/02-seminar/prose/08-how-this-presentation-was-made.md`, `docs/02-seminar/prose/09-what-we-should-do-next.md`
        - planned slide ids: `S25`, `S26`, `S27`, `S28`, `S29`, `S30`, `S31`, `S32`, `S33`
        - default layout families: `content`, `section`, `title`
        - approved reference shells: `content-three-card-shell`, `content-three-step-shell`, `section-divider-shell`, `title-hero-shell`
        - exception slides: `S25`, `S31`, `S33`

        ## Slide Briefs

        ### S25. 실전 워크플로우와 도구
- source section: `docs/02-seminar/prose/07-practical-workflow-and-tooling.md`
- layout family: `section`
- density: `light`
- reference shell: `section-divider-shell`
- claim: 좋은 workflow는 격리와 handoff와 평가를 실전 습관으로 굳힌 운영 구조다
- supporting points:
  - Write
  - Select
  - Compress
- must-keep terms: `Plan-Critic-Build`, `Observability`
- do-not-say: 도구만 바꾸면 해결된다
- evidence requirement: prose source only
- speaker intent: 원리에서 workflow로 내려오는 전환 지점을 연다

### S26. 네 동사로 굴러간다
- source section: `docs/02-seminar/prose/07-practical-workflow-and-tooling.md`
- layout family: `content`
- density: `medium`
- reference shell: `content-three-card-shell`
- claim: 실전 워크플로우는 Write, Select, Compress, Isolate라는 네 동사 위에서 굴러간다
- supporting points:
  - 쓰기와 선택
  - 압축
  - 격리
- must-keep terms: `Write`, `Select`, `Compress`, `Isolate`
- do-not-say: 한 번에 길게 붙들기
- evidence requirement: prose source only
- speaker intent: workflow를 기억 가능한 동사 묶음으로 압축한다

### S27. Plan-Critic-Build
- source section: `docs/02-seminar/prose/07-practical-workflow-and-tooling.md`
- layout family: `content`
- density: `medium`
- reference shell: `content-three-step-shell`
- claim: 구현 전에 계획을 떼어 놓고, 비평을 거친 뒤, 마지막에만 생산을 밀어야 한다
- supporting points:
  - Plan
  - Critic
  - Build
- must-keep terms: `Plan-Critic-Build`
- do-not-say: 생각하면서 바로 구현하면 더 빠르다
- evidence requirement: prose source only
- speaker intent: 실행 전 사고를 떼어 놓는 이유를 구조로 보여 준다

### S28. gate와 observability
- source section: `docs/02-seminar/prose/07-practical-workflow-and-tooling.md`
- layout family: `content`
- density: `medium`
- reference shell: `content-three-card-shell`
- claim: 좋은 workflow는 pass/fail보다 먼저 gate와 observability를 세운다
- supporting points:
  - pre-HTML gate
  - post-HTML gate
  - trace와 checkpoint
- must-keep terms: `gate`, `Observability`
- do-not-say: 마지막에만 한 번 보면 된다
- evidence requirement: prose source only
- speaker intent: 검증을 마지막 이벤트가 아니라 운영 구조로 보게 만든다

### S29. 메인 컨텍스트를 지키는 운영
- source section: `docs/02-seminar/prose/07-practical-workflow-and-tooling.md`
- layout family: `content`
- density: `medium`
- reference shell: `content-three-card-shell`
- claim: 메인 컨텍스트는 가장 비싼 자산이므로 물리적 운영으로 보호해야 한다
- supporting points:
  - cmux
  - Git Worktree
  - issue와 PR
- must-keep terms: `cmux`, `Git Worktree`, `PR`
- do-not-say: 한 세션에 다 몰아 넣자
- evidence requirement: prose source only
- speaker intent: 추상 원리를 물리적 운영 습관으로 내려놓는다

### S30. 이 발표는 이렇게 만들었다
- source section: `docs/02-seminar/prose/08-how-this-presentation-was-made.md`
- layout family: `content`
- density: `medium`
- reference shell: `content-three-step-shell`
- claim: 이 발표의 제작 과정 자체가 source, prose, outline, HTML, gate로 이어지는 하네스 사례다
- supporting points:
  - source를 입력층에 가뒀다
  - prose를 canonical source로 세웠다
  - outline과 manifest 뒤에 HTML을 붙였다
- must-keep terms: `outline`, `manifest`, `Codex`
- do-not-say: 처음부터 slide부터 열었다
- evidence requirement: prose source only
- speaker intent: 앞서 설명한 원리가 실제 제작 과정에 어떻게 꽂혔는지 보여 준다

### S31. 우리가 다음에 해야 할 일
- source section: `docs/02-seminar/prose/09-what-we-should-do-next.md`
- layout family: `section`
- density: `light`
- reference shell: `section-divider-shell`
- claim: 지금 필요한 것은 새 모델 소식보다 작업 환경의 원칙을 먼저 고정하는 일이다
- supporting points:
  - rules
  - gates
  - harness
- must-keep terms: `Harness Engineer`
- do-not-say: 툴 적응만 빨리 하면 된다
- evidence requirement: prose source only
- speaker intent: 사례를 구경으로 끝내지 않고 습관으로 번역하는 장이다

### S32. 암묵지를 밖으로 꺼내라
- source section: `docs/02-seminar/prose/09-what-we-should-do-next.md`
- layout family: `content`
- density: `medium`
- reference shell: `content-three-card-shell`
- claim: 암묵지를 문서와 규칙과 상태 파일로 밖에 꺼내야 숙련이 재사용 가능한 운영 자산이 된다
- supporting points:
  - 규칙 파일
  - 결정론적 gate
  - 세션 밖 상태
- must-keep terms: `4D`, `Thought Partner`
- do-not-say: 프롬프트 몇 줄만 더 잘 쓰면 된다
- evidence requirement: prose source only
- speaker intent: 당장 다음 주에 시작할 습관으로 번역한다

### S33. Harness Engineer가 새 역할이다
- source section: `docs/02-seminar/prose/09-what-we-should-do-next.md`
- layout family: `title`
- density: `light`
- reference shell: `title-hero-shell`
- claim: 숙련은 사라지지 않고 하네스를 설계하고 운영하는 능력 쪽으로 이동한다
- supporting points:
  - 규칙을 밖으로 빼내라
  - 결정론적 문을 세워라
  - 삭제 조건까지 같이 설계하라
- must-keep terms: `Harness Engineer`, `Build to Delete`
- do-not-say: 개발자는 이제 필요 없다
- evidence requirement: prose source only
- speaker intent: 발표 전체를 한 문장으로 닫고 다음 행동으로 밀어 준다

        ## Batch Risks

        - title 길이는 한 줄을 유지한다
        - 밝은 minimal-light 테마에 맞게 body copy를 더 짧게 유지한다
        - shell drift보다 copy 축약을 먼저 선택한다
