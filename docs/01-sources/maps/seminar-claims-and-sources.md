# 세미나 주장과 출처

이 문서는 `docs/02-seminar/prose/` 본문에 들어간 주장, 수치, command, 연구 인용의 provenance를 정리합니다. 본문에서는 narrative를 우선하고, 이 파일에서는 `public source`, `internal source`, `supplemental markdown source`를 분리합니다.

## 사용 원칙

- `public source`로 확인된 항목은 링크와 함께 기록합니다.
- `public source`로 분리 확인되지 않은 수치와 사례는 `카카오 AI 팀 조직 내의 확인된 수치`로만 표기합니다.
- `internal source`를 외부 benchmark나 공개 case study처럼 재인용하지 않습니다.
- `supplemental markdown source`는 이 저장소 루트에 보존된 추가 markdown archive를 뜻합니다. 이 범주의 내용은 세미나 본문 보강에는 사용할 수 있지만, 외부 검증이 끝난 `public source`처럼 취급하지 않습니다.
- OCR의 임시 라벨은 가능하면 official title, `DOI`, repository, product page 기준으로 교정합니다.

## Section 1. 역할 이동과 공개 신호

- 공개 확인 항목
  - `YC W25`의 약 `25%`가 코드베이스의 `95%`를 AI로 생성하고 있다는 수치는 2025년 3월 6일 `TechCrunch` 기사에서 확인됩니다. 이 기사는 `YC`의 `Jared Friedman` 발언을 인용합니다.
  - `Jared Friedman`의 직함과 `YC` 내 역할은 `Y Combinator` 공식 프로필에서 확인합니다.
- 내부 확인 항목
  - page 010에 함께 등장하는 `~3개월`, `Meta engineer`, `사람의 터치 없이 PR에 그대로 올라오는` 계열 서술은 공개 source로 분리 확인되지 않았습니다.
  - 최종 문서에서는 이를 `카카오 AI 팀 조직 내의 확인된 수치`와 내부 실무 사례로만 기록합니다.
- supplemental markdown source
  - `prompt-context-harness-1-15.md`는 `Prompt → Context → Harness` 전환, 추상화의 역사, `Harness Engineer`라는 역할 이동을 보강합니다.

## Section 2. 코딩 도구의 계보와 Harness 수렴

- 공개 확인 항목
  - OpenAI의 2026년 2월 11일 글 `Harness engineering: leveraging Codex in an agent-first world`는 `Codex`를 agent-first workflow 안에서 다루며, 저장소 지식을 system of record로 만들고, 커스텀 린터와 검증 루프를 통해 agent legibility를 높였다고 설명합니다.
  - OpenAI의 2026년 4월 16일 글 `Codex for (almost) everything`은 `Codex`가 coding을 넘어 computer use, browser, images, plugins, SSH devboxes, automations, memory, reusable threads까지 확장되었다고 설명합니다.
  - Anthropic의 2026년 3월 24일 글 `Harness design for long-running application development`는 `planner`, `generator`, `evaluator` 구조와 context resets, structured handoff artifacts를 장기 자율 작업의 핵심 하네스로 제시합니다.
  - Anthropic의 2025년 9월 29일 글 `Enabling Claude Code to work more autonomously`는 `Subagents`, `Hooks`, background tasks, checkpoints를 공식 기능으로 소개합니다.
  - Anthropic의 2025년 10월 20일 글 `Beyond permission prompts: making Claude Code more secure and autonomous`는 filesystem과 network isolation을 결합한 sandboxing이 permission prompts를 줄이면서 더 안전한 자율성을 만든다고 설명합니다.
  - `OpenCode` 공식 사이트와 docs는 `OpenCode`를 terminal, IDE, desktop에서 동작하는 coding agent로 설명하고, `plan`/`build` primary agents, `general`/`explore` subagents, command-level permissions를 전면에 둡니다.
- supplemental markdown source
  - `evolution-of-ai-agentic-patterns.md`는 `GitHub Copilot`에서 시작해 `Copilot Chat`, `Cursor`, `Claude Code`, `Codex`, `Copilot Coding Agent`로 이어지는 genealogy와 `Prompt → Context → Harness` 시대 구분을 보강합니다.
  - `claude-code-seminar-kakao.md`의 page 018은 `GitHub Copilot`, `Cursor`, `Windsurf`, `Codex`, `Claude Code`를 한 장에서 비교하며, 원본 세미나가 이미 vendor comparison보다 tool form factor와 에이전틱 구조에 관심을 두고 있었음을 보여 줍니다.
  - `claude-code-mastery-playbook.md`는 `Claude Code`를 로컬 파일 시스템, 터미널, 전체 코드베이스와 직접 상호작용하는 `agentic coding tool`로 정의하고 `Gather Context → Take Action → Verify Results` 루프를 보강합니다.
- 내부 확인 항목
  - `4~8개월 프로젝트를 2주`, `온보딩 1~2일`, `첫날부터 의미 있는 기여`, `기술 부채 해결`, `즉각 피드백`, `불가능하던 작업 실현`은 모두 `카카오 AI 팀 조직 내의 확인된 수치`로 유지합니다. 본문에서는 외부 공개 사례가 아니라 도입 효과의 방향을 설명하는 내부 체감 사례로만 사용합니다.

## Section 3. AI 시대의 방법론

- 공개 확인 항목
  - `/speckit.specify`, `/speckit.plan`, `/speckit.tasks`는 `GitHub spec-kit` 공식 저장소에서 확인한 exact command입니다.
- supplemental markdown source
  - `claude-code-seminar-kakao.md`의 page 028~034는 `spec-first`, `TDD`, 실행 전 계획 고정, 자동 테스트 루프를 함께 제시합니다.
  - `prompt-context-harness-1-15.md`와 `claude-code-mastery-playbook.md`는 방법론이 결국 하네스 안으로 들어가야 한다는 논지를 보강합니다.

## Section 4. Harness Engineering

- 공개 확인 항목
  - `Agent = Model + Harness`라는 정의와 “모델이 아닌 것은 전부 `Harness`”라는 설명은 `LangChain`의 `Vivek Trivedy`가 쓴 `The Anatomy of an Agent Harness`와 직접 연결됩니다.
  - OpenAI와 Anthropic의 2026년 engineering 글은 각각 `Codex`와 `Claude Code` 문맥에서 하네스를 실행 환경 전체로 다루며, 장기 작업에서 구조적 handoff, evaluator separation, 기계적 제약이 중요하다고 설명합니다.
- supplemental markdown source
  - `prompt-context-harness-1-15.md`는 `Prompt → Context → Harness` 전환, `Guardrails`/`Specification`/`Verification`/`State Management`/`Observability`라는 다섯 실무 블록, `Build to Delete` 원칙을 보강합니다.
  - `claude-code-mastery-playbook.md`는 `CLAUDE.md`, `Skills`, `Hooks`, `MCP`, `Plugins`를 서로 다른 실행 레이어로 구분하는 보강 source로 사용합니다.
  - `evolution-of-ai-agentic-patterns.md`는 `Agent = Model + Harness`, 2x2 가이드/연산적/프롬프트/추론적 피드백 구도, `OpenAI Codex` 사례를 통해 하네스의 구조적 의미를 보강합니다.

## Section 5. long context와 실패 패턴

- 공개 확인 항목
  - `Drew Breunig`의 `How Long Contexts Fail`은 `Context Poisoning`, `Context Distraction`, `Context Confusion`, `Context Clash`를 정리하는 보조 source입니다.
  - `Chroma`의 `Context Rot` technical report는 input length가 늘수록 `LLM` 성능이 균일하지 않게 악화된다는 점을 실험적으로 보여 줍니다.
- supplemental markdown source
  - `prompt-context-harness-1-15.md`는 `AI Slop`, `Doom Loop`, 지시 무시, `Shadow Agent`를 하네스 부재의 실전 실패 징후로 묶습니다.
  - `claude-code-mastery-playbook.md`는 `Calibrated Trust`, 긴 대화에서의 drift, 상태 외부화 필요성을 보강합니다.
  - `evolution-of-ai-agentic-patterns.md`는 `long task coherence`, context reset, evaluator separation이 필요한 이유를 Anthropic 사례와 함께 설명합니다.

## Section 6. Multi-Agent와 역할 분리

- 공개 확인 항목
  - Anthropic의 2026년 3월 24일 글은 `planner`, `generator`, `evaluator` 분리와 structured artifact handoff를 장시간 agentic coding의 핵심 구조로 설명합니다.
  - `OpenCode` docs는 primary agent와 subagent 구분, planning agent, read-only explore agent, permissions를 도구 수준에서 구현하는 예시를 제공합니다.
- supplemental markdown source
  - `claude-code-mastery-playbook.md`는 `Subagent`의 가치가 역할 이름보다 컨텍스트 격리, 최소 권한, 구조화된 출력 형식에 있다는 점을 보강합니다.
  - 같은 source는 “전문가라고 주장만 하는 에이전트”, 맥락 손실이 큰 순차 파이프라인, 로그를 감추는 test runner를 `Subagent` anti-pattern으로 제시합니다.
  - `evolution-of-ai-agentic-patterns.md`는 `Andrew Ng`의 design pattern 계보와 Anthropic의 multi-agent evaluator 구조를 연결합니다.

## Section 7. 운영 구조와 tool hygiene

- supplemental markdown source
  - `prompt-context-harness-1-15.md`는 tool curation, 격리된 sandbox, 결정론적 gate, 인간 승인으로 이어지는 layered workflow를 보강합니다.
  - `claude-code-mastery-playbook.md`는 `Approval`, `Auto-accept`, `Plan Mode`, 유휴 `MCP` 서버 정리 같은 운영 hygiene를 보강합니다.
  - `claude-code-seminar-kakao.md`의 page 067~074는 `Plan-Critic-Build`, 다중 모델 cross-check, `git worktree`, 이슈 기반 운영, `Linear` 연동을 workflow 사례로 제시합니다.
  - `OpenCode` docs는 plan/build/general/explore 분리와 command-level permissions를 통해 tool hygiene가 product surface에 어떻게 구현되는지 보여 줍니다.
- 내부 확인 항목
  - `OMC` 관련 page 071의 `29+ 에이전트`, `30~50%↓`, 최대 `5` worker 병렬은 공개 benchmark가 아니라 local transcript 기준의 운영 예시입니다.
  - `Plan-Critic-Build` 패턴은 `/ralplan`, 검증 루프는 `/ultraqa`를 authoritative literal로 유지합니다.
  - 다중 모델 호출 예시는 `/ask codex "이 계획에서 짠 구조 리뷰해줘. 빠진 부분 있는지"`와 `/ask gemini "이 카드 레이아웃 가독성 어떤지 피드백 줘"`로 복원합니다.

## Section 8. 제작 사례와 이름 표기

- 내부 확인 항목
  - `claude-code-seminar-kakao.md`의 표지와 말미에는 `김영동` 표기가 남아 있고, 부록 reference에는 `이재영` 계정이 등장합니다.
  - 내부 확인 기준으로 두 인물 모두 `카카오 AI 팀` 인원으로만 기록하고, 본문에는 발표자나 제작자 같은 별도 role label을 부여하지 않습니다.
- approved external design/process reference
  - `make-slide`는 본문 claim의 factual source가 아니라 HTML stage의 design/process reference입니다.
  - `minimal-light` theme, shell reuse, hybrid deck runtime 같은 구현 계약만 보강하고 canonical prose의 자리를 대신하지 않습니다.
- supplemental markdown source
  - page 076~082는 수집층, 계획층, 실행층 분리, `CLAUDE.md`, `slides-grab`, 승인 게이트, `피드백 8회 반복`을 통해 발표 자체가 하네스 설계의 사례가 되도록 구성돼 있습니다.

## Section 9. AI FoMO와 실전 도입

- 공개 확인 항목
  - 슬라이드의 `FOMO-AI 2025` 표기는 본문에서 `AI FoMO (fear of missing out) in the workplace`로 복원합니다.
  - 정식 출처는 `Technology in Society` 2026 논문이며, `DOI`는 `10.1016/j.techsoc.2025.103052`입니다.
  - `OECD`의 `Algorithmic management in the workplace` working paper는 workplace-level survey와 policy context를 보강하는 source로 사용합니다.
- supplemental markdown source
  - `claude-code-mastery-playbook.md`는 `Delegation`, `Description`, `Discernment`, `Diligence`라는 `4D` 프레임워크를 통해 인간 책임의 위치를 설명합니다.
  - `prompt-context-harness-1-15.md`는 현대 엔지니어를 `Harness Engineer`로 재정의하고, 좋은 하네스는 모델이 발전할수록 삭제 가능한 구조여야 한다는 논지를 보강합니다.
- 공개 기사
  - `박종천` 관련 메시지는 `TTimes`의 2026년 4월 5일 기사와 4월 7일 기사에서 보강합니다. 전자는 “AI를 많이 쓸 수 있는 사람”이라는 framing을, 후자는 토큰 사용량을 생산성 지표로 보는 관점을 제시합니다.

## 참고 링크

- `YC W25 / 25% / 95%`: [TechCrunch - A quarter of startups in YC’s current cohort have codebases that are almost entirely AI-generated](https://techcrunch.com/2025/03/06/a-quarter-of-startups-in-ycs-current-cohort-have-codebases-that-are-almost-entirely-ai-generated/)
- `Jared Friedman`: [Y Combinator profile](https://www.ycombinator.com/people/jared-friedman)
- `spec-kit`: [github/spec-kit](https://github.com/github/spec-kit)
- `OpenAI / Codex`: [Harness engineering: leveraging Codex in an agent-first world](https://openai.com/index/harness-engineering/), [Codex for (almost) everything](https://openai.com/index/codex-for-almost-everything/)
- `Anthropic / Claude Code`: [Harness design for long-running application development](https://www.anthropic.com/engineering/harness-design-long-running-apps), [Enabling Claude Code to work more autonomously](https://www.anthropic.com/news/enabling-claude-code-to-work-more-autonomously), [Beyond permission prompts: making Claude Code more secure and autonomous](https://www.anthropic.com/engineering/claude-code-sandboxing)
- `OpenCode`: [OpenCode](https://opencode.ai/), [Agents docs](https://opencode.ai/docs/agents/)
- `Vivek Trivedy / LangChain`: [vtrivedy.com](https://www.vtrivedy.com/), [The Anatomy of an Agent Harness](https://www.langchain.com/blog/the-anatomy-of-an-agent-harness)
- `Kai Renner / Harness Engineering`: [About Kai Renner](https://harness-engineering.ai/about/), [What Is Harness Engineering?](https://harness-engineering.ai/blog/what-is-harness-engineering/)
- `AI FoMO`: [ScienceDirect - AI FoMO (fear of missing out) in the workplace](https://www.sciencedirect.com/science/article/abs/pii/S0160791X25002428)
- `OECD`: [Algorithmic management in the workplace](https://www.oecd.org/en/publications/algorithmic-management-in-the-workplace_287c13c4-en.html)
- `Drew Breunig`: [How Long Contexts Fail](https://www.dbreunig.com/2025/06/22/how-contexts-fail-and-how-to-fix-them.html)
- `Chroma`: [Context Rot](https://www.trychroma.com/research/context-rot)
- `박종천 / TTimes`: [블리자드, 넥슨 등 30년 개발자가 말하는 ‘개발자의 삶’](https://www.ttimes.co.kr/article/2022041216177718768), [싸고, 좋은 '토큰'을 많이 만들어 팔겠다는 세 회사](https://www.ttimes.co.kr/article/2026040717517776005), [빅테크가 왜 사람 자르냐구요? 아마존은 어떻게 일하는지 아세요?](https://www.ttimes.co.kr/article/2026040317497781831)
