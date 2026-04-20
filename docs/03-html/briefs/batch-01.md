        # Chapter Batch

        - batch id: `batch-01`
        - chapter or theme: sections `00, 01, 02`
        - approved source files: `docs/02-seminar/prose/00-overview.md`, `docs/02-seminar/prose/01-where-coding-is-going.md`, `docs/02-seminar/prose/02-why-claude-code.md`
        - planned slide ids: `S01`, `S02`, `S03`, `S04`, `S05`, `S06`, `S07`, `S08`, `S09`, `S10`
        - default layout families: `agenda`, `content`, `section`, `title`
        - approved reference shells: `agenda-list-shell`, `content-three-card-shell`, `content-three-step-shell`, `section-divider-shell`, `title-hero-shell`
        - exception slides: `S01`, `S02`, `S03`, `S06`

        ## Slide Briefs

        ### S01. Harness를 설계하는 법
- source section: `docs/02-seminar/prose/00-overview.md`
- layout family: `title`
- density: `light`
- reference shell: `title-hero-shell`
- claim: AI 시대의 경쟁력은 더 좋은 모델보다 더 나은 Harness 설계에서 갈린다
- supporting points:
  - 코딩의 중심이 이동한다
  - 도구는 Harness로 수렴한다
  - workflow와 사례까지 본다
- must-keep terms: `Harness`
- do-not-say: 제품 소개 발표, 모델 비교 쇼케이스
- evidence requirement: prose source only
- speaker intent: 문제의식과 발표 범위를 한 번에 고정한다

### S02. 전체 구조
- source section: `docs/02-seminar/prose/00-overview.md`
- layout family: `agenda`
- density: `medium`
- reference shell: `agenda-list-shell`
- claim: 이 발표는 이동, 수렴, 방법, 운영, 실천의 다섯 묶음으로 읽힌다
- supporting points:
  - 코딩의 중심 이동
  - 도구의 Harness 수렴
  - 방법론과 실패 패턴
  - 실전 workflow와 제작 사례
- must-keep terms: `Harness`, `workflow`
- do-not-say: 세부 구현 튜토리얼
- evidence requirement: prose source only
- speaker intent: 청중이 전체 지도를 먼저 잡게 만든다

### S03. 코딩은 어디로 가는가
- source section: `docs/02-seminar/prose/01-where-coding-is-going.md`
- layout family: `section`
- density: `light`
- reference shell: `section-divider-shell`
- claim: 질문은 코딩이 사라지는가가 아니라 숙련이 어디로 이동하는가다
- supporting points:
  - Prompt
  - Context
  - Harness
- must-keep terms: `Prompt`, `Context`, `Harness`
- do-not-say: 개발자 소멸론
- evidence requirement: prose source only
- speaker intent: 첫 장의 질문을 정확한 질문으로 바꿔 놓는다

### S04. 직접 하던 일은 계속 줄어든다
- source section: `docs/02-seminar/prose/01-where-coding-is-going.md`
- layout family: `content`
- density: `medium`
- reference shell: `content-three-step-shell`
- claim: 소프트웨어 역사는 늘 더 낮은 일을 위임하고 더 큰 구조를 맡기는 방향으로 왔다
- supporting points:
  - 기계와 직접 씨름하던 시기
  - 프레임워크와 클라우드로의 위임
  - AI 에이전트와 환경 설계
- must-keep terms: `AI 에이전트`
- do-not-say: 이번 변화만 유별난 예외
- evidence requirement: prose source only
- speaker intent: 현재 변화를 긴 역사 위에 올려 놓는다

### S05. 타이핑보다 환경 설계가 앞선다
- source section: `docs/02-seminar/prose/01-where-coding-is-going.md`
- layout family: `content`
- density: `medium`
- reference shell: `content-three-card-shell`
- claim: 문서, 문맥, 검증을 어떻게 고정하느냐가 결과의 질을 갈라놓는다
- supporting points:
  - 규칙 파일이 기준선을 고정한다
  - 컨텍스트가 시야를 결정한다
  - 검증 루프가 실패 확산을 막는다
- must-keep terms: `AGENTS.md`, `Harness Engineer`
- do-not-say: 타이핑 실력은 이제 무의미하다
- evidence requirement: prose source only
- speaker intent: 새 숙련의 위치를 세 축으로 압축한다

### S06. 왜 Claude Code인가
- source section: `docs/02-seminar/prose/02-why-claude-code.md`
- layout family: `section`
- density: `light`
- reference shell: `section-divider-shell`
- claim: 중요한 것은 제품 선호가 아니라 도구 진화의 방향을 가장 선명하게 보여 주는 사례라는 점이다
- supporting points:
  - Claude Code
  - Cursor
  - Copilot
- must-keep terms: `Claude Code`, `Harness`
- do-not-say: 도구 순위 발표
- evidence requirement: prose source only
- speaker intent: 제품 비교가 아니라 구조 읽기라는 렌즈를 다시 고정한다

### S07. 도구 진화의 세 단계
- source section: `docs/02-seminar/prose/02-why-claude-code.md`
- layout family: `content`
- density: `medium`
- reference shell: `content-three-step-shell`
- claim: 코딩 도구의 초점은 Prompt에서 Context를 지나 Harness로 이동했다
- supporting points:
  - Prompt Engineering
  - Context Engineering
  - Harness Engineering
- must-keep terms: `Prompt Engineering`, `Context Engineering`, `Harness Engineering`
- do-not-say: 프롬프트는 이제 무의미하다
- evidence requirement: prose source only
- speaker intent: 도구 진화의 큰 흐름을 세 단계로 압축한다

### S08. 에이전트 루프가 문제를 바꾼다
- source section: `docs/02-seminar/prose/02-why-claude-code.md`
- layout family: `content`
- density: `medium`
- reference shell: `content-three-step-shell`
- claim: 긴 작업에서 핵심은 답변 품질보다 루프를 어떤 규칙 아래 두느냐다
- supporting points:
  - Context 수집
  - Action 실행
  - Verify 반복
- must-keep terms: `Context`, `Action`, `Verify`
- do-not-say: 도구가 알아서 안전해진다
- evidence requirement: prose source only
- speaker intent: 에이전트 작업의 위험 지점을 한 루프로 보이게 한다

### S09. Claude Code는 하네스를 드러낸다
- source section: `docs/02-seminar/prose/02-why-claude-code.md`
- layout family: `content`
- density: `medium`
- reference shell: `content-three-card-shell`
- claim: Claude Code가 대표 사례인 이유는 하네스 요소를 가장 노골적으로 드러내기 때문이다
- supporting points:
  - Plan Mode
  - approval과 permission
  - skills와 subagents
- must-keep terms: `Plan Mode`, `Skills`, `Subagents`
- do-not-say: 기능이 많아서 최고다
- evidence requirement: prose source only
- speaker intent: 대표 사례의 이유를 기능 나열이 아니라 구조로 설명한다

### S10. 모델 경쟁이 아니라 하네스 경쟁
- source section: `docs/02-seminar/prose/02-why-claude-code.md`
- layout family: `content`
- density: `medium`
- reference shell: `content-three-card-shell`
- claim: 산업 전체의 경쟁 축은 모델 하나보다 하네스 설계 쪽으로 이동하고 있다
- supporting points:
  - Codex의 agent-first workspace
  - Claude Code의 runtime control
  - OpenCode의 planner와 permission
- must-keep terms: `Codex`, `Claude Code`, `OpenCode`
- do-not-say: 모든 도구가 사실상 같다
- evidence requirement: prose source only
- speaker intent: 산업 전체의 수렴을 세 사례로 압축한다

        ## Batch Risks

        - title 길이는 한 줄을 유지한다
        - 밝은 minimal-light 테마에 맞게 body copy를 더 짧게 유지한다
        - shell drift보다 copy 축약을 먼저 선택한다
