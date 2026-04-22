# HTML Slide Decision Log

이 문서는 `docs/03-html/shared/slide-quality-rules.md`의 `Decision Log`를 보완하는 append-only future decision log다. 이 파일은 preserved Decision Log를 대체하지 않는다. 최상위 authority와 active rule은 항상 `slide-quality-rules.md`에 먼저 기록한다.

## 2026-04-22

- Approved HTML Slide Rules 재정비 계획 v5를 기준으로 `slide-quality-rules.md`를 top-level HTML slide authority로 재구성하기로 결정했다.
- 최상위 구조는 `Authority`, `Workflow Gate`, `Source Discipline`, `Copy/Tone`, `Design Direction`, `Visual Reference Baseline`, `Reference Analysis Protocol`, `Layout Grammar`, `Reusable Patterns`, `Implementation Contract`, `Validation Contract`, `Decision Log`, `Traceability` 순서로 고정했다.
- 기존 `slide-quality-rules.md`의 Decision Log entries는 문서 안에 verbatim 또는 nearly verbatim으로 보존하고, 외부 파일로 이동하거나 요약하지 않기로 결정했다.
- `Deprecated/Replaced Rules`는 active rules가 아니라 `Traceability` history로 둔다.
- slide-number-specific active rules는 가능한 reusable meaning/design patterns로 일반화하고, S001-S027의 fixed values는 `Traceability`에 보존한다.
- Visual Reference Baseline은 `output/pdf/harness-00-01-current-720x405.pdf`, `assets/claude-code-seminar-kakao/page-028.png`, `assets/claude-code-seminar-kakao/page-032.png`, `assets/claude-code-seminar-kakao/page-037.png`, `assets/claude-code-seminar-kakao/page-053.png`, `assets/claude-code-seminar-kakao/page-064.png`, `assets/claude-code-seminar-kakao/page-067.png`로 둔다.
- Visual Reference Baseline은 composition/layout/diagram soft reference only이며 content source가 아니다.
- warm brown palette, section pill, character images 복사를 금지하고, `theme-minimal-light` blue/neutral palette를 유지한다.
- 이번 작업은 rules-document core only로 제한한다. HTML/CSS/generator/tests/generated slides/deck/PDF는 수정하지 않고, `check_slide_*` 같은 HTML 검증도 실행하지 않는다.
- page-specific reference analysis를 `slide-quality-rules.md`에 반영했다. page-028, page-032, page-037, page-053, page-064, page-067은 structure-only soft guidelines로 쓰며, content source나 palette/character/image copying 근거로 쓰지 않는다.
- docs-only HTML rules maintenance pass에서 현재 source root를 `docs/02-seminar/harness-rebuilt-md`로 재확인하고, shared design 계열 문서를 active `theme-minimal-light`와 manifest/generator의 7개 shell 기준으로 압축하기로 결정했다.
- slide copy에서 번역체와 어색한 한국어 표현을 구현 금지 대상으로 승격하고, `check_slide_korean.py`와 reviewer 판단을 함께 통과해야 하는 검증 항목으로 둔다.
- 한국문학적 어휘는 허용하되, source 의미를 선명하게 압축하고 발표 리듬을 살리는 경우로 제한한다. 과한 문예체, 감상적 수사, source 밖 은유는 금지한다.
- 사용자가 피드백은 항상 문서에 기록하고 규칙 적용 가능성을 검토해야 한다고 재확인했다. 이 원칙은 `slide-quality-rules.md`의 deck-wide Workflow Gate로 승격하며, 모든 피드백을 rule-candidate로 분류한다.
- S031은 `Red`/`Green`/`Refactor` 카드에 source-backed 설명을 넣고 title case를 일관되게 맞춘다. 큰 `AI 시대의 TDD는 권한 통제 기법` statement card는 제거한다. 원문 밖 문장 창작 금지는 deck-wide source rule로 다시 강화한다. S033은 중앙 thesis, 두 카드, 하단 결론이 footer safe area 안에서 균형 있게 정렬되도록 수정한다.
- 병렬 worktree에서 전역 slide number는 임시값으로 취급한다. chapter별 작업 폴더 아래에서 local slide order와 임시 번호를 관리하고, 마지막 main 통합에서 모든 작업 브랜치를 병합한 뒤 numbering-only pass로 `SXXX`/`slide-XXX` 번호만 재계산하기로 결정했다. 이 pass에서는 content/layout 의미를 함께 바꾸지 않는다.
- S031은 카드 크기와 글자 크기 hierarchy를 다시 맞춘다. S032는 source 밖 추상 비교 축과 번역투 어휘를 제거하고 원문에 존재하는 표현만 visible copy로 둔다. S033은 `하네스`를 TDD 카드 항목으로 넣지 않고, source-backed 결론/synthesis 레벨에만 둔다.
- S032 reviewer follow-up: row key `문서`, `검증`, `작동 원리`도 추상 label layer로 읽히므로 source 51-55행에서 압축한 `앞단의 문서`, `검증은`, `실제 작동 원리`로 좁힌다. `검증 루프`도 source 밖 조합 label로 보일 수 있으므로 금지한다. 뒤의 별도 SDD/TDD 표 label인 `인간의 역할`, `검증 방식`, `프로덕션 적합도`는 S032에 쓰지 않는다.
- S031은 사용자가 명시한 `assets/claude-code-seminar-kakao/page-028.png`와 canonical Page 028 transcription을 TDD reference로 삼는다. S032는 사용자의 인터넷 검색 지시에 따라 Royce 1970 paper와 GitHub Spec Kit official docs를 보조 source로 삼아 Waterfall/SDD 차이를 다시 정리한다. S033은 source-backed 소제목을 visible하게 둔다.
- S030은 `assets/claude-code-seminar-kakao/page-031.png`를 reference로 삼고, 출처에 `GitHub Copilot icon`과 `GitHub spec-kit`을 명시한다. S032는 SDD header와 row content column을 정렬하고 bottom one-line synthesis를 제거한다. S033은 blue title을 쓰지 않고 중앙 `Spec + TDD` thesis를 제거하며, `assets/claude-code-seminar-kakao/page-033.png`를 참고해 card size와 내부 글자 크기를 재조정한다.
- S033은 copy와 구조를 유지한 채 card size만 한 단계 줄인다. 정보량이 작은 두 카드가 slide 폭을 과하게 점유하지 않도록 조정하되, plus sign과 bottom synthesis의 중심 정렬은 유지한다.
- CHAPTER 04 handoff는 `docs/03-html/chapters/chapter-04/README.md`에 둔다. 현재 `S034`-`S045`는 provisional range이며, final integration에서 다른 contiguous range로 바뀔 수 있다.
- CHAPTER 04 feedback round 2를 blocker로 기록했다. S034의 알약 keyword 렌더링, S037 중앙 카드 overflow, S039 조잡한 도구 mapping, S044 약한 비교 table은 재렌더링 대상이다. S038은 더 나은 source-backed 한 줄 문장을 고르고, S043의 한 줄 claim은 아래로 내린다.
- CHAPTER 04 lock feedback을 반영한다. S039 하단 synthesis는 `도구 이름보다 그 도구가 맡는 책임` 대신 `책임과 도구는 1:1이 아니다`로 고정한다. S040 하단 한 줄은 Anthropic의 context engineering 문장으로 대체하고, 출처 표기는 `Anthropic Research`로 둔다.
- CHAPTER 04 feedback round 3: S037의 한 줄 문장은 원문 대조 결과 verbatim이 아니므로 source-backed 표현으로 교체한다. S036은 quote와 attribution을 table callout보다 강하게 보이게 하고, S040의 Anthropic phrase는 과대 slogan이 아니라 quote/source typography로 낮춘다. S041은 네 단계 process list가 아니라 MCP/Context Hub native architecture layout으로 다시 만든다.
- CHAPTER 04 feedback round 4: S036은 quote card와 compact component cards의 균형으로 재배치한다. S038은 한 문장 thesis card를 제거한다. S040은 S036과 같은 dedicated quote card rule을 따른다. S041은 좌측 MCP 사용 구조, 우측 Context Hub MCP 역할/원리 설명으로 재구성한다. S039의 `하네스의 책임 ↔ 하네스의 도구` label은 제거한다. S042는 인터넷 조사 근거로 RAG 논문, MCP 공식 문서, Context Hub/Context7 문서 기반 비교로 교체한다.
- CHAPTER 04 feedback round 5: S036과 S043은 본문 그룹을 화면 중앙으로 재정렬한다. S040의 Anthropic 문장은 자연스러운 한국어 quote로 번역한다. S041은 nested card 금지 규칙을 contract에 추가하고 flat architecture/explanation 구조로 고친다. S042는 인터넷 조사 근거를 유지하되 번역투 문장을 제거한다. S044는 Manus 사례 문장을 source quote card로 교체한다.
