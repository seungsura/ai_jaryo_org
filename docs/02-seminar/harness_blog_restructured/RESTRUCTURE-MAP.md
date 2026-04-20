# 재구성 작업 기록

## 목적

이 문서는 원본 10개 마크다운과 PDF 자료를 재구성하면서 어떤 내용이 어디로 이동했는지 확인하기 위한 작업 기록입니다. 최종 독자용 본문은 `00-overview.md`부터 `90-appendix-references.md`까지입니다.

## 재구성 원칙

1. 원본의 큰 흐름은 유지했다: 개요 → 역할 변화 → 도구 수렴 → 방법론 → 하네스 → 실패 → 멀티 에이전트 → 실전 워크플로우 → 제작 과정 → 다음 행동.
2. 중복되는 정의는 한 번만 설명하고, 이후 장에서는 운영 관점으로 이어받았다.
3. 한국어 문체는 발표 대본체보다 읽기 쉬운 기술 블로그 문체로 바꿨다.
4. 약한 섹션은 PDF 원본의 논지로 보강했다.
5. 수치와 사례는 원본의 문제의식을 보존하되, 외부 게시 전 최신 확인이 필요한 항목은 부록에 주의사항으로 남겼다.
6. “Harness 잘 사용하기 / 챗봇과 싸우지 않고, 에이전트가 일할 환경을 설계하는 방법”이라는 제목과 부제의 방향을 모든 장에 반영했다.

## 장별 주요 변경

| 새 파일 | 원본 기반 | 주요 변경 |
| --- | --- | --- |
| `00-overview.md` | `00-overview.md`, 1-15 PDF | 제목과 부제를 반영하고, 전체 목차와 핵심 주장을 기술블로그형 개요로 재작성 |
| `01-where-coding-is-going.md` | `01-where-coding-is-going.md`, kakao PDF 1부 | 추상화 역사, 문서 역할, 기본기 중요성을 자연스러운 산문으로 정리 |
| `02-why-claude-code.md` | `02-why-claude-code.md`, evolution PDF | Copilot/ChatGPT/Cursor/Claude Code 흐름과 Prompt→Context→Harness 전환을 통합 |
| `03-ai-era-methodology.md` | `03-ai-era-methodology.md`, kakao PDF 3부 | TDD와 SDD를 하네스의 명세·검증 루프로 재정리하고 Waterfall 반론을 보강 |
| `04-harness-and-context-engineering.md` | `04-harness-and-context-engineering.md`, evolution PDF, 1-15 PDF | Context Engineering, KV-cache, MCP, Memory, 5대 블록, SOLID 재해석을 하나의 하네스 해부학으로 통합 |
| `05-limitations-and-failure-patterns.md` | `05-limitations-and-failure-patterns.md`, evolution PDF, 1-15 PDF | Long Context, Context Rot, 실패 신호, Calibrated Trust, Lethal Trifecta를 한 장으로 정리 |
| `06-multi-agent-patterns.md` | `06-multi-agent-patterns.md`, kakao PDF 6부 | 5대 패턴을 분해 원칙 중심으로 재작성하고 Sub-Agent/Agent Team 차이를 명확화 |
| `07-practical-workflow-and-tooling.md` | `07-practical-workflow-and-tooling.md`, kakao PDF 7부 | OMC, Plan-Critic-Build, 게이트, cmux/worktree, 이슈 기반 workflow를 실전 순서로 재배치 |
| `08-how-this-presentation-was-made.md` | `08-how-this-presentation-was-made.md`, kakao PDF 8부 | 제작 과정을 하네스 사례 연구로 재작성 |
| `09-what-we-should-do-next.md` | `09-what-we-should-do-next.md`, 1-15 PDF | 4D, Build to Delete, 팀 성숙도, 미래 전망을 통합 |
| `90-appendix-references.md` | `90-appendix-references.md` | 출처 층위, 소스별 활용 내역, 후속 읽기 순서, 수치 주의사항 추가 |

## 병합·분리 판단

- `Harness` 정의와 `Context Engineering`은 별도 장으로 완전히 분리하지 않고 4장에서 함께 다뤘다. 실제 운영에서는 두 개념이 분리되어 작동하지 않기 때문이다.
- 보안은 4장의 가드레일에 잠깐 언급하고, 실질 내용은 5장의 실패 패턴으로 이동했다. 보안은 “기능 설명”보다 “실패 방지” 관점에서 읽히는 편이 자연스럽다.
- `Plan-Critic-Build`는 3장과 7장에 모두 등장한다. 3장에서는 방법론적 원칙으로, 7장에서는 실전 명령어와 워크플로우로 다뤘다.
- 멀티 모델 교차 검증은 6장과 7장에 연결했다. 6장에서는 멀티 에이전트와의 차이를 설명하고, 7장에서는 실제 운영법으로 다뤘다.
- 제작 과정은 단순 회고가 아니라 하네스 원리를 증명하는 사례로 8장에 유지했다.

## 누락 방지 체크리스트

- [x] 제목과 부제 반영
- [x] 코딩의 추상화 역사 반영
- [x] 개발자 역할 이동과 기본기 중요성 반영
- [x] Claude Code를 대표 사례로 다룸
- [x] Copilot, ChatGPT, Cursor 흐름 반영
- [x] Prompt → Context → Harness 전환 반영
- [x] CoT, ReAct, Tree-of-Thought, Andrew Ng 패턴 반영
- [x] Vibe Coding과 숙취 반영
- [x] Context Engineering의 Write/Select/Compress/Isolate 반영
- [x] LLM-as-OS, KV-cache, stable prefix/variable suffix 반영
- [x] MCP, Context Hub, Memory 반영
- [x] Agent = Model + Harness 반영
- [x] 하네스 5대 블록 반영
- [x] CLAUDE.md, AGENTS.md, Skills, Hooks, MCP, Plugins 구분 반영
- [x] SOLID 재해석 반영
- [x] TDD, SDD, Spec Kit, Waterfall 비교 반영
- [x] Plan-Critic-Build 반영
- [x] Long Context failure, Context Rot 반영
- [x] AI Slop, Doom Loop, Shadow Agent, Silent Failure 반영
- [x] Calibrated Trust 반영
- [x] Lethal Trifecta, Rule of Two 반영
- [x] Sub-Agent, Orchestrator, Parallel, GAN-Style, Agent Teams 반영
- [x] Anthropic식 Planner/Generator/Evaluator 구조 반영
- [x] OMC, tool curation, gate, approval, worktree, issue workflow 반영
- [x] 제작 파이프라인 source→prose→outline→html→pdf→notes 반영
- [x] 4D, Thought Partner, Build to Delete 반영
- [x] 팀 성숙도와 미래 전망 반영
- [x] 부록의 출처 층위와 후속 읽기 반영
