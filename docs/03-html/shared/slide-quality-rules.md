# HTML Slide Quality Rules

이 문서는 모든 HTML 관련 작업 전에 먼저 읽는 대화 기반 규칙 기록이다. `docs/03-html/`의 outline, manifest, generator output, shared CSS/tokens, deck HTML, screenshot QA, PDF export QA에 모두 적용한다.

## Work Gate

- 작업 시작 전 `AGENTS.md`, `.codex/subagents/README.md`, `.codex/templates/subagent-task-template.md`, 이 문서 전체, 현재 작업 대상 slide의 규칙과 판단 로그를 읽는다.
- HTML 관련 작업은 반드시 subagent에게 위임한다. 본 세션은 오케스트레이터이며, subagent prompt에는 이 문서 사전 확인, 최신 피드백 기록, source/reference 밖 생성 금지, 필요한 검증 명령을 명시한다.
- 새 사용자 피드백은 구현 전에 먼저 이 문서에 기록한다. 기록 위치는 `Non-negotiable Invariants`, slide-specific rule, `Decision Log`, `Deprecated/Replaced Rules` 중 가장 강제력이 높은 곳이다.
- 최신 피드백을 규칙으로 승격하지 않은 상태에서 generator, CSS, renderer, tests, generated HTML, PDF를 수정하지 않는다.
- 구현 순서: 규칙 기록 -> subagent 위임 -> generator/CSS/test/check 갱신 -> HTML/PDF 재생성 -> 정적 검증 -> Playwright screenshot/PDF smoke 검증.
- 충돌 해결 순서: 사용자와 대화하며 확정한 최신 규칙 -> 이 문서 -> `make-slide` 적용 문서 -> 기존 design/layout 문서 -> generator 기존 구현.
- 검증 명령은 작업 범위에 맞게 선택 실행하되 HTML 수정 후에는 `check_slide_contract`, `check_slide_korean`, `check_deck_runtime`, 필요한 Playwright screenshot, 필요한 PDF smoke를 이 문서 기준으로 통과시킨다.
- 이 문서만 정리하는 작업에서는 HTML, CSS, renderer, tests, generated HTML, PDF를 수정하지 않는다.

## Retrospective

- 규칙은 길어졌지만 generator/test/check가 모든 시각 규칙을 막지 못했다. 정적 구조 검증만 믿으면 최신 사용자 피드백이 다시 빠진다.
- 구조 검증은 통과해도 label 위치, 카드 내부/외부, font scale, footer와 본문 겹침, dark quote 대비 같은 visual rule은 screenshot review 없이는 놓친다.
- 최신 사용자 피드백이 slide-specific invariant로 올라가지 않으면 다음 작업에서 예전 layout 관성으로 되돌아간다.
- 오케스트레이터가 구현까지 직접 수행하면 컨텍스트 오염과 규칙 누락이 커진다. HTML 작업은 subagent 위임을 기본 실행 단위로 고정한다.

## Non-negotiable Invariants

- HTML 작업은 subagent 위임 기반으로만 진행한다. 오케스트레이터는 규칙 확정, prompt 구성, 결과 검수, 후속 지시를 맡는다.
- HTML slide 문구와 시각 구조의 의미 단위는 source markdown 또는 사용자가 명시한 reference에서만 가져온다. source/reference 밖 비교 축, label, 의미, 예시, metric, 해설 문구를 만들지 않는다.
- S009 `자연어`는 prompt card 내부 설명 label이 아니라 S005-S008 코드 언어 예시와 같은 좌측 상단 성격 표기다. `자연어 지시`는 금지한다.
- S016 metric value는 카드 상단에 배치한다.
- S017 `Harness` 원의미는 source/reference 확인 없이는 생성하지 않는다.
- CHAPTER 02 body typography는 CHAPTER 01 본문 크기 수준으로 제한한다. 큰 카드 제목, 본문, center claim, data-table text의 과대 확대를 금지한다.
- S019/S020/S023은 예시 중심 native diagram으로 구성한다. raw crop, raw screenshot, 정의 카드 나열을 금지한다.
- S024 loop form을 유지한다. 네 단계 사이 명시적 arrow로 순환을 보이고, dashed repeat label 또는 `↺ repeat`를 쓰지 않는다.
- S025는 tier hierarchy를 유지한다. 좌측 tier label과 계층 row 구조를 흔들지 않는다.
- S027 포함관계는 `Prompt ⊂ Context ⊂ Harness` 텍스트 관계식으로만 표기한다. nested box 그림은 금지한다.
- S013/S014는 `CHAPTER 01` label을 사용하고 `SECTION 1`을 금지한다.
- S014 dark summary quote는 `AI가 더 많이 해줄수록 기초 지식을 가진 사람의 경쟁력 상승`으로 고정한다.
- S001 title은 `Harness 잘 사용하기`로 고정한다.

## Source And Style

- 문구는 명사형 또는 구 단위 중심이다. 공손체, 서술형, 명령형을 피한다.
- slide title, lead, body copy는 압축 문구를 우선한다. 필요한 경우에도 source line으로 추적 가능해야 한다.
- source markdown의 최신 문구가 stale generated phrasing보다 우선한다. 사용자가 페이지를 부정확하게 지칭해도 source markdown의 최신 문장을 따른다.
- source 의미 보존 압축은 허용한다. source에 없는 해설축, 반복 설명, 분류 label, 보조 label, metric 재해석은 금지한다.
- code syntax는 원문을 보존한다. code block 내부 주석 추가는 금지하고, source code block 내부 주석은 slide 표시에서 제거한다.
- 예시 code block은 축약하지 않는다. source-visible 전체 예시 내용이 보여야 한다.
- 부정적 의견 quote는 짧은 구 단위 문구로 유지한다.

## Deck Constants

- `Kuneosu/make-slide` 방식 우선: outline-first, theme/layout 분리, shell reuse, standalone deck, keyboard/touch navigation, print/PDF 친화 CSS.
- 채택 layout/type: title, agenda, section, statement, split comparison, process, evidence table, visual card, closing question.
- 비채택 범위: visible UI chrome, slide counter UI, progress bar, keyboard hint, demo chrome, auto image search demo, fullscreen/notes popup UI, PDF export와 충돌하는 기능.
- theme class는 `theme-minimal-light`를 유지한다.
- palette는 minimal-light 기준을 유지한다: background `#fafafa`, surface `#ffffff`, border `#e0e0e0`, primary `#1a1a1a`, secondary `#555555`, tertiary `#444444`, accent `#0066cc`, highlight `#0a84ff`, code background `#f5f5f5`.
- slide 규격은 `720pt × 405pt`, font는 Pretendard CDN, footer는 좌하단 `Harness 잘 사용하기`, 우하단 page number다.
- 첫 장 발표자 표기는 `게임플랫폼 1팀 라승수`, 하단 우측 영역이다.
- 첫 장 전용 tool mark는 우상단 실제 asset icon만 사용한다: `assets/icons/claude_code_icon.svg`, `assets/icons/codex_icon.png`, `assets/icons/opencode_icon.png`.
- 일반 슬라이드 tool mark, text pill 형태 tool 표기, S014 포함 일반 본문 slide의 pill chip은 금지한다.

## Layout Rules

- 카드 규칙: nested card 금지, slide당 핵심 카드 1~3개, radius 8px 이하. reference가 4-card grid를 요구하는 경우에만 slide당 4개 card를 허용한다.
- tool card/identity card는 actual icon asset을 우선하고 generic document/file glyph를 금지한다.
- 강조 3단계는 theme accent, bold/ink, muted metadata다.
- 제목 아래 subtitle/lead는 기본 금지다. 필요한 경우에만 예외로 둔다.
- 제목은 한 줄 고정이다. 2줄 예상 시 생성 중단 후 사용자 확인. 긴 source heading은 핵심 source phrase만 title에 두고 날짜/부가절은 body metadata로 이동한다.
- 전체 목차 한 장 구성: compact agenda, subtitle 제거, full-page list/table 느낌의 균형 잡힌 가로 사용, footer safe margin 확보.
- 챕터 전환은 dark divider로 일반 content page와 분리한다. 요약/전환 content page에는 chapter divider shell을 쓰지 않는다.
- 핵심 한 마디와 negative quote는 중앙 정렬한다.
- split comparison slide는 좌우 블록 사이 theme accent arrow를 둔다.
- document reference card는 반복 설명 문구 없이 product/file identity만 표기한다.
- role/capability slide는 작은 카드 다발보다 한 줄 핵심 요약과 2축 이상의 구조화 layout을 우선한다.
- final question slide는 source heading을 title로 유지하고 source quote를 centered summary로 배치한다.
- code panel은 source/reference가 dark panel을 명시하지 않는 한 light code panel이다. renderer가 만든 leading/trailing artificial blank line, snippet clipping, `overflow:hidden`으로 인한 코드 잘림은 실패다.
- dark quote block은 white text 대비를 확보한다.

## Composition Rules

- 섹션마다 최소 1장을 둔다. 큰 섹션은 최대 5장까지 허용한다.
- 패턴, 도표, architecture 설명은 시각 요소를 필수로 둔다.
- 같은 인접 주제라도 같은 shell 반복을 금지 검토한다. 특히 S012/S013처럼 연속되는 역할/문서 설명은 서로 다른 shell을 우선한다.
- 실패한 review 결과는 실패 slide id와 수정 범위만 다음 작업자에게 전달한다.
- 규칙 문구가 바뀌면 테스트/contract/visual check 중 하나 이상으로 고정한다. S003/S009/S011과 source-sync slide인 S005/S006/S010은 Playwright screenshot 확인 대상이다.
- nested-card 위험은 contract 단계에서 탐지해야 한다. 렌더 결과만 믿고 넘기지 않는다.

## Reusable Patterns

- centered single-message prompt/claim page: S009처럼 한 장에 하나의 자연어 메시지만 남기고, 카드 좌측 상단에는 source 성격 label만 둔다.
- evidence cards without tables: S011처럼 숫자와 사실만 카드로 압축하고, 해설 열이나 표는 쓰지 않는다.
- role transition flow with right-side analogy: S013처럼 왼쪽에는 위에서 아래로 이어지는 역할 이동 흐름, 오른쪽에는 비유 블록을 둔다.
- dark quote + factual cards for closing: S014처럼 어두운 quote 블록 하나와 그 아래 흰 surface + neutral border 사실 카드 두 개로 끝낸다.
- future source-backed slides는 이 네 패턴을 먼저 검토하고, source-backed label과 copy만 바꾼다.

## Slide Rules

- S002 thesis line은 `개발자의 핵심 역량`과 `AI가 안전하게 일할 환경`을 명시한다.
- S003 agenda는 reference-like balanced layout이다. 왼쪽 title block과 오른쪽 item block을 맞추고, 우측 빈 공간이 두드러지지 않게 하며, compact spacing으로 footer safe area를 비운다.
- S004 section divider는 S013 dark/black family token과 같은 계열을 쓴다.
- S005/S006 language-transition quote는 source markdown negative opinion line을 그대로 따른다. S005 `컴파일러가 만든 코드가 사람보다 효율적일 리 없다!`, S006 `진짜 프로그래머는 파스칼 같은 걸 쓰지 않는다!`.
- S005-S008 code는 source markdown code block에서 가져온 comment 제거 버전이다. 코드 크기와 card geometry는 가독성을 우선하고, flat code panel과 shell-level label로 nested card 위험을 줄인다.
- S005-S009 quote와 S002 thesis는 centered claim이다. S005-S009 split comparison에는 `.compare-arrow`가 있어야 한다.
- S009는 centered prompt card와 restored negative opinion line을 함께 사용한다. prompt body는 실제 code가 아니므로 monospace/code styling이 아니라 readable sans text다.
- S009 prompt card는 본문 영역 중앙보다 약간 상단에 두고 하단 반대 의견과 충분한 간격을 둔다. negative opinion line은 정확히 `자연어로 시키는 건 진짜 개발이 아니다!`다.
- S009는 단일 자연어 지시만 남긴다. `직접 작성`, `AI 작성 비중`, `수동 코딩 감소`, `역할 변화`, `더 큰 구조 설계`, right-side comparison은 금지한다.
- S010 question line은 table 아래에 명확한 간격을 두고 중앙 정렬한다. text는 current source quote `직접하는 일을 줄고, 설계하는 일은 늘어난다`를 따른다.
- S011은 table을 렌더하지 않는다. source fact evidence cards 또는 number cards만 사용하고 `원문 사실`, invented meaning column을 제거한다. 카드 확장은 title/footer clearance가 보존될 때만 허용한다.
- S012 tool card는 실제 icon asset을 사용하고 document glyph를 금지한다. page-011 reference형 2x2 document card는 product/file identity 중심이며 `에이전트 운영 규칙` 반복 문구를 금지한다.
- S013은 page-012 reference처럼 left evolution flow + right analogy blocks 구조다. reference layout을 따르되 footer safe area를 침범하지 않는다.
- S013/S014는 source/reference 밖 카드, 칩, 보조 label 생성을 금지한다. dark blocks/cards는 palette tokens만 쓰며 copper/brown accent token/literal, ivory/paper/beige 계열 token 정의 자체를 금지한다. card background는 `--color-surface` + `--color-line-soft`만 쓴다.
- S014 title은 `그래도 기초가 중요하다`다. page-013 reference처럼 dark quote block + two bottom cards로 구성하고, `BASICS`, `statement-chip`, pill-shaped tag, subtitle-like support를 금지한다.
- S014 bottom card 문구는 source markdown의 기본기 문단에서 추적 가능한 표현만 허용한다.
- S015-S027 chapter label은 모두 `CHAPTER 02`다. `ACT`, `LIMIT` 같은 보조 label은 금지한다.
- S016 `에이전틱 코딩의 실제 성과`는 page-017 reference 내용만 재구성한다. raw screenshot 없이 `2주`, `1~2일`, `불가능하던 작업 실현`의 3분할 성과를 minimal-light metric cards로 만든다. 긴 label은 `큰 숫자 / 짧은 label / 보조 문구 / 출처 meta` 계층으로 분리하고, metric value는 카드 상단에 둔다.
- S017 `Agent = Model + Harness`는 title + dark thesis + source/reference-backed Harness 원의미 구조다. `모델이 아닌 것은 전부 하네스`를 노출하고 `입니다` 종결은 금지한다. 공식, quote, 원의미, decision axis의 시각 위계를 분리한다.
- S018 title exact는 `1막: Copilot과 ChatGPT, 프롬프트의 시대`다. `2022~2024`는 body metadata/era badge/rail에 배치하고 generated title에는 넣지 않는다.
- S019 prompt pattern visual은 CoT/ReAct/ToT/Self-Refine/Reflexion 원문 구조와 research-backed example을 native diagram으로 재구성한다. Chain-of-Thought 예시는 raw screenshot/긴 verbatim quote 없이 `5개 + 2캔 × 3개 -> 6개 -> 11개`처럼 계산 흐름을 한눈에 보이는 그림으로 만든다.
- S019에는 CoT 산술 예시, ReAct 검색/관찰 또는 WebShop 예시, Tree-of-Thought/Game of 24 탐색, Self-Refine code feedback, Reflexion reflection memory 기반 재시도 예시가 들어간다.
- S020 Andrew Ng pattern visual은 네 패턴 관계가 보이는 native quadrant/diagram이다. 각 pattern은 source-backed 효과 한 줄과 예시 mini diagram을 포함하고 이름/효과만 나열하지 않는다.
- S021 Blind Prompting은 중앙 주장 + 원인 카드 구조다. 긴 산문 재현을 금지한다.
- S022는 gradient 배경을 금지하고 neutral surface와 border, `--color-surface`, `--color-line-soft`, `--color-signal-soft`만 사용한다.
- S023 Cursor architecture는 source text diagram과 reference asset을 raw/cropped image가 아니라 native pipeline으로 재작성한다. 사용자 요청, indexing, retrieval, context assembly, edit/run, verify의 연결 구조를 큰 architecture canvas + 보조 카드로 보이고, codebase index와 context bundle 경계를 시각화한다.
- S024 loop visual은 `gather context`, `take action`, `verify`, `repeat` 네 단계와 `loop-cycle-arrow`를 유지한다.
- S025 Claude Code 구성 요소는 page-021 reference처럼 좌측 tier label + 계층 row 구조다. `CLAUDE.md`, `Skills`, `Hooks`, `MCP`, `Subagents`, `승인/샌드박스`와 tier label `기초`, `자동화`, `연결`, `확장`을 유지한다.
- S026 harness decision은 page-021 reference처럼 핵심 공식 아래 source 네 질문의 계층 구조다. `무엇을 보는지`, `무엇을 할 수 있는지`, `언제 멈추는지`, `잘못되었을 때`를 유지하고, `기초/권한/제약/복구` 같은 source 밖 분류 label은 금지한다.
- S027 시대 흐름은 raw timeline image 없이 source era table과 포함 관계를 native timeline/table로 재구성한다. 포함관계는 `Prompt ⊂ Context ⊂ Harness`만 노출하고 `era-native-nesting`은 금지한다.

## Validation Expectations

- 전체: deck/manifest/outline/script/spec JSON이 27장 기준이고 S015-S027 generated HTML이 존재한다.
- 전체 금지어/구조: generated HTML에서 `Harness를 설계하는 법`, `직접 작성`, `AI 작성 비중`, `수동 코딩 감소`, `역할 변화`, `README`, `더 큰 구조 설계`, `BASICS` 미노출.
- S001: title `Harness 잘 사용하기`; `tool-icons`는 S001에만 존재; tool icon `img`는 `assets/icons` 기반 data URI.
- S005-S008: source code에서 comment 제거, artificial leading/trailing blank line 없음, 전체 snippet 노출, `.code-block` scrollHeight <= clientHeight.
- S009: `자연어` label은 카드 좌측 상단 성격 표기로 노출; `자연어 지시`는 어디에도 미노출; prompt card는 중앙보다 약간 상단, prompt language label과 prompt text 간격 유지.
- S010: `.table-question` 중앙 정렬, table과 visible separation 유지, text equals `직접하는 일을 줄고, 설계하는 일은 늘어난다`.
- S011: cards only, no table, no `원문 사실`, no invented meaning column, larger cards allowed only with title/footer clearance.
- S012: actual icon asset만 사용, document glyph와 `에이전트 운영 규칙` 반복 문구 미노출.
- S013: left vertical evolution flow와 right analogy blocks, screenshot에서 footer와 본문 겹침 없음.
- S013/S014: `CHAPTER 01` 노출, `SECTION 1` 미노출, `--color-dark-accent`, `#c76640`, hardcoded copper/brown literals 미노출.
- S014: `그래도 기초가 중요하다`, dark summary quote, two bottom cards 존재; dark quote white text 대비 확보; `statement-chip`/pill-shaped tag 미노출.
- S014: generated CSS/deck에서 `--color-dark-card`, `--color-dark-card-border`, `--color-dark-surface-muted`, `#f3efe7`, `#eee9e1`, `#e8e1d5` 미노출.
- S014: generated HTML에서 `코딩은 에이전트가 일할 환경을 설계하고 검증하는 영역으로 이동하고 있습니다.`, `데모까지는 쉽지만`, `기본기 없이는 질문조차 불가` 미노출.
- S016: `2주`, `1~2일`, `불가능하던 작업 실현` 노출; metric value 상단 배치 screenshot 확인.
- S017: `Agent = Model + Harness`, `모델이 아닌 것은 전부 하네스` 노출; `입니다` 미노출; Harness 원의미는 source/reference 확인 근거가 있을 때만 노출.
- S019: `Chain-of-Thought`, `ReAct`, `Tree-of-Thought`, `Self-Refine`, `Reflexion`, `cot-diagram`, `react-diagram`, `tot-diagram`, `feedback-diagram`, `cot-example-diagram`, `2캔 × 3개`, `11개` 노출.
- S019: ReAct/WebShop, Tree-of-Thought/Game of 24, Self-Refine/code feedback, Reflexion/reflection memory 예시 노출.
- S020: raw reference asset name 미노출, pattern별 mini example diagram 노출.
- S023: raw reference asset name 미노출, architecture example canvas와 codebase index/context bundle 경계 노출.
- S024: `gather context`, `take action`, `verify`, `repeat`, `loop-cycle-arrow` 노출; `loop-repeat-arc`, `↺ repeat` 미노출.
- S025: `CLAUDE.md`, `Skills`, `Hooks`, `MCP`, `Subagents`, `승인/샌드박스`, `기초`, `자동화`, `연결`, `확장` 노출.
- S026: `무엇을 보는지`, `무엇을 할 수 있는지`, `언제 멈추는지`, `잘못되었을 때` 노출.
- S018: generated title에서 `(2022~2024)` 미노출, body에서 `2022~2024` 노출.
- S027: `Prompt ⊂ Context ⊂ Harness` 노출, `era-native-nesting` 미노출.

## Decision Log

- 2026-04-21 00/01 revision: cover tool text pill 제거, S001 icon-only mark 제한, compact agenda, dark chapter divider, language-transition negative quote, source-visible full code examples, S012/S013 shell 분리, subtitle/lead 제거, 명사형 claim, S002 핵심문장 보강을 확정했다.
- 2026-04-21 latest slide feedback: S009 negative quote 복원, prompt sans font, `자연어` label 좌측 상단 복원, `자연어 지시` 금지, prompt card 상단 배치, S003 balanced agenda, S010 question spacing/source quote sync, S011 table 제거와 card 확장 조건, S012 actual icon, S013 reference flow, S014 dark quote + fact cards, S013/S014 token palette 정리를 확정했다.
- 2026-04-21 source-only revision: source markdown code 회귀, source 밖 struct/class 예시 제거, light code panel, S009 invented contrast 제거, S011 invented meaning column 제거, S012 2x2 reference document card, S014 일반 editorial page 분리를 확정했다.
- 2026-04-21 make-slide stricter revision: make-slide outline/layout/type/theme 우선, split comparison arrow, S010 source quote centered question, S012 반복 설명 제거, S013 one-line summary + 2-axis role layout, S014 source heading 복귀를 확정했다.
- 2026-04-21 chapter 02 extension: 27장 deck, S016 metric cards, S017 `Agent = Model + Harness`, 02장 visual slide의 source footnote/reference 기반 native reconstruction을 확정했다.
- 2026-04-21 generator modularization: HTML deck generator는 얇은 entrypoint와 `scripts/jaryo_html_deck/slides/slide_XXX.py` slide module 구조를 유지하고, 공용 렌더링/파일 출력은 slide module에 두지 않는다.
- 2026-04-21 visual correction: S016 tall metric card, S017 title + dark thesis + Harness 원의미 구조, S015-S027 `CHAPTER 02`, pattern/architecture raw crop 금지, S026 hierarchy를 확정했다.
- 2026-04-21 corrective revision: feedback-to-rule hard gate, one-line title, S018 date metadata 이동, S019/S020 example-first native diagrams, S021 압축, S022 gradient 금지, S023 native architecture canvas, S024 arrow-only loop, S025/S026 hierarchy, S027 relationship equation only, CHAPTER 02 body scale down을 확정했다.

## Deprecated/Replaced Rules

- S009 split comparison rhythm 복귀 규칙은 폐기됐다. 최신 규칙은 centered prompt-only block + negative opinion line이며, `자연어`는 card 내부 장식 label이 아니라 언어 예시 성격 표기다.
- S018 긴 source heading을 제목에 그대로 두고 body를 내리는 규칙은 폐기됐다. 최신 규칙은 제목 한 줄 유지, 날짜/부가절 body metadata 이동이다.
- S024 화살표와 반복 arc 필수 규칙은 폐기됐다. 최신 규칙은 arrow-only loop이며 dashed repeat label과 `↺ repeat`를 금지한다.
- S013 capability map, small card grid, compare-card 반복은 폐기됐다. 최신 규칙은 left evolution flow + right analogy blocks와 source-backed role structure다.
- S014 pill chip, `BASICS`, subtitle-like support, reference 문구 직접 차용은 폐기됐다. 최신 규칙은 source-backed dark quote + two factual cards다.
- S011 table/evidence column 및 `원문 사실` 해설 label은 폐기됐다. 최신 규칙은 source fact cards only다.
- S017 Harness 원의미를 source/reference 확인 없이 설명하는 방식은 폐기됐다. 최신 규칙은 확인된 근거 없이는 생성 금지다.
