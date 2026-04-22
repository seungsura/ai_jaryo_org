# HTML Slide Quality Rules

이 문서는 `docs/03-html/` 전체의 최상위 HTML slide authority다. outline, manifest, generator output, shared CSS/tokens, deck HTML, screenshot QA, PDF export QA에 모두 적용한다.

## Authority

- 사용자와 대화하며 확정한 이 문서의 규칙은 `docs/03-html/README.md`, `docs/03-html/shared/README.md`, shared design 문서, layout 문서, generator 기존 구현보다 우선한다.
- HTML은 canonical source가 아니다. slide 문구와 시각 구조의 의미 단위는 source markdown 또는 사용자가 명시한 reference에서만 가져온다.
- `Kuneosu/make-slide`의 outline-first, theme/layout 분리, shell reuse, standalone deck, keyboard/touch navigation, print/PDF 친화 구조를 우선 적용한다.
- 충돌 해결 순서: 사용자와 대화하며 확정한 최신 규칙 -> 이 문서 -> `make-slide` 적용 문서 -> 기존 design/layout 문서 -> generator 기존 구현.
- 이 문서만 정리하는 rules-document 작업에서는 HTML, CSS, renderer, tests, generated HTML, deck, PDF를 수정하지 않는다.

## Workflow Gate

- 모든 HTML 관련 작업 전 `AGENTS.md`, `.codex/subagents/README.md`, `.codex/templates/subagent-task-template.md`, 이 문서 전체, 현재 작업 대상 slide의 source/reference를 읽는다.
- HTML 관련 작업은 subagent 위임 기반으로 진행한다. orchestrator는 규칙 확정, prompt 구성, 결과 검수, 후속 지시를 맡는다.
- HTML 작업 subagent prompt에는 이 문서 사전 확인, 최신 피드백 기록, source/reference 밖 생성 금지, 필요한 검증 명령을 명시한다.
- 새 사용자 피드백은 구현 전에 먼저 이 문서에 기록한다. 기록 위치는 active rule, reusable pattern, Decision Log, Traceability 중 가장 강제력이 높은 곳이다.
- 최신 피드백을 규칙으로 승격하지 않은 상태에서 generator, CSS, renderer, tests, generated HTML, PDF를 수정하지 않는다.
- 일반 구현 순서: 규칙 기록 -> subagent 위임 -> generator/CSS/test/check 갱신 -> HTML/PDF 재생성 -> 정적 검증 -> Playwright screenshot/PDF smoke 검증.

## Source Discipline

- local markdown과 사용자가 명시한 reference만 의미 source로 쓴다. source/reference 밖 비교 축, label, 의미, 예시, metric, 해설 문구를 만들지 않는다.
- 사용자가 지정하지 않은 `assets/`, JPG, PNG, PDF는 content source로 보지 않는다. Visual Reference Baseline의 항목도 composition/layout/diagram soft reference일 뿐 content source가 아니다.
- source markdown의 최신 문구가 stale generated phrasing보다 우선한다. 사용자가 페이지를 부정확하게 지칭해도 source markdown의 최신 문장을 따른다.
- source 의미 보존 압축은 허용한다. source에 없는 해설축, 반복 설명, 분류 label, 보조 label, metric 재해석은 금지한다.
- code syntax는 원문을 보존한다. source code block 내부 주석은 slide 표시에서 제거하고, slide를 위해 새 주석을 추가하지 않는다.
- 예시 code block은 축약하지 않는다. source-visible 전체 예시 내용이 보여야 한다.

## Copy/Tone

- 문구는 한국어를 기본으로 쓰되, English terms/path/name, technical vocabulary, product name, API name, command는 그대로 둔다.
- slide 문구는 명사형 또는 구 단위 중심이다. 공손체, 서술형, 명령형을 피한다.
- 번역체와 어색한 한국어 표현은 구현 금지다. source 의미를 보존하더라도 한국어 리듬이 어색하면 REVISE 대상이다.
- 금지 후보: `상류/하류`, `강하게 호출된다`, `핵심은 ~ 데 있다`, `~의 측면에서`, `~라고 볼 수 있다`, 보고서식 연결어를 붙인 장문 설명.
- 한국문학적 어휘는 허용한다. 단, source 의미를 선명하게 압축하고 발표 리듬을 살릴 때만 쓰며, 과한 문예체, 감상적 수사, source 밖 은유는 금지한다.
- 한국어 표현 검증은 `scripts/check_slide_korean.py`와 reviewer 판단을 함께 통과해야 한다. 자동 검사가 통과해도 어색한 한국어가 보이면 실패다.
- slide title, lead, body copy는 압축 문구를 우선한다. 필요한 경우에도 source line으로 추적 가능해야 한다.
- 제목 아래 subtitle/lead는 기본 금지다. 필요한 경우에만 예외로 둔다.
- 제목은 한 줄 고정이다. 2줄 예상 시 생성 중단 후 사용자 확인. 긴 source heading은 핵심 source phrase만 title에 두고 날짜/부가절은 body metadata로 이동한다.
- 부정적 의견 quote는 짧은 구 단위 문구로 유지한다.

## Design Direction

- theme class는 `theme-minimal-light`를 유지한다.
- palette는 minimal-light 기준을 유지한다: background `#fafafa`, surface `#ffffff`, border `#e0e0e0`, primary `#1a1a1a`, secondary `#555555`, tertiary `#444444`, accent `#0066cc`, highlight `#0a84ff`, code background `#f5f5f5`.
- warm brown palette, copper/brown accent, ivory/paper/beige 계열 token, section pill, character images 복사를 금지한다.
- slide 규격은 `720pt × 405pt`, font는 Pretendard CDN, footer는 좌하단 `Harness 잘 사용하기`, 우하단 page number다.
- deck 화면에는 footer 외의 visible UI chrome, slide counter UI, progress bar, keyboard hint, demo chrome, fullscreen/notes popup UI를 두지 않는다.
- 첫 장 전용 tool mark는 우상단 실제 asset icon만 사용한다: `assets/icons/claude_code_icon.svg`, `assets/icons/codex_icon.png`, `assets/icons/opencode_icon.png`.
- 일반 슬라이드 tool mark, text pill 형태 tool 표기, 일반 본문 slide의 pill chip은 금지한다.

## Visual Reference Baseline

- soft reference baseline은 다음 항목이다: `output/pdf/harness-00-01-current-720x405.pdf`, `assets/claude-code-seminar-kakao/page-028.png`, `assets/claude-code-seminar-kakao/page-032.png`, `assets/claude-code-seminar-kakao/page-037.png`, `assets/claude-code-seminar-kakao/page-053.png`, `assets/claude-code-seminar-kakao/page-064.png`, `assets/claude-code-seminar-kakao/page-067.png`.
- CHAPTER 02 rebuild에서 사용자가 추가 승인한 reference는 `output/pdf/harness-00-02-current-720x405.pdf`의 S016-S018, `assets/evolution-of-ai-agentic-patterns/02-chain-of-thought.png`부터 `06-cursor-ai-code-editor-architecture.png`, `assets/claude-code-seminar-kakao/page-052.png`, `assets/claude-code-seminar-kakao/page-067.png`이다.
- 이 baseline은 composition, layout rhythm, diagram density, spatial hierarchy의 soft reference다.
- 이 baseline은 content source가 아니다. 문구, 비교 축, label, metric, 사례, 해설 의미를 여기서 새로 가져오지 않는다.
- baseline의 warm brown palette, section pill, character image, decorative mood를 복사하지 않는다.
- baseline을 참고하더라도 `theme-minimal-light` blue/neutral palette와 Jaryo deck constants를 유지한다.

## Reference Analysis Protocol

- reference를 볼 수 있는 작업에서는 먼저 reference의 목적을 한 줄로 적는다: composition, layout, diagram, spacing 중 무엇을 참고하는지 명시한다.
- reference에서 추출할 수 있는 것은 구조적 관계뿐이다. content claim, label, metric, 예시는 source markdown 또는 사용자 지정 text에 있을 때만 쓴다.
- reference가 source markdown과 충돌하면 source markdown과 이 문서가 우선한다.
- reference를 raw crop, raw screenshot, character image 복사로 쓰지 않는다. 필요한 경우 native diagram/card/table 구조로 재작성한다.
- reference 분석 결과는 가능한 reusable pattern으로 승격하고, slide-number-specific active rule로 남기지 않는다.
- approved v5 page-specific reference analysis는 hard template가 아니라 soft guideline이다. 각 page는 구조 감각만 참고하고, content claim, label, metric, 예시, warm brown palette, section pill, character image는 가져오지 않는다.
- page-028: main process + rationale card + bottom takeaway 구조를 참고한다.
- page-032: axis rows + column headers + final synthesis 구조를 참고한다.
- page-037: quote/counter-claim + taxonomy cards + caution takeaway 구조를 참고한다.
- page-053: dominant native diagram + outcome cards 구조를 참고한다.
- page-064: card row + mini diagram + 1-line meaning 구조를 참고한다.
- page-067: dominant system map + side explanation + bottom conclusion 구조를 참고한다.

## Layout Grammar

- 채택 layout/type: title, agenda, section, statement, split comparison, process, evidence table, visual card, closing question.
- 카드 규칙: nested card 금지, slide당 핵심 카드 1~3개, radius 8px 이하. reference가 4-card grid를 요구하는 경우에만 slide당 4개 card를 허용한다.
- tool card/identity card는 actual icon asset을 우선하고 generic document/file glyph를 금지한다.
- 강조 3단계는 theme accent, bold/ink, muted metadata다.
- 전체 목차 한 장 구성: compact agenda, subtitle 제거, full-page list/table 느낌의 균형 잡힌 가로 사용, footer safe margin 확보.
- 챕터 전환은 dark divider로 일반 content page와 분리한다. 요약/전환 content page에는 chapter divider shell을 쓰지 않는다.
- 핵심 한 마디와 negative quote는 중앙 정렬한다.
- split comparison slide는 좌우 블록 사이 theme accent arrow를 둔다.
- document reference card는 반복 설명 문구 없이 product/file identity만 표기한다.
- role/capability slide는 작은 카드 다발보다 한 줄 핵심 요약과 2축 이상의 구조화 layout을 우선한다.
- final question slide는 source heading을 title로 유지하고 source quote를 centered summary로 배치한다.
- code panel은 source/reference가 dark panel을 명시하지 않는 한 light code panel이다. renderer가 만든 leading/trailing artificial blank line, snippet clipping, `overflow:hidden`으로 인한 코드 잘림은 실패다.
- dark quote block은 white text 대비를 확보한다.
- CHAPTER 02 body typography는 CHAPTER 01 본문 크기 수준으로 제한한다. 큰 카드 제목, 본문, center claim, data-table text의 과대 확대를 금지한다.

## Reusable Patterns

- centered single-message prompt/claim page: 한 장에 하나의 자연어 메시지만 남기고, 카드 좌측 상단에는 source 성격 label만 둔다.
- evidence cards without tables: 숫자와 사실만 카드로 압축하고, 해설 열이나 표는 쓰지 않는다.
- role transition flow with right-side analogy: 왼쪽에는 위에서 아래로 이어지는 역할 이동 흐름, 오른쪽에는 비유 블록을 둔다.
- dark quote + factual cards for closing: 어두운 quote 블록 하나와 그 아래 흰 surface + neutral border 사실 카드 두 개로 끝낸다.
- metric card trio: 큰 숫자 / 짧은 label / 보조 문구 / 출처 meta 계층으로 분리하고, metric value는 카드 상단에 둔다.
- example-first native diagram: pattern, architecture, workflow 설명은 이름/정의 나열보다 source-backed 예시와 관계를 보이는 native diagram으로 구성한다.
- loop visual: 네 단계 사이 명시적 arrow로 순환을 보인다. dashed repeat label 또는 `↺ repeat`를 쓰지 않는다.
- tier hierarchy: 좌측 tier label과 계층 row 구조를 유지한다.
- inclusion relationship: 포함관계는 텍스트 관계식으로 노출한다. nested box 그림을 기본값으로 쓰지 않는다.
- reference-derived soft patterns: `main process + rationale card + bottom takeaway`, `axis rows + column headers + final synthesis`, `quote/counter-claim + taxonomy cards + caution takeaway`, `dominant native diagram + outcome cards`, `card row + mini diagram + 1-line meaning`, `dominant system map + side explanation + bottom conclusion`를 후보 grammar로 둔다.
- reference-derived soft patterns는 source-backed content를 배치하는 구조 후보일 뿐이다. source에 없는 문구, 비교 축, label, metric, 해설을 채우는 근거로 쓰지 않는다.
- future source-backed slides는 위 패턴을 먼저 검토하고, source-backed label과 copy만 바꾼다.
- CHAPTER 02 pattern/architecture slides는 approved evolution assets 02-06을 raw image로 붙이지 않고 native diagram으로 재작성한다. `assets/claude-code-seminar-kakao/page-052.png`와 `page-067.png`는 큰 제목, 여백, native diagram, 요약 card 배치의 structure-only reference로만 쓴다.
- CHAPTER 02 S016-S018 기존 화면은 재사용하되 중앙 claim/card typography를 CHAPTER 01 수준으로 낮추고, 카드 내부 줄간격과 footer safe margin을 다시 검증한다.
- CHAPTER 02 rebuild에서는 standalone `Agent = Model + Harness` statement page를 두지 않는다. 이 공식은 S027의 `Prompt ⊂ Context ⊂ Harness` 결론 page 안에서 함께 보여준다.

## Implementation Contract

- deck 구조는 `docs/02-seminar/harness-rebuilt-md` source markdown과 승인된 outline을 따라야 한다.
- 섹션마다 최소 1장을 둔다. 큰 섹션은 최대 5장까지 허용한다.
- 패턴, 도표, architecture 설명은 시각 요소를 필수로 둔다.
- 같은 인접 주제라도 같은 shell 반복을 금지 검토한다.
- source-sync slide는 source markdown과 generated copy의 drift를 확인한다.
- generated slide HTML과 `deck/index.html`은 artifact다. 실제 slide 구현 단위는 `scripts/jaryo_html_deck/slides/slide_XXX.py`다.
- HTML deck generator는 얇은 entrypoint와 `scripts/jaryo_html_deck/slides/slide_XXX.py` slide module 구조를 유지하고, 공용 렌더링/파일 출력은 slide module에 두지 않는다.
- 실패한 review 결과는 실패 slide id와 수정 범위만 다음 작업자에게 전달한다.

## Validation Contract

- HTML 수정 후에는 작업 범위에 맞게 `check_slide_contract`, `check_slide_korean`, `check_deck_runtime`, 필요한 Playwright screenshot, 필요한 PDF smoke를 이 문서 기준으로 통과시킨다.
- rules-document core only 작업에서는 HTML 검증을 실행하지 않는다. markdown/file scope 검증만 수행한다.
- 규칙 문구가 바뀌면 테스트/contract/visual check 중 하나 이상으로 고정한다. 단, rules-document only 작업에서는 구조 검증과 범위 검증으로 제한한다.
- 구조 검증은 통과해도 label 위치, 카드 내부/외부, font scale, footer와 본문 겹침, dark quote 대비 같은 visual rule은 screenshot review 없이는 놓칠 수 있다.
- nested-card 위험은 contract 단계에서 탐지해야 한다. 렌더 결과만 믿고 넘기지 않는다.
- 전체 deck 검증 기준은 27장 deck/manifest/outline/script/spec JSON과 generated HTML 존재 여부를 포함한다.

## Decision Log

- 2026-04-21 00/01 revision: cover tool text pill 제거, S001 icon-only mark 제한, compact agenda, dark chapter divider, language-transition negative quote, source-visible full code examples, S012/S013 shell 분리, subtitle/lead 제거, 명사형 claim, S002 핵심문장 보강을 확정했다.
- 2026-04-21 latest slide feedback: S009 negative quote 복원, prompt sans font, `자연어` label 좌측 상단 복원, `자연어 지시` 금지, prompt card 상단 배치, S003 balanced agenda, S010 question spacing/source quote sync, S011 table 제거와 card 확장 조건, S012 actual icon, S013 reference flow, S014 dark quote + fact cards, S013/S014 token palette 정리를 확정했다.
- 2026-04-21 source-only revision: source markdown code 회귀, source 밖 struct/class 예시 제거, light code panel, S009 invented contrast 제거, S011 invented meaning column 제거, S012 2x2 reference document card, S014 일반 editorial page 분리를 확정했다.
- 2026-04-21 make-slide stricter revision: make-slide outline/layout/type/theme 우선, split comparison arrow, S010 source quote centered question, S012 반복 설명 제거, S013 one-line summary + 2-axis role layout, S014 source heading 복귀를 확정했다.
- 2026-04-21 chapter 02 extension: 27장 deck, S016 metric cards, S017 `Agent = Model + Harness`, 02장 visual slide의 source footnote/reference 기반 native reconstruction을 확정했다.
- 2026-04-21 generator modularization: HTML deck generator는 얇은 entrypoint와 `scripts/jaryo_html_deck/slides/slide_XXX.py` slide module 구조를 유지하고, 공용 렌더링/파일 출력은 slide module에 두지 않는다.
- 2026-04-21 visual correction: S016 tall metric card, S017 title + dark thesis + Harness 원의미 구조, S015-S027 `CHAPTER 02`, pattern/architecture raw crop 금지, S026 hierarchy를 확정했다.
- 2026-04-21 corrective revision: feedback-to-rule hard gate, one-line title, S018 date metadata 이동, S019/S020 example-first native diagrams, S021 압축, S022 gradient 금지, S023 native architecture canvas, S024 arrow-only loop, S025/S026 hierarchy, S027 relationship equation only, CHAPTER 02 body scale down을 확정했다.
- 2026-04-22 approved plan v5: 이 문서를 top-level HTML slide authority로 재정비하고, slide-number-specific active rules를 reusable meaning/design patterns와 Traceability로 분리하며, Visual Reference Baseline와 Reference Analysis Protocol을 추가하기로 확정했다.
- 2026-04-22 chapter 02 rebuild start: S016-S018은 scale/spacing 조정 후 재사용하고, standalone `Agent = Model + Harness` page는 S027 결론 page로 통합하며, evolution assets 02-06은 page-052/page-067의 정돈된 구조 감각으로 native diagram 재구성하기로 확정했다.

## Traceability

- Deprecated/Replaced Rules는 active rules가 아니라 history다.
- S009 split comparison rhythm 복귀 규칙은 폐기됐다. 최신 규칙은 centered prompt-only block + negative opinion line이며, `자연어`는 card 내부 장식 label이 아니라 언어 예시 성격 표기다.
- S018 긴 source heading을 제목에 그대로 두고 body를 내리는 규칙은 폐기됐다. 최신 규칙은 제목 한 줄 유지, 날짜/부가절 body metadata 이동이다.
- S024 화살표와 반복 arc 필수 규칙은 폐기됐다. 최신 규칙은 arrow-only loop이며 dashed repeat label과 `↺ repeat`를 금지한다.
- S013 capability map, small card grid, compare-card 반복은 폐기됐다. 최신 규칙은 left evolution flow + right analogy blocks와 source-backed role structure다.
- S014 pill chip, `BASICS`, subtitle-like support, reference 문구 직접 차용은 폐기됐다. 최신 규칙은 source-backed dark quote + two factual cards다.
- S011 table/evidence column 및 `원문 사실` 해설 label은 폐기됐다. 최신 규칙은 source fact cards only다.
- S017 Harness 원의미를 source/reference 확인 없이 설명하는 방식은 폐기됐다. 최신 규칙은 확인된 근거 없이는 생성 금지다.
- S001 title fixed value: `Harness 잘 사용하기`.
- S001 presenter fixed value: `게임플랫폼 1팀 라승수`.
- S002 thesis line includes `개발자의 핵심 역량` and `AI가 안전하게 일할 환경`.
- S005 negative opinion fixed value: `컴파일러가 만든 코드가 사람보다 효율적일 리 없다!`.
- S006 negative opinion fixed value: `진짜 프로그래머는 파스칼 같은 걸 쓰지 않는다!`.
- S009 label fixed value: `자연어`; banned label: `자연어 지시`; negative opinion fixed value: `자연어로 시키는 건 진짜 개발이 아니다!`.
- S010 question fixed value: `직접하는 일을 줄고, 설계하는 일은 늘어난다`.
- S013/S014 chapter label fixed value: `CHAPTER 01`; banned label: `SECTION 1`.
- S014 title fixed value: `그래도 기초가 중요하다`; dark summary quote fixed value: `AI가 더 많이 해줄수록 기초 지식을 가진 사람의 경쟁력 상승`.
- S015-S027 chapter label fixed value: `CHAPTER 02`; banned auxiliary labels include `ACT`, `LIMIT`.
- S016 metric fixed values: `2주`, `1~2일`, `불가능하던 작업 실현`; source에 없는 tool label `Augment Code + Vertex AI`는 visible copy로 쓰지 않는다.
- S017 standalone formula page rule은 CHAPTER 02 rebuild에서 폐기됐다. `Agent = Model + Harness`는 S027 결론 page의 fixed value로 이동한다.
- S017 title fixed value after rebuild: `1막: Copilot과 ChatGPT, 프롬프트의 시대`; `2022~2024`는 generated title이 아니라 body metadata/era badge/rail에 둔다.
- S018 title fixed value after rebuild: `Chain-of-Thought`; required CoT example values include `2캔 × 3개`, `11개`; adjacent pattern names must not appear on this page.
- S019 title fixed value after rebuild: `ReAct / Tree-of-Thought`; required pattern names are `ReAct`, `Tree-of-Thought`; raw asset embeds are forbidden.
- S020 title fixed value after rebuild: `Self-Refine / Reflexion`; required pattern names are `Self-Refine`, `Reflexion`; feedback-loop native diagram structure is required.
- S021 Andrew Ng pattern visual은 네 패턴 관계가 보이는 native quadrant/diagram으로 남긴다.
- S022 Blind Prompting은 중앙 주장 + 원인 카드 구조로 남긴다. gradient 배경은 금지하고 neutral surface와 border, `--color-surface`, `--color-line-soft`, `--color-signal-soft`만 사용한다.
- S023 title fixed value after rebuild: `2막: Cursor와 컨텍스트의 시대`; 초기 Copilot과 Cursor 계열 도구 비교 구조를 유지한다.
- S024 Cursor architecture fixed flow: 사용자 요청, indexing, retrieval, context assembly, edit/run, verify; codebase index와 context bundle 경계를 시각화한다.
- S025 loop fixed values: `gather context`, `take action`, `verify`, `repeat`, `loop-cycle-arrow`; banned values: `loop-repeat-arc`, `↺ repeat`.
- S026 fixed component values: `Plan Mode`, `승인 체계`, `CLAUDE.md`, `Skills`, `Hooks`, `MCP`, `Plugins`, `Subagents`; source-outside tier labels `기초`, `자동화`, `연결`, `확장` are forbidden after rebuild.
- S027 relationship fixed value: `Prompt ⊂ Context ⊂ Harness`; banned structure/class: `era-native-nesting`.
- S027 formula fixed value after rebuild: `Agent = Model + Harness`; relationship fixed value: `Prompt ⊂ Context ⊂ Harness`; both must appear on the same conclusion page.
