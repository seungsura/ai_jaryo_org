# Seminar Script

- target deck: `docs/03-html/deck/index.html`
- scope: 00 overview + 01/02 chapters

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

## S018 Chain-of-Thought
- intent: Chain-of-Thought native example diagram
- opening: 중간 추론 단계를 쓰게 한다
- bridge: source markdown의 Chain-of-Thought row와 approved 02-chain-of-thought asset 구조

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
