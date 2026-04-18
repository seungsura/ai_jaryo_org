# 부록: 출처와 후속 읽기

이 부록은 본문 01~09를 반복 요약하지 않고, 문서의 근거를 `public source`, `카카오 AI 팀` 내부 확인 정보, 로컬 markdown archive의 supplemental source로 나눠 짧게 안내한다. 목적은 독자가 무엇을 어디까지 믿고, 어디서부터 더 읽을지를 빠르게 판단하게 하는 데 있다.

## 본문을 지탱한 근거의 층위

공개 source는 본문의 기준선을 잡는다. Section 1은 `YC W25`와 `Jared Friedman` 관련 공개 기사와 profile을 통해 변화의 방향을 확인하고, Section 2는 OpenAI와 Anthropic의 공식 engineering/product 글, 그리고 `OpenCode` 공식 docs를 통해 최근 coding tool이 `Harness` 중심 구조로 수렴하고 있다는 점을 보강한다. Section 3은 `GitHub spec-kit`으로 `spec-first` command를 고정하고, Section 4부터 Section 7까지는 `LangChain`, OpenAI, Anthropic, `Drew Breunig`, `Chroma` 같은 source를 통해 `Harness`, long context, 검증, 운영 구조를 뒷받침한다. Section 9는 `AI FoMO` 논문, `OECD`, `TTimes` 기사로 불안과 역할 재배치의 바깥 근거를 확보한다.

그보다 강한 체감 수치와 일부 인명 정보는 외부 benchmark처럼 올리지 않고 `카카오 AI 팀` 내부 확인 범위에만 남겼다. Section 2의 생산성 사례와 Section 8의 이름 표기 처리, 그리고 `김영동`, `이재영`, `Youngdong2` 관련 설명은 이 범주에 속한다.

로컬 markdown archive는 공개 증거를 대체하지 않고, 이미 공개 source로 세운 기준선을 보강하는 supplemental source로만 사용됐다. `prompt-context-harness-1-15.md`는 `Prompt → Context → Harness` 전환과 하네스 관점을 보강하고, `claude-code-mastery-playbook.md`는 `agent loop`, 검증, `Multi-Agent` 운영 감각을 보강한다. `evolution-of-ai-agentic-patterns.md`는 `GitHub Copilot` 이후 tool genealogy와 `Harness` 수렴 서사를 보강하는 핵심 supplemental source다. `claude-code-seminar-kakao.md`는 전체 narrative spine과 Section 8의 제작 사례를 지탱하는 base seminar source로 유지한다.

## 후속 읽기의 순서

본문 뒤에서 더 읽고 싶다면 먼저 OpenAI와 Anthropic의 공식 engineering/product 글, `OpenCode` 공식 docs, `spec-kit`, `LangChain`, `AI FoMO`, `OECD`처럼 본문의 기준선을 직접 만든 source부터 보는 편이 안전하다. 그다음에 practitioner writing과 로컬 markdown archive를 붙이면 논지의 실무 맥락을 더 따라가기 쉽다.

한국어권에서는 `빌더 조쉬 (Builder Josh)`, `Team Attention`, 일부 `LinkedIn` 계정 같은 경로를 보조 참고선으로 둘 수 있다. 다만 이 층은 본문 핵심 claim의 primary evidence가 아니라, 해외 담론이 국내 실무 언어로 번역되는 흐름을 따라가는 보조 경로에 가깝다.

## 외부 reference repo의 위치

`Youngdong2/claude-seminar-references`는 공개적으로 존재하는 curated bibliography이며, 이 발표 전체의 직접 근거 저장소라기보다 후속 reading index에 가깝다. 검증 기록상 다수 링크는 살아 있었지만 일부는 깨져 있거나 플랫폼 차단 때문에 자동 확인이 어려웠다. 따라서 이 저장소는 상위 카탈로그로만 참조하고, 실제 claim boundary와 provenance 관리는 로컬 reference 문서에서 유지하는 편이 더 안전하다.

더 자세한 출처 경계와 인물 설명은 [세미나 주장과 source 정리](../../01-sources/maps/seminar-claims-and-sources.md), [세미나 인물과 기관 프로필](../../01-sources/provenance/people-and-orgs.md), [외부 reference repo 검증 기록](../../01-sources/provenance/external-repo-audit.md)에서 따로 관리한다. 이 부록의 역할은 본문 뒤에서 독자가 “무엇을 어디까지 믿고, 어디서부터 더 읽을지”를 판단하게 하는 짧은 provenance note로 충분하다.
