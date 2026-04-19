# 부록: 출처와 후속 읽기를 위한 가이드

## 시작하며: 무엇을 어디까지 믿고, 어디서부터 전진할 것인가

이 부록의 목적은 본문을 다시 요약하는 데 있지 않습니다. 이 글의 주장이 어떤 근거층 위에 서 있는지, 그리고 후속 읽기를 어떤 순서로 이어가야 하는지를 분명히 정리하는 데 있습니다. 여기서는 근거를 공개 출처, 내부 확인 정보, 로컬 markdown archive의 보조 자료라는 세 층으로 나눠 봅니다. 이 구분이 분명해야 무엇을 공개 1차 근거로 읽고, 무엇을 내부 맥락으로 제한해 읽고, 무엇을 보조 재료로 사용할지 흔들리지 않습니다.

## 근거의 세 층위

가장 바깥 기준선은 **공개 출처(Public Source)**입니다. 코딩 패러다임 변화의 속도는 `YC W25`와 `Jared Friedman`의 공개 기사로 붙들고, 최근 도구들이 왜 `Harness` 중심 구조로 수렴하는지는 OpenAI와 Anthropic의 공식 엔지니어링 글, 그리고 `OpenCode` 공식 문서로 설명합니다. 스펙 중심 방법론은 `GitHub spec-kit`이, 런타임 제어와 실전 운영은 `LangChain`, OpenAI, Anthropic, `Drew Breunig`, `Chroma` 등 관련 자료가 받치고 있습니다. 불안과 역할 재배치 논지는 `AI FoMO` 논문, `OECD` 리포트, `TTimes` 기사로 보강됩니다.

다음 층은 내부 확인 정보입니다. 본문 일부의 생산성 체감치나 제작 맥락은 이 층에서만 확인되며, 공개 링크로 완전히 대체되지 않습니다. 그래서 본문에서는 이 층을 공개 1차 근거와 같은 무게로 취급하지 않고, 공개 출처 위에 얹히는 제한적 보강 정보로 다룹니다.

마지막 층은 로컬 마크다운 아카이브입니다. 이 자료들은 독립 1차 근거라기보다, 공개 출처와 내부 확인 정보를 본문 주장으로 연결하는 보조 자료에 가깝습니다. `prompt-context-harness-1-15.md`는 하네스로의 패러다임 전환과 5대 기능 블록을, `claude-code-mastery-playbook.md`는 에이전트 루프와 검증 감각을, `evolution-of-ai-agentic-patterns.md`는 진화 서사를, `claude-code-seminar-kakao.md`는 전체 세미나의 흐름을 보강합니다.

## 로컬 source-to-section map

로컬 마크다운은 전부 같은 무게로 쓰이지 않습니다. 어떤 파일이 어느 주장과 예시를 떠받치는지 구분해 읽어야 합니다.

- **`claude-code-seminar-kakao.md`**: 에이전트 루프, `Plan-Critic-Build` 구조, `Git worktree` 워크플로우, 제작 과정을 떠받치는 기준 스크립트입니다.
- **`claude-code-mastery-playbook.md`**: 실행 레이어, `Calibrated Trust`, `Subagent` 출력 계약, `4D` 책임론을 보강합니다.
- **`prompt-context-harness-1-15.md`**: `Prompt → Context → Harness` 전환, 5대 기능 블록, 툴 큐레이션, 상태의 외부 기록, `Build to Delete` 철학을 떠받칩니다.
- **`evolution-of-ai-agentic-patterns.md`**: 기술 계보, `에이전트 = 모델 + 하네스`라는 정의, `Observability`와 보안 경계 논지를 보강합니다.

## 후속 읽기 순서

후속 읽기의 우선순위는 분명합니다. 먼저 OpenAI와 Anthropic의 공식 엔지니어링 포스트, `OpenCode` 문서, `spec-kit`, `LangChain`, `AI FoMO`, `OECD` 자료 같은 1차 문헌을 읽는 편이 가장 빠르고 정확합니다. 그다음에야 현업 실무자의 경험록(`practitioner writing`)과 로컬 마크다운 아카이브를 읽는 편이 좋습니다. 공개 기준선을 먼저 세워 두어야 보조 자료를 읽을 때도 논지가 흔들리지 않습니다.

한국어 생태계에서는 `빌더 조쉬 (Builder Josh)`, `Team Attention`, 일부 `LinkedIn` 스피커들의 계정이 보조 렌즈로 유용합니다. 다만 이 채널들은 핵심 주장 자체의 출발점이라기보다, 해외 1차 문헌과 현업 언어 사이를 잇는 번역 계층으로 읽는 편이 안전합니다.

### 참고 인덱스

`Youngdong2/claude-seminar-references`는 유용한 큐레이션 창고(`curated bibliography`)입니다. 다만 이 저장소 자체를 1차 근거처럼 읽으면 안 됩니다. 이곳은 어디까지나 정리된 **후속 독서 인덱스**에 가깝고, 개별 링크의 생존 여부나 접근 가능성은 계속 달라질 수 있습니다.

그래서 이 외부 저장소는 상위 카탈로그로만 참고하고, 실제 팩트체크와 출처의 `provenance` 정리는 로컬 레퍼런스 문서를 기준으로 삼는 편이 더 안전합니다.

## 로컬 지도

본문의 주장을 다시 검증하거나 확장하고 싶다면, 다음 로컬 지도부터 열어 보면 됩니다.

- 세미나 주장과 source 정리: `../../01-sources/maps/seminar-claims-and-sources.md`
- Claude Code Mastery Playbook 세미나 연결 맵: `../../01-sources/maps/claude-code-mastery-playbook-to-seminar.md`
- Harness Engineering 참고 메모: `../../01-sources/maps/prompt-context-harness-to-seminar.md`
- AI 에이전틱 패턴 진화 세미나 연결 맵: `../../01-sources/maps/evolution-of-ai-agentic-patterns-to-seminar.md`
- 세미나 인물과 기관 프로필: `../../01-sources/provenance/people-and-orgs.md`
- 외부 reference repo 검증 기록: `../../01-sources/provenance/external-repo-audit.md`

핵심은 출처의 층위를 섞지 않는 일입니다. 공개 근거는 공개 근거로, 내부 확인 정보는 내부 맥락으로, 로컬 아카이브는 보조 연결망으로 읽어야 합니다.
