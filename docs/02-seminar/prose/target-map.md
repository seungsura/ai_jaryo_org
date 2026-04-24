# Harness 잘 사용하기 Target Map

## 현재 상태

- `docs/02-seminar/prose`는 이 `target-map.md`만 남긴 상태에서 새 원고를 다시 작성한다.
- 기존 prose 원고와 1:1로 대응시키지 않는다.
- 새 원고는 `docs/02-seminar/harness-rebuilt-md`의 내용을 1:n으로 재조합한다.
- `docs/02-seminar/harness-rebuilt-md/90-advisor.md`는 agent 도움으로 작성된 문서이므로 source map에서 제외한다.
- speaker notes는 이번 prose 재작성 범위에서 제외한다.

## Source Policy

- 1차 source는 사용자가 작성한 `docs/02-seminar/harness-rebuilt-md/00-*.md`부터 `09-*.md`까지다.
- `assets/`, JPG, PNG, PDF는 보지 않는다.
- `Source sections`는 원문을 그대로 복사할 위치가 아니라, 해당 장을 쓸 때 참고할 source 재료 묶음이다.
- 실제 prose는 각 챕터의 목적에 맞게 재창조한다. 다만 source에 없는 주장, 비교 축, 사례, 수치, 의도를 새로 만들지 않는다.
- 새 주제와 목차가 고정된 뒤에는 인터넷 조사를 보강 자료로 사용할 수 있다.
- 인터넷 조사 시 `https://github.com/Youngdong2/claude-seminar-references`는 `docs/01-sources/local-canonical/claude-code-seminar-kakao.md`가 사용했던 원본 주소를 찾는 reference index로 사용할 수 있다.
- 외부 자료는 주장을 새로 만들기보다, 이미 원고에 있는 주장을 보강하거나 출처를 명확히 하는 데 쓴다.
- 외부 자료를 사용한 경우 prose 본문 또는 별도 reference 문서에 출처를 남긴다.

## Language And Terminology Policy

- 새 prose는 한국어를 기본으로 쓴다.
- 제품명, API명, 프로토콜명, 명령어, 파일 경로, 라이브러리명, 방법론 이름처럼 번역하면 정밀도가 떨어지는 전문 용어는 영어 원문을 유지한다.
- 전문 용어라도 널리 쓰이는 한국어 번역 개념이 있거나, 한국어로 풀어야 문장의 힘이 살아나는 경우에는 한국어 표현을 먼저 쓰고 괄호 안에 영어 원문을 적는다.
- prose는 보고서, 강의안, 제품 문서 말투가 아니라 밀도 높은 기술 블로그 에세이 톤으로 쓴다.
- 문장은 직접적이고 단정적으로 쓴다. 과한 완곡어법, 사내 문서식 관료 문장, 안전한 요약문을 기본값으로 두지 않는다.
- 번역투와 방법론 직역체를 피한다. 특히 `상류/하류`, `강하게 호출된다`, `핵심은 ~ 데 있다`, `~의 측면에서`, `~라고 볼 수 있다`는 더 살아 있는 한국어가 있으면 교체한다.

| English original | Korean expression | Note |
| --- | --- | --- |
| `Context Rot` | 컨텍스트 부패 (`Context Rot`) | 사용자 지정 표현 |
| `Lost in the Middle` | 중간 누락 (`Lost in the Middle`) | 필요하면 첫 등장에 `Lost-in-the-Middle 효과` 병기 |
| `Calibrated Trust` | 보정된 신뢰 (`Calibrated Trust`) | 외부 한국어 자료에서 사용 확인 |
| `Keep Quality Left` | 품질을 앞단으로 당기기 (`Keep Quality Left`) | `시프트 레프트(Shift Left)` 계열 원리로 설명 |

## 새 전체 구조

| 장 | Target file | 제목 | 중심 질문 |
| --- | --- | --- | --- |
| 00 | `docs/02-seminar/prose/00-coding-disappear.md` | 코딩은 사라지는가 | 개발자는 무엇을 계속 위임해 왔고, 무엇을 새로 붙들어야 하는가 |
| 01 | `docs/02-seminar/prose/01-stop-fighting-chatbots.md` | 챗봇과 싸우지 않기 | 왜 더 좋은 프롬프트만으로는 충분하지 않은가 |
| 02 | `docs/02-seminar/prose/02-harness-is-environment.md` | Harness는 환경이다 | 모델 바깥에서 무엇을 통제해야 하는가 |
| 03 | `docs/02-seminar/prose/03-why-agents-get-lost.md` | 에이전트는 왜 길을 잃는가 | 긴 루프와 긴 컨텍스트는 어떻게 실패를 키우는가 |
| 04 | `docs/02-seminar/prose/04-fix-direction-first.md` | 먼저 방향을 고정한다 | 빠른 생성보다 먼저 정해야 하는 것은 무엇인가 |
| 05 | `docs/02-seminar/prose/05-move-deterministic-gates-left.md` | 기계가 막을 수 있는 것은 앞에서 막는다 | 검증과 권한 경계는 어떻게 세워야 하는가 |
| 06 | `docs/02-seminar/prose/06-do-not-give-one-ai-everything.md` | 하나의 AI에게 다 맡기지 않는다 | 역할, 컨텍스트, 검증 책임을 어떻게 나누는가 |
| 07 | `docs/02-seminar/prose/07-practical-harness-as-files-and-commands.md` | 실전 Harness는 파일과 명령어로 남는다 | 원칙을 실제 작업 환경에 어떻게 고정하는가 |
| 08 | `docs/02-seminar/prose/08-this-presentation-was-harness.md` | 이 발표 자체가 Harness였다 | source에서 prose, outline, HTML, PDF까지 어떤 구조로 만들었는가 |
| 09 | `docs/02-seminar/prose/09-harness-engineer.md` | Harness Engineer | 개인과 팀은 무엇부터 바꿔야 하는가 |

## Source To Target Map

### 00. 코딩은 사라지는가

- Target file: `docs/02-seminar/prose/00-coding-disappear.md`
- Main source:
  - `docs/02-seminar/harness-rebuilt-md/01-코딩은 사라지는가.md`
  - `docs/02-seminar/harness-rebuilt-md/00-overview.md`
- Source sections:
  - 01 `시작하며: 언어의 발전`
  - 01 `추상화의 역사: 직접 하던 일은 계속 줄어들었다`
  - 01 `문서가 코드다`
  - 01 `개발자의 새로운 역할: 컨텍스트를 설계하는 능력`
  - 01 `그래도 기초가 중요하다`
  - 00 `코딩보다 환경 구성을 해야한다`
- Core claims:
  - 우리는 늘 직접 작성하는 비중을 도구와 추상화에 위임해 왔다.
  - 코딩은 사라지는 것이 아니라 추상화 수준이 올라간다.
  - 손으로 타이핑하는 비중은 줄고, 규칙을 세우고 컨텍스트를 고르고 검증하는 비중이 커진다.
  - `CLAUDE.md`, `AGENTS.md`, `Cursor Rules`, `copilot-instructions.md` 같은 문서는 에이전트가 실제로 따르는 운영 규칙이 된다.
  - AI가 더 많이 해줄수록 기본기는 더 중요해진다.
- Writing direction:
  - 기존 `01-코딩은 사라지는가.md`의 의미와 문장 흐름을 원본에 가깝게 살린다.
  - 각 소제목은 슬라이드 한 장으로 옮길 수 있을 정도의 의미 단위로 둔다.
  - 한 소제목의 내용이 많더라도 억지로 쪼개지 않는다.
  - `기계어 -> C/Pascal` 전환은 발표 도입부의 설득력을 높이는 배경으로 둔다.
  - 00장은 원본을 거의 그대로 가져오되, 사용자가 요청한 첫 전환 구조와 역사적 정확성 보정만 반영한다.
  - 숫자 사례는 source에 있으므로 유지 가능하지만, 외부 검증 전에는 과하게 강조하지 않는다.
  - 장의 결론은 `개발자의 역할은 환경 설계로 이동한다`로 닫고, 01장의 `챗봇과 싸우지 않기`로 넘긴다.
- Accuracy note:
  - `컴파일러가 만든 코드가 사람보다 효율적일 리 없다`는 반발은 C/Pascal 자체보다 앞선 FORTRAN 같은 초기 고급 언어와 컴파일러 도입 맥락에서 먼저 확인된다.
  - prose에서는 발표 흐름상 `기계어/어셈블리 -> C/Pascal`로 압축할 수 있지만, 문장 안에서는 초기 고급 언어와 컴파일러 일반에 대한 반발이었다고 정확히 적는다.
- Possible revision targets:
  - 코드 예시가 너무 길어 블로그 prose의 압력을 떨어뜨리는 경우 압축한다.
  - `코딩은 끝났다`처럼 과하게 단정적인 표현은 문맥상 오해를 만들면 조정한다.
  - 외부 수치는 나중에 보강 조사로 확인한다.

### 01. 챗봇과 싸우지 않기

- Target file: `docs/02-seminar/prose/01-stop-fighting-chatbots.md`
- Main source:
  - `docs/02-seminar/harness-rebuilt-md/00-overview.md`
  - `docs/02-seminar/harness-rebuilt-md/04-프롬프트를 넘어서: 에이전트를 움직이는 기술, Harness.md`
  - `docs/02-seminar/harness-rebuilt-md/05-이렇게 하면 망한다: 한계와 실패 패턴.md`
- Source sections:
  - 00 `시작하며`
  - 00 `코딩보다 환경 구성을 해야한다`
  - 04 `Prompt, Context, Harness`
  - 05 `오류의 나비효과`
  - 05 `긴 작업이 위험한 이유`
- Core claims:
  - AI를 잘 쓰는 문제는 더 긴 프롬프트나 말씨름의 문제가 아니다.
  - 일이 길어지는 순간 문제는 말투가 아니라 환경이 된다.
  - 좋은 결과는 한 번의 멋진 프롬프트가 아니라 반복 가능한 규칙, 선별된 컨텍스트, 권한 경계, 검증, 상태 기록이 함께 작동할 때 나온다.
  - 이 전체 구조가 `Harness`로 이어진다.
- Writing direction:
  - 첫 문단은 제품명보다 독자의 경험에서 시작한다.
  - "남들은 잘 쓰는데 나는 왜 계속 AI와 싸우는가"라는 감각을 주제의 입구로 삼는다.
  - `Harness`의 상세 구성요소는 02장으로 넘기고, 이 장은 문제 전환에 집중한다.
  - 소제목은 PPT 한 장으로 옮길 수 있는 크기로 둔다.
  - 01장의 소제목은 `AI와 말씨름하는 순간`, `챗봇은 답하고, 에이전트는 일한다`, `Harness는 말이 아니라 환경이다`를 기준으로 삼는다.
  - 프롬프트의 한계와 에이전트 루프 설명은 한 장면으로 묶고, 좋은 결과와 Harness 정의도 한 장면으로 묶는다.
  - 별도의 전환 전용 섹션은 두지 않고 마지막 문단에서 자연스럽게 다음 장으로 넘긴다.

### 02. Harness는 환경이다

- Target file: `docs/02-seminar/prose/02-harness-is-environment.md`
- Main source:
  - `docs/02-seminar/harness-rebuilt-md/04-프롬프트를 넘어서: 에이전트를 움직이는 기술, Harness.md`
  - `docs/02-seminar/harness-rebuilt-md/02-왜 Claude Code인가, 그리고 왜 Harness 인가.md`
  - `docs/02-seminar/harness-rebuilt-md/01-코딩은 사라지는가.md`
  - `docs/02-seminar/harness-rebuilt-md/05-이렇게 하면 망한다: 한계와 실패 패턴.md`
  - `docs/02-seminar/harness-rebuilt-md/07-실전 워크플로우와 도구 세팅.md`
- Source sections:
  - 04 `에이전트 루프: 하네스의 심장`
  - 04 `Prompt, Context, Harness`
  - 04 `하네스의 구성요소`
  - 04 `하네스의 책임`
  - 05 `컨텍스트가 클수록 항상 좋은 것은 아니다`
  - 07 `시작하며: 두 가지 막다른 길`
  - 01 `문서가 코드다`
  - 01 `개발자의 새로운 역할`
  - 02 `Agent = Model + Harness`
- Core claims:
  - 챗봇은 답을 내지만, 에이전트는 루프를 돈다.
  - 거의 모든 코딩 에이전트는 `gather context -> take action -> verify -> repeat`로 움직인다.
  - 하네스의 책임과 구성요소는 이 루프를 통제하기 위해 존재한다.
  - `Prompt ⊂ Context ⊂ Harness`.
  - 하네스는 모델이 실제 일을 하는 실행 환경 전체다.
- Writing direction:
  - 01장이 이미 `Harness`를 환경으로 정의하고 끝나므로 02장은 정의를 반복하지 않고 에이전트 루프에서 바로 시작한다.
  - 첫 장면은 `에이전트 루프는 작업의 기본 단위다`로 시작한다.
  - 루프를 작업 단위로 설명하되, 실패 누적 구조는 짧게 예고하고 03장으로 넘긴다.
  - `오류의 나비효과`, `Poisoning`, `Distraction`, `Confusion`, `Clash`, `Context Rot`의 본론은 03장에 둔다.
  - 그다음 `Prompt ⊂ Context ⊂ Harness`, `Agent = Model + Harness`, `Harness의 구성요소`, `구성요소/책임/도구의 관계`, 도구 레이어로 확장한다.
  - 구성요소는 하네스가 갖춰야 할 능력, 책임은 그 능력으로 지킬 운영 기준, 도구는 그 책임을 실행 환경에 고정하는 수단으로 설명한다.
  - `Human-in-the-Loop Control`은 별도 루프가 아니라 `take action`과 `verify` 전후에 걸리는 승인 관문으로 설명한다.
  - 장의 중심은 "개발자는 사라지는가"가 아니라 "환경을 설계하는 사람이 왜 중요해지는가"다.
  - `~가 강합니다` 같은 번역투는 피하고 자연스러운 발표체로 쓴다.

### 03. 에이전트는 왜 길을 잃는가

- Target file: `docs/02-seminar/prose/03-why-agents-get-lost.md`
- Main source:
  - `docs/02-seminar/harness-rebuilt-md/05-이렇게 하면 망한다: 한계와 실패 패턴.md`
  - `docs/02-seminar/harness-rebuilt-md/04-프롬프트를 넘어서: 에이전트를 움직이는 기술, Harness.md`
  - `docs/02-seminar/harness-rebuilt-md/02-왜 Claude Code인가, 그리고 왜 Harness 인가.md`
- Source sections:
  - 05 `긴 작업이 위험한 이유`
  - 05 `컨텍스트가 클수록 항상 좋은 것은 아니다`
  - 05 `대표 실패 패턴 네 가지`
  - 05 `Context Rot`
  - 04 `Context Engineering: 더 많이 넣는 기술이 아니다`
  - 02 `컨텍스트 시대의 벽`
- Core claims:
  - 긴 작업에서는 작은 오해가 다음 루프의 입력으로 들어가며 증폭된다.
  - 컨텍스트가 크다고 안전한 것은 아니다. 신호 대 잡음비가 핵심이다.
  - `Poisoning`, `Distraction`, `Confusion`, `Clash`는 모두 컨텍스트가 썩는 방식이다.
  - 모델이 멍청해서가 아니라, 누적 루프를 통제하지 못해서 길을 잃는다.
- Writing direction:
  - 공포 조장이 아니라 구조의 필요성을 설득한다.
  - `Context Rot`은 본문에서 `컨텍스트 부패 (Context Rot)`로 쓴다.
  - "오늘 모델이 이상하다"에서 "어떤 게이트와 상태 관리가 비어 있었는가"로 시선을 바꾼다.

### 04. 먼저 방향을 고정한다

- Target file: `docs/02-seminar/prose/04-fix-direction-first.md`
- Main source:
  - `docs/02-seminar/harness-rebuilt-md/03-AI 시대의 개발 방법론.md`
  - `docs/02-seminar/harness-rebuilt-md/07-실전 워크플로우와 도구 세팅.md`
  - `docs/02-seminar/harness-rebuilt-md/08-이 글과 발표가 만들어진 과정.md`
- Source sections:
  - 03 `SDD: 스펙이 진실의 원천`
  - 03 `Waterfall과는 무엇이 다른가`
  - 03 `SDD + TDD 가장 강력한 조합`
  - 07 `Plan-Critic-Build`
  - 08 `outline과 manifest가 계획을 들고 간다`
- Core claims:
  - AI가 빠르기 때문에 방향 고정이 더 중요해진다.
  - `SDD`는 문서를 많이 쓰자는 말이 아니라, 에이전트가 길을 잃지 않게 기준을 저장소에 박아두는 운영 전략이다.
  - 구현 전에 목표, 범위, 수용 기준, 모호한 질문을 고정해야 한다.
  - `Plan-Critic-Build`는 나쁜 전제를 실행으로 밀고 가는 일을 막는다.
- Writing direction:
  - `Waterfall` 회귀가 아니라 빠른 루프를 위한 기준선이라는 점을 분명히 한다.
  - 스펙과 계획은 발표/글 제작 사례와도 연결한다.

### 05. 기계가 막을 수 있는 것은 앞에서 막는다

- Target file: `docs/02-seminar/prose/05-move-deterministic-gates-left.md`
- Main source:
  - `docs/02-seminar/harness-rebuilt-md/03-AI 시대의 개발 방법론.md`
  - `docs/02-seminar/harness-rebuilt-md/05-이렇게 하면 망한다: 한계와 실패 패턴.md`
  - `docs/02-seminar/harness-rebuilt-md/04-프롬프트를 넘어서: 에이전트를 움직이는 기술, Harness.md`
  - `docs/02-seminar/harness-rebuilt-md/07-실전 워크플로우와 도구 세팅.md`
- Source sections:
  - 03 `TDD: AI 가드레일`
  - 05 `결정 제어와 확률 제어를 분리하라`
  - 04 `하네스의 책임`
  - 04 `하네스의 도구`
  - 07 `필요없는 도구는 덜어내라`
  - 07 `Approval, Auto-accept, Plan Mode`
- Core claims:
  - AI에게 "잘 확인해줘"라고 말하는 것보다 실제 테스트, lint, type check, 승인 게이트를 통과하게 만드는 편이 덜 흔들린다.
  - 결정론적으로 막을 수 있는 것은 앞쪽 게이트로 옮겨야 한다.
  - `TDD`는 단순 품질 관리가 아니라 에이전트의 자유를 제한하는 통제선이다.
  - 작업 위험도에 따라 권한과 승인 방식을 다르게 둬야 한다.
- Writing direction:
  - 이 장은 "검증"과 "권한"의 장이다.
  - `Keep Quality Left`는 본문에서 `품질을 앞단으로 당기기 (Keep Quality Left)`로 쓰고, 필요하면 `시프트 레프트(Shift Left)`와 연결해 설명한다.

### 06. 하나의 AI에게 다 맡기지 않는다

- Target file: `docs/02-seminar/prose/06-do-not-give-one-ai-everything.md`
- Main source:
  - `docs/02-seminar/harness-rebuilt-md/06-멀티 에이전트 활용 패턴.md`
  - `docs/02-seminar/harness-rebuilt-md/04-프롬프트를 넘어서: 에이전트를 움직이는 기술, Harness.md`
  - `docs/02-seminar/harness-rebuilt-md/08-이 글과 발표가 만들어진 과정.md`
- Source sections:
  - 06 `왜 하나의 에이전트만으로는 부족한가`
  - 06 `하나의 에이전트 = 하나의 역할`
  - 06 `Sub-Agent`
  - 06 `Orchestrator`
  - 06 `GAN-Style`
  - 06 `Agent Teams`
  - 06 `설계 원칙`
  - 08 `생성과 검증을 같은 손에 쥐지 않았다`
- Core claims:
  - 멀티 에이전트의 본질은 병렬화가 아니라 분해다.
  - 컨텍스트, 역할, 검증 책임을 쪼개야 한다.
  - 생성자와 평가자를 같은 손에 쥐면 blind spot이 남는다.
  - `Sub-Agent`는 중간 작업을 격리하는 기본형이고, `Agent Team`은 양방향 토론이 필요할 때만 쓴다.
- Writing direction:
  - 패턴명을 모두 길게 설명하기보다, "왜 분해해야 하는가"를 먼저 설득한다.
  - 생성과 검증 분리는 이 발표 제작 사례와 이어지게 쓴다.

### 07. 실전 Harness는 파일과 명령어로 남는다

- Target file: `docs/02-seminar/prose/07-practical-harness-as-files-and-commands.md`
- Main source:
  - `docs/02-seminar/harness-rebuilt-md/07-실전 워크플로우와 도구 세팅.md`
  - `docs/02-seminar/harness-rebuilt-md/04-프롬프트를 넘어서: 에이전트를 움직이는 기술, Harness.md`
  - `docs/02-seminar/harness-rebuilt-md/01-코딩은 사라지는가.md`
- Source sections:
  - 07 `두 가지 막다른 길`
  - 07 `Plan-Critic-Build`
  - 07 `반복의 자산화`
  - 07 `Ralph Loop`
  - 07 `암묵지를 파일로 뽑아내라`
  - 07 `한 모델에만 기대지 않는다`
  - 07 `cmux와 Git Worktree`
  - 07 `세션이 아니라 이슈가 상태를 들고 간다`
  - 07 `첫 주에 바로 세울 수 있는 최소 워크플로우`
  - 04 `CLAUDE.md`, `AGENTS.md`, `Skills`, `Hooks`, `MCP`, `Plugins`
  - 01 `문서가 코드다`
- Core claims:
  - 실전 Harness는 말로 아는 원칙이 아니라 파일, 명령어, 게이트, 이슈, worktree로 남는 구조다.
  - 반복 지시는 `Skills`, 우회하면 안 되는 규칙은 `Hooks`, 프로젝트 기준은 `AGENTS.md`나 `CLAUDE.md`에 둔다.
  - 암묵지는 파일로 뽑아낼 때 팀의 자산이 된다.
  - 세션이 아니라 이슈와 파일이 상태를 들고 가야 한다.
- Writing direction:
  - 특정 preset pack 소개처럼 보이지 않게 한다.
  - "첫 주에 바로 세울 수 있는 최소 워크플로우"를 실천 결론으로 둔다.

### 08. 이 발표 자체가 Harness였다

- Target file: `docs/02-seminar/prose/08-this-presentation-was-harness.md`
- Main source:
  - `docs/02-seminar/harness-rebuilt-md/08-이 글과 발표가 만들어진 과정.md`
- Source sections:
  - 08 `전체 파이프라인`
  - 08 `source 수집`
  - 08 `prose를 canonical source로 세웠다`
  - 08 `outline과 manifest가 계획을 들고 간다`
  - 08 `design contract를 먼저 고정했다`
  - 08 `생성과 검증을 같은 손에 쥐지 않았다`
  - 08 `이 제작 과정이 보여 주는 하네스 원리`
- Core claims:
  - 이 발표와 글에서 봐야 할 것은 결과물만이 아니라 결과물이 만들어지는 과정이다.
  - `source -> prose -> outline -> html -> pdf`의 층을 분리했다.
  - source boundary, prose spine, outline/manifest, design contract, generation/validation separation이 Harness 원리로 작동했다.
  - 생성과 검증을 같은 손에 쥐지 않았다.
- Writing direction:
  - 자기참조 사례지만 자랑처럼 쓰지 않는다.
  - 앞 장에서 말한 원리가 실제 제작 과정에 어떻게 박혔는지 보여주는 proof 장으로 둔다.
  - speaker notes는 중심 파이프라인에서 제외한다.

### 09. Harness Engineer

- Target file: `docs/02-seminar/prose/09-harness-engineer.md`
- Main source:
  - `docs/02-seminar/harness-rebuilt-md/09-우리가 다음에 해야 할 일.md`
  - `docs/02-seminar/harness-rebuilt-md/01-코딩은 사라지는가.md`
  - `docs/02-seminar/harness-rebuilt-md/07-실전 워크플로우와 도구 세팅.md`
- Source sections:
  - 09 `FOMO 와 피로`
  - 09 `팀 차원의 성숙도`
  - 09 `결론: Harness Engineer`
  - 01 `그래도 기초가 중요하다`
  - 07 `첫 주에 바로 세울 수 있는 최소 워크플로우`
- Core claims:
  - AI FOMO를 줄이는 길은 더 많은 뉴스를 읽는 것이 아니라 직접 운영 구조를 세우는 것이다.
  - 팀 차원의 차이는 모델 선택보다 성숙도에서 난다.
  - 개인과 팀은 반복 규칙, 검증 게이트, 세션 밖 상태 기록부터 시작할 수 있다.
  - `Harness Engineer`는 코드를 덜 쓰는 사람이 아니라 에이전트가 일할 환경을 만드는 사람이다.
- Writing direction:
  - 결론은 큰 선언보다 다음 행동으로 닫는다.
  - 새 모델 소식에 휩쓸리는 것이 아니라 내 환경 안에서 AI를 현실로 만드는 일로 마무리한다.

## 보강 조사 계획

새 목차와 각 장의 논지가 확정되면 인터넷 조사는 다음 목적에 한정한다.

1. 이미 원고에 있는 주장에 대한 정확한 출처 확인
2. `Prompt -> Context -> Harness` 흐름을 보강하는 대표 문헌 확인
3. 컨텍스트 부패 (`Context Rot`), 중간 누락 (`Lost in the Middle`), 보정된 신뢰 (`Calibrated Trust`), 품질을 앞단으로 당기기 (`Keep Quality Left`) 같은 표현의 근거와 한국어 정착 표현 확인
4. `SDD`, `TDD`, `Plan-Critic-Build`, multi-agent pattern의 최신 사용 사례 확인
5. 비용, 성숙도, 내부 공유 사례처럼 민감하거나 맥락이 필요한 수치는 공개 가능한 범위와 표현을 재검토

외부 자료가 기존 원고의 방향을 바꿔야 할 정도로 강하면 바로 본문을 고치지 않고, 먼저 이 target map 또는 별도 research note에 판단을 남긴다.

## 다음 작성 순서

1. 00장과 01장을 먼저 작성해 새 원고의 첫 호흡을 고정한다.
2. 02장에서 에이전트 루프를 먼저 설명한 뒤 Harness의 책임과 구성요소로 들어간다.
3. 03-05장에서 실패 원인, 방향 고정, 검증 게이트를 연결한다.
4. 06-07장에서 역할 분해와 실전 운영 구조를 쓴다.
5. 08-09장에서 제작 사례와 Harness Engineer 결론으로 닫는다.
