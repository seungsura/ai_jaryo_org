        # Chapter Batch

        - batch id: `batch-02`
        - chapter or theme: sections `03, 04`
        - approved source files: `docs/02-seminar/prose/03-ai-era-methodology.md`, `docs/02-seminar/prose/04-harness-and-context-engineering.md`
        - planned slide ids: `S11`, `S12`, `S13`, `S14`, `S15`, `S16`, `S17`, `S18`
        - default layout families: `content`, `section`
        - approved reference shells: `content-three-card-shell`, `content-three-step-shell`, `section-divider-shell`
        - exception slides: `S11`, `S15`

        ## Slide Briefs

        ### S11. 방법론이 다시 앞에 온다
- source section: `docs/02-seminar/prose/03-ai-era-methodology.md`
- layout family: `section`
- density: `light`
- reference shell: `section-divider-shell`
- claim: 에이전트 자율성이 커질수록 무엇을 만들지와 어디서 멈출지가 더 중요해진다
- supporting points:
  - SDD
  - TDD
  - Harness
- must-keep terms: `SDD`, `TDD`
- do-not-say: 방법론은 이제 구식이다
- evidence requirement: prose source only
- speaker intent: 속도보다 방향 고정과 검증이 앞서는 이유를 여는 장이다

### S12. 왜 지금 방법론인가
- source section: `docs/02-seminar/prose/03-ai-era-methodology.md`
- layout family: `content`
- density: `medium`
- reference shell: `content-three-step-shell`
- claim: AI 코딩의 대중화는 곧 방향 고정과 검증 규율을 다시 전면으로 끌어냈다
- supporting points:
  - Vibe Coding의 속도
  - Spec-first의 반작용
  - TDD의 재등장
- must-keep terms: `Vibe Coding`, `Spec-first`, `TDD`
- do-not-say: 속도는 이제 쓸모없다
- evidence requirement: prose source only
- speaker intent: 업계 흐름을 반작용의 연대기로 읽게 만든다

### S13. Spec-first가 방향을 못 박는다
- source section: `docs/02-seminar/prose/03-ai-era-methodology.md`
- layout family: `content`
- density: `medium`
- reference shell: `content-three-card-shell`
- claim: 구현 전에 목적, 범위, 완료 기준을 고정해야 에이전트의 속도가 방향을 해치지 않는다
- supporting points:
  - 무엇을 만들지
  - 무엇을 빼야 하는지
  - 무엇을 통과로 볼지
- must-keep terms: `Spec-first`, `GitHub Spec Kit`
- do-not-say: 문서만 잘 쓰면 구현은 자동이다
- evidence requirement: prose source only
- speaker intent: Spec-first의 실무적 이유를 세 기준으로 압축한다

### S14. TDD가 가장 거친 가드레일
- source section: `docs/02-seminar/prose/03-ai-era-methodology.md`
- layout family: `content`
- density: `medium`
- reference shell: `content-three-step-shell`
- claim: TDD는 품질 기법이자 에이전트가 멋대로 기준을 바꾸지 못하게 막는 권한 통제 기법이다
- supporting points:
  - Red
  - Green
  - Review
- must-keep terms: `TDD`, `Red`, `Green`
- do-not-say: 테스트만 있으면 모든 게 해결된다
- evidence requirement: prose source only
- speaker intent: TDD를 품질 관리에서 운영 통제로 재정의한다

### S15. 프롬프트를 넘어서 Harness
- source section: `docs/02-seminar/prose/04-harness-and-context-engineering.md`
- layout family: `section`
- density: `light`
- reference shell: `section-divider-shell`
- claim: 이제 병목은 문장 자체보다 에이전트를 움직이는 운영 구조에 있다
- supporting points:
  - Prompt
  - Context
  - Harness
- must-keep terms: `Prompt`, `Context`, `Harness`
- do-not-say: 프롬프트는 아무 의미가 없다
- evidence requirement: prose source only
- speaker intent: 문장 중심 사고에서 구조 중심 사고로 전환한다

### S16. Prompt, Context, Harness
- source section: `docs/02-seminar/prose/04-harness-and-context-engineering.md`
- layout family: `content`
- density: `medium`
- reference shell: `content-three-card-shell`
- claim: 세 층은 서로 다른 질문에 답하고, 가장 바깥 질문이 가장 큰 위험을 다룬다
- supporting points:
  - Prompt는 말의 품질
  - Context는 정보의 품질
  - Harness는 시스템 안정성
- must-keep terms: `Prompt`, `Context`, `Harness`
- do-not-say: 세 층은 서로 대체 가능하다
- evidence requirement: prose source only
- speaker intent: 세 층을 섞지 말아야 하는 이유를 짧게 보여 준다

### S17. Agent = Model + Harness
- source section: `docs/02-seminar/prose/04-harness-and-context-engineering.md`
- layout family: `content`
- density: `medium`
- reference shell: `content-three-card-shell`
- claim: 에이전트의 품질은 모델 자체와 그 모델을 둘러싼 하네스가 함께 만든다
- supporting points:
  - Model은 생성의 엔진
  - Tools는 행동의 팔
  - Harness는 통제와 관측의 뼈대
- must-keep terms: `Agent = Model + Harness`
- do-not-say: 좋은 모델이면 하네스가 필요 없다
- evidence requirement: prose source only
- speaker intent: 에이전트를 하나의 런타임 시스템으로 보게 만든다

### S18. 하네스의 다섯 블록
- source section: `docs/02-seminar/prose/04-harness-and-context-engineering.md`
- layout family: `content`
- density: `medium`
- reference shell: `content-three-card-shell`
- claim: 하네스의 다섯 블록은 결국 경계 고정, 결과 필터링, 상태 가시화로 묶인다
- supporting points:
  - Guardrails와 Specification
  - Verification
  - State Management와 Observability
- must-keep terms: `Guardrails`, `Specification`, `Verification`, `State Management`, `Observability`
- do-not-say: 툴만 많으면 하네스가 된다
- evidence requirement: prose source only
- speaker intent: 다섯 블록을 세 묶음으로 압축해 기억 가능하게 만든다

        ## Batch Risks

        - title 길이는 한 줄을 유지한다
        - 밝은 minimal-light 테마에 맞게 body copy를 더 짧게 유지한다
        - shell drift보다 copy 축약을 먼저 선택한다
