# 부록: 출처와 후속 읽기를 위한 가이드

## 시작하며: 무엇을 어디까지 믿고, 어디서부터 전진할 것인가

이 부록은 본문을 다시 요약하는 곳이 아닙니다. 이 글이 어디에 기대어 서 있는지, 그리고 후속 읽기를 어디서부터 이어가야 하는지를 가르는 곳입니다. 공개 근거, 내부 확인 정보, 로컬 markdown archive를 한 덩어리로 읽기 시작하면 본문도 쉽게 흐려집니다. 무엇을 먼저 믿고, 무엇을 제한적으로 참고하고, 무엇을 연결 메모로만 써야 하는지 선부터 그어야 합니다.

핵심은 출처의 양이 아니라 자리를 섞지 않는 일입니다. 이 선이 분명해야 공개 근거와 내부 사정과 로컬 메모가 서로의 자리를 넘보지 않습니다.

## 근거의 세 층위

가장 바깥 기준선은 **공개 출처(Public Source)**입니다. 코딩 패러다임 변화의 속도는 `YC W25`와 `Jared Friedman`의 공개 기사로 붙들고, 최근 도구들이 왜 `Harness` 중심 구조로 수렴하는지는 OpenAI와 Anthropic의 공식 엔지니어링 글, 그리고 `OpenCode` 공식 문서로 설명합니다. 스펙 중심 방법론은 `GitHub spec-kit`이, 런타임 제어와 실전 운영은 `LangChain`, OpenAI, Anthropic, `Drew Breunig`, `Chroma` 등 관련 자료가 받칩니다. 불안과 역할 재배치 논지는 `AI FoMO` 논문, `OECD` 리포트, `TTimes` 기사로 보강합니다. 본문에서 혼자 서야 하는 주장들은 먼저 여기서 버텨야 합니다.

그 다음 층은 **내부 확인 정보**입니다. 본문 일부의 생산성 체감치나 제작 맥락은 이 층에서만 확인되며, 공개 링크로 완전히 바뀌지 않습니다. 그래서 이 층은 공개 1차 근거와 같은 무게로 읽지 않습니다. 공개 출처 위에 제한적으로 덧대는 정보로만 다룹니다. 내부 확인 정보가 앞줄로 나오기 시작하면, 글은 설명이 아니라 내부 사정의 요약으로 기웁니다.

마지막 층은 **로컬 markdown archive**입니다. 이 자료들은 독립 1차 근거라기보다, 공개 출처와 내부 확인 정보를 본문 문장으로 연결해 주는 보조 재료입니다. `prompt-context-harness-1-15.md`는 하네스로의 전환과 5대 기능 블록을, `claude-code-mastery-playbook.md`는 에이전트 루프와 검증 감각을, `evolution-of-ai-agentic-patterns.md`는 진화 서사를, `claude-code-seminar-kakao.md`는 전체 세미나 흐름을 두껍게 만듭니다. 이 archive는 본문을 혼자 떠받치는 층이 아니라, 이미 잡아 둔 근거를 더 촘촘히 이어 주는 층입니다.

## 로컬 source-to-section map

로컬 markdown은 전부 같은 무게로 쓰이지 않습니다. 어떤 파일이 어느 주장과 예시를 떠받치는지 구분해 읽어야 합니다.

- **`claude-code-seminar-kakao.md`**: 에이전트 루프, `Plan-Critic-Build` 구조, `Git worktree` workflow, 제작 과정을 떠받치는 기준 스크립트입니다.
- **`claude-code-mastery-playbook.md`**: 실행 레이어, `Calibrated Trust`, `Subagent` 출력 계약, `4D` 책임론을 보강합니다.
- **`prompt-context-harness-1-15.md`**: `Prompt → Context → Harness` 전환, 5대 기능 블록, tool curation, 상태의 외부 기록, `Build to Delete` 철학을 떠받칩니다.
- **`evolution-of-ai-agentic-patterns.md`**: 기술 계보, `에이전트 = 모델 + 하네스`라는 정의, `Observability`, 보안 경계 논지를 보강합니다.

이 구분이 중요한 이유는 단순합니다. 로컬 archive는 본문을 더 풍성하게 만들 수 있지만, 공개 근거의 자리를 대신할 수는 없습니다. 어떤 문장을 어디까지 끌어올릴 수 있는지는 그 자료가 어느 줄에 서 있는지에 따라 달라집니다.

## 후속 읽기 순서

후속 읽기의 순서도 분명합니다. 먼저 OpenAI와 Anthropic의 공식 엔지니어링 포스트, `OpenCode` 문서, `spec-kit`, `LangChain`, `AI FoMO`, `OECD` 자료 같은 1차 문헌을 읽는 편이 가장 빠르고 안전합니다. 그다음에야 practitioner writing과 로컬 markdown archive를 읽는 편이 좋습니다. 기준선을 먼저 세워 두어야, 뒤에서 만나는 해설과 메모가 앞자리를 차지하지 못합니다.

한국어 생태계에서는 `빌더 조쉬 (Builder Josh)`, `Team Attention`, 일부 `LinkedIn` 스피커들의 계정이 보조 렌즈로 유용합니다. 다만 이 채널들은 핵심 주장 자체의 출발점이 아니라, 해외 1차 문헌과 현업 언어 사이를 이어 주는 해설 층으로 읽는 편이 안전합니다. 해설은 유용하지만, 해설이 먼저 앞에 서면 기준이 뒤집힙니다.

## 외부 reference repo를 다루는 법

`Youngdong2/claude-seminar-references`는 유용한 큐레이션 창고입니다. 다만 이 저장소 자체를 1차 근거처럼 읽으면 안 됩니다. 이곳은 어디까지나 정리된 **후속 독서 인덱스**에 가깝습니다. 개별 링크의 생존 여부는 계속 달라질 수 있고, 잘 정리된 목록이라고 해서 개별 출처의 신뢰도까지 한꺼번에 보증되지는 않습니다.

그래서 이 외부 저장소는 길잡이 정도로만 참고하고, 실제 팩트체크와 출처 정리는 로컬 레퍼런스 문서를 기준으로 삼는 편이 더 안전합니다. 인덱스는 빠른 길을 알려 주지만, 끝까지 대신 읽어 주지는 않습니다.

`make-slide`도 비슷하게 다뤄야 합니다. 다만 역할은 다릅니다. 이 저장소에서 `make-slide`는 factual source가 아니라 HTML stage의 design/process reference입니다. 그래서 `minimal-light` theme와 shell reuse 원리, 최종 deck runtime만 선별해서 읽고, 본문의 주장과 wording 기준은 계속 local canonical prose에 둡니다.

## 다시 열어볼 로컬 지도

본문의 주장을 다시 검증하거나 확장하고 싶다면, 다음 로컬 지도부터 열어 보면 됩니다.

- 세미나 주장과 source 정리: `../../01-sources/maps/seminar-claims-and-sources.md`
- Claude Code Mastery Playbook 세미나 연결 맵: `../../01-sources/maps/claude-code-mastery-playbook-to-seminar.md`
- Harness Engineering 참고 메모: `../../01-sources/maps/prompt-context-harness-to-seminar.md`
- AI 에이전틱 패턴 진화 세미나 연결 맵: `../../01-sources/maps/evolution-of-ai-agentic-patterns-to-seminar.md`
- 세미나 인물과 기관 프로필: `../../01-sources/provenance/people-and-orgs.md`
- 외부 reference repo 검증 기록: `../../01-sources/provenance/external-repo-audit.md`

이 지도들은 본문을 다시 쓰기 위한 새로운 세계관이 아닙니다. 이미 쓴 문장이 어떤 근거와 어떤 보조 연결망 위에 놓였는지를 다시 확인하는 도구입니다. 공개 근거는 공개 근거로, 내부 확인 정보는 내부 맥락으로, 로컬 archive는 보조 연결망으로 읽어야 합니다. 이 선을 흐리지 않는 것이 결국 가장 중요합니다.
