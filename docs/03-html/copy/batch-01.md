        # Korean Copy Packet

        - batch id: `batch-01`
        - active theme: `theme-minimal-light`
        - approved slide ids: `S01`, `S02`, `S03`, `S04`, `S05`, `S06`, `S07`, `S08`, `S09`, `S10`

        ### S01. Harness를 설계하는 법
- family: `title`
- shell: `title-hero-shell`
- lead: 챗봇과 씨름하는 대신, 에이전트가 일할 구조를 짠다
- body:
  - 타이핑보다 규칙과 검증이 앞에 온다
  - 도구 경쟁은 Harness 경쟁으로 모인다
  - 마지막은 실전 workflow와 제작 사례다

### S02. 전체 구조
- family: `agenda`
- shell: `agenda-list-shell`
- lead: 이동, 수렴, 방법, 운영, 실천 순으로 좁혀 간다
- agenda rows:
  - 01 | 이동 | 코딩의 중심이 손가락에서 운영 구조로 옮겨 간다
  - 02 | 수렴 | 도구 경쟁은 결국 Harness 경쟁으로 모인다
  - 03 | 방법 | Spec-first와 TDD가 다시 앞줄로 나온다
  - 04 | 운영 | 실패 패턴과 멀티 에이전트 운영 원리를 본다
  - 05 | 실천 | 이 발표 제작 과정과 다음 습관으로 닫는다

### S03. 코딩은 어디로 가는가
- family: `section`
- shell: `section-divider-shell`
- chapter marker: CHAPTER 01
- line: 타이핑이 사라지는가가 아니라 숙련이 어디로 옮겨 가는가
- keywords: Prompt, Context, Harness

### S04. 직접 하던 일은 계속 줄어든다
- family: `content`
- shell: `content-three-step-shell`
- chapter label: CHAPTER 01
- lead: 직접 제어에서 환경 설계로
- steps:
  - STEP 01 | 직접 제어 | 기계어와 포인터를 손으로 붙들었다 | 낮은 수준의 세부를 사람이 끝까지 책임졌다
  - STEP 02 | 위임 확장 | 프레임워크와 클라우드가 반복 작업을 가져갔다 | 직접 구현보다 구조 선택과 조합이 더 중요해졌다
  - STEP 03 | 환경 설계 | 코딩을 맡기고 환경을 설계 | 규칙, 문맥, 검증이 핵심 축 [focus]

### S05. 타이핑보다 환경 설계가 앞선다
- family: `content`
- shell: `content-three-card-shell`
- chapter label: CHAPTER 01
- lead: 손보다 먼저 붙들 일
- cards:
  - RULE | 규칙 | 문서와 규칙 파일이 기준선을 잠근다 | 참고 문서가 아니라 실행 기준선
  - CONTEXT | 문맥 | 무엇을 읽힐지 선택하는 일이 앞에 온다 | 시야를 잘못 주면 좋은 모델도 흔들림
  - VERIFY | 검증 | 결과를 걸러내는 루프가 실력을 드러낸다 | 새 역할은 Harness Engineer 쪽 [focus]

### S06. 왜 Claude Code인가
- family: `section`
- shell: `section-divider-shell`
- chapter marker: CHAPTER 02
- line: 중요한 것은 제품 선호가 아니라 도구 진화의 방향이다
- keywords: Claude Code, Cursor, Copilot

### S07. 도구 진화의 세 단계
- family: `content`
- shell: `content-three-step-shell`
- chapter label: CHAPTER 02
- lead: 질문도 바뀌었다. 무엇을 말할지에서 무엇을 통제할지로 갔다
- steps:
  - 2022 | Prompt | 어떻게 말해야 원하는 코드를 얻는가 | 초점은 지시문의 품질과 추론 기법에 있었다
  - 2025 | Context | 무엇을 보여 줘야 덜 틀리게 만드는가 | 프로젝트 전체를 읽히는 주입과 선별이 중요해졌다
  - 2026 | Harness | 무엇을 통제하고 어디서 멈출 것인가 | 권한, 검증, 상태, 분업이 경쟁력의 중심이 됐다 [focus]

### S08. 에이전트 루프가 문제를 바꾼다
- family: `content`
- shell: `content-three-step-shell`
- chapter label: CHAPTER 02
- lead: 루프가 길어질수록 Harness가 앞
- steps:
  - LOOP 01 | Gather | 무엇을 읽을지 잘못 고르면 출발부터 오염된다 | 쓰레기 문맥이 들어오면 이후 단계도 흔들림
  - LOOP 02 | Action | 권한이 느슨하면 실수는 곧바로 사고가 된다 | 수정과 실행은 도구 규칙 아래서만 안전
  - LOOP 03 | Verify | 검증이 약하면 틀린 방향으로 질주 | 바깥 구조가 없으면 멈출 지점도 사라짐 [focus]

### S09. Claude Code는 하네스를 드러낸다
- family: `content`
- shell: `content-three-card-shell`
- chapter label: CHAPTER 02
- lead: 좋은 에이전트의 기준
- cards:
  - PLAN | 계획 분리 | Plan Mode가 실행 전 사고를 떼어 놓는다 | 판단과 실행을 같은 층에 두지 않음
  - CONTROL | 권한 통제 | approval과 permission이 행동 경계를 잘게 나눈다 | 무엇을 못 하게 할지가 더 중요 [focus]
  - DIVIDE | 분업 구조 | skills와 subagents가 책임을 좁게 쪼갠다 | 에이전트를 하나 더 쓰는 이유가 선명

### S10. 모델 경쟁이 아니라 하네스 경쟁
- family: `content`
- shell: `content-three-card-shell`
- chapter label: CHAPTER 02
- lead: 도구 이름보다 구조
- cards:
  - OPENAI | Codex | agent-first workspace로 일의 단위를 다시 묶는다 | 문맥과 행동을 작업 공간 수준에서 다룸
  - ANTHROPIC | Claude Code | runtime control을 전면에 드러낸다 | 권한, 계획, 분업을 하네스 부품으로 보여 준다 [focus]
  - OTHER | OpenCode | planner와 permission 경계 | 도구 경쟁이 같은 구조 문제로 모인다는 증거
