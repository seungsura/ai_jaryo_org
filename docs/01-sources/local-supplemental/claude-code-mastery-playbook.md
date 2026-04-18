# Claude Code Mastery Playbook 자료 분석

- Source PDF: `/Users/seungsu/Downloads/claude-code-mastery-playbook.pdf`
- Total pages: 53
- Generated at: `2026-04-16T14:26:57Z`
- Preservation strategy: 상단에는 분석 메모를 두고, 하단에는 각 페이지의 렌더 이미지와 추출 텍스트를 함께 보존한다.
- Note: 추출 텍스트의 띄어쓰기나 특수기호는 PDF 원본 인코딩 영향으로 일부 거칠 수 있으므로, 세부 표현 확인은 페이지 이미지를 우선한다.

## Executive Summary

이 플레이북은 Anthropic Claude 생태계를 단순 기능 소개가 아니라 '사람-에이전트 협업 운영체계'로 설명한다. 앞부분은 Claude, Claude Code, Cowork의 기본 작동 원리와 운영 모델을 정리하고, 중반부는 4D 프레임워크와 API/MCP/RAG/워크플로우 설계를 다루며, 후반부는 교육·비영리·클라우드 배포·스킬·서브에이전트·한계 모델까지 확장한다.

문서 전체를 관통하는 핵심 메시지는 세 가지다. 첫째, AI 활용의 성패는 모델 자체보다 맥락 설계, 검증 루프, 권한 통제, 상태 외부화 같은 하네스에 달려 있다. 둘째, 인간은 지시자가 아니라 위임 범위와 평가 기준을 설계하는 책임자여야 한다. 셋째, 안정적인 제품화에서는 만능 에이전트보다 워크플로우, 평가 파이프라인, 리소스 분리, 구조화된 출력이 우선한다.

## Section Map

### 1. Foundation

- Course 1-4는 Claude, Claude Code, Cowork, 실제 코딩 워크플로우를 다룬다. 공통 주제는 에이전트 루프, 컨텍스트 관리, 권한 모드, 훅, 성공 기준, 결과 검증이다.
- 여기서 Claude Code는 단순 코드 생성기가 아니라 탐색-계획-실행-검증을 반복하는 로컬 실행형 에이전트로 정의된다.

### 2. AI Fluency

- Course 5, 8, 9, 13, 14는 4D(Delegation, Description, Discernment, Diligence)와 설명-판별 루프, 위임-성실 루프를 다양한 역할군에 맞게 반복 적용한다.
- 즉, 좋은 활용법은 프롬프트 묘기보다 역할 분배, 맥락 제공, 비판적 검토, 책임 있는 공개의 습관에 가깝다.

### 3. API, MCP, Platforms

- Course 6, 7, 10, 11, 12는 Claude API, MCP 기본/고급, Bedrock, Vertex AI를 연결한다. 반복 메시지는 stateless 아키텍처, 도구 호출 루프, 하이브리드 RAG, 프롬프트 캐싱, 워크플로우 우선 설계다.
- 특히 MCP는 도구, 리소스, 프롬프트를 분리해 통합 비용을 낮추는 계층으로 설명된다.

### 4. Reusable Agent Assets

- Course 15-16은 스킬과 서브에이전트를 조직 자산으로 다룬다. 자주 반복하는 규칙은 스킬로, 중간 탐색 노이즈를 숨기고 싶은 작업은 서브에이전트로 옮기라는 메시지가 분명하다.
- 동시에 둘 다 과용하지 말고, description 품질과 출력 형식, 최소 권한이 성능을 좌우한다고 경고한다.

### 5. Limits and Trust

- Course 17은 생성형 AI를 다음 토큰 예측, 멈춘 지식, 유한한 작업 기억, 조종성 간극이라는 네 가지 속성으로 설명한다.
- 결론은 맹신도 전면 불신도 아닌 '조정된 신뢰'이며, 긴 컨텍스트 분할, 사실 검증, 목표 기반 프롬프팅, 새 세션 전환이 실무 대응책으로 제시된다.

## Cross-cutting Themes

- Context is a budget: 모든 섹션이 과도한 컨텍스트 주입을 성능 저하의 주범으로 본다. 필요한 정보만 선택적으로 넣고, 긴 세션은 압축하거나 초기화하라고 권한다.
- Workflows over agents: 제품 환경에서는 무제한 자율성보다 체이닝, 라우팅, 평가 파이프라인 같은 구조화된 워크플로우가 우선이다.
- Human-in-the-loop: 교육, 비영리, 개발, API 설계 모두에서 최종 책임과 승인, 검증은 인간에게 남겨둔다.
- Externalized state: CLAUDE.md, 프로젝트 지침, 학습 컨텍스트 문서, RAG 저장소, 루트 기반 파일 접근처럼 상태를 외부 아티팩트로 관리하라고 반복한다.
- Verification beats confidence: 인용, 통계, 날짜, 파일 변경 결과, 검색 결과는 모델의 어조가 아니라 별도 검증 루프로 확인해야 한다.

## Jaryo 적용 메모

- 이 저장소가 이미 채택한 프로젝트 로컬 스킬, 문서 중심 워크스페이스, 분리된 서브에이전트 구조는 플레이북의 권장 방향과 강하게 일치한다. 특히 `SKILL.md`, `AGENTS.md`, `docs/`, `assets/` 분리는 '항상 로드되는 규칙'과 '필요할 때만 로드되는 전문 지식'을 나누라는 스킬 섹션의 조언과 맞닿아 있다.
- 문서 재구성 작업에서는 긴 대화에 상태를 묻어두기보다 `docs/01-sources/intake/source-inbox.md`, `docs/01-sources/intake/open-questions.md`, `docs/01-sources/registry.md` 같은 외부 파일에 상태를 적층하는 편이 낫다. 이는 플레이북이 반복해서 강조하는 상태 외부화와 컨텍스트 절약 원칙에 부합한다.
- 향후 발표 자료 재생성이나 문서 정제 자동화를 강화하려면, '작은 워크플로우 + 명시적 검증' 구성을 기본으로 삼고 서브에이전트는 조사·요약·리뷰처럼 중간 과정 노이즈를 숨겨도 되는 작업에만 제한적으로 쓰는 편이 안전하다.

## Page Archive

## Page 001

![Page 001](assets/claude-code-mastery-playbook/page-001.png)

### Transcription

```text
Anthropic Claude
Mastery Playbook
Name: Donghee (Chad) Kim
Role: AWS SA | AI Architect
LinkedIn: https://www.linkedin.com/in/donghee-kim-478a27297/
Last Updated: Apr 2026 (v1.0)
```

## Page 002

![Page 002](assets/claude-code-mastery-playbook/page-002.png)

### Transcription

```text
Table of Contents
01. Claude 101
02. Claude Code 101
03. Introduction to Claude Cowork
04. Claude Code in Action
05. AI Fluency: Framework & Foundations
06. Building with the Claude API
07. Introduction to Model Context Protocol
08. AI Fluency for educators
09. AI Fluency for students
10. Model Context Protocol: Advanced Topics
11.  Claude with Amazon Bedrock
12. Claude with Google Cloud's Vertex AI
13. Teaching AI Fluency
14. AI Fluency for nonprofits
15. Introduction to agent skills
16. Introduction to subagents
17. AI Capabilities and Limitations
```

## Page 003

![Page 003](assets/claude-code-mastery-playbook/page-003.png)

### Transcription

```text
[Course 1: Claude 101]
단순한  챗봇을  넘어 , 당신의  전문성과  결합하여  최상의  결과를  도출하는  지능적  협력자 (Thought
Partner) 활용  가이드임 .
핵심  원리  및  개념  (Core Principles & Concepts)
Claude 가  작동하는  근본적인  배경과  AI 협업을  위해  반드시  알아야  할  핵심  개념임 .
실전  활용  가이드  (Practical Implementation Guide)
헌법적  AI (Constitutional AI): Claude 는  유익하고 (Helpful), 무해하며 (Harmless), 정직하게
(Honest) 설계됨 . 인간의  가치관에  부합하며  투명하게  작동하도록  훈련되어  높은  신뢰성과  예
측  가능성을  제공함 .
•
지적  동반자  (Thought Partner): 단순한  질문 - 답변  도구가  아님 . 사용자의  어렴풋한  아이디어
를  기억하고 , 복잡한  인지  작업 , 전략적  분석 , 코딩  및  문제  해결을  함께  수행하는  능동적  협력
자임 .
•
대용량  컨텍스트  처리  및  RAG: 20 만  개  이상의  토큰 ( 약  500 페이지  분량 ) 을  한  번에  처리함 . 정
보량이  한계에  달하면  검색  증강  생성 (RAG) 모드를  자동  활성화하여  응답  품질을  유지하며  용
량을  최대  10 배까지  확장함 .
•
AI 활용  능력  4D 프레임워크: AI 와의  효과적인  협업을  위한  4 가지  핵심  역량임 .•
위임  (Delegation): 인간과  AI 간의  전략적  작업  분배-
설명  (Description): AI 시스템과의  명확한  소통  및  지시-
분별력  (Discernment): AI 의  출력과  프로세스에  대한  비판적  평가-
성실성  (Diligence): 책임감  있고  윤리적인  AI 사용  및  투명성  유지-
확장된  사고  (Extended Thinking): 복잡한  분석이나  수학 , 코딩  문제  해결  시  즉각적인  반응
대신  심층적인  추론  과정을  거쳐  단계별로  문제를  해결하는  하이브리드  추론  모드임 .
•
3 단계  프롬프트  엔지니어링  프레임워크: 직장  동료에게  업무를  지시하듯  자연스럽고  명확하
게  작성하는  것이  핵심임 . ( 프롬프트  작성  공식 : 상황  설정  -> 과제  정의  -> 규칙  명시 )
•
아티팩트 (Artifacts) 를  활용한  시각적  창작: 채팅창에  묻히지  않는  독립적이고  대화형인  결과
물을  생성하는  기능임 .
•
지원  포맷: 마크다운  문서 , 코드  스니펫 (Python, JS 등 ), 완전한  HTML 웹페이지 , SVG 이미
지 , Mermaid 다이어그램 , React 컴포넌트 ( 대화형  UI).
-
활용  팁: " 이것을  아티팩트로  생성해  줘 " 라고  명시적으로  요청할  것 . 생성된  아티팩트는
즉시  미리보기 , 코드  확인 , 다운로드  및  외부  링크로  공개  게시 ( 게시  취소  가능 ) 가  가능함 .
-
```

## Page 004

![Page 004](assets/claude-code-mastery-playbook/page-004.png)

### Transcription

```text
전략적  인사이트  및  주의사항  (Strategic Insights & Considerations)
Claude 를  실무에  도입할  때  발생할  수  있는  안티  패턴을  방지하고  가치를  극대화하기  위한  전략
임 .
생태계  확장 : 커넥터 (Connectors) 와  엔터프라이즈  검색: MCP(Model Context Protocol)
기술을  통해  Claude 를  사용자의  실제  업무  데이터와  연결함 .
•
웹  커넥터: Google Drive, Notion, Slack, Asana 등  클라우드  서비스와  연결하여  문서  검색 ,
이메일  요약 , 티켓  생성  등을  대화창  내에서  직접  수행함 .
-
데스크톱  확장: 로컬  파일  시스템  접근 , 브라우저  제어 , 네이티브  애플리케이션  통합을  지
원함 .
-
엔터프라이즈  검색: 조직  내  여러  도구 (SharePoint, Slack, Gmail 등 ) 에  흩어진  정보를  한
번에  검색하고  종합하여  출처와  함께  답변을  제공하는  전용  기능임 .
-
심층  분석을  위한  연구  모드  (Research Mode): 단순  검색을  넘어 , Claude 가  능동적으로  다단
계  조사를  수행하는  자율  에이전트  기능임 .
•
작동  방식: 접근  방식  계획 ( 확장된  사고 ) → 다중  검색  수행  및  단서  추적  → 정보  종합  →
출처 (Citations) 가  포함된  검증  가능한  보고서  생성 .
-
소요  시간: 일반  보고서는  5~15 분 , 복잡한  조사는  최대  45 분이  소요되며 , 인간이  수작업으
로  수  시간  걸릴  작업을  대체함 .
-
활용  팁: 목표 , 구조 , 제약  조건 ( 예산 , 일정  등 ) 을  프롬프트에  매우  구체적으로  명시할  것 .-
위임 - 실사  루프  (Delegation-Diligence Loop) 구축: AI 의  분석  결과를  무조건  신뢰하는  것은
위험함 . 이미  정답을  알고  있는  과거  데이터를  활용해  Claude 의  분석  능력을  체계적으로  테스
트할  것 . 결과물의  논리적  공백을  면밀히  평가 ( 실사 ) 하고 , 프롬프트를  수정하여  재시험하는  과
정을  거쳐  신뢰가  구축된  작업만  위임해야  함 .
•
반복적  사고방식  (Iterative Mindset) 수용: 첫  번째  프롬프트로  완벽한  결과가  나오는  경우는
드묾 . 초안을  출발점으로  삼고 , " 처음  두  단락을  삭제하고  결론을  행동  지향적으로  수정해 " 와
같이  구체적인  피드백을  제공하며  결과를  다듬어  나가야  함 . 대화가  엉뚱한  방향으로  흘렀다
면  새  채팅을  시작하는  것이  효율적임 .
•
보안  및  데이터  접근  권한의  이해: 커넥터  및  엔터프라이즈  검색  사용  시 , Claude 는  ' 사용자  본
인이  접근  권한을  가진  데이터 ' 에만  접근할  수  있음 . 대화  내용은  비공개로  유지되며  연결된  데
이터는  별도로  색인화되거나  학습에  사용되지  않음 . 단 , Chrome 확장  프로그램  등에서  민감한
작업 ( 결제  등 ) 수행  시  반드시  인간의  최종  승인  단계를  거쳐야  함 .
•
환각 (Hallucination) 방지  및  팩트  체크: Claude 는  때때로  그럴듯하지만  잘못된  정보를  제공할
수  있음 . 중요도가  높은  업무의  경우  반드시  출처 (Citations) 를  요구하고 , 웹  검색  기능을  활성
화하여  최신  정보에  근거하도록  유도하며 , 핵심  사실은  독립적으로  교차  검증해야  함 .
•
인간의  맥락 (Context) 제공  필수: Claude 는  강력한  지능을  제공하지만 , 업무에  의미를  부여하
는  ' 맥락 ' 과  ' 전문  지식 ' 은  인간의  몫임 . AI 에게  모든  것을  맡기는  것이  아니라 , 데이터  분석가  동
료와  일하듯  답변의  근거를  묻고  과정을  명확히  요구하며  소통해야  함 .
•
```

## Page 005

![Page 005](assets/claude-code-mastery-playbook/page-005.png)

### Transcription

```text
마스터  한  줄  평: "Claude 는  당신을  대체하는  도구가  아니라 , 당신의  고유한  전문성과  결합하여  최
상의  결과를  도출하는  지능적  협력자 ."
```

## Page 006

![Page 006](assets/claude-code-mastery-playbook/page-006.png)

### Transcription

```text
[Course 2: Claude Code 101]
본  플레이북은  개발자를  위한  AI 코딩  에이전트  도구인  Claude Code의  핵심  작동  원리부터  고급
사용자  정의  설정까지 , 실무에  즉시  적용  가능한  고밀도  가이드라인을  제공함 . 단순한  코드  생성을
넘어 , 자율적으로  환경과  상호작용하며  문제를  해결하는  ' 에이전트 ' 로서의  Claude 를  마스터할  것 .
핵심  원리  및  개념  (Core Principles & Concepts)
Claude Code 가  기존의  채팅  기반  AI(Claude.ai) 와  구별되는  근본적인  배경과  필수  개념임 .
실전  활용  가이드  (Practical Implementation Guide)
실무  생산성을  극대화하기  위한  구체적인  워크플로우와  환경  설정  가이드임 .
에이전트형  코딩  도구  (Agentic Coding Tool): 단순히  텍스트 ( 코드 ) 를  반환하는  것을  넘어 , 로
컬  파일  시스템 , 터미널 , 전체  코드베이스에  직접  접근함 . 정해진  목표를  달성하기  위해  스스로
환경과  상호작용하며  코드를  수정하고  명령어를  실행하는  자율  소프트웨어임 .
•
에이전트  루프  (The Agentic Loop): Claude Code 작동의  심장부임 . 사용자의  프롬프트가  입
력되면  다음  과정을  실시간으로  반복함 .
•
Gather Context ( 컨텍스트  수집 ): 코드베이스에서  필요한  정보를  탐색함 .-
Take Action ( 행동  수행 ): 파일을  수정하거나  터미널  명령어를  실행함 .-
Verify Results ( 결과  검증 ): 의도대로  완료되었는지  확인하고 , 미비할  경우  루프를  재실행
함 .
-
컨텍스트  윈도우  (Context Window): Claude 의  '; 작업  기억  장치 (Working Memory)' 임 . 파일  읽
기 , 명령어  실행 , 대화  내용  등  모든  상호작용이  공간을  차지함 . 무한하지  않으므로 , 에이전트
는  전체  코드를  로드하는  대신  전략적으로  필요한  정보만  찾아내는  방식을  취함 .
•
도구  (Tools) 와  시맨틱  이해: Claude 는  Bash( 터미널 ), 파일  읽기 / 쓰기 , 웹  검색  등의  도구를  갖
추고  있으며 , 상황에  맞춰  어떤  도구를  언제  사용할지  시맨틱 ( 의미론적 ) 이해를  바탕으로  스스
로  판단함 .
•
권한  및  제어  (Permissions & Modes): 자율성에는  통제가  수반되어야  함 . 개발자는  다음  모드
를  통해  제어권을  유지함 .
•
Approval ( 승인  모드 ): 파일  수정  및  명령어  실행  전  명시적  승인  요구  ( 기본값 ).-
Auto-accept ( 자동  승인 ): 파일  수정은  자동  승인하되 , 명령어  실행만  승인  요구 .-
Plan Mode ( 플랜  모드 ): 읽기  전용  도구만  사용하여  실제  수정  없이  작업  계획만  수립 .-
4 단계  핵심  워크플로우 : Explore → Plan → Code → Commit: 코드를  바로  작성해달라고  요
청하는  대신 , 다음  프로세스를  따르면  시행착오를  획기적으로  줄일  수  있음 .
•
```

## Page 007

![Page 007](assets/claude-code-mastery-playbook/page-007.png)

### Transcription

```text
전략적  인사이트  및  주의사항  (Strategic Insights & Considerations)
Explore ( 탐색 ): 프로젝트  구조와  스타일을  Claude 가  충분히  이해하도록  지시함 . ( 예 : 하
위  에이전트  활용 )
-
Plan ( 계획 ): Shift + Tab 으로  ' 플랜  모드 ' 를  켜고  구현  전략을  수립함 . 실제  코드  작성
전 , Claude 가  제시한  액션  플랜을  검토하고  수정 (Course-correct) 하는  가장  중요한  단계
임 .
-
Code ( 구현 ): 승인된  계획을  바탕으로  자율적인  파일  수정  및  터미널  명령어 ( 테스트  스위
트  실행  등 ) 를  수행하게  함 . 명확한  ' 성공  기준 (Success criteria)' 을  제시해야  함 .
-
Commit ( 반영 ): code-reviewer 하위  에이전트를  호출하여  편향  없는  코드  리뷰를  진
행한  후 , /commit-push-pr 스킬을  통해  한  번에  PR 까지  생성함 .
-
컨텍스트 ( 기억 ) 최적화  명령어: 컨텍스트가  가득  차면  성능이  저하됨 . 다음  명령어로  기억  공
간을  관리할  것 .
•
/context: 현재  컨텍스트  사용량을  시각화된  그래프와  카테고리별로  확인함 .-
/compact: 현재까지의  긴  세션을  핵심만  요약하여  공간을  확보함 . ( 특정  기능  개발을  이
어갈  때  유용 )
-
/clear: 이전  기억을  모두  지우고  완전히  새로운  작업을  시작함 . ( 이전  대화의  편향  방
지 )
-
프로젝트  맞춤형  확장  (Customization):•
CLAUDE.md ( 프로젝트  메모리 ): 프로젝트  루트에  위치하는  온보딩  가이드임 . 기술  스택 ,
실행  명령어 , 코드  스타일 ( 예 : "2-space 들여쓰기  사용 ") 을  기록하면  매  세션마다  Claude
가  이를  자동  숙지함 . (/init 명령어로  자동  생성  가능 )
-
Subagents ( 하위  에이전트 ): 복잡한  탐색이나  리뷰  작업을  메인  에이전트와  분리된  별도
의  컨텍스트  윈도우에서  병렬  처리함 . 메인  창에는  ' 최종  요약  결과 ' 만  전달되어  컨텍스트
를  깨끗하게  유지함 .
-
Skills ( 스킬 ): 특정  작업  방식 ( 예 : 커밋  메시지  형식 ) 을  마크다운으로  정의해두면 , Claude
가  상황을  인식하여  온디맨드 (On-demand) 로  자동  적용함 .
-
MCP (Model Context Protocol): Linear, AWS, 외부  DB 등  코드베이스  외부의  데이터  소
스나  도구를  Claude 와  연결하는  오픈  표준임 .
-
Hooks ( 훅 ): 확률에  의존하지  않고  결정론적 (Deterministic) 으로  작동하는  강제  실행  규칙
임 . settings.json 에  설정함 .
-
PostToolUse: 파일  편집  후  Prettier 등  자동  포맷터  무조건  실행 .-
PreToolUse: rm -rf 나  프로덕션  DB 수정  같은  파괴적  명령어  감지  및  실행  원천
차단 .
-
전략적  가치 : Debug and Destress: Claude Code 의  진정한  가치는  단순히  타이핑  속도를  높
이는  것이  아님 . 복잡한  버그  추적 , 반복적인  리팩토링 , 환경  설정  등  개발자의  에너지를  고갈
시키는  작업을  AI 에이전트에게  위임함으로써 , 개발자는  아키텍처  설계와  비즈니스  로직  구현
이라는  ' 창의적이고  본질적인  문제  해결 ' 에  집중할  수  있음 .
•
```

## Page 008

![Page 008](assets/claude-code-mastery-playbook/page-008.png)

### Transcription

```text
마스터  한  줄  평: "Claude Code 는  코드를  짜주는  수동적인  도구를  넘어 , 개발자의  의도를  자율적
으로  탐색 · 계획 · 실행 · 검증하는  가장  완벽한  AI 동료 (Agent)."
실무  안티  패턴  및  주의사항  (Anti-patterns):•
모호한  프롬프트  작성  (Context Bloat): 현상 : " 이거  고쳐줘 " 식의  짧고  모호한  지시 . 결과 :
Claude 가  의도를  파악하기  위해  불필요하게  많은  파일을  탐색하며  귀중한  컨텍스트  윈도
우를  낭비함 . 해결책 : 프롬프트는  구체적이고  상세하게  작성해야  오히려  컨텍스트를  절약
할  수  있음 .
-
무분별한  자동  승인  (Bypassing Permissions): 현상 : 편의를  위해  모든  명령어  실행  권한
을  무조건  허용 . 결과 : AI 의  환각 (Hallucination) 이나  오판으로  인해  치명적인  시스템  변경
이나  데이터  삭제가  발생할  수  있음 . 해결책 : 기본적으로  ' 승인  모드 ' 를  유지하거나 ,
PreToolUse 훅 (Hook) 을  설정하여  위험한  명령어 (exit code 2 반환 ) 를  시스템  레벨에서
차단해야  함 .
-
방치된  MCP 서버  및  도구: 현상 : 현재  프로젝트와  무관한  다수의  MCP 서버를  계속  켜두
는  행위 . 결과 : 활성화된  모든  도구의  정의 (Definition) 가  기본적으로  컨텍스트  윈도우를  차
지하여 , 정작  필요한  코드  분석  공간이  부족해짐 . ( 도구가  컨텍스트의  10% 를  초과하면  불
안정한  도구  검색  모드로  전환됨 ). 해결책 : /mcp 명령어를  통해  사용하지  않는  서버는  즉
시  비활성화할  것 .
-
CLAUDE.md 의  과도한  비대화: 현상 : 프로젝트의  모든  문서와  사소한  규칙까지
CLAUDE.md 에  욱여넣는  행위 . 결과 : 매  세션마다  방대한  텍스트가  프롬프트에  추가되어
시작부터  컨텍스트를  낭비함 . 해결책 : 처음에는  파일  없이  시작하여  Claude 가  자주  실수
하는  부분만  선별적으로  기록할  것 . 방대한  문서는  @README.md 처럼  참조  링크  형태로
제공하는  것이  효율적임 .
-
```

## Page 009

![Page 009](assets/claude-code-mastery-playbook/page-009.png)

### Transcription

```text
[Course 3: Introduction to Claude Cowork]
핵심  원리  및  개념  (Core Principles & Concepts)
Cowork 는  단순한  대화형  AI(Chat) 를  넘어 , 사용자의  로컬  환경에서  직접  파일을  읽고  편집하며  최
종  결과물을  생산하는  실행형  AI(Action-oriented AI) 에이전트임 . 대화 (Conversation) 에서  위임
(Delegation) 으로  업무의  패러다임을  전환함 .
실전  활용  가이드  (Practical Implementation Guide)
3 대  핵심  작동  원리  (Plan, Execute, Connect)•
Plan ( 계획 ): 다단계  작업  수행  전 , Claude 가  접근  방식을  제시하고  사용자의  검토  및  승인
을  받음 .
-
Execute ( 실행 ): 로컬  컴퓨터의  격리된  환경에서  파일  생성 , 데이터  분석  등  장기  실행  작
업을  자율적으로  수행함 .
-
Connect ( 연결 ): 이메일 , 공유  드라이브 , 슬랙  등  기존  업무  도구와  연동하여  수동  복사 / 붙
여넣기  없이  컨텍스트를  자동으로  수집함 .
-
확장된  에이전트  역량  (Agentic Capabilities)•
Subagents ( 하위  에이전트 ): 복잡하고  독립적인  여러  작업을  병렬로  처리하기  위해  별도
의  에이전트들을  동시에  가동함 . ( 예 : 여러  공급업체  동시  비교  분석 )
-
Local Computation ( 로컬  연산 ): 파일을  업로드 / 다운로드할  필요  없이 , 파일이  있는  위치
에서  직접  코드를  실행하고  결과를  기록함 .
-
Plugins & Skills ( 플러그인  및  스킬 ): 영업 , 재무  등  특정  직무에  특화된  도메인  지식과  워
크플로우 (Skills) 를  패키지  형태로  제공하여  전문가  수준의  접근을  가능하게  함 .
-
네이티브  아티팩트 (Artifacts) 생성: 텍스트  답변을  넘어 , 편집  가능한  차트가  포함된
PowerPoint, 수식이  작동하는  Excel, 변경  내용  추적이  적용된  Word 문서  등  실제  드라이브에
저장되는  완성형  파일을  생성함 .
•
4 단계  핵심  워크플로우  (The Core Loop): Cowork 의  모든  작업은  사용자의  지시와  AI 의  계획 ,
그리고  상호작용을  통한  조향 (Steering) 으로  완성됨 .
•
Describe ( 작업  지시 ): 검토할  대상 , 원하는  결과물 , 저장  위치를  명확히  지시함 . 부족한  정
보는  Claude 가  후속  질문을  통해  보완함 .
-
Review & Answer ( 계획  검토 ): Claude 가  제안하는  작업  계획을  확인하고 , 우선순위나  접
근  방식을  선택하여  승인함 .
-
Execute & Steer ( 실행  및  조향 ): 진행  상황  패널을  통해  실시간으로  읽고  있는  파일과  생
성  중인  결과물을  확인함 . 작업  중  언제든  채팅을  입력해  방향을  수정할  수  있음 .
-
```

## Page 010

![Page 010](assets/claude-code-mastery-playbook/page-010.png)

### Transcription

```text
전략적  인사이트  및  주의사항  (Strategic Insights & Considerations)
Cowork 의  진정한  가치는  단일  채팅창에  담을  수  없는  대규모  데이터  처리 (Research & analysis at
scale) 에  있음 . 수많은  문서를  병렬로  읽고  교차  검증하여 , 순차적으로  읽었을  때는  발견하기  힘든
패턴 , 모순 (Contradictions), 이상치 (Outliers) 를  도출하는  데  최적화되어  있음 . 단순  요약이  아닌  " 이
문서들  사이에서  서로  충돌하는  주장은  무엇인가 ?" 와  같은  날카로운  질문 (Signal) 을  던질  때  극대
화됨 .
Open ( 결과물  확인 ): 지정된  폴더나  연동된  도구 ( 예 : Gmail, Drive) 에  생성된  최종  파일을
열어  초안으로서  검토  및  편집함 .
-
고효율  프롬프트  작성  공식  (The Prompt Pattern): 성공적인  Cowork 프롬프트는  다음  세  가지
요소를  반드시  포함해야  함 . [Input] + [Transformation] + [Output]
•
Input ( 입력 ): 소스  자료의  위치  지정  ( 예 : " 이  폴더에  있는  회의록과  작년  보고서를 ...")-
Transformation ( 변환 ): 수행할  구체적  작업  명시  ( 예 : "... 브랜드  가이드라인  스킬을  적용
하여  주요  액션  아이템을  추출하고 ...")
-
Output ( 출력 ): 최종  포맷  및  위치  지정  ( 예 : "... 요약된  슬라이드  덱 (PPTX) 으로  만들어
줘 .")
-
컨텍스트  유지  및  자동화  설정•
Projects ( 프로젝트  설정 ): 특정  로컬  폴더에  'Instructions( 지시사항 )' 를  부여하여  세션  간
컨텍스트를  유지함 . 참여자  역할 , 파일  저장  규칙 , 출력  포맷  선호도  등을  한  번만  설정하
면  매번  설명할  필요가  없음 .
-
Scheduled Tasks ( 예약  작업 ): 검증된  프롬프트나  스킬을  특정  주기 ( 매시간 , 매일 , 매주 )
로  자동  실행하도록  설정함 . ( 예 : " 매주  월요일  오전  9 시 , 캘린더를  확인하여  주간  우선순
위  이메일  초안  작성 ")
-
전략적  활용  가치 : 규모의  한계  극복•
운영  주의사항  및  안티  패턴  (Anti-patterns)•
Chat vs Cowork 의  명확한  구분: 파일  접근 , 외부  도구  연동 , 실제  파일  생성이  필요  없는
단순  질의응답이나  브레인스토밍은  리소스  소모가  적은  Chat 모드를  사용하는  것이  훨씬
효율적임 .
-
모델  최적화  실패: 모든  작업에  최고  성능  모델 (Opus) 을  고집하면  사용량 (Allocation) 이  급
감함 . 작업의  복잡도에  따라  일상적  작업에는  Sonnet( 기본값 ) 을 , 가볍고  빠른  작업에는
Haiku 를  전략적으로  선택해야  함 .
-
맹목적  신뢰  경계  (Reviewing Mindset): AI 가  생성한  결과물은  그  완성도와  무관하게  항
상  확신에  찬  형태를  띰 . 최종  의사결정이나  외부  공유  전 , 반드시  실제  파일을  열어  수치
와  논리  전개를  직접  검토 (Review) 하는  습관이  필수적임 .
-
보안  및  권한  관리•
Cowork 는  사용자가  명시적으로  권한을  부여한  폴더와  도구에만  접근하는  격리된  환경에
서  실행됨 .
-
```

## Page 011

![Page 011](assets/claude-code-mastery-playbook/page-011.png)

### Transcription

```text
마스터  한  줄  평: " 단순한  대화형  조수를  넘어 , 내  로컬  환경에서  직접  데이터를  분석하고  실무  문
서를  완성해  내는  자율형  AI 동료의  탄생 ."
파일의  영구  삭제는  자율적으로  진행되지  않으며 , 반드시  사용자의  사전  승인 (Gated
deletion) 을  요구함 .
-
규제  요구사항이  있는  민감한  데이터를  다룰  경우 , 사용  중인  플랜의  감사  로그 (Audit
logging) 및  컴플라이언스  정책을  사전에  확인해야  함 .
-
```

## Page 012

![Page 012](assets/claude-code-mastery-playbook/page-012.png)

### Transcription

```text
[Course 4: Claude Code in Action]
핵심  원리  및  개념  (Core Principles & Concepts)
Claude Code 는  단순한  코드  생성기를  넘어 , 개발  환경과  직접  상호작용하며  복잡한  문제를  자율
적으로  해결하는  지능형  파트너임 . 본  코스에서  다루는  핵심  작동  원리는  다음과  같음 .
💡  핵심  요약: Claude 모델의  탁월한  ' 도구  사용 ' 능력은  보안을  유지하면서도 ( 전체  코드  외부  인덱
싱  불필요 ) 복잡하고  변화무쌍한  개발  과제를  효과적으로  해결하는  기반이  됨 .
실전  활용  가이드  (Practical Implementation Guide)
실무  환경에서  Claude Code 의  생산성을  극대화하기  위한  구체적인  명령어와  워크플로우임 .
코딩  어시스턴트의  3 단계  아키텍처: 특정  작업을  해결하기  위해  맥락  파악 (Gather
Context) → 계획  수립 (Formulate a Plan) → 작업  실행 (Take an Action) 의  지능
적  단계를  반복 (Iterate) 함 .
•
도구  사용  (Tool Use) 메커니즘: 언어  모델 (LM) 의  한계를  극복하는  핵심  개념임 . 모델이  텍스
트로  명령을  내리면 , 시스템이  이를  해석해  실제  파일  시스템  제어 (Read, Write, Edit), 시스템
제어 (Bash, LS), 고급  기능 (Agent, WebSearch) 등을  수행함 .
•
다층적  맥락  관리  (Context Management): 불필요한  정보는  AI 의  성능을  저하시킴 . Claude
Code 는  세  가지  수준의  CLAUDE.md 파일을  통해  맥락을  제어함 .
•
CLAUDE.md ( 프로젝트  레벨 ): Git 에  커밋되어  팀원과  공유되는  공통  지침 .-
CLAUDE.local.md ( 로컬  레벨 ): 개인적인  설정  및  지침 .-
~/.claude/CLAUDE.md ( 글로벌  레벨 ): 모든  프로젝트에  적용되는  범용  지침 .-
확장성  (Extensibility) 및  MCP: 모델  컨텍스트  프로토콜 (MCP) 서버를  통해  기본  제공되지  않
는  외부  도구 ( 예 : Playwright 를  통한  브라우저  제어 ) 를  통합하여  기능을  무한히  확장할  수  있음 .
•
제어와  자동화  (Hooks & SDK): PreToolUse 및  PostToolUse 훅 (Hooks) 을  통해  AI 의  행
동을  사전에  차단하거나  사후  작업을  자동화하며 , SDK 를  통해  프로그래밍  방식으로  AI 를  파
이프라인에  통합함 .
•
1. 초기  설정  및  맥락  최적화•
프로젝트  초기화: 터미널에서  /init 실행 . 전체  코드베이스를  스캔하여  아키텍처와  코
딩  패턴을  요약한  CLAUDE.md 를  자동  생성함 . ( 파일  생성  자동  승인 : Shift + Tab)
-
정밀한  맥락  주입:-
@ 파일명: 질문  시  특정  파일을  멘션하여  해당  내용을  즉시  컨텍스트에  포함  ( 예 :
How does auth work? @auth.ts).
-
```

## Page 013

![Page 013](assets/claude-code-mastery-playbook/page-013.png)

### Transcription

```text
전략적  인사이트  및  주의사항  (Strategic Insights & Considerations)
Claude Code 를  조직  단위로  도입하거나  고도화된  프로젝트에  적용할  때  반드시  고려해야  할  전략
적  요소와  안티  패턴임 .
# 명령어 ( 메모리  모드 ): 대화  중  # Use comments sparingly 입력  시  지침을
CLAUDE.md 에  지능적으로  병합하여  기억함 .
-
시각적  소통: UI 수정  시  텍스트  설명  대신  스크린샷을  캡처  후  터미널에  Ctrl + V 로  붙
여  넣어  정확한  수정  위치를  지시함 .
-
2. 대화  제어  및  추론  모드  활용•
대화  흐름  제어  ( 집중력  유지 ):-
Esc: AI 가  엉뚱한  방향으로  갈  때  즉시  응답  중단 .-
Esc 두  번 : 대화  되감기 . 디버깅  중  쌓인  불필요한  노이즈를  제거하고  이전  시점으
로  복귀 .
-
/compact: 핵심  정보만  유지한  채  긴  대화  기록을  요약  압축  ( 토큰  절약  및  집중력
향상 ).
-
/clear: 대화  기록  완전  삭제 . 전혀  다른  작업으로  전환할  때  사용 .-
고급  추론  모드:-
Planning Mode ( 기획  모드 ): Shift + Tab 두  번  누름 . 코드  작성  전  전체  코드베이
스를  조사하고  상세  실행  계획을  먼저  제안받아  검토함 . ( 넓은  범위의  작업에  적합 )
-
Thinking Mode ( 사고  모드 ): 프롬프트에  "Ultra-think" 또는  "Think longer" 포함 . 복잡
한  로직이나  어려운  버그  해결  시  더  많은  토큰을  할당하여  심도  있게  분석함 . ( 깊이
있는  작업에  적합 )
-
3. 워크플로우  확장  및  자동화•
사용자  지정  명령  (Custom Commands): .claude/commands/ 명령어 .md 생성 .
$ARGUMENTS 플레이스홀더를  사용하여  동적  인수를  받는  반복  작업 ( 예 : 테스트  코드  작
성 , 보안  감사 ) 을  자동화함 .
-
MCP 서버  연동  (Playwright 예시 ):-
설치 : claude mcp add playwright npx @playwright/mcp@latest-
권한  자동  승인 : .claude/settings.local.json 의  allow 배열에
"mcp__playwright" 추가 .
-
활용 : Claude 가  직접  브라우저를  열어  UI 를  확인하고 , 시각적  피드백을  바탕으로  스
스로  코드를  수정  및  개선함 .
-
1. 훅 (Hooks) 을  활용한  강력한  가드레일  구축: AI 의  자율성은  양날의  검이  될  수  있음 . 훅을  통
해  보안과  코드  품질을  강제해야  함 .
•
보안  통제  (PreToolUse): Claude 가  민감한  파일 ( 예 : .env) 에  접근하려  할  때  이를  원천
차단해야  함 . matcher: "Read|Grep" 으로  설정하고 , 스크립트에서  Exit Code 2 를  반환
-
```

## Page 014

![Page 014](assets/claude-code-mastery-playbook/page-014.png)

### Transcription

```text
마스터  한  줄  평: "Claude Code 는  단순한  코드  완성  도구를  넘어 , 문맥을  이해하고  스스로  도구를
선택해  문제를  해결하는  ' 자율적인  개발  파트너 '"
하여  도구  실행을  차단 (Block) 함과  동시에  stderr 로  명확한  차단  사유를  AI 에게  피드백
해야  함 .
품질  강제  (PostToolUse): AI 가  함수  시그니처를  수정할  때  호출  지점  업데이트를  누락하
는  경우가  발생할  수  있음 . 파일  수정  직후  tsc --noEmit ( 타입  검사 ) 이나  코드  포맷터
를  자동  실행하는  사후  훅을  설정하여 , 오류  발생  시  즉각적으로  AI 가  재수정하도록  유도
해야  함 .
-
⚠  주의사항  ( 경로  문제 ): 보안상  훅  스크립트는  절대  경로  사용이  권장되나 , 이는  팀원  간
settings.json 공유를  어렵게  만듦 . $PWD 플레이스홀더를  활용한  셋업  스크립트
(settings.example.json → settings.local.json 변환 ) 를  구축하여  이  문제를
우회할  것 .
-
2. 토큰  비용  및  성능  최적화  (Anti-patterns)•
과도한  맥락  주입  지양: 프로젝트의  모든  파일을  컨텍스트에  밀어  넣는  것은  성능  저하와
비용  낭비의  주범임 . @ 멘션과  CLAUDE.md 를  활용해  ' 필요한  정보만 ' 선별적으로  제공
할  것 .
-
추론  모드의  남용  금지: Planning Mode 와  Thinking Mode 는  매우  강력하지만  추가적인  토
큰을  대량으로  소모함 . 단순한  타이포  수정이나  명확한  단일  파일  작업에는  기본  모드를
사용하고 , 다단계  구현이나  복잡한  알고리즘  디버깅에만  전략적으로  추론  모드를  활성화
할  것 .
-
3. GitHub 연동을  통한  팀  차원의  협업  스케일링•
로컬  환경의  개인  도우미를  넘어 , GitHub Actions(/install-github-app) 와  연동하여
팀의  자동화된  구성원으로  활용할  것 .
-
새로운  PR 생성  시  Claude 가  자동으로  코드  리뷰  및  영향도  분석  리포트를  작성하게  하
고 , 이슈  발생  시  @claude 멘션으로  즉각적인  디버깅  및  PR 생성을  위임 (Delegate) 하여
리뷰  병목  현상을  해소할  수  있음 .
-
```

## Page 015

![Page 015](assets/claude-code-mastery-playbook/page-015.png)

### Transcription

```text
[Course 5: AI Fluency: Framework & Foundations]
핵심  원리  및  개념  (Core Principles & Concepts)
본  과정은  AI 를  단순한  기술  도구가  아닌 , 인간의  전문성과  결합하여  최상의  성과를  창출하는  ' 사
고의  파트너 ' 로  정의함 . 기술의  빠른  변화  속에서도  변하지  않는  근본적인  협업  프레임워크를  제시
함 .
실전  활용  가이드  (Practical Implementation Guide)
AI 상호작용의  3 가지  진화  모델•
자동화  (Automation): 명확한  결과값이  존재하는  특정  작업을  사용자의  지시에  따라  AI 가
실행하는  단계  ( 예 : 문서  요약 , 이메일  초안  작성 ).
-
증강  (Augmentation): 정답이  없는  복잡한  문제에  대해  AI 를  ' 창의적  사고의  파트너 ' 로  대
우하며  탐색과  실험을  함께  수행하는  단계 .
-
에이전시  (Agency): 사용자가  구체적  행동  대신  지식  범위와  비전을  설정하면 , AI 가  독립
적으로  대리  업무를  수행하는  고도화된  단계 .
-
인간 -AI 협업을  위한  4D 프레임워크: 특정  도구나  프롬프트  유행에  의존하지  않는 , 효과적이고
윤리적인  상호작용을  위한  4 가지  핵심  역량임 .
•
위임  (Delegation): 전체  프로세스에서  인간의  전문성이  필요한  영역과  AI 의  효율성이  필
요한  영역을  전략적으로  분담하는  구조  설계  능력 .
-
설명  (Description): 단순한  명령을  넘어 , 풍부한  맥락 (Context) 을  제공하여  사용자의  비전
과  의도를  AI 에게  정확히  전달하는  소통  능력 .
-
분별  (Discernment): AI 가  생성한  결과물의  사실관계 , 논리 , 상호작용  방식을  비판적으로
검토하고  가치를  판단하는  검증  능력 .
-
성실  (Diligence): 데이터  프라이버시  보호 , 편향성  제어  등  AI 활용  전반에  걸쳐  투명성을
유지하고  최종  결과물에  책임을  지는  윤리적  역량 .
-
생성형  AI 의  기술적  본질과  작동  원리•
비검색  기반  생성: 데이터베이스에서  정보를  검색하는  것이  아니라 , 방대한  데이터  학습
을  통해  파악한  통계적  패턴을  바탕으로  새로운  텍스트를  생성 .
-
학습의  2 단계: 수십억  개의  텍스트로  언어의  지도를  구축하는  ' 사전  학습 (Pre-training)' 과
지시를  따르고  유해성을  피하도록  교정하는  ' 미세  조정 (Fine-tuning)' 으로  구성 .
-
컨텍스트  윈도우  (Context Window): AI 의  ' 작동  기억 (Working Memory)'. 한  번에  처리하
고  기억할  수  있는  정보량의  한계점 .
-
```

## Page 016

![Page 016](assets/claude-code-mastery-playbook/page-016.png)

### Transcription

```text
4D 프레임워크를  실무  워크플로우에  즉시  적용하기  위한  단계별  가이드라인과  프롬프트  엔지니
어링  기법임 .
전략적  인사이트  및  주의사항  (Strategic Insights & Considerations)
Step 1: 전략적  위임  (Delegation) 설계•
문제  인식: AI 개입  전 , 달성하려는  목표와  성공  기준을  인간의  전문성을  바탕으로  명확히
정의 .
-
플랫폼  인식: 활용할  AI 모델의  고유한  강점 ( 속도 , 창의성 , 정확도  등 ) 을  파악하여  적재적
소에  배치 .
-
과업  분배: 비판적  분석과  최종  결론  도출은  ' 인간 ' 이 , 방대한  자료  조사와  초안  작성은
'AI' 가  담당하도록  사고적  분업  실행 .
-
Step 2: 입체적  설명  (Description) 및  프롬프트  작성: AI 는  마음을  읽을  수  없음 . 다음  3 가지  차
원 (3P) 을  프롬프트에  반드시  포함할  것 .
•
제품  (Product): 최종  결과물의  형식 , 대상  독자 , 톤앤매너  명시 .-
프로세스  (Process): AI 가  취해야  할  접근  방식 , 분석  스타일 , 단계별  지침  제공 .-
성능  (Performance): 상호작용  태도  설정  ( 예 : " 내  가설에  비판적으로  도전해줘 ", " 다양한
가능성을  탐색해줘 ").
-
전문가를  위한  6 대  프롬프트  기법•
맥락  제공  (Give Context): 내가  누구이며 , 이  정보가  왜  필요하고  어디에  쓰일  것인지  배
경지식  상세  제공 .
-
예시  활용  (Show Examples): 원하는  출력  스타일이나  포맷을  예시로  제시하여  패턴  모방
유도  (Few-shot prompting).
-
제약  조건  설정  (Specify Constraints): 답변  길이 , 제외할  단어 , 특정  포맷 (Markdown,
JSON 등 ) 을  명확히  지정 .
-
단계별  분해  (Break into Steps): 복잡한  작업은  순서를  나열하여  AI 의  논리적  오류  방지
(Chain of Thought).
-
먼저  생각하게  하기  (Ask to Think First): 답변  도출  전 , 문제의  요인과  제약  사항을  먼저
검토할  수  있는  사고  공간 (Thinking space) 부여 .
-
역할  부여  (Define Role): "10 년  차  UX 전문가로서 " 와  같이  특정  페르소나를  부여하여  전
문적인  시각  유도 .
-
Step 3: 설명 - 식별  루프  (Description-Discernment Loop)•
제품  분별: 결과물이  사실적으로  정확한가 ? 실제  문제를  해결하는가 ?-
프로세스  분별: AI 의  사고  과정에  논리적  비약이나  순환  논리가  없는가 ?-
반복과  실험  (Iteration): 분별을  통해  발견된  문제점을  바탕으로  프롬프트 ( 설명 ) 를  수정하
고 , 만족스러운  결과가  나올  때까지  피드백  루프  가동 . 막혔을  때는  새로운  대화창을  여는
것이  효과적 .
-
```

## Page 017

![Page 017](assets/claude-code-mastery-playbook/page-017.png)

### Transcription

```text
AI 도입의  실질적  가치를  극대화하고  리스크를  최소화하기  위해  리더와  실무자가  반드시  숙지해
야  할  전략적  관점임 .
마스터  한  줄  평: "AI 는  지시를  따르는  단순한  도구가  아니라  비전을  공유하는  '; 사고의  파트너 ' 이
며 , 성공적인  협업의  완성은  기술의  성능이  아닌  인간의  명확한  설명 (Description) 과  비판적  분별력
(Discernment) 에  달려  있음 ."
책임감  있는  AI 활용  (Diligence) 3 원칙•
생성  성실성  (Creation Diligence): 민감한  데이터  입력  전 , 해당  AI 시스템의  데이터  보호
정책과  조직의  보안  규정을  비판적으로  검토 .
-
투명성  성실성  (Transparency Diligence): 업무  결과물에  AI 가  기여한  바를  동료  및  이해
관계자에게  정직하게  공개하여  신뢰  기반의  협업  환경  조성 .
-
배포  성실성  (Deployment Diligence): AI 가  생성한  콘텐츠의  사실  여부 , 편향성 , 저작권
등을  직접  검증 . 최종  결과물에  대한  책임은  전적으로  인간에게  있음 .
-
치명적인  안티  패턴  (Anti-patterns) 및  주의사항•
환각  현상 (Hallucination) 맹신: AI 는  매우  자신감  있는  어조로  틀린  정보를  제공할  수  있
음 . 인간의  도메인  전문성을  바탕으로  한  교차  검증 (Fact-checking) 이  필수적임 .
-
지식  컷오프 (Knowledge Cutoff) 간과: 모델이  학습된  특정  시점  이후의  최신  정보는  알지
못함을  인지하고 , 필요시  외부  검색  도구 (RAG 등 ) 와  결합해야  함 .
-
과도한  컨텍스트  주입: 컨텍스트  윈도우의  한계를  초과하면  AI 가  대화의  앞부분이나  핵심
지시사항을  잊어버릴  수  있음 . 핵심만  간결하게  유지할  것 .
-
비결정론적  특성  무시: 동일한  프롬프트에도  매번  다른  결과가  나올  수  있음 . 일관성이  극
도로  중요한  작업 ( 예 : 엄격한  코드  생성 , 규정  준수  문서 ) 에서는  인간의  철저한  감독이  요
구됨 .
-
' 은총알 (Silver Bullet)' 의  환상: AI 는  모든  문제를  해결하는  마법이  아님 . 도메인  지식이  부
족한  상태에서의  무분별한  위임은  프로젝트의  방향성을  상실하게  만듦 .
-
```

## Page 018

![Page 018](assets/claude-code-mastery-playbook/page-018.png)

### Transcription

```text
[Course 6: Building with the Claude API]
핵심  원리  및  개념  (Core Principles & Concepts)
본  코스는  Claude API 를  단순한  텍스트  생성  도구가  아닌 , 신뢰할  수  있는  엔터프라이즈급  AI 시스
템으로  통합하기  위한  근본적인  아키텍처와  엔지니어링  원리를  다룸 .
실전  활용  가이드  (Practical Implementation Guide)
실무  환경에서  Claude API 의  성능과  효율성을  극대화하기  위한  구체적인  구현  패턴과  체크리스트
임 .
상태  비저장 (Stateless) 대화와  메시지  수명주기: Claude API 는  이전  대화의  맥락을  기억하지
않음 . 다중  턴 (Multi-turn) 대화를  구현하려면  개발자가  직접  사용자 (User) 와  어시스턴트
(Assistant) 의  메시지  배열 (History) 을  관리하고 , 매  요청마다  전체  컨텍스트를  전송해야  함 .
•
프롬프트  엔지니어링과  평가 (Evaluation) 파이프라인: 직관에  의존한  프롬프트  작성을  배제
함 . 명확한  지시 , XML 태그를  통한  구조화 , 다중  샷 (Multi-shot) 예제를  통해  품질을  제어함 . 더
중요한  것은  ' 측정할  수  없는  것은  개선할  수  없다 ' 는  원칙  하에 , 테스트  데이터셋을  구축하고
모델  기반  채점자 (Model Grader) 를  통해  객관적인  점수를  산출하는  반복적인  평가  파이프라인
을  구축하는  것임 .
•
도구  사용 (Tool Use) 과  모델  컨텍스트  프로토콜 (MCP): Claude 의  훈련  데이터  한계를  극복하
기  위해  외부  함수 (Tools) 를  연결함 . MCP(Model Context Protocol) 는  이러한  도구 , 리소스 , 프롬
프트를  표준화된  서버 - 클라이언트  구조로  분리함 . 이를  통해  개발자는  매번  복잡한  통합  코드
를  작성할  필요  없이 , 외부  시스템 (GitHub, DB 등 ) 의  기능을  Claude 에게  매끄럽게  제공할  수
있음 .
•
검색  증강  생성 (RAG) 과  하이브리드  검색: 대규모  문서를  처리하기  위해  텍스트를  논리적  청크
(Chunk) 로  분할하고  임베딩을  생성함 . 의미론적  검색 (Semantic Search) 이  놓치기  쉬운  고유
명사나  ID 검색의  한계를  보완하기  위해 , 정확한  키워드  매칭을  지원하는  BM25(Lexical
Search) 를  결합한  다중  인덱스 (Multi-Index) 하이브리드  검색  아키텍처를  활용함 .
•
워크플로우 (Workflows) vs. 에이전트 (Agents): 해결하려는  문제의  성격에  따라  아키텍처를
선택해야  함 . 단계가  명확한  작업은  병렬화 (Parallelization), 체이닝 (Chaining), 라우팅 (Routing)
등의  ' 워크플로우 ' 로  설계하여  신뢰성과  예측  가능성을  극대화함 . 반면 , 예측  불가능하고  다양
한  변수가  있는  작업은  추상적인  도구를  제공하여  모델이  스스로  계획을  수립하는  ' 에이전트 '
패턴을  적용함 .
•
1. 구조화된  데이터 (JSON) 완벽  추출  기법: 설명  텍스트  없이  순수한  JSON 이나  코드만  추출
해야  하는  자동화  파이프라인에서는  어시스턴트  메시지  프리필링 (Prefilling) 과  중단  시퀀스
(Stop Sequences) 를  결합함 .
•
```

## Page 019

![Page 019](assets/claude-code-mastery-playbook/page-019.png)

### Transcription

```text
전략적  인사이트  및  주의사항  (Strategic Insights & Considerations)
성공적인  AI 프로덕트  런칭을  위해  실무자가  반드시  인지해야  할  아키텍처적  트레이드오프와  안
티  패턴임 .
messages = [
    {"role": "user", "content": "AWS CLI 명령어  3 개를  JSON 배열로  생성해줘 .",}
    {"role": "assistant", "content": "```json"} # 프리필링 : 마크다운  시작  강제
]
# 중단  시퀀스  설정 : 마크다운  종료  태그에서  생성  즉시  중단
response = chat(messages, stop_sequences=["```"])
2. 다중  턴  도구  호출 (Multi-turn Tool Use) 루프  구현: Claude 가  도구를  요청할  때  이를  처리하
고  결과를  반환하는  자동화된  대화  루프를  구축해야  함 .
•
감지: 응답의  stop_reason 이  "tool_use" 인지  확인함 .-
실행: response.content 내의  tool_use 블록에서  함수  이름과  인자 (Input) 를  추출
하여  로컬  함수를  실행함 .
-
결과  반환: 실행  결과를  tool_result 타입의  블록으로  구성하여  사용자 (User) 메시지
로  Claude 에게  다시  전송함 . ( 이때  tool_use_id 가  반드시  일치해야  함 .)
-
3. 프롬프트  캐싱 (Prompt Caching) 을  통한  비용 / 지연  시간  최적화: 대형  시스템  프롬프트나
복잡한  도구  스키마를  반복적으로  전송할  때  캐싱을  적용하여  비용과  속도를  개선함 . ( 최소
1024 토큰  이상  시  유효 , 1 시간  유지 )
•
시스템  프롬프트나  도구  배열의  마지막  항목에  {"cache_control": {"type":
"ephemeral"}} 속성을  추가하여  캐시  중단점 (Breakpoint) 을  설정함 .
-
주의 : 캐시  중단점  이전의  내용이  단  한  글자라도  변경되면  캐시가  무효화되므로 , 정적인
컨텍스트 ( 문서 , 스키마 ) 를  앞에  배치해야  함 .
-
4. RAG 파이프라인  최적화  체크리스트•
청킹  전략: 마크다운처럼  구조가  명확하면  헤더  기반 (Structure-based) 분할을 , 일반  텍스
트는  문장  기반  분할에  오버랩 (Overlap) 을  추가하여  문맥  유실을  방지함 .
-
원본  텍스트  저장: 벡터  DB 에는  임베딩  수치뿐만  아니라 , 검색  후  프롬프트에  주입할  원본
텍스트 (Content) 를  반드시  함께  저장해야  함 .
-
상호  순위  융합 (RRF): 벡터  검색 ( 의미 ) 과  BM25( 키워드 ) 의  결과를  병합할  때
RRF(Reciprocal Rank Fusion) 공식을  적용하여  가장  관련성  높은  청크를  도출함 .
-
온도 (Temperature) 파라미터의  전략적  튜닝: 모든  작업에  기본값을  사용하지  마십시오 . 데이
터  추출 , 코드  생성 , 사실  기반  응답에는  0.0 ~ 0.3( 결정론적 ) 을  적용하고 , 브레인스토밍이나  창
의적  글쓰기에는  0.8 ~ 1.0 을  적용해야  함 . 목적에  맞지  않는  온도는  할루시네이션이나  경직된
응답의  주원인이  됨 .
•
단일  거대  프롬프트의  한계  (The Long Prompt Problem): 수많은  제약  조건 ( 예 : "AI 임을  밝히
지  말  것 ", " 이모지  금지 ", " 전문적  톤  유지 ") 을  하나의  프롬프트에  몰아넣으면  모델이  일부  지시
를  누락함 . 이를  해결하기  위해  초안  생성  후  수정  지시를  내리는  체이닝 (Chaining) 이나 , 요청
유형을  먼저  분류하고  특화된  프롬프트로  보내는  라우팅 (Routing) 워크플로우를  도입해야  함 .
•
```

## Page 020

![Page 020](assets/claude-code-mastery-playbook/page-020.png)

### Transcription

```text
마스터  한  줄  평: "Claude API 는  단순한  텍스트  생성기를  넘어 , 명확한  지시 , 도구  통합 , 그리고  체
계적인  평가를  통해  신뢰할  수  있는  자율형  AI 시스템을  구축하는  강력한  엔지니어링  플랫폼 ."
에이전트  환경  검사 (Environment Inspection) 누락  ( 치명적  안티  패턴 ): 에이전트에게  파일  수
정이나  UI 조작  권한을  줄  때 , ' 결과를  관찰할  수  있는  도구 ' 를  제공하지  않으면  에이전트는  맹
인과  같음 . 코드를  수정하기  전에  파일을  읽고 (Read), UI 조작  후  스크린샷을  확인하는  피드백
루프를  시스템  프롬프트에  명시적으로  강제해야  함 .
•
스트리밍 (Streaming) 과  도구  호출의  UX 딜레이: 도구  호출  시  API 는  완전한  JSON 키 - 값  쌍이
완성될  때까지  청크를  버퍼링하므로  UI 에  지연이  발생할  수  있음 . 즉각적인  반응이  필요하다
면  fine_grained=True 를  설정하여  검증을  우회할  수  있으나 , 이  경우  클라이언트  측에서
불완전한  JSON 에  대한  예외  처리 (Error Handling) 를  반드시  직접  구현해야  함 .
•
에이전트  만능주의  경계  (Workflows > Agents): 에이전트는  유연하지만  예측  가능성과  작업
성공률이  상대적으로  낮음 . 프로덕션  환경의  사용자는  ' 멋진  에이전트 ' 보다  ' 일관되게  작동하
는  제품 ' 을  원함 . 가능한  한  신뢰성이  높은  워크플로우  패턴 ( 평가자 - 최적화자  등 ) 을  우선  적용
하고 , 에이전트는  사전  정의가  불가능한  동적인  영역에만  제한적으로  도입할  것 .
•
```

## Page 021

![Page 021](assets/claude-code-mastery-playbook/page-021.png)

### Transcription

```text
[Course 7: Introduction to Model Context Protocol]
핵심  원리  및  개념  (Core Principles & Concepts)
Model Context Protocol(MCP) 은  대규모  언어  모델 (LLM) 이  외부  데이터  및  도구와  상호작용  할  수
있도록  설계된  표준  통신  계층 (Communication Layer) 임 . 복잡한  통합  코드를  작성하는  부담을  줄
이고 , 모델에  필요한  컨텍스트를  우아하게  제공함 .
실전  활용  가이드  (Practical Implementation Guide)
공식  Python MCP SDK 를  활용하면  복잡한  JSON 스키마를  수동으로  작성할  필요  없이 , 파이썬  데
코레이터와  타입  힌트만으로  강력한  서버와  클라이언트를  구축할  수  있음 .
1. 아키텍처의  분리와  책임  전가  (Shift the Burden)•
기존  방식의  한계: 개발자가  수많은  API 엔드포인트에  대응하는  도구  스키마 (Schema) 와
함수를  직접  정의 , 테스트 , 유지보수해야  하는  높은  비용이  발생했음 .
-
MCP 아키텍처: 시스템을  클라이언트 (Client) 와  서버 (Server) 로  분리함 . 도구  정의와  실행
의  부담을  특화된  'MCP 서버 ' 로  넘김 . 개발자는  이미  정의된  서버를  연결하기만  하면  됨 .
-
전송  방식  독립성  (Transport Agnostic): 특정  프로토콜에  구애받지  않음 . 로컬  환경에서
는  Standard IO 를 , 원격  환경에서는  HTTP, Webhooks, Websockets 등을  유연하게  사용함 .
-
2. MCP 서버의  3 대  핵심  구성  요소  (Primitives): MCP 서버는  외부  서비스 ( 예 : GitHub, Google
Drive) 와  LLM 사이의  래퍼 (Wrapper) 역할을  하며 , 다음  세  가지  요소를  제공함 .
•
Tools ( 도구 ): 모델  (Claude) 제어 . 모델이  필요에  따라  스스로  판단하여  호출하는  실행  가
능한  기능적  인터페이스임 . ( 예 : 파일  수정 , API 호출 )
-
Resources ( 리소스 ): 애플리케이션  (App) 제어 . 서버가  보유한  데이터나  문서를  클라이언
트에게  공유하는  읽기  전용  통로임 . 컨텍스트  주입에  사용됨 .
-
Prompts ( 프롬프트 ): 사용자  (User) 제어 . 모델이  특정  작업을  더  잘  수행하도록  서버에  미
리  튜닝  및  저장된  고품질의  지침  템플릿임 .
-
3. 전체  통신  흐름  (Request-Response Flow)•
도구  탐색: 클라이언트가  서버에  ListToolsRequest 를  보내  사용  가능한  도구  목록을
확보함 .
-
모델  전달: 사용자  질문과  도구  목록이  Claude 에게  전달됨 .-
실행  결정  및  요청: Claude 가  도구  사용을  결정하면 , 클라이언트는  서버에
CallToolRequest 를  보냄 .
-
결과  반환: 서버가  외부  API 를  호출한  뒤  CallToolResult 를  반환하고 , Claude 는  이를
바탕으로  최종  답변을  생성함 .
-
```

## Page 022

![Page 022](assets/claude-code-mastery-playbook/page-022.png)

### Transcription

```text
전략적  인사이트  및  주의사항  (Strategic Insights & Considerations)
MCP 를  실무에  도입할  때  아키텍처의  의도를  정확히  이해하고 , 세  가지  원시  요소  (Primitives) 를
목적에  맞게  취사선택하는  것이  프로젝트의  성패를  좌우함 .
1. MCP 서버  구축  (Server Implementation)•
초기화: from mcp.server.fastmcp import FastMCP 를  사용하여  단  한  줄로  서버를
초기화함 .
-
Tools 정의  ( @mcp.tool): 함수  위에  데코레이터를  추가하여  도구로  등록함 .
pydantic 의  Field 와  파이썬  타입  힌트를  사용하면  SDK 가  Claude 가  이해할  수  있는
JSON 스키마를  자동으로  생성함 .
-
Resources 정의  ( @mcp.resource):-
Direct Resource: 고정된  URI ( 예 : "docs://documents"). 인자  없이  목록  등을  반
환할  때  사용함 .
-
Templated Resource: 동적  매개변수  포함  ( 예 :
"docs://documents/{doc_id}"). SDK 가  URI 에서  인자를  자동  추출하여  함수에
전달함 .
-
반드시  mime_type( 예 : application/json, text/plain) 을  명시하여  클라이
언트가  데이터를  올바르게  파싱하도록  도움 .
-
Prompts 정의  ( @mcp.prompt): 사용자  입력  변수 ( 예 : doc_id) 를  받아  완성된  메시지
리스트 (list[base.Message]) 를  반환하도록  구성함 .
-
2. MCP 클라이언트  구축  (Client Implementation)•
세션  관리: stdio_client 와  ClientSession 을  사용하며 , 비동기  환경에서  리소스
누수를  막기  위해  AsyncExitStack 으로  연결을  안전하게  관리함 .
-
주요  메서드:-
list_tools() / call_tool(name, args): 도구  목록  조회  및  실행 .-
read_resource(uri): 반환된  ReadResourceResult 의  mimeType 을  확인하
여  JSON 파싱 (json.loads) 또는  일반  텍스트로  분기  처리함 .
-
list_prompts() / get_prompt(name, args): 프롬프트  템플릿  조회  및  변수가
보간된  최종  메시지  수신 .
-
3. 테스트  및  디버깅  (MCP Server Inspector): 전체  앱을  실행하지  않고도  서버  로직을  독립적
으로  검증할  수  있는  브라우저  기반  내장  도구임 .
•
실행  명령어: mcp dev mcp_server.py-
활용: 웹  UI 에  접속하여  Resources, Prompts, Tools 탭을  이동하며  인자를  직접  입력하고
반환되는  JSON/ 텍스트  결과를  실시간으로  확인함 . ( 예 : 문서  수정  도구  실행  후 , 읽기  도
구로  상태  변경  영속성  교차  검증 )
-
1. Primitives 선택을  위한  전략적  가이드라인•
```

## Page 023

![Page 023](assets/claude-code-mastery-playbook/page-023.png)

### Transcription

```text
마스터  한  줄  평: "MCP 는  복잡한  통합  코드를  제거하고 , 도구 ( 모델 )· 리소스 ( 앱 )· 프롬프트 ( 사용자 )
라는  명확한  역할  분담을  통해  LLM 과  외부  세계를  연결하는  가장  우아하고  표준화된  통신  계층 ."
Tools 모델에게  자율성을  부여할  때 : 계산 , 외부  API 호출 , 파일  수정  등  모델이  상황을  판
단하여  능동적으로  ' 행동 ' 해야  할  때는  도구를  사용할  것 .
-
Resources 앱의  컨텍스트를  주입할  때 : UI 의  자동  완성  목록을  구성하거나 , 사용자가  특
정  문서 (@doc) 를  멘션했을  때  도구  호출의  오버헤드  없이  즉각적으로  모델의  프롬프트
에  데이터를  밀어  넣어야 (Inject) 할  때  리소스를  사용할  것 .
-
Prompts 사용자  워크플로우를  표준화할  때 : 사용자가  매번  복잡한  지시사항을  입력하게
두지  말  것 . 도메인  지식이  반영된  정교한  프롬프트를  서버에  정의하고 , 사용자는  슬래시
명령어 (/format) 나  버튼  클릭만으로  일관된  고품질  결과를  얻게  할  것 .
-
2. 실무  적용  시  주의사항  (Anti-patterns & Details)•
수동  JSON 스키마  작성  지양: 과거의  API 연동  방식처럼  모델에게  도구를  설명하기  위해
방대한  JSON 을  직접  작성하지  말  것 . Python SDK 의  데코레이터와  pydantic.Field 의
description 속성을  활용하여  타입  검증과  스키마  생성을  자동화해야  유지보수성이
극대화됨 .
-
MIME 타입  처리  누락  주의: 클라이언트가  리소스를  읽어올  때 , 서버가  전달한
mime_type 을  무시하고  일괄적으로  텍스트로  처리하면  구조화된  데이터 (JSON 등 ) 의
이점을  잃게  됨 . 반드시  클라이언트  단에서  MIME 타입에  따른  분기  파싱  로직을  구현할
것 .
-
도구와  리소스의  혼동: 단순히  데이터를  읽어와서  프롬프트에  포함시키는  목적이라면
Tools 가  아닌  Resources 를  사용해야  함 . Tools 를  사용하면  모델이  도구를  호출할지  말지
결정하는  단계가  추가되어  응답  지연이  발생할  수  있음 .
-
클라이언트 / 서버  동시  구현의  오해: 본  교육  과정은  학습을  위해  둘  다  구현했지만 , 실제
프로덕션  환경에서는  일반적으로  MCP 서버만  구축하여  기존의  강력한  클라이언트 ( 예 :
Claude Desktop) 에  연결하거나 , 반대로  자체  앱을  위한  클라이언트만  구축하여  퍼블릭
MCP 서버들을  활용하는  방식으로  역할을  분리해야  함 .
-
```

## Page 024

![Page 024](assets/claude-code-mastery-playbook/page-024.png)

### Transcription

```text
[Course 8: AI Fluency for educators]
본  플레이북은  교육자가  AI 를  단순한  도구가  아닌  ' 사고의  파트너 (Thinking Partner)' 로  활용하여  교
과  과정  설계 , 학습  자료  제작 , 평가  개발  등  교육  활동  전반을  혁신하는  체계적인  방법론을  제공
함 .
핵심  원리  및  개념  (Core Principles & Concepts)
💡  핵심  마인드셋: AI 기술은  빠르게  변하므로  모든  것을  완벽히  알  필요는  없음 . 학생들과  함께  탐
구하고  더  나은  질문을  던지는  법을  배우는  과정  자체가  ' 유창성 ' 의  핵심임 .
실전  활용  가이드  (Practical Implementation Guide)
1. AI 유창성 (AI Fluency) 의  본질 : 자동화가  아닌  증강•
증강 (Augmentation) 중심: AI 가  인간의  업무를  단순히  대신하는  ' 자동화 (Automation)' 가
아니라 , 교육자의  전문성을  확장하고  더  나은  성과를  내도록  돕는  ' 증강 ' 에  초점을  맞춤 .
-
기술보다  교육학 (Pedagogy) 우선: 최신  AI 기능  숙지보다  교육자가  가진  기존의  교육적
가치관과  철학을  중심에  두고  AI 를  도구로써  녹여내는  것이  핵심임 .
-
2. 4D AI 유창성  프레임워크  (The 4D Framework): AI 와  효과적이고  윤리적으로  협업하기  위
한  4 가지  핵심  역량임 .
•
위임  (Delegation): 문제와  플랫폼을  인식하고 , 인간의  창의성 / 판단력과  AI 의  속도 / 데이터
처리  능력을  결합하여  어떤  작업을  맡길지  전략적으로  결정함 .
-
설명  (Description): 단순한  프롬프트  입력을  넘어 , 최종  결과물의  형식 , 프로세스 , AI 의  수
행  방식 ( 역할 ) 을  명확히  지시하고  구체적인  교육적  맥락을  제공함 .
-
식별  (Discernment): AI 가  생성한  결과물의  정확성 , 유용성 , 추론  과정을  비판적으로  평가
함 .
-
근면  (Diligence): 보안 , 개인정보  보호를  준수하고 , AI 의  역할과  기여도를  투명하게  밝히
며 , 최종  결과물에  대한  책임을  유지하는  윤리적  태도임 .
-
3. 설명 - 식별  루프  (Description-Discernment Loop): AI 에게  지시 ( 설명 ) 를  내리고 , 도출된  결
과를  비판적으로  평가 ( 식별 ) 한  뒤 , 그  이유를  AI 에게  피드백하여  다시  지시를  수정하는  지속적
인  상호작용  과정임 . 이  루프를  통해  AI 는  교육자의  의도를  깊이  학습하며  단순한  도구에서  진
정한  ' 사고의  파트너 ' 로  진화함 .
•
Phase 1: 교육  맥락  문서화  (Building Shared Context): 매번  처음부터  지시하지  않도록 , AI 와
공유할  ' 재사용  가능한  교육  환경  요약본 ' 을  생성함 .
•
사전  성찰  항목: 핵심  교육  가치  및  철학 , 직면한  제약 ( 제도 / 기술 / 시간 ), 학생들의  특성 ( 배
경 / 어려움 / 목표 ), 선호하는  교수법 .
-
```

## Page 025

![Page 025](assets/claude-code-mastery-playbook/page-025.png)

### Transcription

```text
전략적  인사이트  및  주의사항  (Strategic Insights & Considerations)
프롬프트  예시: " 나는  교육자로서  향후  AI 와의  협업을  위해  내  교육  방식과  맥락을  담은  재
사용  가능한  요약  문서를  만들고  싶어 . 내  과목 , 학생들의  어려움 , 교육  철학에  대해  네가
나를  인터뷰해  줘 . 대화를  통해  정보를  종합함 ."
-
Phase 2: 교과  과정  설계  워크플로우  (Course Design): 4D 프레임워크를  적용하여  고수준의
계획부터  구체적인  학습  목표까지  도출함 .
•
개념  식별  ( 위임  & 설명 ): 일반적인  주제  요구가  아닌  구체적  맥락을  제공함 . ( 예 : " 수학에
불안감이  있는  저널리즘  전공  학생들을  위한  통계  코스를  설계  중이야 . 적합한  주제를  제
안함 .")
-
학습  여정  매핑  ( 역할극  활용 ): AI 에게  학생  페르소나를  부여하여  사각지대를  발견함 . ( 예 :
" 내  학생  중  한  명처럼  행동해  봐 . 이  3 주  차  강의  계획에서  어느  부분에서  가장  혼란을  느
낄  것  같니 ?")
-
학습  목표  도출: 강의  계획서를  업로드하고 , 학습  목표를  실제  ' 이력서  역량 (Resume
Skills)' 과  매칭하여  학생들의  동기  부여를  강화하도록  AI 에게  지시함 .
-
Phase 3: 학습  자료  및  평가  도구  제작  (Material Creation): 구축된  맥락을  바탕으로  일관된  학
습  여정을  지원하는  자료를  제작함 .
•
워크시트 / 연습문제  제작: 결과물뿐만  아니라  AI 가  작업할  ' 프로세스 ' 를  지시함 . ( 예 : " 지난
주  논의한  소셜  미디어  분석  사례를  활용해서 , 10 학년  읽기  수준에  맞춘  귀무가설  연습  문
제를  만들어줘 . 순서는  1) 오개념  짚기 , 2) 일상  사례  제시 , 3) 변수  식별  순으로  구성해 .")
-
식별 (Discernment) 적용: AI 의  제안을  단순히  수용 / 거부하지  않고  ' 왜 ' 적절한지  또는  부적
절한지  AI 에게  설명하여  파트너를  교육시킴 .
-
평가  도구 (Quiz) 제작: 다양한  난이도와  문제  유형 ( 객관식 , 단답형 , 적용형 ) 을  혼합하고 , AI
에게  정답과  오답에  대한  상세한  해설 ( 왜  맞고  틀린지 ) 을  작성하도록  지시함 .
-
전략적  가치  (Strategic Value)•
효율성을  넘어선  역량  강화  (Enhancement over Efficiency): AI 활용의  진정한  가치는  자
료를  ' 빨리 ' 만드는  데  있지  않음 . 교육  과정  전반에  걸쳐  논리적으로  연결된  ' 고품질 ' 의  학
습  경험을  설계하고  교육의  질을  높이는  데  있음 .
-
숨겨진  가설의  표면화: AI 와의  대화  및  협업  과정은  교육자  스스로가  무의식적으로  가지
고  있던  편견이나  숨겨진  가설 , 교육적  사각지대를  발견하는  강력한  계기가  됨 .
-
지속  가능한  프레임워크: 특정  AI 도구의  ' 비밀  프롬프트 ' 를  외우는  것은  무의미함 . 4D 모
델은  기술이  진화하더라도  변하지  않는  교육자의  본질적인  개인적  역량 (Personal
Competencies) 을  구축함 .
-
주의사항  및  안티  패턴  (Anti-patterns & Warnings)•
맥락  없는  일반적  지시  (Context-less Prompts): " 워크시트  만들어줘 ", " 통계학  주제  알려
줘 " 와  같은  지시는  실패의  지름길임 . 반드시  학생의  특성 , 제약  사항 , 교육  철학이  담긴  구
체적인  ' 문제  공간 (Problem Space)' 으로  AI 를  초대해야  함 .
-
무비판적  수용  및  아웃소싱  (Outsourcing Decisions): AI 가  초안을  훌륭하게  작성하더라
도 , 편향성 , 오류 , 학습  목표와의  정렬  상태를  최종적으로  검토하고  결정할  책임은  항상  교
-
```

## Page 026

![Page 026](assets/claude-code-mastery-playbook/page-026.png)

### Transcription

```text
마스터  한  줄  평: "AI 유창성이란  기술적  숙련도를  넘어 , 확고한  교육  철학을  바탕으로  AI 를  비판적
사고의  파트너로  삼아  인간의  전문성을  증폭시키는  과정 ."
육자  (Human-in-the-loop) 에게  있음 .
투명성  결여  (Lack of Transparency): AI 활용  사실을  숨기는  것은  학업적  무결성을  해침 .
교육자가  먼저  AI 를  어떻게  활용하고  검증했는지  문서화하고  학생들에게  공유함으로써 ,
책임감  있는  AI 사용의  롤모델이  되어야  함 .
-
```

## Page 027

![Page 027](assets/claude-code-mastery-playbook/page-027.png)

### Transcription

```text
[Course 9: AI Fluency for students]
핵심  원리  및  개념  (Core Principles & Concepts)
본  과정은  AI 를  단순히  작업을  자동화하는  도구가  아닌 , 학습과  경력  개발을  위한  ' 사고의  파트너
(Thinking Partner)' 로  활용하는  근본적인  방법론을  제시함 .
💡  핵심  인사이트 : 설명 - 통찰  루프  (Description-Discernment Loop)
AI 활용  능력은  단번에  완성되지  않음 . 명확한  ' 설명 ' 을  통해  결과를  얻고 , 이를  비판적으로  ' 통찰 ' 하
여  다시  설명을  수정하는  지속적인  피드백  루프를  통해  진정한  사고의  파트너십이  형성됨 .
실전  활용  가이드  (Practical Implementation Guide)
4D 프레임워크를  학업과  경력  설계에  즉시  적용할  수  있는  구체적인  워크플로우임 .
자동화 (Automation) 가  아닌  확장 (Augmentation): AI 유창성의  핵심은  AI 에게  일을  떠넘기는
것 ( 자동화 ) 이  아님 . 인간이  주도권을  쥐고  AI 와  협력하여  자신의  지식 , 비판적  사고 , 문제  해결
능력을  증폭 ( 확장 ) 시키는  데  있음 .
•
AI 유창성 (AI Fluency) 의  정의: 특정  프롬프트  기술이나  일시적인  도구  사용법을  넘어서는  개
념임 . 기술의  변화와  무관하게  AI 와  효과적 (Effective), 효율적 (Efficient), 윤리적 (Ethical), 안전
(Safe) 하게  협업할  수  있는  지속  가능한  핵심  역량임 .
•
4D 프레임워크  (The 4D Framework): AI 와의  성공적인  협업을  위한  4 가지  필수  역량•
위임  (Delegation): 문제의  본질을  인식하고 , 인간의  창의성과  AI 의  속도를  고려하여  어떤
작업을  AI 에게  맡길지  지능적으로  결정하는  능력 .
-
설명  (Description): 단순한  명령을  넘어 , 결과물의  형식 (Product), 사고의  과정 (Process),
AI 의  페르소나 (Performance) 를  구체적으로  설정하여  생산적인  대화를  이끄는  능력 .
-
통찰 / 식별  (Discernment): AI 가  생성한  결과물의  정확성과  논리적  근거를  비판적으로  검
토하고 , 스스로의  학습  상태를  점검하는  능력 .
-
성실  (Diligence): 보안  유지 , AI 사용  사실의  투명한  공개 , 그리고  최종  결과물에  대해  인
간이  전적으로  책임을  지는  윤리적  태도 .
-
A. 학습  파트너로서의  AI 세팅  (AI as a Learning Partner)•
학습  컨텍스트  문서 (Learning Context Document) 생성: AI 와  대화하기  전 , 본인의  전공 ,
취약  과목 , 학습  스타일 , 목표  등을  정리한  문서를  AI 에게  제공하여  맞춤형  지원의  기반을
마련할  것 .
-
페르소나  및  상호작용  방식  지정  ( 프롬프트  예시 ): " 나는  [ 전공 / 학년 ] 학생이야 . 이  개념의
정답을  바로  설명해주지  마 . 대신  튜터처럼  행동하면서 , 내가  스스로  생각하고  답을  찾아
갈  수  있도록  이전  수업  내용과  연결된  질문을  단계별로  던져줌 ."
-
```

## Page 028

![Page 028](assets/claude-code-mastery-playbook/page-028.png)

### Transcription

```text
전략적  인사이트  및  주의사항  (Strategic Insights)
AI 시대에  대체  불가능한  경쟁력을  갖추기  위해  반드시  유념해야  할  전략적  관점과  경계해야  할  함
정임 .
살아있는  학습  일지 (Living Learning Journal) 운영: 주간  단위로  AI 와  함께  ' 이번  주  학습
한  개념 ', 'AI 의  도움을  받은  부분  vs 독립적으로  수행한  부분 ', ' 새롭게  깨달은  점 ' 을  기록하
고  성찰할  것 .
-
B. 경력  설계  및  취업  준비  워크플로우  (AI in Career Planning)•
경력  탐색  ( 정보  수집과  자아  성찰의  결합 ): AI 의  강점 ( 산업  트렌드 , 필요  기술 , 연봉  정보
등  광범위한  데이터  수집 ) 과  인간의  고유  영역 ( 에너지를  얻는  업무 , 개인적  가치관 ) 을  결
합하여  최적의  진로를  브레인스토밍  할  것 .
-
이력서 (CV/Resume) 개선  3 단계:-
1. 비판적  분석  요청: AI 에게  목표  직무  기술서와  현재  이력서를  제공하고 , 누락되거
나  불명확한  부분에  대한  ' 개선  To-do 리스트 ' 작성을  지시함 .
-
2. 경험  구체화: AI 가  던지는  질문에  구체적인  사례로  답하며  본인의  경험을  깊이  있
게  발굴함 .
-
3. 진정성  있는  수정: AI 의  분석을  바탕으로 , 반드시  ' 본인의  목소리 ' 로  이력서를  최종
수정함 . (AI 가  작성한  일반적인  문장  지양 )
-
모의  면접  코치  세팅  ( 프롬프트  예시 ): " 내  이력서와  직무  기술서를  바탕으로  실전  면접  질
문  5 가지를  준비해  줘 . 반드시  한  번에  하나의  질문만  하고  내  답변을  기다려 . 필요하다면
꼬리  질문을  1 개만  하고  다음  질문으로  넘어가 . 모든  질문이  끝난  후  내  답변의  명확성과
직무  적합성에  대해  피드백함 ."
-
인간  주도권  유지  (Being the Human in the Loop)•
의사결정의  주체: AI 와의  모든  상호작용에서  배의  키를  쥐는  것은  인간이어야  함 . 무엇을
질문할지  결정하고 , 결과물의  품질을  평가하며 , 최종적으로  어떻게  사용할지  판단하는  것
은  전적으로  인간의  몫임 .
-
대체  불가능한  인간의  가치: 기술이  아무리  발전해도  개인의  고유한  재능 , 삶의  경험 , 윤리
적  판단력 , 그리고  타인에  대한  보살핌 (Care) 은  AI 가  결코  모방할  수  없는  핵심  경쟁력임 .
-
경계해야  할  안티  패턴  (Anti-patterns)•
학습의  외주화  ( 핵심  근육의  퇴화 ): 과제나  글쓰기를  AI 에게  전적으로  맡기면 , 실제  시험이
나  실무에서  스스로  문제를  해결하고  논리를  전개하는  ' 비판적  사고  근육 ' 이  약화됨 . AI 는
코치이지  대리인이  아님 .
-
진정성  상실  (Generic Content): AI 가  생성한  뻔하고  일반적인  이력서나  자기소개서는  고
용주들이  즉각적으로  알아챔 . AI 는  아이디어를  다듬는  데  사용하되 , 최종  결과물에는  반
드시  본인만의  구체적인  경험과  진정성이  담겨야  함 .
-
무비판적  수용  ( 통찰의  부재 ): AI 의  답변을  사실  확인이나  논리적  검증  없이  그대로  수용하
는  것은  치명적인  오류를  낳을  수  있음 . 항상  " 내가  이  결과물을  온전히  설명하고  책임질
수  있는가 ?" 를  자문해야  함 .
-
```

## Page 029

![Page 029](assets/claude-code-mastery-playbook/page-029.png)

### Transcription

```text
마스터  한  줄  평: "AI 는  당신의  일을  대신하는  도구가  아니라 , 당신이  더  깊이  생각하고  고유한  가
치를  발휘하도록  돕는  사고의  파트너 (Thinking Partner)."
개인적  약속  (Personal Commitment) 수립: 성공적인  AI 활용을  위해  자신만의  'AI 협업  가이
드라인 ( 북극성 )' 을  명문화할  것 . 포함되어야  할  내용 : AI 를  절대  사용하지  않을  영역 (Red lines),
학습  시  AI 활용  원칙 , AI 사용  사실에  대한  투명성  공개  기준 , AI 없이  독립적으로  훈련할  핵심
기술  목록 .
•
```

## Page 030

![Page 030](assets/claude-code-mastery-playbook/page-030.png)

### Transcription

```text
[Course 10: Model Context Protocol: Advanced Topics]
핵심  원리  및  개념  (Core Principles & Concepts)
MCP(Model Context Protocol) 의  고급  기능과  서버 - 클라이언트  아키텍처를  관통하는  4 가지  핵심
원리임 .
실전  활용  가이드  (Practical Implementation Guide)
실무  환경에서  MCP 서버를  구축하고  고도화하기  위한  구체적인  구현  가이드라인임 .
샘플링  (Sampling): 책임과  비용의  전가•
서버가  직접  LLM(Claude 등 ) 에  연결하는  대신 , 연결된  클라이언트에게  텍스트  생성을  위
임하는  기술임 .
-
서버의  구조적  복잡성을  낮추고 , API 키  관리  및  토큰  생성  비용  부담을  클라이언트 ( 사용
자 ) 측으로  완벽히  이전함 .
-
루트  시스템  (Roots): 컨텍스트  기반의  안전한  파일  탐색•
서버가  접근할  수  있는  로컬  파일  시스템의  경계를  명시적으로  정의하는  권한  시스템임 .-
AI 가  파일의  정확한  전체  경로를  몰라도 , 허용된  루트  내에서  자율적으로  파일을  탐색
(Discovery) 할  수  있는  컨텍스트를  제공하여  UX 를  극대화함 .
-
양방향  JSON 메시지  아키텍처  (Bidirectional JSON Messages)•
JSON-RPC 2.0 표준을  따르며 , 응답을  기대하는  Request-Result 쌍과  단방향  상태  보
고인  Notification 으로  구성됨 .
-
가장  중요한  특징은  클라이언트뿐만  아니라  서버도  클라이언트에게  요청 (Server-initiated
Requests) 을  주도할  수  있다는  점임 . ( 예 : 샘플링  요청 , 루트  목록  요청 )
-
전송  메커니즘  (Transport Mechanisms): STDIO vs StreamableHTTP•
STDIO: 클라이언트가  서버를  자식  프로세스로  실행하여  표준  입출력 (stdin/stdout) 으로  통
신하는  로컬  최적화  방식임 .
-
StreamableHTTP: 원격  호스팅을  위한  방식으로 , HTTP 의  단방향성  한계를  극복하기  위
해  SSE(Server-Sent Events) 를  활용하여  서버에서  클라이언트로  메시지를  푸시함 .
-
A. UX 향상을  위한  알림 (Notification) 구현•
목적: 대규모  데이터  리서치  등  실행  시간이  긴  작업  시  사용자의  불확실성 ( 시스템  멈춤  오
해 ) 제거 .
-
서버  측  구현  (Context 객체  활용 ):-
로그  전송 : await context.info(" 리서치  진행  중 ...")-
```

## Page 031

![Page 031](assets/claude-code-mastery-playbook/page-031.png)

### Transcription

```text
전략적  인사이트  및  주의사항  (Strategic Insights & Considerations)
프로덕션  환경  배포  시  발생할  수  있는  아키텍처의  한계와  보안적  안티  패턴 (Anti-patterns) 을  분석
함 .
진행률  업데이트 : await context.report_progress( 현재값 , 전체값 )-
클라이언트  측  구현: ClientSession 생성  또는  도구  호출  시  logging_callback 및
progress_callback 함수를  인수로  전달하여  UI( 터미널 , 프로그레스  바  등 ) 에  반영함 .
-
B. 샘플링 (Sampling) 워크플로우  적용•
서버  측  ( 요청 ): 도구  함수  내에서  ctx.session.create_message 를  호출하여  프롬프
트 , 최대  토큰  수 , 시스템  프롬프트를  정의하고  클라이언트에  전송함 .
-
클라이언트  측  ( 실행 ): sampling_callback 함수를  작성하여  서버의  메시지를  실제
LLM(Anthropic SDK 등 ) 으로  전달하고 , 생성된  결과를  CreateMessageResult 형태로
서버에  반환함 .
-
C. Roots 기반  파일  접근  제어  체크리스트•
서버에  list_roots 및  read_dir 도구를  반드시  추가하여  AI 가  디렉토리를  탐색할
수  있도록  구성함 .
-
[ 필수 ] 서버  코드  내에  is_path_allowed() 와  같은  도우미  함수를  직접  구현해야  함 . 요
청된  경로가  승인된  루트  내에  있는지  검증한  후  파일  작업을  수행할  것 .
-
D. 전송  방식 (Transport) 설정  (FastMCP 기준 )•
로컬  환경  (STDIO): mcp.run(transport="stdio")-
주의 : 서버  코드  내에서  일반적인  print() 문  사용을  엄격히  금지함 . stdout 을  통신
채널로  사용하므로  프로토콜이  깨짐 . 반드시  MCP 로깅  알림을  사용할  것 .
-
원격  환경  (HTTP): mcp.run(transport="streamable-http")-
초기화 (POST) → SSE 연결 (GET) → 도구  호출 (POST) 의  다중  연결  구조로  작동함 .-
확장성 (Scaling) 과  기능의  치명적  트레이드오프•
이슈: 수많은  사용자를  처리하기  위해  로드  밸런서를  도입하면 , 클라이언트의  POST 요청
이  SSE 연결이  맺어지지  않은  다른  서버  인스턴스로  라우팅되어  통신이  단절될  수  있음 .
-
해결책: stateless_http=True 플래그를  설정하여  무상태  모드로  전환함 .-
주의사항  ( 기능  상실 ): 무상태  모드  활성화  시  SSE 우회  메커니즘이  비활성화됨 . 이로  인
해  서버  주도  요청 , 샘플링 , 진행  상황  보고 , 리소스  구독  기능이  모두  불가능해짐 . 단순  도
구  호출  서버에만  적합함 .
-
보안  책임의  오해  (Anti-pattern)•
위험: MCP SDK 가  Roots 에  지정된  경로  외의  접근을  ' 자동으로 ' 차단해  줄  것이라고  맹신
하는  것은  심각한  보안  취약점을  낳음 .
-
인사이트: Roots 는  AI 에게  탐색  컨텍스트를  제공할  뿐 , 물리적  접근  통제는  전적으로  서버
개발자의  몫임 . 모든  파일  I/O 작업  전  경로  검증  로직이  필수적임 .
-
```

## Page 032

![Page 032](assets/claude-code-mastery-playbook/page-032.png)

### Transcription

```text
마스터  한  줄  평: "MCP 의  진정한  가치는  단순한  도구  연결을  넘어 , 샘플링과  양방향  통신을  통해
AI 의  컨텍스트를  안전하고  확장  가능하게  제어하는  아키텍처적  유연성에  있음 ."
퍼블릭  서버  설계의  경제성•
누구나  접근  가능한  공개  MCP 서버를  구축할  때 , 서버가  직접  LLM API 키를  관리하는  것
은  비용  폭탄 (Anti-pattern) 으로  이어짐 .
-
반드시  ' 샘플링 (Sampling)' 아키텍처를  채택하여 , AI 통합의  복잡성과  토큰  과금  책임을  이
미  자격  증명을  갖춘  클라이언트  측으로  분리해야  함 .
-
JSON Response 플래그의  이해•
json_response=True 설정  시  스트리밍  응답이  비활성화되고  최종  결과만  순수  JSON
으로  반환됨 . 중간  진행  메시지나  로그가  필요  없는  단순  통합  시스템에  유용함 .
-
```

## Page 033

![Page 033](assets/claude-code-mastery-playbook/page-033.png)

### Transcription

```text
[Course 11: Claude with Amazon Bedrock]
본  플레이북은  Amazon Bedrock 환경에서  Anthropic 의  Claude 모델을  통합 , 배포  및  최적화하여
프로덕션  수준의  AI 애플리케이션과  자율  에이전트를  구축하기  위한  고밀도  실무  가이드라인임 .
핵심  원리  및  개념  (Core Principles & Concepts)
실전  활용  가이드  (Practical Implementation Guide)
모델  라인업과  트레이드오프  (Model Lineup & Trade-offs): Claude 는  지능 , 속도 , 비용의  우선
순위에  따라  세  가지  모델을  제공함 . 복잡한  추론과  자율적  프로젝트  관리가  필요한  경우
Opus, 코딩  능력과  텍스트  생성  속도의  완벽한  균형이  필요한  경우  Sonnet, 실시간  사용자  상
호작용과  비용  효율성이  최우선인  경우  Haiku 를  선택하는  전략적  접근이  필수적임 .
•
상태  비저장  API 와  컨텍스트  관리  (Stateless API &; Context): Bedrock API 와  Claude 는  이전
대화  내용을  저장하지  않음 . Multi-turn 대화에서  맥락을  유지하려면  개발자가  직접  전체  메시
지  히스토리 (User 와  Assistant 역할의  교차 ) 를  관리하고  매  요청마다  전달해야  함 .
•
도구  사용과  MCP (Tool Use & Model Context Protocol): Claude 의  지식  한계를  극복하는  핵
심  메커니즘임 . Tool Use 는  모델이  외부  데이터를  요청하고  실행  결과를  받아  답변을  생성하는
과정임 . MCP 는  이를  한  단계  발전시켜 , 개발자가  모든  도구를  직접  구현하는  대신  특화된
MCP 서버 (GitHub, DB 등 ) 를  통해  도구 , 리소스 , 프롬프트를  표준화된  방식으로  제공받는  아키
텍처임 .
•
검색  증강  생성  (RAG) 파이프라인: 대규모  문서  처리의  한계를  극복하기  위해  문서를  논리적
단위로  분할 (Chunking) 하고 , 임베딩 (Embedding) 하여  벡터  DB 에  저장함 . 사용자  질의  시  의미
론적  검색 (Semantic) 과  어휘론적  검색 (BM25) 을  결합하여  가장  관련성  높은  컨텍스트만을  프
롬프트에  주입하여  환각 (Hallucination) 을  방지함 .
•
자율  에이전트  (Autonomous Agents): 단순한  텍스트  생성을  넘어 , 환경을  관찰하고  도구를
반복적으로  사용하며  스스로  판단하여  목표를  달성하는  시스템임 . 터미널  기반의  코딩  어시스
턴트인  Claude Code 와  시각적  인터페이스를  직접  조작하는  Computer Use 가  대표적인  에이
전트  구현체임 .
•
1. 출력  제어  및  구조화  (Output Control): 프로그램에서  즉시  파싱  가능한  순수  데이터 (JSON,
코드  등 ) 를  추출하기  위한  필수  기법임 .
•
Message Prefilling: Assistant 메시지  배열의  끝에  ```json 과  같은  시작  구분자를  미리
채워  넣어 , 모델이  불필요한  서론 (Preamble) 없이  즉시  원하는  형식으로  답변을  시작하도
록  강제함 .
-
Stop Sequences: ``` 와  같은  중지  시퀀스를  설정하여 , 모델이  코드  블록을  닫으려  할
때  생성을  즉시  중단시킴 . 이를  통해  맺음말 (Footer) 을  원천  차단함 .
-
```

## Page 034

![Page 034](assets/claude-code-mastery-playbook/page-034.png)

### Transcription

```text
전략적  인사이트  및  주의사항  (Strategic Insights & Considerations)
XML 태그  구조화: 대규모  컨텍스트나  복잡한  지시사항을  전달할  때  <sales_records>
와  같은  XML 태그를  사용하여  데이터와  지시사항의  경계를  명확히  구분함 .
-
2. 프롬프트  평가  파이프라인  (Prompt Evaluations): 프롬프트는  직관이  아닌  데이터로  검증
해야  함 . 1~2 번의  수동  테스트는  프로덕션  환경에서  반드시  실패함 .
•
데이터셋  구축: 다양한  엣지  케이스를  포함한  평가  데이터셋을  구성함 .-
객관적  채점  (Graders): 모델의  출력을  평가하기  위해  구문  유효성을  검사하는  Code
Grader( 예 : JSON 파싱  성공  여부 ) 와 , 채점  기준 (Solution Criteria) 을  바탕으로  강점 / 약점 / 점
수를  논리적으로  반환하는  Model Grader 를  결합하여  사용함 .
-
3. 고급  RAG 파이프라인  구축: 단순한  벡터  검색의  한계를  극복하고  검색  정확도를  극대화하
는  워크플로우임 .
•
하이브리드  검색  (Hybrid Search): 의미론적  검색 (Vector) 과  정확한  키워드  매칭 (BM25) 을
병렬로  실행한  후 , RRF(Reciprocal Rank Fusion) 알고리즘을  사용하여  결과를  병합함 .
-
LLM 기반  Re-ranking: 병합된  검색  결과를  Claude 에게  전달하여  사용자  질의와의  실제
관련성을  기준으로  최종  순위를  재조정함 .
-
컨텍스트  검색  (Contextual Retrieval): 문서를  청킹할  때 , Claude 를  활용해  해당  청크가
전체  문서에서  차지하는  문맥 (Context) 을  요약하여  청크  텍스트에  추가한  뒤  임베딩함 .
-
4. 도구  사용  (Tool Use) 워크플로우:•
Step-by-Step:-
1. JSON Schema 로  도구의  이름 , 설명 , 매개변수를  상세히  정의하여  Claude 에  전달 .-
2. Claude 가  stopReason: "tool_use" 와  함께  도구  실행  요청  반환 .-
3. 로컬  서버에서  해당  함수  실행  후  결과  획득 .-
4. toolUseId 를  일치시킨  toolResult 메시지를  대화  히스토리에  추가하여
Claude 에  최종  답변  요청 .
-
1. 성능  및  비용  최적화  (Optimization)•
프롬프트  캐싱  (Prompt Caching): 시스템  프롬프트 , 도구  목록 , 대형  문서  등  반복적으로
전송되는  대규모  컨텍스트에  cachePoint 를  설정하십시오 . 초기  요청  시  캐시에  기록
(Write) 되고 , 이후  5 분  내의  후속  요청에서  이를  읽어 (Read) 지연  시간 (Latency) 과  비용을
획기적으로  절감할  수  있음 .
-
온도 (Temperature) 제어: 사실  기반의  데이터  추출이나  코딩  작업에는  0.0~0.3 의  낮은  온
도를 , 브레인스토밍이나  창의적  텍스트  생성에는  0.8~1.0 의  높은  온도를  설정하여  출력의
결정론적  성향을  제어해야  함 .
-
스트리밍  (Streaming): 사용자  경험 (UX) 향상을  위해  converse_stream 을  사용하여  전
체  응답을  기다리지  않고  생성되는  즉시  텍스트  청크를  UI 에  렌더링할  것 .
-
2. 안티  패턴  및  주의사항  (Anti-patterns)•
```

## Page 035

![Page 035](assets/claude-code-mastery-playbook/page-035.png)

### Transcription

```text
마스터  한  줄  평: "Claude 의  진정한  잠재력은  단순한  텍스트  생성이  아닌 , 도구와  컨텍스트를  결합
하여  자율적으로  문제를  해결하는  에이전트  워크플로우의  구축에  있음 ."
사용자  메시지에  시스템  지시사항  혼재: "AWS 서비스만  언급해 " 와  같은  제약사항을  매번
사용자  메시지에  넣는  것은  비효율적임 . System Prompt 를  통해  모델에  명확한  페르소나
( 예 : AWS 클라우드  지원  전문가 ) 를  부여하여  일관된  톤과  제약을  강제할  것 .
-
순차적  도구  호출의  늪: 여러  개의  독립적인  도구  호출이  필요할  때 , 모델이  이를  순차적으
로  처리하게  두면  지연  시간이  급증함 . 여러  도구를  동시에  호출할  수  있는  Batch Tool 패
턴을  구현하여  병렬  처리를  유도할  것 .
-
에이전트의  고위험  작업  투입: 에이전트는  코딩과  같이  ' 가치가  높지만  오류  비용이  낮은
(High value, Low error costs)' 작업에  최적화되어  있음 . 오류가  심각한  경제적 / 안전상  문제
를  초래할  수  있는  고위험  의사결정에는  자율  에이전트를  단독으로  사용하지  말  것 .
-
3. MCP 를  통한  아키텍처  분리•
모든  외부  연동  도구를  단일  애플리케이션  내에  직접  구현하는  것은  유지보수성을  저하시
킴 . MCP(Model Context Protocol) 를  도입하여  도구 (Tools), 리소스 (Resources), 프롬프트
(Prompts) 의  제공  책임을  특화된  MCP 서버로  위임할  것 . 이를  통해  클라이언트는  비즈니
스  로직에만  집중할  수  있는  확장  가능한  아키텍처를  확보할  수  있음 .
-
```

## Page 036

![Page 036](assets/claude-code-mastery-playbook/page-036.png)

### Transcription

```text
[Course 12: Claude with Google Cloud's Vertex AI]
핵심  원리  및  개념  (Core Principles & Concepts)
본  코스는  Claude AI 모델을  Google Cloud Vertex AI 환경에  통합하고 , 단순한  텍스트  생성을  넘어
자율적인  에이전틱 (Agentic) 시스템으로  확장하기  위한  근본적인  기술  스택을  다룸 .
실전  활용  가이드  (Practical Implementation Guide)
1. 모델  제품군과  상태  비저장 (Stateless) 아키텍처•
모델  최적화: 지능 (Opus), 균형 (Sonnet), 속도 (Haiku) 의  특성에  따라  유스케이스를  분리함 .-
Stateless 통신: Claude API 는  대화  기록을  기억하지  않음 . 다중  턴 (Multi-turn) 대화를  구현
하려면  애플리케이션  서버에서  전체  메시지  배열 (User/Assistant 역할 ) 을  로컬에  유지하고
매  요청  시  전체  컨텍스트를  전송해야  함 .
-
생성  프로세스: 토큰화 (Tokenization) → 임베딩 (Embedding) → 문맥화 (Contextualization)
→ 생성 (Generation) 의  4 단계를  거치며 , Max tokens, 자연스러운  종료 , 또는  Stop
sequence 도달  시  생성을  중단함 .
-
2. 프롬프트  엔지니어링  및  정량적  평가 (Evaluation)•
구조화된  프롬프트: XML 태그를  활용하여  데이터와  지시사항의  경계를  명확히  하고 , 시
스템  프롬프트로  페르소나를  부여하여  출력의  일관성을  확보함 .
-
평가  파이프라인: 직관에  의존한  테스트 (Option 1, 2) 를  배제하고 , 데이터셋  구축  → 모델
실행  → Grader( 코드 / 모델  기반 ) 채점  → 프롬프트  개선의  체계적인  루프 (Option 3) 를  통해
객관적인  성능  지표를  확보함 .
-
3. 도구  사용 (Tool Use) 과  모델  컨텍스트  프로토콜 (MCP)•
Tool Use: Claude 가  외부  세계 (API, DB) 와  상호작용하는  메커니즘임 . 모델에  JSON 스키
마로  도구를  정의해  주면 , 모델이  필요  시  tool_use 블록을  반환하고 , 서버가  이를  실행
한  뒤  tool_result 를  다시  모델에  전달하는  루프를  형성함 .
-
MCP (Model Context Protocol): 도구  통합의  복잡성을  해결하는  클라이언트 - 서버  아키
텍처임 . 개발자가  모든  도구를  직접  구현하는  대신 , 특화된  MCP 서버 ( 예 : GitHub, AWS) 가
도구 , 리소스 , 프롬프트를  제공하고  Claude(Client) 가  이를  호출하는  표준화된  통신  계층
임 .
-
4. 검색  증강  생성 (RAG) 파이프라인  고도화•
하이브리드  검색: 대규모  문서를  처리할  때 , 의미론적  이해를  위한  벡터  임베딩 (Semantic
Search) 과  정확한  키워드  매칭을  위한  어휘론적  검색 (BM25) 을  결합함 .
-
RRF (Reciprocal Rank Fusion): 서로  다른  스코어링  체계를  가진  검색  결과를  순위
(Rank) 기반으로  병합하여  최적의  컨텍스트를  추출함 .
-
```

## Page 037

![Page 037](assets/claude-code-mastery-playbook/page-037.png)

### Transcription

```text
전략적  인사이트  및  주의사항  (Strategic Insights & Considerations)
1. 출력  제어  및  프롬프트  최적화  기법•
메시지  프리필링 (Prefilling): 구조화된  데이터 (JSON, 코드 ) 만  추출할  때  유용함 . Assistant
메시지  배열  끝에  ```json 또는  { 를  미리  주입하여  모델이  불필요한  서술  없이  데이
터  생성만  이어가도록  강제함 .
-
Stop Sequences: stop_sequences=["```"] 파라미터를  설정하여 , 마크다운  코드  블
록이  닫히는  순간  텍스트  생성을  즉시  중단시켜  깔끔한  출력을  얻음 .
-
Multi-shot Prompting: 엣지  케이스 ( 예 : 비꼬는  표현의  감정  분석 ) 처리를  위해
<sample_input> 과  <ideal_output> 태그를  활용하여  이상적인  입출력  예시를  프롬
프트에  직접  제공함 .
-
2. Tool Use 및  다중  턴 (Multi-turn) 구현  워크플로우•
스키마  정의: Python 함수  작성  후 , name, description, input_schema 가  포함된
JSON 스키마를  작성함 . (Claude 에게  스키마  작성을  위임하는  것을  권장 )
-
다중  블록  메시지  처리: 도구  사용  시  Claude 는  텍스트  블록과  tool_use 블록이  섞인  응
답을  반환함 . 대화  기록을  유지하려면  텍스트만  추출하지  말고  전체
response.content 를  Assistant 메시지로  저장해야  함 .
-
Batch Tool 구현: Claude 가  여러  도구를  병렬로  호출하도록  유도하기  위해 , 여러  도구  호
출을  배열로  받는  'Batch Tool' 스키마를  우회적으로  구현하여  지연  시간 (Latency) 을  줄임 .
-
3. RAG 파이프라인  구축  단계•
Chunking: 문서  특성에  따라  Size-based( 문자  수 ), Structure-based( 마크다운  헤더 ),
Semantic-based( 문장  단위 ) 전략을  선택하고  반드시  오버랩 (Overlap) 을  설정함 .
-
Embedding: Vertex AI 의  text-embedding-005 모델을  사용하여  텍스트를  벡터로  변
환하고  정규화 (Normalization) 하여  벡터  DB 에  저장함 .
-
Contextual Retrieval: 청크가  원본  문맥을  잃는  것을  방지하기  위해 , 청킹  전  Claude 를  활
용해  각  청크에  원본  문서의  요약  문맥 (Context) 을  덧붙이는  전처리  작업을  수행함 .
-
4. Claude Code & Computer Use 설정•
Claude Code: 터미널  기반  에이전틱  코딩  어시스턴트 . npm install -g @anthropic-
ai/claude-code 로  설치  후 , Vertex AI 연동을  위해  CLAUDE_CODE_USE_VERTEX=1 및
프로젝트  ID 환경  변수를  설정함 .
-
Computer Use: 모델에  computer, text_editor, bash 도구  스키마를  제공하여 , 화
면  스크린샷의  좌표 (x, y) 를  분석하고  마우스 / 키보드를  직접  제어하게  함 .
-
1. 워크플로우 (Workflows) vs. 에이전트 (Agents) 아키텍처  선택•
Workflows ( 권장 ): 문제  해결  단계가  명확할  때  사용함 . 예측  가능성과  신뢰성이  높으며
디버깅이  용이함 .
-
Evaluator-Optimizer: 생성 (Producer) → 평가 (Grader) → 피드백  루프 .-
```

## Page 038

![Page 038](assets/claude-code-mastery-playbook/page-038.png)

### Transcription

```text
마스터  한  줄  평: "Claude 는  단순한  텍스트  생성기를  넘어 , 도구와  컨텍스트를  결합해  복잡한  비즈
니스  로직을  자율적으로  수행하는  강력한  에이전틱  시스템 ."
Parallelization: 복잡한  단일  요청을  여러  개의  특화된  하위  작업으로  병렬  처리  후  병
합 .
-
Chaining: 제약  조건이  많은  작업을  순차적인  단계로  분리하여  모델의  집중력  유지 .-
Routing: 사용자  입력을  먼저  분류 (Categorization) 한  뒤  특화된  파이프라인으로  전달 .-
Agents: 목표와  도구만  주어지고  해결  경로는  모델이  스스로  판단함 . 유연성은  극대화되
지만 , 작업  성공률이  상대적으로  낮고  비용  통제  및  디버깅이  어려움 . 프로덕션  환경에서
는  가능한  워크플로우  패턴을  우선적으로  적용해야  함 .
-
2. 프롬프트  캐싱 (Prompt Caching) 을  통한  최적화•
비용  및  속도  개선: 시스템  프롬프트나  도구  스키마  등  반복적으로  전송되는  대규모  컨텍
스트 ( 최소  1024 토큰  이상 ) 에  cache_control: {"type": "ephemeral"} 을  적용함 .
-
주의사항: 캐시의  수명은  5 분이며 , 단  한  글자라도  변경되면  캐시가  무효화 (Invalidation)
됨 . 따라서  동적인  데이터보다는  정적인  도구  정의나  시스템  프롬프트의  마지막  배열에
중단점 (Breakpoint) 을  설정하는  것이  핵심임 .
-
3. RAG 및  검색  품질의  한계  극복  (Re-ranking)•
하이브리드  검색 (Vector + BM25) 만으로는  사용자  의도 (Intent) 를  완벽히  파악하기  어려움 .-
검색된  상위  문서들을  다시  LLM 에  통과시켜  질문과의  연관성을  기준으로  재정렬하는  리
랭킹 (Re-ranking) 단계를  추가해야  함 . 이때  전체  텍스트가  아닌  문서  ID(Document IDs) 만
반환하도록  프롬프트를  설계하여  지연  시간과  토큰  비용을  최소화해야  함 .
-
4. 에이전트  환경  검사 (Environment Inspection) 의  중요성•
Claude 는  시각적  피드백  없이  맹목적으로  작동할  수  없음 . 파일  수정  전  read 도구로  현
재  상태를  파악하거나 , Computer Use 조작  후  스크린샷을  다시  분석하는  등  ' 행동  전후의
상태  확인 (Inspection)' 단계를  시스템  프롬프트에  명시적으로  강제해야  치명적인  오류를
방지할  수  있음 .
-
```

## Page 039

![Page 039](assets/claude-code-mastery-playbook/page-039.png)

### Transcription

```text
[Course 13: Teaching AI Fluency]
Anthropic & Academic Experts 공동  개발 : 교육자를  위한  AI 유창성  교육  및  평가  프레임워크
핵심  원리  및  개념  (Core Principles & Concepts)
이  코스는  AI 를  단순한  도구가  아닌  '; 사고와  판단이  필요한  협업  파트너 ' 로  인식하도록  돕는  교육
적  기틀을  제공함 . 다음은  AI 유창성을  구성하는  핵심  프레임워크임 .
①  4D AI 유창성  프레임워크  (The 4D Framework): AI 와  협업할  때  발생하는  현상을  설명하는
기술적 (Descriptive) 지도이자 , 더  나은  결과를  위한  규범적 (Prescriptive) 가이드라인임 .
•
위임  (Delegation): 어떤  작업을  AI 에게  맡기고 , 어떤  작업을  인간이  직접  수행할지  결정하
는  전략적  선택  능력 .
-
설묘  (Description): 요구사항을  명확히  전달하고 , AI 와  공유된  맥락을  구축하는  프롬프트
작성  및  소통  기술 .
-
판별  (Discernment): AI 가  생성한  결과물의  정확성 , 유용성 , 그리고  도출  과정을  비판적으
로  평가하는  능력 .
-
성실  (Diligence): AI 활용  전  과정에서  윤리성 , 투명성 , 책임감을  유지하는  태도 .-
②  위임 - 성실  루프  (The Delegation-Diligence Loop): "AI 를  어떻게  사용하는가 ?" 에서  "AI 에
대해  어떻게  최선의  결정을  내리는가 ?" 로  전환하는  거시적 , 전략적  의사결정  과정임 .
•
양방향  상호작용: 위임  결정은  즉각적인  윤리적  질문 ( 성실 ) 을  낳고 , 반대로  윤리적  제약
( 성실 ) 은  작업  위임  방식을  재구성함 .
-
구성  요소: 문제 / 플랫폼  인식  및  과업  위임 (Delegation) ↔ 생성 / 투명성 / 배포에  대한  책임
(Diligence).
-
효과: 윤리적  경계가  제약이  아닌 , 더  창의적이고  강력한  의사결정을  돕는  촉매제로  작용
함 .
-
③  설묘 - 판별  루프  (The Description-Discernment Loop): 단순한  ' 입출력 (Input-Output)' 을  넘
어 , AI 와  ' 함께  생각하는  인지적  환경 (Cognitive Environment)' 을  구축하는  미시적 , 전술적  과정
임 .
•
3 가지  핵심  렌즈  (The Three Ps):-
산출물  (Product): 모호한  아이디어에서  시작해  반복을  통해  결과물의  기준을  구체
화 .
-
과정  (Process): 사고와  문제  해결에  대한  공유된  접근  방식  개발 .-
수행  (Performance): 최선의  사고력을  발휘할  수  있도록  AI 와의  역할  및  역동성  조정 .-
```

## Page 040

![Page 040](assets/claude-code-mastery-playbook/page-040.png)

### Transcription

```text
실전  활용  가이드  (Practical Implementation Guide)
교육  현장에서  4D 프레임워크를  학생들에게  효과적으로  가르치고  평가하기  위한  구체적인  방법
론임 .
전략적  인사이트  및  주의사항  (Strategic Insights & Considerations)
①  4 가지  교수법  접근  방식  (Teaching Approaches): 학생의  숙련도와  수업  목표에  따라  유연
하게  선택할  수  있는  교육  전략임 .
•
단계별  접근  (Linear): 초보자  최적화 . 위임  → 설묘  → 판별  → 성실  순으로  순차적  학습 .-
자율  시작  접근  (Non-linear): 경험자용 . AI 작업이  유기적  시스템임을  이해하고 , 특정  시
나리오의  요구에  맞춰  필요한  역량부터  유연하게  시작 .
-
집중  학습  접근  (Focused): 제한된  시간  내에  특정  역량 ( 예 : 판별력 ) 하나만을  심도  있게
파고들어  숙련도  극대화 .
-
이중  루프  접근  (Two Loops): 고급  방식 . 상호작용을  전략적  공간 ( 위임 - 성실 ) 과  전술적  공
간 ( 설묘 - 판별 ) 으로  나누어  시스템적으로  이해 .
-
②  3 차원  평가  전략  (Assessment Strategies): " 학생이  AI 를  썼는가 ?" 가  아닌 , " 얼마나  지능적
이고  책임감  있게  협업했는가 ?" 를  측정하는  다각적  평가  프레임워크임 .
•
결과  기반  평가  (Outcome-based): 최종  산출물의  품질  평가 . ( 예 : AI 출력물을  얼마나  탁
월하게  개선했는가 ? 여러  AI 플랫폼의  결과를  비교  분석했는가 ?)
-
과정  기반  평가  (Process-based): 시간  흐름에  따른  협업  방식  평가 . ( 예 : 주석이  달린  채
팅  로그  제출 , 실패한  시도에서의  피벗 (Pivot) 분석 , 실시간  작업  화면  녹화  및  내레이션 ).
-
성찰  기반  평가  (Reflection-based): 메타인지  능력  평가 . ( 예 : 학습  저널  작성 , 특정  전략
이  효과적이었던  이유  설명 , 직면했던  윤리적  딜레마에  대한  개인  정책  성명서  작성 ).
-
③  AI 유창성  과제  설계  3 대  원칙  (Assignment Design Principles)•
실제성  (Authenticity): 인위적인  연습이  아닌 , AI 파트너십이  실제로  가치를  더하는  현업
의  진짜  문제를  다루어야  함 .
-
반복성  (Iteration): 단발성  프롬프트  입력을  넘어 , 결과물을  수정하고  재고하며  다시  시도
할  수  있는  기회를  반드시  포함해야  함 .
-
교육적  투명성  (Pedagogy Transparency): 최종  결과물뿐만  아니라  ' 협업  과정의  품질 ' 과
' 성찰 ' 자체가  주요  평가  대상임을  학생들에게  명확히  공지해야  함 .
-
①  전문  지식의  증폭  (Amplification of Expertise): AI 시대에  학문적  전문  지식은  무용지물이
되는  것이  아니라 , 전례  없는  성취를  위한  견고한  토대가  됨 . AI 유창성은  기존  지식을  대체하
는  것이  아니라  신중한  파트너십을  통해  인간의  통찰력과  판단력을  증폭 (Amplify) 시킴 .
•
암묵적  지식의  명시화: 해당  분야에서  ' 품질 ' 이  무엇인지 , 전문가들이  어떻게  소통하는지
명확히  정의 (Rubrics 구축 ) 할  수  없다면  AI 와  파트너가  될  수  없음 .
-
교육자의  3 대  전문성  활용: 학문적  전문성 ( 핵심  가치  식별 ), 교수법적  전문성 ( 학습  여정  지
원 ), 평가  전문성 ( 진정한  이해  식별 ) 이  AI 통합의  핵심  동력임 .
-
②  교육의  3 대  요소  재정의  (Curriculum, Pedagogy, Assessment)•
```

## Page 041

![Page 041](assets/claude-code-mastery-playbook/page-041.png)

### Transcription

```text
마스터  한  줄  평: "AI 유창성  교육의  궁극적  목표는  학생을  AI 로  대체하는  것이  아니라 , 비판적  사고
와  명확한  소통 , 윤리적  책임을  바탕으로  AI 와  지능적으로  협업하는  ' 대체  불가능한 (Irreplaceable)'
인재로  길러내는  것임 ."
커리큘럼: AI 가  일상적  과업을  자동화할  때 , 어떤  기초  개념이  더  중요해지는지  식별해야
함 .
-
교수법: AI 를  개인  맞춤형  튜터나  시뮬레이션  도구로  활용하되 , ' 학습을  돕는  시스템 ' 과  ' 단
순한  지름길 ' 을  구별하는  혜안이  필요함 .
-
평가: AI 가  결과물을  대신  생성할  수  있는  환경에서는 , 최종  산출물 (Product) 중심에서  과
정 (Process) 과  성장 (Growth) 중심의  평가  모델로의  전환이  시급함 .
-
③  안티  패턴  및  주의사항  (Anti-patterns)•
단일  프롬프트  의존  (Single Prompting): 한  번의  명령으로  완벽한  결과를  기대하는  것은
실패의  지름길임 . AI 와의  협업은  지속적인  대화를  통해  공유된  언어와  맥락을  형성하는
' 탐색적  사고 ' 과정이어야  함 .
-
결과물  중심의  맹목적  평가: 과정에  대한  검증  없이  최종  결과물만  평가하면 , 학생의  실제
역량  성장 (AI 유창성 ) 을  측정할  수  없으며  학문적  무결성을  훼손할  위험이  큼 .
-
평가  업무의  과부하: 과정과  성찰을  모두  평가하면  교사의  업무가  급증할  수  있음 . 세부  루
브릭  활용 , 동료  평가 (Peer Review) 적극  도입 , 선택적  샘플링  검토  등의  효율화  전략이  필
수적임 .
-
```

## Page 042

![Page 042](assets/claude-code-mastery-playbook/page-042.png)

### Transcription

```text
[Course 14: AI Fluency for nonprofits]
핵심  원리  및  개념  (Core Principles & Concepts)
본  과정은  자원이  한정된  비영리  단체가  미션  중심의  가치를  훼손하지  않으면서  AI 를  효과적 , 윤리
적 , 안전하게  통합하기  위한  근본적인  프레임워크를  제시함 .
실전  활용  가이드  (Practical Implementation Guide)
4D 프레임워크를  비영리  단체의  핵심  실무에  즉시  적용하기  위한  단계별  가이드라인 .
AI 숙련도  (AI Fluency): 단순히  도구를  조작하는  기술적  능력을  넘어섬 . 변화하는  기술  환경에
적응하면서도  조직의  고유한  미션과  가치를  유지하며  AI 시스템을  다루는  통합적  통찰력임 .
•
4D 프레임워크  (The 4D Framework): AI 와의  책임감  있는  협업을  가능하게  하는  4 가지  핵심
역량 .
•
위임  (Delegation): 인간과  AI 의  강점을  고려하여  어떤  업무를  AI 에게  맡길지  전략적으로
선택하는  능력 .
-
설명  (Description): AI 가  의도대로  작업을  수행할  수  있도록  맥락 , 형식 , 페르소나를  명확
하게  지시하는  능력 .
-
식별  (Discernment): AI 의  산출물을  비판적으로  검토하고 , 논리적  공백이나  오류를  판단
하는  능력 .
-
성실  (Diligence): 결과의  정확성을  검증하고 , 윤리적  사용  및  투명성에  대한  최종  책임을
지는  능력 .
-
위임 - 성실  루프  (Delegation-Diligence Loop): 거시적  의사결정  모델 . 문제와  플랫폼을  인식하
여  AI 사용  여부를  결정 ( 위임 ) 하고 , 생성 · 투명성 · 배포  과정에서  인간이  최종  책임을  지는 ( 성실 )
상위  수준의  순환  과정임 .
•
설명 - 식별  루프  (Description-Discernment Loop): 미시적  실무  모델 . AI 와  상호작용하며  결과
물 (Product), 과정 (Process), 성과 (Performance) 에  대해  구체적으로  지시 ( 설명 ) 하고 , 이를  비판
적으로  평가 ( 식별 ) 하여  결과물을  반복적으로  다듬는  실무  루프임 .
•
인간  중심의  루프  (Human in the Loop): AI 는  효율성을  극대화하는  보조  수단일  뿐임 . 비영리
활동의  본질인  ' 관계  구축 ', ' 진정성 ', ' 최종  의사결정 ' 의  키는  반드시  인간이  쥐고  있어야  한다는
핵심  철학임 .
•
1. 리서치  및  정보  수집  (Researching with AI)•
맥락  중심의  프롬프트  설계  (Description): 단순  검색어가  아닌 , 조직의  정체성과  목적을
명시할  것 .
-
```

## Page 043

![Page 043](assets/claude-code-mastery-playbook/page-043.png)

### Transcription

```text
전략적  인사이트  및  주의사항  (Strategic Insights & Considerations)
[ 프롬프트  공식 ] 역할  정의  + 구체적  주제 / 범위  + 비교  대상  + 톤앤매너 . 예시 : " 저는  포틀
랜드의  비영리  주거  단체  디렉터입니다 . 시애틀로  사업을  확장하려  합니다 . 최근  2 년  내
시애틀의  세입자  보호법  변경  사항을  포틀랜드와  비교하여 , 실무에  바로  적용  가능한  보
고서  형식으로  요약해  주세요 ."
-
비판적  검증  체크리스트  (Discernment):-
프로그램  명칭 , 보조금  수치 , 마감일이  정확한가 ? (Product)-
AI 가  최신  정보를  검색했는가 , 아니면  과거  데이터로  추측했는가 ? (Process)-
" 정부  공식  웹사이트  링크를  통해  이  수치들을  재검증해줘 " 와  같이  후속  질문으로  교
차  검증할  것 .
-
2. 진정성을  담은  글쓰기  (Writing with AI)•
조직의  목소리 (Voice) 학습시키기: 과거에  성공적으로  작성된  보조금  제안서나  미션  선언
문을  업로드하여  조직  특유의  문체와  강점을  AI 에게  기준점으로  제시할  것 .
-
인간  고유의  지식  주입: AI 는  외부  데이터만  앎 . 실제  지역사회  파트너십 , 현장  실적 , 주민
들과의  세부적인  관계망  등  ' 인간만이  아는  정보 ' 를  프롬프트에  직접  추가해야  본질
(Substance) 이  담김 .
-
구체적인  정교화  (Refine): " 더  매력적으로  써줘 " 라는  모호한  지시를  피할  것 . " 우리  단체
의  자원봉사자  네트워크  규모에  대한  구체적인  데이터를  두  번째  문단에  추가해줘 " 와  같
이  명확하게  수정 (Discernment) 을  요구할  것 .
-
3. 안전한  데이터  분석  (Data Analysis & Privacy)•
철저한  데이터  위생  (Data Hygiene): AI 에  데이터를  업로드하기  전 , 이름 , 연락처  등  개인
식별정보 (PII) 를  완벽히  제거 ( 익명화 ) 할  것 . 대부분의  분석은  우편번호나  통계적  수치만으
로도  충분함 .
-
플랫폼  보안  인식  (Platform Awareness): 무료  AI 도구는  입력  데이터를  모델  학습에  사
용할  확률이  높음 . 민감한  데이터는  학습에  사용하지  않고  즉시  삭제하는  ' 제로  데이터  보
존 (ZDR)' 정책이  적용된  기업용  플랜을  활용할  것 .
-
검증된  데이터로  신뢰도  테스트: 새로운  분석을  맡기기  전 , 이미  정답을  알고  있는  과거  데
이터를  AI 에게  분석하게  할  것 . AI 가  동일한  결과를  도출하는지  확인 (Diligence) 한  후  새로
운  업무를  위임해야  함 .
-
4. 워크플로우  증강  (Workflow Augmentation)•
전략적  업무  분류  (Delegation): 모든  것을  자동화하지  말  것 .-
AI 위임 : 영수증  요청 , 행사  세부  정보  안내  등  정형화되고  문서화된  반복  작업 .-
인간  유지 : 고액  기부자  상담 , 감정적  공감이  필요한  불만  사항 , 복잡한  가치  판단 .-
시스템  행동  정의  (Performance Description): AI 가  처리할  업무의  톤앤매너와  한계를  명
확히  설정할  것 . ( 예 : " 전문적이되  따뜻한  톤을  유지하고 , 알레르기  관련  문의는  반드시  담
당자에게  에스컬레이션  할  것 .")
-
```

## Page 044

![Page 044](assets/claude-code-mastery-playbook/page-044.png)

### Transcription

```text
AI 도입  시  비영리  단체  리더와  실무자가  반드시  경계하고  숙지해야  할  전략적  관점 .
마스터  한  줄  평: "AI 는  비영리의  미션을  대체하는  것이  아니라 , 인간이  더  ' 인간적인  가치 ' 에  집중
할  수  있도록  돕는  전략적  증강  도구 ."
미션  중심의  평가  (Mission-Driven Evaluation): "AI 가  이  일을  할  수  있는가 ?" 라는  기술적  질
문에  매몰되지  말  것 . "AI 가  이  일을  해야만  하는가 ?", " 이  효율성이  우리의  미션과  커뮤니티에
어떻게  기여하는가 ?" 를  끊임없이  자문해야  함 .
•
효율성의  역설  경계: AI 를  통해  절약된  시간은  조직의  인건비  감축이  아닌 , ' 인간적인  연결
(Human Touch)' 에  재투자되어야  함 . 자동화로  확보한  시간은  기부자를  위한  손편지  작성이나
지역사회  주민과의  직접적인  대화  등  고관여  업무로  전환되어야  함 .
•
책임의  외주화  불가  (Anti-pattern): AI 는  훌륭한  초안  작성자이자  리서치  파트너지만 , 최종  결
과물에  대한  책임은  질  수  없음 . AI 가  작성한  보조금  신청서나  데이터  분석  결과에  대해  " 우리
가  AI 가  무엇을  했는지  완벽히  설명할  수  있는가 ?" 라고  자문할  것 . 설명할  수  없다면  배포해서
는  안  됨 .
•
조직적  AI 정책 (AI Policy) 수립의  필수성: 실무자  개인의  산발적인  AI 사용은  리스크를  동반
함 . 허용되는  플랫폼 , 데이터  취급  가이드라인 , AI 산출물에  대한  감독  주체 , 그리고  이해관계
자 ( 기부자  등 ) 에  대한  투명성  고지  방법 (Transparency Diligence) 을  명문화한  전사적  정책을  수
립해야  함 .
•
```

## Page 045

![Page 045](assets/claude-code-mastery-playbook/page-045.png)

### Transcription

```text
[Course 15: Introduction to agent skills]
핵심  원리  및  개념  (Core Principles & Concepts)
Claude Code 의  'Skills'; 는  반복적인  지시를  제거하고 , 특정  작업에  대한  전문  지식을  Claude 에게
단  한  번만  학습시켜  자동화하는  핵심  기능임 . 다음은  이  기능이  작동하는  근본적인  배경과  필수
개념임 .
실전  활용  가이드  (Practical Implementation Guide)
실무  환경에서  즉시  적용  가능한  스킬  생성  워크플로우와  고급  구성  방법임 .
온디맨드  지식  주입  (On-demand Knowledge via Semantic Matching)•
스킬은  특정  작업을  수행하는  방법을  정의한  Markdown 파일 (SKILL.md) 임 .-
모든  대화에  강제로  로드되는  설정과  달리 , 사용자의  요청 (Request) 과  스킬의
description 이  시맨틱  매칭 ( 의미적  일치 ) 될  때만  활성화됨 .
-
이를  통해  불필요한  정보  로드를  방지하고  컨텍스트  창 (Context Window) 을  극도로  효율
적으로  관리함 .
-
스코프와  배포  범위  (Scope & Distribution)•
Personal ( 개인용 ): ~/.claude/skills 에  저장되며 , 사용자의  모든  프로젝트에  걸쳐
공통으로  적용되는  선호도 ( 예 : 커밋  메시지  스타일 ) 를  관리함 .
-
Project ( 프로젝트용 ): 리포지토리  루트의  ./.claude/skills 에  저장됨 . Git 을  통해  버
전  관리되며 , 리포지토리를  클론하는  모든  팀원에게  팀  표준 ( 예 : 브랜드  가이드라인 , 코드
리뷰  기준 ) 을  자동으로  공유함 .
-
점진적  공개  원칙  (Progressive Disclosure)•
컨텍스트  최적화를  위해  메인  SKILL.md 파일은  500 라인  이하로  유지하는  것이  권장됨 .-
상세한  아키텍처  가이드나  실행  스크립트는  /references, /scripts, /assets 등
의  하위  디렉토리로  분리하고 , 필요할  때만  Claude 가  읽도록  링크를  연결하는  멀티  파일
구조를  취함 .
-
우선순위  계층  (Priority Hierarchy)•
동일한  이름의  스킬이  존재하여  충돌 (Conflict) 이  발생할  경우 , 시스템은  엄격한  우선순위
에  따라  하나의  스킬만  적용함 .
-
우선순위  순서: Enterprise ( 관리자  강제  설정 , 최우선 ) > Personal ( 개인 ) > Project ( 프로젝
트 ) > Plugins ( 플러그인 , 최하위 )
-
1. 스킬  생성  및  테스트  워크플로우•
```

## Page 046

![Page 046](assets/claude-code-mastery-playbook/page-046.png)

### Transcription

```text
전략적  인사이트  및  주의사항  (Strategic Insights & Considerations)
디렉토리  생성: 스킬  이름과  동일한  폴더를  생성함 . ( 예 : mkdir -p
~/.claude/skills/pr-description)
-
SKILL.md 작성: 폴더  내에  SKILL.md 파일을  생성하고  Frontmatter( 메타데이터 ) 와
Instructions( 지시사항 ) 를  작성함 .
-
세션  재시작: 스킬은  Claude Code 시작  시  로드되므로  반드시  세션을  재시작함 .-
검증: What skills are available? 명령어로  로드  여부를  확인함 .-
2. 고급  Frontmatter 구성  ( 프롬프트  예시 )
---
name: codebase-onboarding
description: 새로운  개발자가  시스템  작동  방식을  이해하도록  돕습니다 .
                         " 아키텍처  설명해줘 ", " 이  모듈  어떻게  동작해 ?" 라고  물을  때  사용하세요
allowed-tools: Read, Grep, Glob, Bash
model: sonnet
---
# Instructions
1. 시스템  아키텍처에  대한  질문을  받으면  `references/architecture-guide.md` 를  먼저  읽으세요 .
2. 코드를  수정하지  말고  설명만  제공하세요 .
•
description: " 무엇을  하는지 ", " 언제  사용하는지 " 를  명확히  기술하고 , 실제  사용자가
입력할  법한  트리거  문구를  포함해야  매칭  확률이  높아짐 .
-
allowed-tools: 보안에  민감한  작업  시  Claude 의  권한을  제한함 . 위  예시처럼  설정하
면  파일  수정이나  쓰기  권한이  차단되어  안전한  읽기  전용 (Read-only) 스킬이  됨 .
-
3. Claude Code 기능별  최적  활용  체크리스트: 모든  것을  스킬로  만들지  마십시오 . 목적에  맞
는  도구를  선택해야  함 .
•
Skills: 특정  작업에만  필요한  전문  지식  ( 예 : PR 리뷰  체크리스트 , 특정  프레임워크  디버
깅 ). 요청  시에만  로드됨 .
-
CLAUDE.md: 모든  대화에  항상  적용되어야  하는  프로젝트  전반의  표준  및  제약  조건  ( 예 :
" 데이터베이스  스키마  절대  수정  금지 ", " 항상  TypeScript 엄격  모드  사용 ").
-
Hooks: 파일  저장 , 도구  호출  전  유효성  검사  등  특정  이벤트  발생  시  자동으로  실행되는
작업 .
-
Subagents: 메인  대화와  격리된  독립적인  컨텍스트에서  작업을  위임할  때  사용 .-
4. 서브에이전트 (Subagents) 와의  스킬  연동•
주의사항: 서브에이전트는  메인  대화의  스킬을  자동으로  상속받지  않음 .-
해결책: .claude/agents/ 에  위치한  커스텀  에이전트  파일의  Frontmatter 에  사용할  스
킬을  명시적으로  선언해야  함 . (skills: accessibility-audit, performance-
check)
-
```

## Page 047

![Page 047](assets/claude-code-mastery-playbook/page-047.png)

### Transcription

```text
마스터  한  줄  평: "Claude 에게  같은  지시를  반복하고  있다면 , 그것이  바로  스킬로  만들어  조직의  자
산으로  동기화해야  할  완벽한  타이밍 ."
1. 실질적  가치와  배포  전략: 스킬의  진정한  가치는  ' 개인의  편의 ' 를  넘어  ' 조직의  표준화 ' 에  있
음 . 팀의  인프라  코드 (IaC) 작성  표준 , 보안  정책 , 브랜드  가이드라인을  스킬로  자산화할  것 .
•
Git 공유: 프로젝트  종속적인  워크플로우는  리포지토리에  커밋하여  팀원과  즉시  동기화
함 .
-
Enterprise 배포: 강제적인  보안  요구사항이나  컴플라이언스는  관리자가  managed-
settings.json 을  통해  전사적으로  배포하여  개인  설정을  덮어쓰고  표준을  강제할  수
있음 .
-
스크립트  번들링: 환경  검증이나  데이터  변환  등은  생성형  코드에  의존하기보다 , 테스트
된  유틸리티  스크립트를  스킬  내에  포함시켜  실행  결과값만  토큰으로  소비하게  하는  것이
신뢰성과  비용  측면에서  압도적으로  유리함 .
-
2. 안티  패턴  (Anti-patterns) 및  트러블슈팅  가이드: 스킬이  의도대로  작동하지  않을  때  확인해
야  할  핵심  진단  요소임 .
•
트리거  실패  ( 존재하지만  실행  안  됨 ):-
원인 : 사용자의  요청과  description 의  시맨틱  매칭  실패 .-
해결 : 설명란에  사용자가  실제로  말할  법한  다양한  변형  키워드 (Trigger phrases) 를
추가할  것 .
-
로드  실패  ( 목록에  나타나지  않음 ):-
원인 : 구조적  오류 .-
해결 : 파일명이  반드시  대문자  SKILL.md 인지 , 개별  폴더  안에  위치하는지  확인할
것 . skills-ref validate [ 경로 ] 명령어로  문법을  검증하고 , claude --
debug 모드로  로딩  에러를  추적할  것 .
-
충돌  및  섀도잉  ( 엉뚱한  스킬이  실행됨 ):-
원인 : 스킬  이름이  너무  일반적이거나 ( 예 : review), 상위  우선순위 (Enterprise) 에  동
일한  이름이  존재함 .
-
해결 : frontend-pr-review 와  같이  구체적이고  차별화된  이름으로  변경할  것 .-
런타임  오류  ( 실행  중  중단 ):-
해결 : 스크립트  파일의  실행  권한 (chmod +x) 을  확인하고 , Windows 환경이더라도
모든  경로  구분자는  슬래시 (/) 를  사용할  것 . 외부  패키지  의존성이  있다면
description 에  명시해야  함 .
-
```

## Page 048

![Page 048](assets/claude-code-mastery-playbook/page-048.png)

### Transcription

```text
[Course 16: Introduction to subagents]
본  플레이북은  Claude Code 의  서브에이전트 (Subagents) 기능을  활용하여  복잡한  작업을  분할하
고 , 컨텍스트  윈도우를  효율적으로  관리하는  전략적  가이드라인을  제공함 .
핵심  원리  및  개념  (Core Principles & Concepts)
서브에이전트는  클로드  코드가  특정  작업을  위임할  수  있는  전문화된  보조  에이전트임 . 복잡한  문
제를  한  번에  해결하기보다 , 작고  집중된  단위로  나누어  처리하는  핵심  메커니즘을  가짐 .
실전  활용  가이드  (Practical Implementation Guide)
서브에이전트가  방황하지  않고  정확한  결과를  도출하도록  만드는  생성  및  설정  최적화  가이드임 .
독립적인  컨텍스트  격리  (Isolated Context): 각  서브에이전트는  메인  대화와  완전히  분리된
자신만의  '; 대화  컨텍스트  창 ' 에서  실행됨 . 수십  개의  파일  읽기 , 검색 , 도구  호출  등  중간  작업
과정이  메인  스레드를  오염시키지  않음 .
•
토큰  효율성  및  집중도  향상: 작업이  완료되면  서브에이전트는  세부  기록을  폐기하고  오직  요
약된  결과물만  메인  스레드에  반환함 . 이를  통해  메인  컨텍스트  윈도우의  공간을  보존하고 , 클
로드가  이전  대화의  맥락을  잃는  것을  방지함 .
•
맞춤형  지침  기반의  자율성: 사용자가  정의한  시스템  프롬프트 (System Prompt) 를  통해  특정
역할 ( 예 : 코드  리뷰어 , 문서  생성기 ) 을  부여받으며 , 할당된  도구를  사용하여  자율적으로  작업
을  수행함 .
•
기본  제공  서브에이전트  (Built-in Subagents): 클로드  코드는  즉시  사용  가능한  세  가지  기본
에이전트를  제공함 .
•
General-purpose (Sonnet): 탐색과  실행이  모두  필요한  다목적  작업용-
Explore (Haiku): 코드베이스의  빠른  검색  및  구조  파악용-
Plan (Haiku/Sonnet): 코드  수정  전  연구  및  분석을  통한  계획  수립용-
1. 서브에이전트  생성  워크플로우•
명령어  호출: 대화창에  /agents 를  입력하여  관리  인터페이스를  염 .-
범위  설정: 현재  프로젝트  전용 (Project-level) 또는  모든  프로젝트  공유용 (User-level) 중  선
택함 .
-
자동  생성  권장: 수동  작성보다  클로드에게  원하는  역할을  설명하여 ( 예 : " 코드  품질과  보
안을  검토하는  에이전트 ") 이름 , 설명 , 프롬프트를  자동  생성하게  하는  것이  효율적임 .
-
2. 설정  파일 (YAML) 최적화  전략: 생성된  에이전트는  .md 파일로  저장되며 , 상단의  YAML 데
이터는  메인  에이전트가  ' 언제 , 어떻게  위임할지 ' 를  결정하는  핵심  지표임 .
•
```

## Page 049

![Page 049](assets/claude-code-mastery-playbook/page-049.png)

### Transcription

```text
전략적  인사이트  및  주의사항  (Strategic Insights & Considerations)
서브에이전트의  도입  여부를  결정하는  핵심은  "; 중간  작업  과정이  메인  대화창에  노출될  필요가
있는가 ?" 임 . 결과만  필요하다면  위임하고 , 과정에  대한  피드백이  필요하다면  메인  스레드를  유지
해야  함 .
Description ( 설명 ): 메인  에이전트가  서브에이전트를  호출하는  기준이  되며 , 입력  프롬프
트의  방향을  결정함 .
-
Proactively: 설명에  "proactively( 적극적으로 )" 를  포함하면  클로드가  적절한  상황에
스스로  작업을  위임함 .
-
구체성: " 검토할  파일을  정확히  지정하라 " 와  같은  구체적인  지시를  설명에  포함하면 ,
메인  에이전트가  훨씬  명확한  입력  프롬프트를  작성하여  전달함 .
-
Model ( 모델  선택 ): 작업  성격에  맞춰  지능  수준을  결정함 . ( 빠른  작업 : Haiku, 균형 :
Sonnet, 복잡한  분석 : Opus)
-
3. 시스템  프롬프트  설계의  3 대  원칙: 시스템  프롬프트 ( 마크다운  본문 ) 의  품질이  서브에이전트
의  성능을  좌우함 .
•
구조화된  출력  형식 (Output Format) 정의  ( 가장  중요 ): 결과물의  목차를  강제하여  서브에
이전트에게  ' 명확한  정지  지점 ' 을  제공함 . 이를  통해  무한  루프나  과도한  리소스  낭비를  방
지함 .
1. Summary ( 요약  및  전반적  평가 )
2. Critical Issues ( 즉시  수정해야  할  심각한  문제 )
3. Major/Minor Issues ( 품질 , 스타일  등  주요 / 경미한  문제 )
4. Recommendations ( 개선  권장  사항 )
5. Approval Status ( 승인  상태 )
-
장애물  보고 (Report Obstacles) 요구: 작업  중  발견한  해결책 ( 의존성  문제  해결법 , 특수
플래그  등 ) 을  출력  형식에  포함하도록  지시함 . 메인  스레드가  동일한  문제를  다시  분석하
는  시간과  토큰을  절약함 .
-
도구  권한  최소화  (Principle of Least Privilege): 작업에  꼭  필요한  도구만  부여하여  부수
효과 (Side effects) 를  방지함 .
-
조사 / 탐색 : Read, Glob, Grep ( 읽기  전용 )-
코드  리뷰 : Bash 추가  (git diff 확인용 , 수정  권한  없음 )-
코드  수정 : Edit, Write 권한  부여-
1. 서브에이전트가  빛을  발하는  순간  ( 권장  패턴 )•
조사  및  탐색  (Research & Investigation): 생소한  코드베이스에서  특정  로직 ( 예 : 인증  방
식 ) 을  찾을  때 . 수십  개의  파일을  뒤지는  과정은  숨기고  " 인증은  X 파일의  Y 라인에  있습니
다 " 라는  깔끔한  결과만  획득할  수  있음 .
-
전문적인  코드  리뷰  (Code Review): 메인  에이전트는  자신이  작성한  코드에  대해  객관성
을  잃기  쉬움 . 서브에이전트는  작성  이력이  없는  ' 신선한  시각 (Fresh eyes)' 으로  코드를  검
토하며 , 팀의  특정  리뷰  표준을  일관되게  적용할  수  있음 .
-
```

## Page 050

![Page 050](assets/claude-code-mastery-playbook/page-050.png)

### Transcription

```text
마스터  한  줄  평: " 효과적인  서브에이전트  활용의  본질은  '; 맥락의  격리 ' 에  있으며 , 중간  과정의  노
이즈를  제거하고  최종  결과에만  집중할  때  클로드의  토큰  효율성과  작업  정확도가  극대화됨 ."
특정  지침이  필요한  작업  (Custom Instructions): 마케팅  카피라이팅 ( 특정  톤앤매너  요
구 ) 이나  디자인  시스템  준수 ( 사전  정의된  CSS 변수  활용 ) 등 , 기본  코딩  프롬프트와는  다
른  특수한  규칙이  필요할  때  매우  효과적임 .
-
2. 생산성을  저해하는  안티  패턴  ( 지양해야  할  패턴 )•
전문가라고  주장만  하는  에이전트  (Expert Claims): 시스템  프롬프트에  단순히  " 너는  파
이썬  전문가야 " 라고  적는  것은  무의미함 . 클로드  모델은  이미  해당  지식을  보유하고  있으
며 , 구체적인  도구  사용법이나  특수  지침이  없다면  메인  에이전트와  차별점이  없음 .
-
다단계  파이프라인  (Sequential Pipelines): ' 버그  재현  → 디버깅  → 수정 ' 과  같이  각  단계
가  이전  단계의  발견에  의존하는  작업을  여러  에이전트에게  순차적으로  위임하는  것은  위
험함 . 에이전트  간  핸드오프  과정에서  중요한  맥락 (Context) 이  유실될  가능성이  높음 .
-
테스트  실행기  (Test Runners): 테스트  결과를  단순히  " 성공 / 실패 " 로만  요약하여  반환하
는  에이전트는  디버깅을  방해함 . 문제  해결을  위해서는  전체  로그와  실행  맥락이  필요하
므로 , 테스트는  메인  스레드에서  직접  실행하여  전체  출력을  확인하는  것이  바람직함 .
-
```

## Page 051

![Page 051](assets/claude-code-mastery-playbook/page-051.png)

### Transcription

```text
[Course 17: AI Capabilities and Limitations]
본  플레이북은  생성형  AI 시스템이  어떻게  작동하고  왜  그렇게  행동하는지에  대한  ' 작동  멘탈  모델
(Working Mental Model)' 을  제공함 . 인간의  역량 (4D 프레임워크 ) 이  대응해야  할  기계의  본질적  속
성을  다룸 .
핵심  원리  및  개념  (Core Principles & Concepts)
생성형  AI 는  균일하게  뛰어나거나  무능하지  않으며 , 예측  가능한  4 가지  핵심  속성의  스펙트럼 ( 능
력 ~ 한계 ) 위에서  작동함 . 이  기계적  속성을  이해하는  것이  ' 조정된  신뢰 (Calibrated Trust)' 의  출발점
임 .
실전  활용  가이드  (Practical Implementation Guide)
AI 의  성격을  결정하는  2 단계  학습  (Pretraining & Fine-tuning)•
사전  학습 (Pretraining): 방대한  텍스트를  읽고  ' 다음  토큰을  예측 ' 하는  문서  완성기
(Document completer) 를  만듦 . 이  단계의  AI 는  사용자를  돕는다는  개념이  없음 .
-
미세  조정 (Fine-tuning): 인간의  선호도를  반영하여  문서  완성기를  ' 어시스턴트 ' 로  변모시
킴 . 이  과정에서  인간의  판단이  개입되어  아부 (Sycophancy), 장황함 (Verbosity), 과도한  주
의 (Over-caution) 라는  특유의  ' 지문 (Fingerprints)' 을  남김 .
-
다음  토큰  예측  (Next Token Prediction): 유창함과  환각의  양면성•
AI 는  정보를  검색하는  것이  아니라 , 통계적으로  다음에  올  조각을  예측하여  작성함 .-
익숙한  패턴 ( 요약 , 설명 ) 에서는  강력한  능력을  발휘하지만 , 이름 , 날짜 , 인용구 , 통계  등
' 구체성 (Specificity)' 이  요구되는  영역에서는  환각 (Hallucination) 과  작화 (Confabulation) 가
집중됨 . 유창한  어조가  정확성을  담보하지  않음 .
-
지식  (Knowledge): 방대하지만  멈춰있는  정보•
AI 의  지식은  오직  학습  데이터에  의존하며 , 특정  시점 (Knowledge cutoff) 에서  멈춰  있음 .-
주류  토픽에는  깊은  역량을  보이나 , 희귀하거나  최신  정보 , 지역적  주제에  대해서는  정보
의  진부화 (Staleness) 와  출처  망각 (Source amnesia) 이  발생함 .
-
작업  기억  (Working Memory): 컨텍스트  윈도우의  절벽•
AI 가  현재  주의를  기울이는  공간은  고정된  크기의  ' 컨텍스트  윈도우 ' 임 .-
다른  속성들이  점진적으로  저하되는  것과  달리 , 기억은  한계를  초과하면  경고  없이  정보
가  잘려나가는  ' 절벽 (Cliff)' 형태를  띰 . 특히  긴  문서의  중간에  있는  정보가  무시되는  'Lost
in the middle' 현상이  발생함 .
-
조종성  (Steerability): 단어와  의도  사이의  간극•
```

## Page 052

![Page 052](assets/claude-code-mastery-playbook/page-052.png)

### Transcription

```text
기계의  4 가지  속성을  실무 (4D: Delegation, Description, Discernment, Diligence) 에  적용하여  출력
의  품질을  통제하고  오류를  방지하는  구체적인  방법론임 .
전략적  인사이트  및  주의사항  (Strategic Insights & Considerations)
실무에서  발생하는  대부분의  AI 실패는  단일  속성의  오류가  아님 . 진정한  전문가 (Master) 는  ' 무엇
이  고장  났는가 ?' 가  아니라  ' 어떤  두  속성이  충돌했는가 ?' 를  진단함 .
A. 컨텍스트  최적화  워크플로우  (Working Memory 대응 )•
원칙: 더  많은  컨텍스트가  더  나은  결과를  의미하지  않음 . AI 의  주의력은  유한하므로  무자
비하게  선별 (Curate ruthlessly) 해야  함 .
-
프롬프트  구조화  ( 안전한  패턴  적용 ): 가장  중요한  지시사항이나  제약  조건은  프롬프트의
최상단 ( 시작 ) 과  최하단 ( 끝 ) 에  중복  배치할  것 . 중간에  묻힌  정보는  무시될  확률이  높음 .
-
청크 (Chunk) 분할: 50 페이지  이상의  긴  문서를  검토할  때는  한  번에  업로드하지  말고 , 논
리적  단위로  나누어  여러  번에  걸쳐  작업할  것 .
-
컨텍스트  리셋: 긴  대화  중  출력  품질이  저하된다면 ( 컨텍스트  한계  도달 ), 현재까지의  상
황을  짧게  요약한  뒤  완전히  새로운  세션 (New Chat) 에서  시작할  것 .
-
B. 환각  통제  및  검증  체크리스트  (Next Token Prediction & Knowledge 대응 )•
구체성  검증  타겟팅: AI 가  생성한  결과물  중  이름 , 날짜 , 통계 , 인용구 , URL 이  포함되어  있
다면  이를  1 순위  검증  대상으로  삼을  것 . 정밀한  주장일수록  조작 (Fabrication) 이  숨어있을
확률이  높음 .
-
지식의  외부  수혈: 최신  정보나  사내  규정  등  AI 가  모르는 (Cutoff 이후  또는  비공개 ) 정보가
필요할  때는  AI 의  지식에  의존하지  말  것 . 웹  검색  기능 , RAG( 검색  증강  생성 ), 또는  관련
문서를  직접  프롬프트에  제공 (Context-as-leverage) 하여  지식의  공백을  메울  것 .
-
불확실성  신호  유도: 프롬프트에  " 확실하지  않은  정보라면  추측하지  말고  모른다고  답하
거나 , 정보가  부족하다고  명시해라 " 라는  제약을  추가하여  작화를  방지할  것 .
-
C. 정밀한  조종을  위한  프롬프팅  (Steerability 대응 )•
형식 (Format) 과  목표 (Goal) 의  동시  제시: 지시가  글자  그대로만  해석되는  것을  막으려면
궁극적인  목적을  밝혀야  함 .
-
Anti-pattern: " 이  이메일을  더  짧게  써줘 ." ( 핵심  내용이  누락될  수  있음 )-
Best Practice: " 이  이메일을  더  짧게  써줘 . 나의  목표는  임원진이  2 페이지에  있는  핵심  결
과에  끝까지  집중하게  만드는  것임 ."
-
속성의  충돌  진단법  (When Properties Collide)•
환각적  인용  (Hallucinated Citation) = [ 다음  토큰  예측 ] × [ 지식의  한계 ]: 니치한  주제를
물었을  때  존재하지  않는  논문  제목과  저자를  그럴듯하게  생성하는  현상임 . 기계는  자신
이  아는  것과  발명해낸  것을  구분하지  못함 . ( 해결책 : 독립적  검증  또는  실제  문서  기반의
소스  그라운딩 )
-
긴  대화에서의  표류  (Long-conversation Drift) = [ 작업  기억  한계 ] × [ 조종성 ]: 초기에  설
정한  엄격한  제약  조건이  스무  번의  대화가  오간  후  무시되는  현상임 . 초기  컨텍스트는  희
-
```

## Page 053

![Page 053](assets/claude-code-mastery-playbook/page-053.png)

### Transcription

```text
마스터  한  줄  평: "AI 의  유창함에  속지  말고 , 기계의  4 가지  본질적  속성 ( 예측 , 지식 , 기억 , 조종성 ) 을
이해하여  조정된  신뢰를  구축할  것 ."
미해지고 , AI 는  현재  가장  눈에  띄는  지시에만  패턴을  맞춤 . ( 해결책 : 핵심  컨텍스트  재공
급  또는  새  세션  시작 )
실무  안티  패턴  (Anti-patterns to Avoid)•
신뢰의  양극화  ( 전면적  신뢰  vs 전면적  불신 ): AI 에  대한  신뢰는  부여하거나  거두는  것이
아님 . 현재  부여된  작업이  AI 의  ' 능력  영역 ( 잘  닦인  길 )' 에  있는지  ' 한계  영역 ( 새로운  영
토 )' 에  있는지  위치를  파악하고 , 그에  맞춰  검증  수준을  조절하는  ' 조정된  신뢰 (Calibrated
trust)' 가  필요함 .
-
목소리  높이기  (Repeating with more force): AI 가  지시를  문자  그대로만  따르고  의도를
놓쳤을  때 , " 더  간결하게 !" 라고  동일한  지시를  반복하는  것은  간극을  좁히지  못함 . 지시가
아닌  ' 목표 (Goal)' 를  다시  설명해야  함 .
-
자신감의  오독: AI 의  매끄럽고  확신에  찬  산문 (Smooth prose) 은  ' 다음  토큰  예측 ' 이  성공적
으로  작동했다는  뜻일  뿐 , 내용이  ' 사실 (True)' 이라는  신호가  아님 .
-
지속  가능한  멘탈  모델•
AI 모델의  버전이  올라가고  컨텍스트  윈도우가  커지더라도 , 이  4 가지  속성의  ' 형태
(Shape)' 는  변하지  않음 . AI 는  여전히  정확성보다  유창성이  앞서는  예측기이며 , 유한한  창
안에서  작동하고 , 단어와  의도  사이의  간극을  통해  지시를  따름 . 이  멘탈  모델은  기술  변화
에도  견고하게  유지됨 .
-
```
