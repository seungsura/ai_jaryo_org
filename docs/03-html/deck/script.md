# Seminar Script

- target deck: `docs/03-html/deck/index.html`
- scope: 00 overview + 01/02/03/04/05/06/07/08/09 chapters

## S001 Harness 잘 사용하기
- intent: 첫 장에서 제목, 부제, 발표자만 고정
- opening: 에이전트가 일할 환경 설계
- bridge: 제목과 부제만 두고, 발표자는 게임플랫폼 1팀 라승수로 표시한다.

## S002 시작하며
- intent: 챗봇 사용 경험과 도구 수렴을 Harness 문제로 연결
- opening: AI에게 무엇을 말할까에서 AI가 일할 환경 설계로 이동
- bridge: 좋은 결과는 한 번의 프롬프트보다 반복 가능한 구조에서 나온다는 흐름을 고정한다.

## S003 전체 목차
- intent: 00-overview의 목차 표를 한 장에 압축
- opening: Harness 관점으로 읽는 9개 장
- bridge: 전체 표를 한 장으로 보여 주고, 다음 장부터 각 항목을 순서대로 펼친다.

## S004 코딩은 사라지는가
- intent: 01장의 질문을 챕터 단위로 고정
- opening: 개발의 추상화 수준 상승
- bridge: 코딩이 사라지는가보다 개발자가 직접 붙들 일이 어디로 이동하는가를 묻는다.

## S005 기계어 → 어셈블리
- intent: source code block 기반 첫 전환 사례
- opening: 이진 코드 직접 작성 부담의 감소
- bridge: source markdown의 기계어와 어셈블리 코드 블록

## S006 어셈블리 → C/Pascal
- intent: source code block 기반 두 번째 전환 사례
- opening: 어셈블리 표현량에서 C 함수 표현으로
- bridge: source markdown의 어셈블리와 C 코드 블록

## S007 C → Java
- intent: source code block 기반 세 번째 전환 사례
- opening: 수동 메모리 관리에서 GC로
- bridge: source markdown의 C와 Java 코드 블록

## S008 Java → Python
- intent: source code block 기반 네 번째 전환 사례
- opening: 같은 출력과 더 짧은 표현
- bridge: source markdown의 Java와 Python 코드 블록

## S009 AI 개발
- intent: source prompt와 quote 기반 AI 개발 사례
- opening: 개발의 추상화 수준 상승
- bridge: source markdown의 AI 개발 prompt와 quote

## S010 직접 하던 일의 감소
- intent: 시대별 위임 표와 질문 반전
- opening: 직접 작성 부담의 지속적 위임
- bridge: 시대별 전환을 표로 압축하고, 변경된 source 질문을 독립된 한 줄로 배치한다.

## S011 숫자로 보는 변화
- intent: source 숫자 사실만 압축
- opening: 수동 코드 작성 비중 감소의 현장 신호
- bridge: source markdown의 YC W25, OpenAI Codex 팀, Meta 엔지니어 사례

## S012 문서가 코드
- intent: page-011 reference 기반 문서 card layout
- opening: 에이전트가 매 세션 읽고 따라야 할 운영 규칙
- bridge: source markdown의 규칙 파일 네 가지

## S013 개발자의 새로운 역할
- intent: reference layout 기반 evolution and analogy blocks
- opening: 환경 설계와 결과 판단
- bridge: source markdown의 개발자 역할 bullet list

## S014 그래도 기초가 중요하다
- intent: reference layout 기반 quote and summary cards
- opening: AI 코딩은 에이전트가 일할 환경을 설계하고 검증하는 영역
- bridge: source markdown의 기본기와 시스템 이해 문단

## S015 왜 Claude Code인가
- intent: 02장 진입과 제품 리뷰가 아닌 흐름 분석 고정
- opening: AI 코딩 도구 흐름의 대표 사례
- bridge: Claude Code를 특정 제품 리뷰가 아니라 하네스 흐름의 대표 사례로 둔다.

## S016 에이전틱 코딩의 실제 성과
- intent: page-017 reference 기반 성과 metric cards
- opening: 속도, 온보딩, 불가능하던 작업의 변화
- bridge: source markdown의 에이전틱 코딩 실제 성과와 page-017 reference

## S017 1막: Copilot과 ChatGPT, 프롬프트의 시대
- intent: 프롬프트 시대의 출발점 비교
- opening: 자동완성에서 자연어 지시 인터페이스로
- bridge: source markdown의 초기 Copilot과 ChatGPT 전환

## S018 CoT / ReAct / ToT
- intent: CoT / ReAct / ToT native three-card comparison
- opening: 세 추론 패턴의 구조 차이
- bridge: source markdown의 CoT, ReAct, ToT row와 approved page-064 layout 구조

## S019 네 가지 에이전틱 패턴
- intent: Andrew Ng four patterns node-only native quadrant
- opening: 모델 바깥 구조가 성능을 좌우
- bridge: source markdown의 Andrew Ng 네 가지 패턴과 approved 05 asset 구조, diagram 내부 text 제거

## S020 프롬프트 시대의 벽
- intent: 프롬프트 시대의 한계
- opening: 모델은 보지 못한 것을 알 수 없음
- bridge: source markdown의 Blind Prompting 문단 + LangChain/Vivek Trivedy context-window quote

## S021 2막: Cursor와 컨텍스트의 시대
- intent: 초기 Copilot과 Cursor 계열 도구 비교
- opening: 현재 파일에서 전체 코드베이스로
- bridge: source markdown의 Cursor 비교 표, Tools 문장, Context Engineering 문단

## S022 Cursor 아키텍처
- intent: Cursor architecture raw asset with source-backed arrow flow
- opening: 긴 프롬프트가 아니라 검색기와 편집기
- bridge: 사용자 승인 예외: approved 06 asset raw embed + source text arrow graph

## S023 컨텍스트만으로는 부족하다
- intent: 컨텍스트 시대의 벽을 통제 관점으로 재구성
- opening: 좋은 입력만으로는 루프 통제 불가
- bridge: source heading + risk list + control question 4개를 context-wall 구조로 압축

## S024 3막: 하네스의 시대
- intent: Harness era minimal transition
- opening: 작업 환경 전체를 품기 시작한 코딩 도구
- bridge: source markdown + user-requested S026 simplification

## S025 3막: Claude Code, Codex, OpenCode 와 하네스의 시대
- intent: 2장 결론 관계식을 source heading 중심으로 고정
- opening: Agent = Model + Harness
- bridge: source markdown 3막 heading + 시대 구분 표 + 포함 관계 문장

## S026 AI 시대의 개발 방법론
- intent: 03장 진입을 source heading 키워드와 함께 고정
- opening: TDD·SDD·Spec-first 재부상
- bridge: 03장 source heading의 핵심 축(SDD/TDD/Waterfall)만 keyword rail로 노출

## S027 왜 지금 방법론
- intent: AI 코딩 방법론 재부상 연대기
- opening: AI에게 무엇을 시킬지, 어떻게 검증할 것인지
- bridge: 생성 속도에서 검증 절차로 생각이 이동한 흐름

## S028 SDD
- intent: GitHub Spec Kit의 세 단계와 멈춤 장치
- opening: 스펙이 진실의 원천
- bridge: 요구사항, 계획, 태스크를 파일로 고정하는 흐름

## S029 TDD (Test-Driven Development)
- intent: Page 028 TDD lead와 anti-cheat 규칙
- opening: 테스트를 먼저 쓰고, 통과하는 코드를 나중에 쓴다
- bridge: 테스트가 에이전트의 자유를 제한하는 통제선

## S030 Waterfall vs SDD
- intent: Royce 1970과 spec-driven.md evidence로 Waterfall vs SDD 비교
- opening: Waterfall은 순차적으로 진행되고, SDD는 스펙을 실행 기준으로 둔다
- bridge: 요구사항·설계·코딩·테스트 vs specification·plan·tasks

## S031 SDD + TDD가 Harness로 이어지는 이유
- intent: 03장에서 04장 Harness 구조로 넘어가는 bridge
- opening: 이 시스템이 곧 하네스 엔지니어링
- bridge: 스펙과 테스트 루프를 사람이 매번 손으로 굴리지 않도록 시스템화

## S032 프롬프트를 넘어서
- intent: 04장 진입을 알리는 section divider
- opening: Prompt, Context, Harness
- bridge: 프롬프트와 컨텍스트를 포함하는 하네스 구조로 진입

## S033 Prompt, Context, Harness
- intent: source page 36/37 의미를 한 장의 hierarchy로 압축
- opening: Prompt ⊂ Context ⊂ Harness
- bridge: 프롬프트, 컨텍스트, 하네스의 포함 관계

## S034 Agent = Model + Harness
- intent: 공식, 인용구, 여섯 구성 요소를 한 장에 배치
- opening: 모델이 아닌 것은 전부 하네스입니다.
- bridge: Agent 공식과 하네스의 여섯 구성 요소

## S035 에이전트 루프: 하네스의 심장
- intent: gather context, take action, verify work, repeat loop
- opening: 거의 모든 에이전트가 반복하는 4단계.
- bridge: 거의 모든 코딩 에이전트가 반복하는 네 단계

## S036 하네스의 책임
- intent: 5 responsibility cards와 설계 순서 rail
- opening: 다섯 개 기능 블록
- bridge: 운영 관점에서 보는 하네스의 책임

## S037 하네스의 도구
- intent: 책임 anchor와 도구 node의 다대다 관계 지도
- opening: 책임과 도구는 1:1이 아니다
- bridge: 기능 블록과 도구 레이어는 1:1로 대응하지 않음

## S038 Context Engineering
- intent: Write, Select, Compress, Isolate 네 전략
- opening: Anthropic의 4가지 전략: 필요한 정보만 남기고 잡음은 덜어낸다.
- bridge: 좋은 컨텍스트는 넓은 컨텍스트가 아니라 선별된 컨텍스트

## S039 MCP와 Context 7
- intent: MCP 원리와 Context 7 MCP 서버 연결 의미
- opening: 연결 방식을 표준화
- bridge: 외부 도구와 최신 문서 연결은 컨텍스트 엔지니어링의 핵심 인프라

## S040 RAG vs Context 7
- intent: RAG와 Context 7의 차이를 표로 비교
- opening: 검색 범위와 기준 시점의 차이
- bridge: RAG는 넓은 저장소 검색, Context 7은 최신/버전 지정 문서 확인

## S041 Memory: 세션을 넘어서는 기억
- intent: 외부 artifact map과 memory claim
- opening: 대화창을 기억 저장소로 착각하지 않는다
- bridge: 상태와 근거는 파일 시스템, Git, 이슈, PR, 문서로 나가야 함

## S042 Stable Prefix와 Variable Suffix
- intent: prefix/suffix diagram
- opening: 잘 쓰는 것 못지않게 안 바꾸는 것도 능력
- bridge: 자주 변하지 않는 것은 앞쪽에, 최신 입력과 도구 결과는 뒤쪽에 둠

## S043 하네스는 환경 그 자체다
- intent: chapter 04 closing statement
- opening: 필요한 파일, 필요한 도구, 필요한 규칙
- bridge: Harness Builder는 에이전트가 쓸 수 있는 환경을 만드는 사람

## S044 이렇게 하면 망한다
- intent: chapter 05 opener
- opening: 한계와 실패 패턴
- bridge: 05장 진입을 알리는 opener

## S045 오류의 나비효과
- intent: 작은 오해가 루프 전체로 누적되는 구조
- opening: 작은 오류가 다음 단계로 번진다
- bridge: 읽기-수정-실행-판단 루프와 단계별 성공률

## S046 작업이 길어질 때 특히 위험한 이유
- intent: 첫 번째 결과물에서 20 단계 결과물까지의 성공률 하락
- opening: 작업이 길어질수록 기준이 달라진다
- bridge: 1 단계 95%에서 20 단계 36%로 내려가는 카드형 진행

## S047 컨텍스트가 길수록 항상 좋은 것은 아니다
- intent: 길어진 컨텍스트의 잡음 문제
- opening: 신호 대 잡음비가 핵심이다
- bridge: 컨텍스트는 길이보다 신호 대 잡음비

## S048 대표 실패 패턴 네 가지
- intent: 컨텍스트 실패 모드 네 가지 정리
- opening: 기억과 잡음과 규칙이 하나의 컨텍스트 안에서 썩고 있다
- bridge: Drew Breunig 실패 모드와 source transcription facts

## S049 현실에서 보이는 증상들
- intent: 실전 증상 3종을 source-backed 카드로 압축
- opening: 작은 오류가 누적되면 증상으로 드러난다
- bridge: source markdown의 AI Slop, Doom Loop, Shadow Agent 문단

## S050 Context Rot: 길어진 기억은 조용히 썩는다
- intent: Context Rot의 길이 문제와 외부 아티팩트 전환
- opening: 길이보다 신호 대 잡음비가 중요하다
- bridge: source markdown의 Context Rot 설명과 아티팩트 보존 문단

## S051 신뢰는 조율되어야 한다
- intent: Calibrated Trust를 비용 구간으로 압축
- opening: 자율성은 작업 비용에 맞춰 조절해야 한다
- bridge: source markdown의 Calibrated Trust 문단

## S052 결정 제어와 확률 제어를 분리하라
- intent: 결정론적 제어와 확률적 제어의 분리
- opening: 기계가 확인할 것은 기계에게, 유연한 판단은 AI에게
- bridge: source markdown의 deterministic / probabilistic control 구분

## S053 더 긴 컨텍스트보다 더 좋은 게이트
- intent: 05장 결론을 source-backed gate principle로 마무리
- opening: 더 긴 컨텍스트보다 더 좋은 게이트
- bridge: source markdown의 conclusion block

## S054 왜 하나의 에이전트만으로는 부족한가
- intent: 단일 에이전트의 세 가지 문제를 3-card 구조로 압축
- opening: 멀티 에이전트는 세 가지 벽을 줄이기 위한 구조
- bridge: source lines 3-11, page 063 structure-only reference

## S055 하나의 에이전트 = 하나의 역할
- intent: 다섯 패턴과 Planner/Generator/Evaluator 원칙 연결
- opening: 멀티 에이전트의 본질은 병렬화가 아니라 분해
- bridge: source lines 15-24, page 064 layout reference

## S056 1. Sub-Agent: 중간 작업을 격리하는 기본형
- intent: Main -> Sub-Agent -> summary 흐름과 least privilege 원칙
- opening: 서브 에이전트는 메인 컨텍스트를 지키는 격리 패턴
- bridge: source lines 28-51, page 066 structure reference

## S057 Advisor 전략: 작은 실행자, 큰 자문
- intent: executor와 advisor의 결정 책임 분리
- opening: 막히는 순간에만 상위 판단을 빌림
- bridge: source lines 55-59, page 065 high-contrast split reference

## S058 2. Orchestrator: 계획자 하나가 여러 실행자를 배치한다
- intent: source numbered flow를 1:N chain으로 구현
- opening: Orchestrator는 1:N 위임 구조
- bridge: source lines 63-76, page 064/066 fan-out reference

## S059 3. Parallel: 같은 목표를 평면으로 벌리고 나중에 합친다
- intent: 독립 lane과 merge 조건을 source 예시로 압축
- opening: 좋은 병렬은 서로를 더럽히지 않는 구조
- bridge: source lines 80-92, page 064 parallel lanes reference

## S060 4. GAN-Style: 생성자와 평가자를 분리한다
- intent: Planner/Generator/Evaluator loop
- opening: 생성과 평가는 같은 손에 묶지 않음
- bridge: source lines 96-108, page 064 feedback-loop reference

## S061 5. Agent Teams: 양방향 대화가 가능한 팀을 만든다
- intent: team graph reference를 role cards로 재구성
- opening: Agent Teams는 함께 토론하고 합의하는 구조
- bridge: source lines 112-124, page 067 structure reference

## S062 Sub-Agent와 Agent Team은 다르다
- intent: source table을 그대로 비교 표로 구성
- opening: 단순한 심부름은 Sub-Agent, 양방향 토론은 Agent Team
- bridge: source lines 128-138, page 065 reference

## S063 설계 원칙: 패턴보다 경계가 중요하다
- intent: 다섯 설계 원칙을 source 문구로 카드화
- opening: 컨텍스트, 역할, 검증을 쪼개는 경계 설계
- bridge: source lines 142-162, page 068 reference

## S064 설계 원칙: 패턴보다 경계가 중요하다
- intent: SOLID reinterpretation table
- opening: SOLID도 에이전트 중심으로 다시 읽힘
- bridge: source lines 164-175

## S065 멀티 모델과 멀티 에이전트
- intent: 멀티 모델 distinction과 Claude/Codex/Gemini 역할
- opening: 여러 모델 교차 사용은 독립 평가자 풀에 가까움
- bridge: source lines 179-183

## S066 결론: 더 많은 AI가 아니라 더 좁은 역할의 AI 여럿
- intent: chapter 06 closing lines
- opening: 더 좁은 역할의 AI 여럿을, 더 명확한 경계 안에서 일하게 한다
- bridge: source lines 187-189

## S067 시작하며: 두 가지 막다른 길
- intent: 두 dead-end split comparison
- opening: 출발점은 원리를 시스템이 대신 강제하게 만드는 일
- bridge: source lines 3-9, page 070 reference

## S068 OMC(Oh My Claude Code)
- intent: preset command/routing map without canonical-only claims
- opening: preset pack이 모드와 검증 루프를 먼저 고정
- bridge: source lines 13-31, page 064/067 structure reference

## S069 Plan-Critic-Build
- intent: Plan/Critic/Build와 Explore/Plan/Code/Commit 연결
- opening: 합의된 뒤에만 실행
- bridge: source lines 36-49

## S070 필요없는 도구는 덜어내라
- intent: tool curation과 gate 목록
- opening: 도구 큐레이션은 취향이 아니라 성능 문제
- bridge: source lines 53-69

## S071 Approval, Auto-accept, Plan Mode
- intent: source table exact-mode mapping
- opening: 위험도에 따라 모드를 나눔
- bridge: source lines 73-82

## S072 반복의 자산화
- intent: /context, /compact, /clear와 Skills/Hooks/Commands/AGENTS mapping
- opening: 반복되는 지침은 시스템 바깥에 있어야 할 지식
- bridge: source lines 86-102, page 066/067 split reference

## S073 Ralph Loop
- intent: PROMPT.md loop
- opening: PROMPT.md 하나를 루프의 중심에 둠
- bridge: source lines 106-110, page 053 structure-only reference

## S074 암묵지를 파일로 뽑아내라
- intent: four numbered steps and closing source
- opening: 암묵지가 파일로 옮겨지는 순간 하네스가 됨
- bridge: source lines 114-123, page 054 structure-only reference

## S075 한 모델에만 기대지 않는다
- intent: Claude/Codex/Gemini cross-check roles
- opening: 여러 모델의 응답을 합의, 불일치, 불확실로 나눔
- bridge: source lines 127-135, page 072 reference

## S076 cmux와 Git Worktree
- intent: four-window workspace map
- opening: 창과 작업 디렉터리를 나누어 메인 컨텍스트를 보호
- bridge: source lines 139-152, page 073 reference

## S077 세션이 아니라 이슈가 상태를 들고 간다
- intent: issue -> worktree -> session -> PR -> verification chain
- opening: 이슈는 세션보다 오래가는 상태 저장소
- bridge: source lines 156-169, page 074 reference

## S078 첫 주에 바로 세울 수 있는 최소 워크플로우
- intent: six minimal habits
- opening: 대화창의 기준을 작업 환경의 일부로 만드는 첫 단계
- bridge: source lines 173-182

## S079 결론: 실전 워크플로우의 중심은 운영 구조다
- intent: chapter 07 closing lines
- opening: 검증과 흔적 위에 다음 판단을 올리는 운영 구조
- bridge: source lines 186-188, page 068/063 closing structure reference

## S080 이 글과 발표가 만들어진 과정
- intent: 08장 chapter divider
- opening: 이 글과 발표가 만들어진 과정
- bridge: Page 076-077 and source 08 chapter entry

## S081 이 글과 발표가 만들어진 과정
- intent: 코드/PPT 직접 제작이 아니라 하네스 설계였다는 증거 진입
- opening: 코드 한 줄, PPT 한 장도 직접 만들지 않았습니다
- bridge: source 08 lines 1-3; canonical Page 076

## S082 이 발표를 만든 방법
- intent: source에서 pdf까지 이어지는 제작 pipeline
- opening: source → prose → outline → html → pdf
- bridge: source 08 lines 5-30; canonical Page 077

## S083 재료 1 source 수집
- intent: source 계층과 중요도 분리
- opening: 불확실한 부분은 억지로 메우지 않았습니다
- bridge: source 08 lines 32-38; canonical Page 078

## S084 재료 2 단일 진실원 만들기
- intent: prose를 기준 문장과 판단 기준으로 세운 과정
- opening: prose는 source of truth
- bridge: source 08 lines 40-53

## S085 재료 3- slides-grab, Skill 경계로 박힌 분리
- intent: outline, manifest, slides-grab의 단계 분리와 승인 관문
- opening: 단계 사이에 사용자 승인을 물리적으로 강제
- bridge: source 08 lines 55-67, 83-96; canonical Page 080

## S086 재료 4 규칙 세우기
- intent: design contract와 validation contract를 한 장에 압축
- opening: design contract를 먼저 고정
- bridge: source 08 lines 69-96; canonical Page 079

## S087 생성과 검증을 같은 손에 쥐지 않았다
- intent: HTML generation 이후 기계적 검증과 사람 검토 분리
- opening: 생성과 검증을 분리
- bridge: source 08 lines 83-96; canonical Page 081

## S088 이 발표가 증거
- intent: 제작 과정 자체가 Harness 방식으로 만들어진 사례
- opening: 원하는 것을 글로 작성 → 규칙을 문서로 작성 → 결과를 사람이 검증
- bridge: source 08 lines 102-121; canonical Page 081-082

## S089 우리가 다음에 해야 할 일
- intent: 09장 chapter divider
- opening: 우리가 다음에 해야 할 일
- bridge: source 09 chapter entry

## S090 시작하며: FOMO 와 피로
- intent: FOMO와 피로를 직접 써 보기로 연결
- opening: 더 많은 정보를 읽는 일이 아니라 직접 써 보는 일
- bridge: source 09 lines 1-7; canonical Page 084

## S091 증폭되는 경험 - 세 개의 증언
- intent: Page 085 testimony cards and bottom support line
- opening: AI 시대의 경험 - 축소가 아니라 증폭
- bridge: source 09 lines 9-17; canonical Page 085

## S092 내일부터
- intent: Page 086 actions and source line
- opening: 글로 먼저 · 직접 써보기 · 도구
- bridge: source 09 lines 35-43; canonical Page 086
