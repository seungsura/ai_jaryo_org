# 부록: 출처와 후속 읽기를 위한 가이드

## 시작하며: 무엇을 어디까지 믿고, 어디서부터 전진할 것인가

이 부록의 목적은 본문을 다시 요약하는 데 있지 않습니다. 이 글의 주장이 어떤 근거층 위에 서 있는지, 그리고 후속 읽기를 어떤 순서로 이어가야 하는지 정리하는 데 있습니다.

AI 코딩 도구와 에이전트 하네스 분야는 변화가 빠릅니다. 그래서 자료를 한 덩어리로 섞어 읽으면 위험합니다. 공개 1차 자료, 실무자 경험담, 로컬 마크다운 아카이브, 발표 슬라이드, 내부 제작 맥락은 서로 다른 무게를 갖습니다.

이 부록에서는 근거를 세 층으로 나눕니다.

1. 공개 출처와 공식 문서
2. 실무자 글과 사례 자료
3. 로컬 마크다운 및 발표 제작 자료

이 구분이 분명해야 무엇을 사실의 기준선으로 읽고, 무엇을 보조 렌즈로 읽고, 무엇을 다음 작업의 아이디어로 읽을지 흔들리지 않습니다.

## 근거의 세 층위

### 1. 공개 출처와 공식 문서

가장 바깥의 기준선은 공개 출처입니다. 모델과 도구가 빠르게 바뀌는 분야일수록 공식 문서와 1차 자료를 우선해야 합니다. 예를 들면 다음 자료군입니다.

- OpenAI의 Codex 및 agentic workflow 관련 엔지니어링 글
- Anthropic의 agent, context engineering, long-running harness 관련 글
- GitHub Copilot과 Spec Kit 관련 공식 자료
- Claude Code 공식 문서
- MCP(Model Context Protocol) 공식 자료
- LangChain, HumanLayer, Chroma, Drew Breunig 등 에이전트 운영과 context failure 관련 자료
- OECD, AI FoMO 관련 연구와 리포트

본문의 도구와 방법론 논지는 이 공개 자료군을 기준선으로 삼아 읽는 편이 안전합니다.

### 2. 실무자 글과 사례 자료

두 번째 층은 실무자 경험담과 사례 자료입니다. Mitchell Hashimoto, Simon Willison, Martin Fowler와 Birgitta Böckeler, Ethan Mollick, Andrew Ng, Andrej Karpathy, Philipp Schmid 같은 인물의 글과 발표가 여기에 들어갑니다.

이 자료들은 현업 언어와 문제의식을 이해하는 데 매우 유용합니다. 다만 실무자 글은 특정 환경과 경험에 기대는 경우가 많으므로, 공식 문서나 독립 검증 자료와 함께 읽어야 합니다. “어떤 관점이 업계에서 왜 설득력을 얻었는가”를 파악하는 데 강합니다.

### 3. 로컬 마크다운 및 발표 제작 자료

세 번째 층은 이 프로젝트에서 제공된 로컬 마크다운과 발표 자료입니다. 이 자료들은 독립 1차 근거라기보다 공개 출처와 실무자 글을 본문 주장으로 연결하는 보조 자료에 가깝습니다.

- `00-overview.md`: 전체 제목, 부제, 시리즈 방향
- `01-where-coding-is-going.md`: 코딩의 추상화와 개발자 역할 이동
- `02-why-claude-code.md`: Claude Code를 렌즈로 본 도구 수렴
- `03-ai-era-methodology.md`: TDD, SDD, Spec-first의 재부상
- `04-harness-and-context-engineering.md`: Prompt/Context/Harness 구분과 하네스 5대 블록
- `05-limitations-and-failure-patterns.md`: Long Context, Context Rot, 실패 패턴, Calibrated Trust
- `06-multi-agent-patterns.md`: Sub-Agent, Orchestrator, Parallel, GAN-Style, Agent Teams
- `07-practical-workflow-and-tooling.md`: OMC, Plan-Critic-Build, Hooks, Worktree, 이슈 기반 워크플로우
- `08-how-this-presentation-was-made.md`: 제작 파이프라인과 Codex 투입 위치
- `09-what-we-should-do-next.md`: 4D, Build to Delete, Harness Engineer
- `90-appendix-references.md`: 출처 층위와 후속 읽기

## 원본 소스별 활용 내역

이번 재구성에서는 원본 파일의 구조를 완전히 버리지 않았습니다. 대신 중복을 줄이고, 약한 연결부를 보강하고, 독자가 자연스럽게 따라갈 수 있는 기술 블로그 흐름으로 재배치했습니다.

| 원본 | 재구성 후 반영 위치 | 처리 방식 |
| --- | --- | --- |
| `00-overview.md` | 00장 | 제목과 부제, 전체 문제의식을 새 개요로 확장 |
| `01-where-coding-is-going.md` | 1장 | 추상화 역사, 문서의 역할, 개발자 역할 이동을 보강 |
| `02-why-claude-code.md` | 2장 | Claude Code 중심 논지를 도구 진화사와 통합 |
| `03-ai-era-methodology.md` | 3장 | TDD/SDD/Spec-first를 하네스의 검증·명세 루프로 재정리 |
| `04-harness-and-context-engineering.md` | 4장 | 하네스 정의, 5대 블록, 도구 레이어, 컨텍스트 엔지니어링을 통합 |
| `05-limitations-and-failure-patterns.md` | 5장 | 실패 패턴과 보안 경계를 한 장으로 정리 |
| `06-multi-agent-patterns.md` | 6장 | 다섯 패턴을 역할·컨텍스트·검증 분해 관점으로 재작성 |
| `07-practical-workflow-and-tooling.md` | 7장 | 실전 명령어, 게이트, worktree, 이슈 워크플로우로 구체화 |
| `08-how-this-presentation-was-made.md` | 8장 | 제작 과정을 하네스 사례 연구로 재정리 |
| `09-what-we-should-do-next.md` | 9장 | 개인·팀 실천 원칙과 미래 전망으로 확장 |
| `90-appendix-references.md` | 부록 | 출처 층위와 source-to-section map을 정리 |
| `evolution-of-ai-agentic-patterns.pdf` | 2장, 4장, 5장, 9장 | Prompt→Context→Harness 연대기, MCP, KV-cache, Lethal Trifecta, 전망 보강 |
| `claude-code 잘 사용하기 kakao.pdf` | 1~8장 | Claude Code 발표 흐름, 도구 레이어, 워크플로우, 실패 패턴, 제작 과정 보강 |
| `1-15_merged_with_source.pdf` | 0장, 4장, 5장, 7장, 9장 | “챗봇과 싸우지 마라” 메시지, 5대 해부학, 도구 큐레이션, 상태 관리, Build to Delete 보강 |

## 후속 읽기 순서

처음 이 주제를 공부한다면 다음 순서를 권합니다.

### 1단계: 큰 흐름 잡기

- Andrej Karpathy의 AI 시대 소프트웨어 관련 발표와 글
- Andrew Ng의 Agentic Design Patterns
- Simon Willison의 Agentic Engineering Patterns와 Lethal Trifecta
- Martin Fowler/Birgitta Böckeler의 Harness Engineering 관련 글

이 단계에서는 세부 도구보다 패러다임 이동을 이해하는 것이 중요합니다. 프롬프트에서 컨텍스트로, 컨텍스트에서 하네스로 왜 이동했는지를 먼저 봐야 합니다.

### 2단계: 공식 문서로 기준선 세우기

- Claude Code 문서
- OpenAI Codex 및 Agents 관련 문서
- Anthropic의 Building Effective Agents, Context Engineering, Harness 관련 글
- MCP 공식 자료
- GitHub Spec Kit 문서

이 단계에서는 실제 도구가 어떤 구조를 제공하는지 확인합니다. 규칙 파일, 도구 호출, 승인, 훅, 서브에이전트, 스펙 기반 흐름을 공식 문서 기준으로 읽는 것이 좋습니다.

### 3단계: 실무 패턴과 실패 사례 읽기

- HumanLayer의 12-Factor Agents
- Drew Breunig의 context failure 관련 글
- Chroma의 Context Rot 관련 자료
- Vibe Coding hangover 관련 기사와 분석
- AI FoMO 및 workplace AI 관련 자료

이 단계에서는 실패와 운영 문제를 봅니다. 어떤 구조가 없을 때 실제로 무엇이 무너지는지 봐야 하네스가 왜 필요한지 체감됩니다.

### 4단계: 로컬 자료로 자기 워크플로우에 적용하기

마지막으로 로컬 마크다운과 발표 자료를 다시 읽습니다. 이 단계에서는 “좋은 글이네”로 끝내지 말고 자신의 저장소에 다음을 실제로 만들어 보는 것이 좋습니다.

- 규칙 파일 하나
- 반복 업무용 스킬 하나
- 위험 명령 차단 또는 검증 훅 하나
- 이슈 템플릿 하나
- 세션 종료 요약 템플릿 하나
- Plan-Critic-Build 명령 하나

## 팩트와 수치 사용 시 주의

본문에는 여러 수치와 사례가 등장합니다. 예를 들어 AI 생성 코드 비율, 특정 도구의 ARR, 사용자 수, 실험 성공률, 비용 절감률, 벤치마크 향상 같은 항목입니다. 이런 수치는 원본 자료의 문제의식을 보존하기 위해 남겼지만, 실제 외부 게시 전에는 최신 공개 출처로 다시 확인하는 편이 안전합니다.

특히 다음 항목은 업데이트 가능성이 큽니다.

- 특정 도구의 사용자 수, 매출, 기업가치
- 모델 성능 비교와 벤치마크 수치
- 보안 취약점 비율과 코드 품질 리포트 수치
- MCP, A2A, Agents SDK 같은 프로토콜·도구의 채택 현황
- 기업 인수, 라이선스, 제품 출시 일정

이 글의 핵심은 특정 숫자 하나가 아니라 구조적 논지입니다. 숫자는 흐름을 보여 주는 보조 자료로 읽어야 합니다.

## 핵심 개념 사전

### Harness

에이전트가 어떤 정보를 보고, 어떤 도구를 쓰고, 어떤 권한을 가지며, 어떤 검증을 통과해야 하는지를 정하는 운영 구조입니다. 모델 바깥의 실행 환경 전체에 가깝습니다.

### Context Engineering

이번 턴 또는 이번 작업에 필요한 정보를 컨텍스트 윈도우에 선별, 압축, 격리, 주입하는 기술입니다. 더 많이 넣는 것이 아니라 더 맞게 넣는 것이 핵심입니다.

### Guardrails

위험한 행동을 막고 권한 경계를 설정하는 장치입니다. 승인 규칙, 샌드박스, 위험 명령 차단, 권한 제한이 여기에 들어갑니다.

### Verification

에이전트의 결과를 기계적 또는 사람의 검토로 확인하는 과정입니다. 린트, 타입 체크, 테스트, 리뷰, LLM-as-a-judge, E2E 테스트가 포함됩니다.

### State Management

세션이 바뀌어도 작업 상태가 사라지지 않도록 외부 아티팩트에 기록하는 일입니다. 이슈, PR, Git, 진행 파일, ADR 등이 여기에 해당합니다.

### Observability

에이전트 루프가 어디서 흔들렸는지 볼 수 있게 만드는 장치입니다. 실행 로그, 행동 trace, 체크포인트, 비용 기록, 실패 원인 기록이 포함됩니다.

### Build to Delete

현재 모델의 약점을 보완하기 위해 만든 하네스라도, 나중에 모델이나 도구가 개선되면 삭제할 수 있게 설계하라는 원칙입니다. 하네스는 영구 관료제가 아니라 진화하는 운영 구조여야 합니다.

## 마무리

이 글의 논지는 단순합니다. AI 시대에도 소프트웨어 엔지니어링의 엄밀함은 사라지지 않습니다. 위치가 이동합니다. 프롬프트 문장에서 컨텍스트 구성으로, 컨텍스트 구성에서 에이전트가 일하는 환경의 설계로 옮겨갑니다.

따라서 출처를 읽을 때도 같은 관점이 필요합니다. 개별 도구의 기능 목록보다, 그 기능이 어떤 하네스 블록을 채우는지 보아야 합니다. 좋은 자료는 “AI가 무엇을 할 수 있는가”보다 “AI가 안전하고 반복 가능하게 일하려면 어떤 구조가 필요한가”를 더 선명하게 보여 줍니다.
