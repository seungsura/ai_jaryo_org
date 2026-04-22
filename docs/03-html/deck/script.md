# Seminar Script

- target deck: `docs/03-html/deck/index.html`
- scope: 00 overview + 01/02/03/04 chapters

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

## S019 ReAct / Tree-of-Thought
- intent: ReAct / Tree-of-Thought native diagrams
- opening: 행동 루프와 경로 탐색
- bridge: source markdown의 ReAct, Tree-of-Thought rows와 approved assets 구조

## S020 Self-Refine / Reflexion
- intent: Self-Refine / Reflexion native feedback-loop diagrams
- opening: 출력 이후의 피드백 루프
- bridge: source markdown의 Self-Refine, Reflexion row

## S021 네 가지 에이전틱 패턴
- intent: Andrew Ng four patterns native quadrant
- opening: 모델 바깥 구조가 성능을 좌우
- bridge: source markdown의 Andrew Ng 네 가지 패턴과 approved 05 asset 구조

## S022 프롬프트 시대의 벽
- intent: 프롬프트 시대의 한계
- opening: 모델은 보지 못한 것을 알 수 없음
- bridge: source markdown의 Blind Prompting 문단

## S023 2막: Cursor와 컨텍스트의 시대
- intent: 초기 Copilot과 Cursor 계열 도구 비교
- opening: 현재 파일에서 전체 코드베이스로
- bridge: source markdown의 Cursor 비교 표, Tools 문장, Context Engineering 문단

## S024 Cursor 아키텍처
- intent: Cursor architecture native system map
- opening: 긴 프롬프트가 아니라 검색기와 편집기
- bridge: source markdown의 Cursor 아키텍처 text diagram과 approved 06 asset 구조

## S025 컨텍스트 시대의 벽
- intent: 컨텍스트 시대의 한계와 에이전트 루프
- opening: 좋은 입력만으로는 루프 통제 불가
- bridge: source markdown의 gather context to repeat loop

## S026 3막: 하네스의 시대
- intent: Harness era signs without chapter 4 mechanics
- opening: 작업 환경 전체를 품기 시작한 코딩 도구
- bridge: source markdown의 Claude Code 구성 요소와 하네스 시대 전환

## S027 시대의 흐름
- intent: final relationship page
- opening: Agent = Model + Harness
- bridge: source markdown의 Agent 공식과 프롬프트/컨텍스트/하네스 포함 관계

## S028 AI 시대의 개발 방법론
- intent: 03장 진입을 알리는 section divider
- opening: TDD·SDD·Spec-first 재부상
- bridge: AI 시대의 개발 방법론 장 진입

## S029 왜 지금 방법론
- intent: AI 코딩 방법론 재부상 연대기
- opening: AI에게 무엇을 시킬지, 어떻게 검증할 것인지
- bridge: 생성 속도에서 검증 절차로 생각이 이동한 흐름

## S030 SDD
- intent: GitHub Spec Kit의 세 단계와 멈춤 장치
- opening: 스펙이 진실의 원천
- bridge: 요구사항, 계획, 태스크를 파일로 고정하는 흐름

## S031 TDD (Test-Driven Development)
- intent: Page 028 TDD lead와 anti-cheat 규칙
- opening: 테스트를 먼저 쓰고, 통과하는 코드를 나중에 쓴다
- bridge: 테스트가 에이전트의 자유를 제한하는 통제선

## S032 Waterfall vs SDD
- intent: Royce 1970과 spec-driven.md evidence로 Waterfall vs SDD 비교
- opening: Waterfall은 순차적으로 진행되고, SDD는 스펙을 실행 기준으로 둔다
- bridge: 요구사항·설계·코딩·테스트 vs specification·plan·tasks

## S033 SDD + TDD가 Harness로 이어지는 이유
- intent: 03장에서 04장 Harness 구조로 넘어가는 bridge
- opening: 이 시스템이 곧 하네스 엔지니어링
- bridge: 스펙과 테스트 루프를 사람이 매번 손으로 굴리지 않도록 시스템화

## S034 프롬프트를 넘어서
- intent: 04장 진입을 알리는 section divider
- opening: Prompt, Context, Harness
- bridge: 프롬프트와 컨텍스트를 포함하는 하네스 구조로 진입

## S035 Prompt, Context, Harness
- intent: source page 36/37 의미를 한 장의 hierarchy로 압축
- opening: Prompt ⊂ Context ⊂ Harness
- bridge: 프롬프트, 컨텍스트, 하네스의 포함 관계

## S036 Agent = Model + Harness
- intent: 공식, 인용구, 여섯 구성 요소를 한 장에 배치
- opening: 모델이 아닌 것은 전부 하네스입니다.
- bridge: Agent 공식과 하네스의 여섯 구성 요소

## S037 에이전트 루프: 하네스의 심장
- intent: gather context, take action, verify work, repeat loop
- opening: 네 지점을 신뢰성 있게 만드는 일
- bridge: 거의 모든 코딩 에이전트가 반복하는 네 단계

## S038 하네스의 책임
- intent: 5 responsibility cards와 설계 순서 rail
- opening: 다섯 개 기능 블록
- bridge: 운영 관점에서 보는 하네스의 책임

## S039 하네스의 도구
- intent: 책임 anchor와 도구 node의 다대다 관계 지도
- opening: 책임과 도구는 1:1이 아니다
- bridge: 기능 블록과 도구 레이어는 1:1로 대응하지 않음

## S040 Context Engineering
- intent: Write, Select, Compress, Isolate 네 전략
- opening: smallest set of high-signal tokens
- bridge: 좋은 컨텍스트는 넓은 컨텍스트가 아니라 선별된 컨텍스트

## S041 MCP와 Context Hub
- intent: MCP native architecture와 Context Hub 연결 의미
- opening: 연결 방식을 표준화
- bridge: 외부 도구와 최신 문서 연결은 컨텍스트 엔지니어링의 핵심 인프라

## S042 RAG vs Context Hub
- intent: RAG 논문과 MCP/Context Hub 문서 조사 기반 비교
- opening: 넓게 찾는가, 지금 맞는 문서를 지정하는가
- bridge: RAG는 넓은 검색 인덱스, Context Hub MCP는 최신/버전 지정 문서 주입

## S043 Memory: 세션을 넘어서는 기억
- intent: 외부 artifact map과 memory claim
- opening: 대화창을 기억 저장소로 착각하지 않는다
- bridge: 상태와 근거는 파일 시스템, Git, 이슈, PR, 문서로 나가야 함

## S044 Stable Prefix와 Variable Suffix
- intent: prefix/suffix diagram
- opening: 잘 쓰는 것 못지않게 안 바꾸는 것도 능력
- bridge: 자주 변하지 않는 것은 앞쪽에, 최신 입력과 도구 결과는 뒤쪽에 둠

## S045 하네스는 환경 그 자체다
- intent: chapter 04 closing statement
- opening: 필요한 파일, 필요한 도구, 필요한 규칙
- bridge: Harness Builder는 에이전트가 쓸 수 있는 환경을 만드는 사람
