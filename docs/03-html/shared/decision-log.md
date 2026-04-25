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
- CHAPTER 04 feedback round 6: S037의 한 줄 synthesis를 다시 바꾸고, S040은 `신호가 큰 토큰` 같은 설명이 필요한 표현을 제거한다. S041은 parent card/panel과 `card` class가 남지 않는 flat lane 구조로 고친다. S042는 여러 카드 layout으로 바꾸며 출처와 `선택 기준` 문구를 visible copy에서 제거한다. S044는 Manus 사례 quote를 더 이해 쉬운 한국어로 다시 쓴다.
- CHAPTER 04 feedback round 7: S037 한 줄은 `거의 모든 에이전트가 반복하는 4단계.`로 고정한다. S040은 `Anthropic의 4가지 전략: 필요한 정보만 남기고 잡음은 덜어낸다.`로 바꾼다. S041은 좌우 모두 sibling card로 만들되 우측 card 내부에 또 card를 넣지 않고, `Context Hub`를 `Context 7`로 바꾼다. S042는 RAG와 Context 7 차이를 표 형태로 다시 구성한다. S044 출처는 `Manus Research`로 바꾼다.
- CHAPTER 04 feedback round 8: S041은 좌우 sibling card만 card로 보고, 내부 단계/역할/원리/효과는 border/shadow/background 없는 flat typography로 낮춘다. S044 문구는 변경 churn을 멈추기 위해 source-backed KV-cache 문장 `최신 입력과 도구 결과만 뒤에서 갈아 끼워야 KV-cache hit rate가 살아납니다.`로 고정한다.
- Final main integration: 1-4장은 현재 main의 S001-S045를 유지한다. CHAPTER 05 worktree는 S046-S055, CHAPTER 06-07 worktree는 S056-S081, CHAPTER 08-09 worktree는 S082-S094로 재번호화한다. 이 pass는 numbering/registry/generator/validation 통합만 수행하며 각 chapter worktree의 slide copy와 visual structure는 변경하지 않는다.

## 2026-04-23

- CHAPTER 06-07 worktree의 provisional S046-S071 작업물을 main 통합본의 S056-S081로 병합한다. main 브랜치는 이동하지 않고, 현재 main의 94장 registry에 맞춰 slide module number, generated HTML, manifest, outline, deck ordering을 재계산한다.
- 병합 시 source heading drift를 main의 최신 `docs/02-seminar/harness-rebuilt-md` 기준으로 해결한다. S057 title은 `하나의 에이전트 = 하나의 역할`, S067 title은 `멀티 모델과 멀티 에이전트`, S072 title은 `필요없는 도구는 덜어내라`로 둔다.
- CHAPTER 06-07에서 승인된 `assets/claude-code-seminar-kakao/page-062.png`부터 `page-068.png`까지의 structure-only reference와 QA blocker를 main 규칙에 흡수한다. 특히 dark split panel `small` contrast와 artifact/command column clipping은 통합 후에도 blocker로 본다.
- Final main merge는 branch 이동 없이 현재 main checkout에서 수행한다. CHAPTER 05 local `S034`-`S043`은 global `S046`-`S055`로 매핑하고, 최신 feedback round 6 수정은 `S048`, `S049`, `S051`에만 반영한다.
- Chapter-scoped preview artifacts는 flat global deck과 충돌하지 않는 namespaced path로만 병합한다. `ch06`, `ch07`, `chapter-08-09` preview deck/data/slides/source namespace는 보존하되, `docs/03-html/slides/slide-XXX.html`의 provisional 번호 파일로 덮어쓰지 않는다.
- 사용자가 지정한 선호 페이지 `1-18`, `21`, `24`, `37`, `39`, `40`, `52`, `53`을 deck-wide 고정 baseline으로 채택한다. page 해석은 `output/pdf/harness-full-main-94-current-720x405.pdf`의 1-based PDF export 기준으로 고정한다. 이후 피드백 루프에서는 이 묶음을 우선 비교군으로 사용하고, baseline 교체는 사용자 명시 승인 없이는 수행하지 않는다.
- 반복 루프(`html 생성 -> pdf 생성 -> 피드백 -> html 수정 -> html 생성`)에서 footer 우하단 번호 drift를 blocker로 본다. 검증 단계에서 전역 번호의 중복/누락/역순을 매회 확인한다.
- slide source 구현 경로를 chapter folder(`scripts/jaryo_html_deck/slides/chapter_XX/`)로 분리하고, 전체 deck은 기존처럼 한 번의 build로 렌더링한다. 파일 경로 분리와 전역 `spec.order` contiguous 검증을 함께 사용해 번호 충돌을 방지한다.
- 사용자가 선호 baseline을 legacy PDF page로 계속 지칭할 수 있으므로 `docs/03-html/shared/page-number-mapping.md`와 `docs/03-html/shared/page-number-mapping.json`을 추가한다. 삭제된 legacy page는 `19`, `20`이고, 변환 규칙은 `1-18 유지`, `21 이상은 -2`다.
- 선호 baseline remap은 `1-18 -> 1-18`, `21 -> 19`, `24 -> 22`, `37 -> 35`, `39 -> 37`, `40 -> 38`, `52 -> 50`, `53 -> 51`로 고정한다.
- 현재 main 기준 23페이지 `컨텍스트만으로는 부족하다`는 임시 custom layout보다 deck의 기존 `split-compare` family가 더 적합하다고 판단했다. 왼쪽은 `잘못된 결과나 응답 유입`, `느슨한 실행 권한`, `잘못된 검증` 세 축으로 압축하고, 오른쪽은 `허용/차단 범위`, `멈춤 기준`, `검증 경로`를 둔다. 하단 한 줄은 `멈춤 기준과 검증 경로를 먼저 설계해야 한다`로 묶고, body 폭은 chapter 02의 다른 slide와 비슷한 압축 밀도로 줄인다.
- 현재 main 기준 23페이지 latest feedback에서는 더 단순한 관계도가 필요하다고 판단했다. 좌측은 `index.html` 기준 35페이지의 loop diagram만 축소 재사용한 loop panel로 두고, 우측 상단은 `도구 호출 실패`, `목표 망각`, `테스트 오해`, `보안 경계` 네 카드만 남긴다. 중간 레일은 각 card에서 loop 쪽으로 향하는 화살표와 `잘못된 응답 주입` label로 관계를 직접 보여 준다. 하단 dark one-line은 유지한다.

## 2026-04-25

- 사용자가 선호 baseline page를 재확인했다. 기준은 legacy mapping이 아니라 현재 생성본 `output/pdf/harness-full-main-94-current-720x405.pdf`의 1-based PDF page number이며, 선호 page는 `1-18`, `21`, `24`, `37`, `39`, `40`, `52`, `53`이다.
- 같은 현재 PDF 기준 비선호 page는 `41`, `54`, `57-68`이다. 특히 `57-68`은 `assets/claude-code-seminar-kakao/page-062.png`부터 `page-068.png`까지의 구조 감각을 따라갔어야 했던 묶음으로 보고, 재작업 시 이 reference를 우선 비교한다.
- 사용자는 `assets/claude-code-seminar-kakao`를 가장 원하는 slide style reference로 지정했다. 이 reference는 content source가 아니라 구조, 여백, 정보 위계, 도식 밀도, 결론 처리 방식의 기준으로 쓴다.
- Gemini CLI는 primary builder가 아니라 다른 시각의 검토자와 visual reference analyst로 쓰는 데 동의했다. HTML 구현은 Codex CLI 또는 project-local HTML 전용 subagent로 spawn하되, PM, builder, QA, reviewer gate를 유지한다.
- current PDF page number는 사용자 피드백 handle로만 쓴다. `output/pdf/harness-full-main-94-current-720x405.pdf`는 94page이고 현재 manifest/source는 92-slide deck이므로 구현 대상은 title/source match로 확정한다. 확인된 mapping은 `p41 -> S039`, `p54 -> S052`, `p57-p68 -> S055-S066`이다.
- `docs/03-html/shared/current-pdf-disliked-pages-rework-packet.md`를 PM packet으로 추가했다. 이 packet은 `Advisor`가 target-map에서 제외된 source에 기대고, `Parallel`/`멀티 모델`도 최신 prose 위치와 충돌 가능성이 있으므로 visual rebuild 전에 source-alignment gate를 먼저 통과해야 한다고 정리한다.
- Codex CLI는 현재 `codex-cli 0.125.0`, Gemini CLI는 현재 `0.39.1`로 확인했다. 사용자는 HTML 작업 agent에 Codex CLI와 Gemini CLI 사용을 허용했고, 우선 model을 `gpt-5.5`, `gpt-5.4`, `gpt-5.3-codex`, `gemini-3.1-pro-preview`, `gemini-3.1-flash-preview`로 지정했다. 정확한 model명이 거부되면 가장 가까운 같은 계열 model로 fallback하고 handoff에 `requested model`, `actual model`, `command`, `fallback reason`을 남긴다.
- 현재 세션은 rules/planning 세션으로 고정한다. 따라서 HTML 생성, PDF export, generated HTML 수정, slide source 수정, CSS/generator/test 수정, build/check 실행은 하지 않는다. orchestrator rules-edit mode에서는 규칙 문서, decision log, PM packet, open question/handoff 정리만 허용하고, CLI/subagent reviewer를 read-only review mode로 띄운 경우에는 그 reviewer가 파일을 수정하지 않는다.
- 역할별 reasoning effort는 PM/reviewer/final source-alignment high 또는 xhigh, builder high, QA high, quick visual sanity/단순 목록화 medium 이하로 둔다. CLI가 reasoning flag를 직접 지원하지 않으면 prompt에 검토 깊이와 reasoning budget을 명시한다.
- Codex/Gemini read-only rules review 결과에 따라 `rules-edit mode`와 `read-only review mode`를 분리하고, model fallback handoff fields를 `requested model`, `actual model`, `command`, `fallback reason`으로 통일했다. Gemini 검토는 보조 의견이며 PM/QA/reviewer gate를 대체하거나 다음 gate로 자동 진행시키지 않는다.
