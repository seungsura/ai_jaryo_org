# Harness 잘 사용하기 Target Map

## 작업 원칙

- 대상 원고는 `docs/02-seminar/harness-rebuilt-md`의 markdown만 근거로 삼는다.
- `assets/`, JPG, PNG, PDF는 보지 않는다.
- speaker notes는 이번 prose 재작성 범위에서 제외한다.
- 기존 prose 본문은 이 map 승인 전까지 수정하지 않는다.
- 새 원고의 중심 주제는 특정 도구 리뷰가 아니라 `Harness 잘 사용하기`다.
- `Claude Code`, `Cursor`, `Copilot`, 카카오 내부 사례, 비용 수치 등은 중심축이 아니라 배경 사례 또는 증거로만 사용한다.

## 새 전체 구조

| 새 장 | Target file | 새 제목 | 중심 질문 |
| --- | --- | --- | --- |
| 00 | `docs/02-seminar/prose/00-overview.md` | 챗봇과 싸우지 않기 | 왜 더 좋은 프롬프트만으로는 충분하지 않은가 |
| 01 | `docs/02-seminar/prose/01-where-coding-is-going.md` | 코딩보다 환경을 설계한다 | 개발자의 숙련은 어디로 이동하는가 |
| 02 | `docs/02-seminar/prose/02-why-claude-code.md` | 도구는 Harness로 수렴한다 | 최근 AI 코딩 도구는 왜 비슷한 구조로 모이는가 |
| 03 | `docs/02-seminar/prose/03-ai-era-methodology.md` | 먼저 방향을 고정한다 | 빠른 생성보다 먼저 정해야 하는 것은 무엇인가 |
| 04 | `docs/02-seminar/prose/04-harness-and-context-engineering.md` | Harness는 환경이다 | 모델 바깥에서 무엇을 통제해야 하는가 |
| 05 | `docs/02-seminar/prose/05-limitations-and-failure-patterns.md` | 에이전트는 왜 길을 잃는가 | 긴 루프와 긴 컨텍스트는 어떻게 실패를 키우는가 |
| 06 | `docs/02-seminar/prose/06-multi-agent-patterns.md` | 하나의 AI에게 다 맡기지 않는다 | 역할, 컨텍스트, 검증 책임을 어떻게 나누는가 |
| 07 | `docs/02-seminar/prose/07-practical-workflow-and-tooling.md` | 실전 Harness는 파일과 명령어로 남는다 | 원칙을 실제 작업 환경에 어떻게 고정하는가 |
| 08 | `docs/02-seminar/prose/08-how-this-presentation-was-made.md` | 이 발표 자체가 Harness였다 | source에서 HTML/PDF까지 어떤 구조로 만들었는가 |
| 09 | `docs/02-seminar/prose/09-what-we-should-do-next.md` | Harness Engineer | 개인과 팀은 무엇부터 바꿔야 하는가 |

## 장별 Section Map

### 00. 챗봇과 싸우지 않기

- Target file: `docs/02-seminar/prose/00-overview.md`
- Source markdown: `docs/02-seminar/harness-rebuilt-md/00-overview.md`, `04-프롬프트를 넘어서: 에이전트를 움직이는 기술, Harness.md`
- Relevant heading cluster: `시작하며`, `코딩보다 환경 구성을 해야한다`, `Prompt, Context, Harness`, `하네스의 구성요소`
- Core claims to preserve:
  - AI를 잘 쓰는 문제는 말씨름이나 프롬프트 기교만의 문제가 아니다.
  - 좋은 결과는 반복 가능한 규칙, 선별된 컨텍스트, 권한 경계, 결정론적 검증, 세션 밖 상태 기록이 함께 작동할 때 나온다.
  - 이 전체 구조를 `Harness`라고 부른다.
- 낮출 내용:
  - 기존 목차 소개는 새 목차 기준으로 교체한다.
  - 특정 제품명은 첫 장에서 거의 쓰지 않는다.
- Missing or ambiguous points:
  - 없음. 다만 첫 문단의 독자 호칭은 발표 구어체와 블로그 에세이 톤 사이에서 사용자가 선호를 정하면 좋다.

### 01. 코딩보다 환경을 설계한다

- Target file: `docs/02-seminar/prose/01-where-coding-is-going.md`
- Source markdown: `docs/02-seminar/harness-rebuilt-md/01-코딩은 사라지는가.md`
- Relevant heading cluster: `추상화의 역사`, `문서가 코드다`, `개발자의 새로운 역할`, `그래도 기초가 중요하다`
- Core claims to preserve:
  - 코딩은 사라지는 것이 아니라 추상화 수준이 올라간다.
  - 손으로 타이핑하는 비중은 줄고, 규칙을 세우고 컨텍스트를 고르고 검증하는 비중이 커진다.
  - `CLAUDE.md`, `AGENTS.md`, `Cursor Rules`, `copilot-instructions.md` 같은 문서는 에이전트가 실제로 따르는 운영 규칙이 된다.
  - AI가 더 많이 해줄수록 기본기는 더 중요해진다.
- 재배치 판단:
  - 기존 01의 내용은 제거하지 않는다.
  - 다만 기계어, 어셈블리, C, Java, Python의 긴 역사 서술은 새 원고에서는 짧은 배경으로 압축한다.
  - 중심은 "코딩은 사라지는가"가 아니라 "환경 설계가 개발자의 새 전면으로 올라온다"로 옮긴다.
- Missing or ambiguous points:
  - YC/OpenAI/Meta 수치를 새 원고에 유지할지 여부는 확인 필요. 현재 markdown에는 존재하지만 새 주제에서는 과한 외부 증거가 될 수 있다.

### 02. 도구는 Harness로 수렴한다

- Target file: `docs/02-seminar/prose/02-why-claude-code.md`
- Source markdown: `docs/02-seminar/harness-rebuilt-md/02-왜 Claude Code인가, 그리고 왜 Harness 인가.md`
- Relevant heading cluster: `프롬프트의 시대`, `컨텍스트의 시대`, `하네스의 시대`, `Agent = Model + Harness`
- Core claims to preserve:
  - AI 코딩 도구의 중심 질문은 `어떤 말을 해야 하나`에서 `어떤 정보를 넣어야 하나`, 다시 `어떤 시스템을 만들어야 하나`로 이동했다.
  - `Prompt Engineering`, `Context Engineering`, `Harness Engineering`은 대체 관계가 아니라 포함 관계다.
  - 하네스는 모델이 아닌 모든 실행 환경이다.
- 낮출 내용:
  - `왜 Claude Code인가`라는 제품 중심 제목은 새 주제와 맞지 않으므로 바꾼다.
  - `Claude Code`는 대표 사례로만 둔다.
  - 유출 사고, 오픈소스 농담, 도구 홍보처럼 읽히는 문장은 삭제하거나 각주성 배경으로 낮춘다.
- Missing or ambiguous points:
  - `Claude Code`, `Codex`, `OpenCode`를 모두 나열할지, 도구명은 최소화할지 사용자 선택 필요.

### 03. 먼저 방향을 고정한다

- Target file: `docs/02-seminar/prose/03-ai-era-methodology.md`
- Source markdown: `docs/02-seminar/harness-rebuilt-md/03-AI 시대의 개발 방법론.md`, `07-실전 워크플로우와 도구 세팅.md`
- Relevant heading cluster: `SDD`, `TDD`, `Waterfall과는 무엇이 다른가`, `Plan-Critic-Build`
- Core claims to preserve:
  - AI가 빠르기 때문에 방향 고정이 더 중요해진다.
  - `SDD`는 문서를 많이 쓰자는 말이 아니라 에이전트가 따라야 할 북극성을 저장소에 박아두는 운영 전략이다.
  - 구현 전에 계획과 수용 기준을 세워야 한다.
  - `Plan-Critic-Build`는 나쁜 전제를 실행으로 밀고 가는 일을 막는다.
- 재배치 판단:
  - `TDD` 상세는 04장 검증 게이트로 일부 이동한다.
  - 이 장은 스펙, 계획, 수용 기준, 승인 전 멈춤에 집중한다.
- Missing or ambiguous points:
  - `GitHub Spec Kit` 같은 특정 도구 예시는 유지하되 길이는 줄이는 편이 좋다.

### 04. Harness는 환경이다

- Target file: `docs/02-seminar/prose/04-harness-and-context-engineering.md`
- Source markdown: `docs/02-seminar/harness-rebuilt-md/04-프롬프트를 넘어서: 에이전트를 움직이는 기술, Harness.md`
- Relevant heading cluster: `Prompt, Context, Harness`, `하네스의 구성요소`, `에이전트 루프`, `하네스의 책임`, `하네스의 도구`, `Context Engineering`, `Memory`, `Stable Prefix와 Variable Suffix`
- Core claims to preserve:
  - `Prompt ⊂ Context ⊂ Harness`.
  - 하네스는 `gather context -> take action -> verify -> repeat` 루프의 각 지점에 개입한다.
  - 하네스의 책임은 `Guardrails`, `Specification`, `Verification`, `State Management`, `Observability`로 볼 수 있다.
  - 도구 이름보다 도구가 맡는 책임이 중요하다.
  - 컨텍스트 엔지니어링은 더 많이 넣는 기술이 아니라 필요한 것을 고르고 낡은 것을 버리는 기술이다.
- 재배치 판단:
  - 이 장은 새 원고의 이론적 중심이다.
  - `MCP`, `Context 7`, `KV-cache`는 본문 후반의 예시로 유지하되 과하게 길어지면 07장으로 일부 이동한다.
- Missing or ambiguous points:
  - `Context 7` 표기를 그대로 둘지, 더 일반적인 `Context Hub` 표현으로 바꿀지 확인 필요.

### 05. 에이전트는 왜 길을 잃는가

- Target file: `docs/02-seminar/prose/05-limitations-and-failure-patterns.md`
- Source markdown: `docs/02-seminar/harness-rebuilt-md/05-이렇게 하면 망한다: 한계와 실패 패턴.md`
- Relevant heading cluster: `오류의 나비효과`, `긴 작업이 위험한 이유`, `컨텍스트가 클수록 항상 좋은 것은 아니다`, `대표 실패 패턴 네 가지`, `Context Rot`, `신뢰는 조율되어야 한다`, `결정 제어와 확률 제어를 분리하라`
- Core claims to preserve:
  - 긴 루프에서는 작은 오류가 다음 단계의 입력으로 들어가며 증폭된다.
  - 컨텍스트가 크다고 안정적인 것은 아니다. 신호 대 잡음비가 중요하다.
  - `Poisoning`, `Distraction`, `Confusion`, `Clash`는 긴 컨텍스트가 썩는 대표 방식이다.
  - `Calibrated Trust`는 감정 문제가 아니라 작업별 자율성을 조절하는 운영 문제다.
  - 기계가 확인할 수 있는 것은 앞쪽의 결정론적 게이트로 옮겨야 한다.
- 재배치 판단:
  - 이 장은 공포 조장이 아니라 "왜 구조가 필요한가"를 설득하는 장이어야 한다.
  - `Keep Quality Left`는 04장 또는 07장과 연결되는 다리로 쓴다.
- Missing or ambiguous points:
  - 외부 논문/글 링크는 markdown에 있으나 source policy상 로컬 markdown에 적힌 참조로만 취급한다.

### 06. 하나의 AI에게 다 맡기지 않는다

- Target file: `docs/02-seminar/prose/06-multi-agent-patterns.md`
- Source markdown: `docs/02-seminar/harness-rebuilt-md/06-멀티 에이전트 활용 패턴.md`
- Relevant heading cluster: `왜 하나의 에이전트만으로는 부족한가`, `하나의 에이전트 = 하나의 역할`, `Sub-Agent`, `Advisor`, `Orchestrator`, `Parallel`, `GAN-Style`, `Agent Teams`, `설계 원칙`
- Core claims to preserve:
  - 멀티 에이전트의 본질은 병렬화가 아니라 분해다.
  - 컨텍스트, 역할, 검증 책임을 쪼개야 한다.
  - `Sub-Agent`는 중간 작업을 격리하는 기본형이다.
  - 생성자와 평가자는 갈라야 한다.
  - `Agent Team`은 양방향 토론이 필요할 때만 쓴다.
- 낮출 내용:
  - 패턴 나열이 길어지면 발표용 prose에서 호흡이 늘어진다.
  - `SOLID` 표는 유지하되 본문 흐름을 끊으면 짧게 압축한다.
- Missing or ambiguous points:
  - `Advisor`를 별도 패턴으로 강조할지, `Sub-Agent`의 변형으로 낮출지 확인 필요.

### 07. 실전 Harness는 파일과 명령어로 남는다

- Target file: `docs/02-seminar/prose/07-practical-workflow-and-tooling.md`
- Source markdown: `docs/02-seminar/harness-rebuilt-md/07-실전 워크플로우와 도구 세팅.md`, `04-프롬프트를 넘어서: 에이전트를 움직이는 기술, Harness.md`
- Relevant heading cluster: `두 가지 막다른 길`, `OMC`, `Plan-Critic-Build`, `필요없는 도구는 덜어내라`, `Approval, Auto-accept, Plan Mode`, `반복의 자산화`, `Ralph Loop`, `암묵지를 파일로 뽑아내라`, `cmux와 Git Worktree`, `세션이 아니라 이슈가 상태를 들고 간다`, `첫 주에 바로 세울 수 있는 최소 워크플로우`
- Core claims to preserve:
  - 실전 워크플로우의 중심은 도구 수가 아니라 운영 일관성이다.
  - 반복 지시는 `Skills`, 우회하면 안 되는 규칙은 `Hooks`, 공통 기준은 `AGENTS.md`나 `CLAUDE.md`에 둔다.
  - 위험도에 따라 approval, auto-accept, plan mode를 나눠야 한다.
  - `Ralph Loop`와 암묵지 파일화는 반복을 자산화하는 예다.
  - 긴 작업은 이슈와 `Git Worktree`로 상태와 작업 공간을 분리한다.
  - 첫 주에 할 수 있는 최소 워크플로우를 제시한다.
- 낮출 내용:
  - `OMC`는 특정 preset pack 소개처럼 읽히지 않게 사례로만 둔다.
- Missing or ambiguous points:
  - 사용자가 실제 발표에서 특정 제품/프리셋 이름을 어느 정도까지 노출하고 싶은지 확인 필요.

### 08. 이 발표 자체가 Harness였다

- Target file: `docs/02-seminar/prose/08-how-this-presentation-was-made.md`
- Source markdown: `docs/02-seminar/harness-rebuilt-md/08-이 글과 발표가 만들어진 과정.md`
- Relevant heading cluster: `전체 파이프라인`, `source 수집`, `prose를 canonical source로 세웠다`, `outline과 manifest`, `design contract`, `생성과 검증을 같은 손에 쥐지 않았다`, `이 제작 과정이 보여 주는 하네스 원리`
- Core claims to preserve:
  - 이 발표와 글의 핵심은 결과물이 아니라 결과물이 만들어지는 과정이다.
  - `source -> prose -> outline -> html -> pdf`의 층을 분리했다.
  - source boundary, prose spine, outline/manifest, design contract, generation/validation separation이 하네스 원리로 작동했다.
  - 생성과 검증을 같은 손에 쥐지 않았다.
- 제거 또는 낮출 내용:
  - speaker notes는 이번 목표에서 고려하지 않으므로 중심 파이프라인에서 뺀다.
  - 필요하면 "나중 단계" 정도로만 언급한다.
- Missing or ambiguous points:
  - 실제 발표 제작 사례를 얼마나 자기참조적으로 드러낼지 사용자 선호 확인 필요.

### 09. Harness Engineer

- Target file: `docs/02-seminar/prose/09-what-we-should-do-next.md`
- Source markdown: `docs/02-seminar/harness-rebuilt-md/09-우리가 다음에 해야 할 일.md`, `01-코딩은 사라지는가.md`
- Relevant heading cluster: `FOMO와 피로`, `팀 차원의 성숙도`, `결론: Harness Engineer`, `개발자의 새로운 역할`, `그래도 기초가 중요하다`
- Core claims to preserve:
  - AI FOMO를 줄이는 길은 더 많은 뉴스를 읽는 것이 아니라 직접 운영 구조를 세우는 것이다.
  - 팀 차원의 차이는 모델 선택보다 성숙도에서 난다.
  - 개인과 팀은 반복 규칙, 검증 게이트, 세션 밖 상태 기록부터 시작할 수 있다.
  - `Harness Engineer`는 코드를 덜 쓰는 사람이 아니라 에이전트가 일할 환경을 만드는 사람이다.
- 낮출 내용:
  - 비용 수치는 내부 공유 사례로 짧게 제한한다.
  - 결론은 과장된 선언보다 다음 행동으로 닫는다.
- Missing or ambiguous points:
  - 팀 성숙도 표를 유지할지, prose 안에서 문장으로 풀지 확인 필요.

## 01장 제거처럼 보였던 이유에 대한 작업 판단

기존 `01-where-coding-is-going.md`의 내용은 새 구조에서 폐기 대상이 아니다. 다만 새 주제가 `Harness 잘 사용하기`로 바뀌면서, 기존 01장의 긴 역사 도입은 중심 논지로 두기 어렵다. 새 01장은 다음처럼 다룬다.

1. "코딩은 사라지는가"라는 질문은 짧게만 남긴다.
2. 추상화의 역사는 한두 문단으로 압축한다.
3. `문서가 코드다`, `컨텍스트를 설계하는 능력`, `검증 게이트`, `기초가 더 중요하다`를 본론으로 끌어올린다.
4. 새 02장부터는 도구사가 아니라 Harness 수렴 구조로 넘어간다.

즉 제거가 아니라 비중 조정이다.

## 다음 작성 순서 제안

1. 이 target map을 사용자가 승인한다.
2. 00장과 01장을 먼저 재작성해 새 톤을 고정한다.
3. 02장은 제품 리뷰 냄새를 빼고 도구 수렴 장으로 다시 쓴다.
4. 03-07장은 Harness 원리와 실전 운영의 본론으로 작성한다.
5. 08-09장은 사례와 행동 결론으로 닫는다.
