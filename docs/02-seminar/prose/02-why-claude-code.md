# 왜 코딩 도구는 결국 Harness로 수렴하는가

## 00. 왜 특정 도구가 아니라 흐름을 봐야 하는가

이 섹션의 질문은 “왜 `Claude Code`인가”에서 한 걸음 더 나아간다. 더 정확한 질문은 왜 최근의 코딩 도구들이 비슷한 방향으로 진화하고 있는가다. 어떤 제품은 IDE에서 시작했고, 어떤 제품은 터미널에서 시작했으며, 어떤 제품은 chat UI에서 출발했다. 하지만 흐름을 길게 보면 거의 모든 modern coding tool이 결국 더 많은 `Context`, 더 많은 tool use, 더 많은 권한 제어, 더 많은 검증 루프를 필요로 하게 된다. 즉, 도구 경쟁의 핵심은 단일 모델보다 `Harness`의 두께와 구조로 이동한다.

## 01. GitHub Copilot이 연 Prompt 시대

이 계보의 출발점은 2022년 6월의 `GitHub Copilot`이다. `OpenAI Codex`를 엔진으로 삼은 초기 `Copilot`은 현재 파일을 바탕으로 다음 줄을 제안하는 자동완성에 가까웠다. 코드 자체가 사실상 프롬프트 역할을 했고, 컨텍스트는 현재 파일 하나에 가깝고, 하네스는 거의 존재하지 않았다. 그럼에도 이 도구는 “코드는 사람이 쓰고 AI는 옆에서 조금 돕는다”는 감각을 무너뜨리기 시작했다.

이 시기의 핵심은 모델에게 어떻게 말할 것인가였다. 더 나은 지시문, 더 나은 설명, 더 나은 예시가 성능을 좌우하는 것처럼 보였다. 그래서 `Copilot`과 `ChatGPT`가 함께 등장한 2022년과 2023년 초반은 자연스럽게 프롬프트 시대의 상징처럼 읽힌다.

## 02. Copilot Chat과 Cursor가 연 Context 시대

하지만 프롬프트만으로는 곧 벽이 드러났다. 같은 규칙을 써도 모델이 관련 파일이나 기존 구현을 보지 못하면 엉뚱한 결과가 나왔기 때문이다. 그래서 다음 단계는 codebase-level `Context`를 다루는 도구들의 부상으로 이어졌다. `Copilot Chat`, `Cursor`, `Windsurf` 같은 도구들은 현재 파일을 넘어서 프로젝트 전체를 읽고, 여러 파일을 함께 수정하고, 문서와 코드를 동시에 참조하는 방식으로 이동했다.

이 변화는 도구의 작동 표면도 바꿨다. 자동완성 중심의 플러그인에서 질문과 탐색과 편집이 결합된 AI-native editor로 관심이 옮겨 갔다. 중요한 것은 이 시점에도 아직 핵심 질문이 “무엇을 보여 줄 것인가”였다는 점이다. 컨텍스트의 범위와 밀도는 커졌지만, 긴 작업을 반복 가능하게 만드는 구조는 아직 충분히 정리되지 않았다.

## 03. agent loop와 tool use가 하네스를 요구하게 된 이유

문제가 더 분명해진 것은 코딩 도구가 답변을 주는 존재를 넘어 행동하는 존재가 되면서부터다. 원본 세미나가 정리하듯, 거의 모든 코딩 에이전트는 `Gather Context → Take Action → Verify Work → Repeat`라는 루프를 반복한다. 처음에는 관련 자료를 모으고, 그다음 파일을 수정하거나 명령을 실행하고, 이어서 테스트와 리뷰로 결과를 확인하고, 마지막으로 그 결과를 다음 루프의 입력으로 다시 주입한다. 이 순간부터 문제는 더 이상 모델 답변 품질 하나로 닫히지 않는다.

왜냐하면 루프의 각 단계마다 다른 종류의 실패가 생기기 때문이다. 너무 많은 정보를 넣으면 `signal-to-noise`가 무너지고, 권한이 과하면 잘못된 행동 비용이 커지고, 검증이 약하면 그럴듯한 오답이 다음 루프의 사실처럼 굳어진다. 그래서 도구를 제대로 쓰는 문제는 “좋은 모델을 붙였는가”보다 “에이전트 루프를 어떤 규칙과 권한과 상태 관리 아래에 두는가”의 문제로 이동한다. 이 지점이 바로 `Harness`가 필요해지는 순간이다.

## 04. Claude Code가 대표 사례가 된 이유

이 흐름 속에서 `Claude Code`가 대표 사례로 자주 등장하는 이유는 단순히 성능 주장 때문만은 아니다. 로컬 전사와 보강 자료를 함께 읽어 보면, `Claude Code`는 `terminal-native workflow`, `Plan Mode`, `Approval`, `Auto-accept`, `CLAUDE.md`, `Skills`, `Hooks`, `MCP`, `Plugins`, `Subagents`처럼 하네스를 구성하는 층을 비교적 노골적으로 드러내는 도구다. 즉, “좋은 에이전트란 결국 어떤 실행 환경 위에서 일하는가”라는 질문을 가장 선명하게 보여 준다.

또 다른 이유는 이 도구가 실행과 검증을 하나의 작업 표면 안에서 다루게 만든다는 점이다. 파일을 읽고, 셸 명령을 실행하고, 결과를 확인하고, 다시 수정하는 흐름을 한 루프로 묶기 때문에, 개발자는 단순한 코드 생성기보다 더 완결된 작업 시스템으로 이 도구를 읽게 된다. 세미나가 `Claude Code`를 제품 이름을 넘어 하나의 개발 환경으로 다루는 이유도 여기에 있다.

## 05. Codex와 OpenCode가 같은 방향을 확인해 주는 이유

이 흐름이 특정 vendor의 취향에 그치지 않는다는 점은 `Codex`와 `OpenCode`를 함께 보면 더 분명해진다. OpenAI는 2026년 2월 11일 공개한 `Harness engineering: leveraging Codex in an agent-first world`에서, 엔지니어의 주요 역할이 직접 코드를 쓰는 일보다 에이전트가 안정적으로 일할 수 있는 저장소 지식, 기계적 제약, 피드백 루프를 설계하는 일로 이동했다고 설명했다. 같은 글에서 `Codex` 팀은 리포지토리 지식을 system of record로 만들고, 커스텀 린터로 아키텍처와 취향을 강제하고, 수천 페이지 문서 대신 지도를 주는 방식으로 `agent legibility`를 높였다고 정리한다.

OpenAI는 다시 2026년 4월 16일 `Codex for (almost) everything`에서 `Codex`를 더 넓은 작업 공간으로 확장했다. 이 업데이트는 background computer use, in-app browser, image generation, plugins, SSH devbox, automations, memory, reusable threads까지 포함하며, `Codex`가 단순 코딩 도우미보다 더 두꺼운 `Harness`를 품는 방향으로 진화하고 있음을 보여 준다. 이제 중요한 것은 모델이 코드를 써 주는가가 아니라, 컴퓨터 사용, 장기 작업, 도구 연결, 기억, 반복 작업을 어떤 구조로 다루는가다.

`OpenCode`는 open source 진영에서도 같은 수렴이 일어나고 있음을 보여 준다. 공식 사이트는 `OpenCode`를 터미널, IDE, desktop에서 동작하는 open source AI coding agent로 설명하고, docs는 `plan`과 `build`라는 primary agent, `general`과 `explore`라는 subagent, 그리고 명령 단위 permission 제어를 전면에 둔다. 즉, `OpenCode` 역시 planner 분리, subagent 분해, permission 경계, multi-session 같은 하네스 언어로 자신을 설명한다.

## 06. 2026 최신 흐름: 코딩을 넘는 Codex, 장기 자율 작업으로 가는 Claude Code

최신 흐름은 이 수렴을 더 분명하게 만든다. OpenAI의 2026년 4월 16일 업데이트는 `Codex`를 코딩을 넘는 broader agent workspace로 확장했고, Anthropic은 2026년 3월 24일 `Harness design for long-running application development`에서 `planner`, `generator`, `evaluator`로 구성된 3-agent architecture를 공개하며 장기 자율 작업 성능이 하네스 설계에 달려 있음을 전면에 내세웠다. 핵심은 모델 하나를 더 오래 돌리는 것이 아니라, context reset, structured artifact handoff, evaluator separation 같은 구조를 도입하는 데 있었다.

Anthropic의 흐름도 같은 결론으로 이어진다. 2025년 9월 29일 `Enabling Claude Code to work more autonomously`는 `Subagents`, `Hooks`, background tasks, checkpoints를 공식 기능으로 소개했고, 2025년 10월 20일 `Beyond permission prompts: making Claude Code more secure and autonomous`는 filesystem isolation과 network isolation을 갖춘 sandboxing이 permission prompts를 줄이면서도 더 안전한 자율성을 만든다고 설명했다. 자율성과 안전이 함께 올라가는 방향 역시 결국 더 좋은 `Harness`의 문제로 귀결된다.

## 07. 결론: 도구 경쟁의 종착지는 model choice보다 harness quality

따라서 이 섹션의 결론은 특정 도구의 우열을 선언하는 데 있지 않다. 더 중요한 결론은 `GitHub Copilot` 이후 코딩 도구의 진화가 결국 `Harness`를 더 두껍게 만드는 방향으로 수렴하고 있다는 점이다. `Claude Code`는 그 경향을 가장 선명하게 보여 주는 대표 사례이고, `Codex`와 `OpenCode`는 같은 방향이 industry-wide movement임을 확인해 주는 사례다. 이제 개발자가 봐야 할 핵심은 “무엇이 더 잘 써 주는가”보다 “어떤 도구가 더 나은 context, permission, verification, memory, multi-agent, workflow 구조를 제공하는가”에 가깝다.
