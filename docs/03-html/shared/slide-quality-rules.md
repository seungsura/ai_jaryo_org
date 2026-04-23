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
- 사용자 피드백은 단순 작업 메모로 흘려보내지 않는다. 매번 문서에 남기고, fixed rule, reusable pattern, validation rule, Traceability history 중 어디로 승격할 수 있는지 먼저 검토한다.
- 피드백을 규칙으로 승격하지 않을 때도 이유를 남긴다. one-off correction, 현재 slide 한정, source/reference 부족, 또는 다른 active rule과 충돌 같은 보류 사유를 Decision Log나 Traceability에 기록한다.
- 최신 피드백을 규칙으로 승격하지 않은 상태에서 generator, CSS, renderer, tests, generated HTML, PDF를 수정하지 않는다.
- 모든 사용자 피드백은 작업 지시이기 전에 rule-candidate다. slide-specific 수정 요청, visual reference 요청, 검증 누락 지적, workflow 지적을 모두 문서 기록 대상으로 본다.
- 피드백 기록에는 적용 범위 판단을 함께 둔다: deck-wide rule, chapter/slide-specific rule, reusable pattern, validation rule, one-off exception 중 하나로 분류한다.
- "기록만 하고 규칙화하지 않음"도 명시적 판단이다. 이 경우에도 이후 작업자가 같은 피드백을 재해석하지 않도록 보류 사유와 적용 한계를 남긴다.
- 일반 구현 순서: 규칙 기록 -> subagent 위임 -> generator/CSS/test/check 갱신 -> HTML/PDF 재생성 -> 정적 검증 -> Playwright screenshot/PDF smoke 검증.
- 병렬 worktree에서 slide numbering은 임시값이다. 다른 chapter 작업과 겹칠 수 있으므로 chapter 작업자는 전역 `SXXX`/`slide-XXX` 번호를 안정된 소유권으로 가정하지 않는다.
- 병렬 HTML 작업은 chapter별 작업 폴더를 우선한다. chapter-local 폴더 아래에서 해당 chapter의 local slide order와 임시 slide number를 함께 관리하고, 전역 deck 번호는 마지막 main 통합 단계에서만 재부여한다.
- 사용자가 선호 페이지 baseline을 지정하면 즉시 deck-wide reference set으로 고정한다. 2026-04-23 기준 고정 baseline은 page `1-18`, `21`, `24`, `37`, `39`, `40`, `52`, `53`이다.
- page 번호는 `output/pdf/harness-full-main-94-current-720x405.pdf`의 1-based PDF export page를 기준으로 해석한다.
- legacy page 기준이 현재 deck 번호와 다를 때는 `docs/03-html/shared/page-number-mapping.json`을 우선 참조해 현재 `index.html` footer page로 변환한다.
- 2026-04-23 삭제 반영(`legacy page 19, 20` 제거) 이후 선호 baseline 매핑은 `1-18->1-18`, `21->19`, `24->22`, `37->35`, `39->37`, `40->38`, `52->50`, `53->51`로 고정한다.

## Source Discipline

- local markdown과 사용자가 명시한 reference만 의미 source로 쓴다. source/reference 밖 비교 축, label, 의미, 예시, metric, 해설 문구를 만들지 않는다.
- 모든 visible slide 요소는 source markdown, 사용자가 명시한 reference, 또는 사용자가 직접 지시한 문구로 추적 가능해야 한다. 원문에 없는 내용이나 문장을 보기 좋게 보이기 위해 창작해서 넣는 것은 deck-wide 실패다.
- source에 없는 문구가 필요해 보이면 새로 만들지 않는다. 해당 요소를 제거하거나, 사용자 확인 전까지 open question으로 남긴다.
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
- CHAPTER 06-07 slide title은 `docs/02-seminar/harness-rebuilt-md` 원문 소제목을 그대로 사용한다. reference/canonical page에만 있는 장 제목, section label, 요약 제목은 title로 쓰지 않는다.
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
- S018 feedback round 3에서 추가 승인한 reference는 `assets/claude-code-seminar-kakao/page-064.png`, 사용자가 첨부한 ReAct screenshot, `https://pub.towardsai.net/chain-of-thought-vs-tree-of-thought-vs-graph-of-thought-reasoning-method-comparison-1f19d238a005`의 CoT/ToT comparison structure다. S018은 `CoT`, `ReAct`, `ToT` 3개를 한 페이지에 모두 visible copy로 두고, `2캔 × 3개`, `11개` 같은 산수 예시는 쓰지 않는다. `Graph-of-Thought`, `GoT`는 S018 visible copy에 넣지 않는다.
- CHAPTER 06-07 revision에서 사용자가 승인한 primary visual reference는 `assets/claude-code-seminar-kakao/page-062.png`, `page-063.png`, `page-064.png`, `page-065.png`, `page-066.png`, `page-067.png`, `page-068.png`다. 이 묶음은 CHAPTER 06뿐 아니라 CHAPTER 07의 재구성에도 structure-only reference로 쓴다.
- 2026-04-23 사용자 고정 baseline은 `output/pdf/harness-full-main-94-current-720x405.pdf` 기준 page `1-18`, `21`, `24`, `37`, `39`, `40`, `52`, `53`이다. 이 묶음은 향후 피드백 루프에서 우선 비교군으로 사용한다.
- legacy baseline과 현재 deck 번호의 대응표는 `docs/03-html/shared/page-number-mapping.md`와 `docs/03-html/shared/page-number-mapping.json`을 단일 진실원으로 유지한다.
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
- CHAPTER 06-07 approved references: page-062는 dark chapter divider, page-063은 3-wall card composition, page-064는 5-pattern card row, page-065는 high-contrast split comparison, page-066은 Main/Sub relationship map with side cards, page-067은 system map + side explanation + bottom conclusion, page-068은 4-principle grid + dark conclusion 구조를 참고한다.
- 고정 선호 page cluster 해석: `1-3`(opening cadence), `4-14`(chapter 01 narrative rhythm), `15-18/21/24`(chapter 02 정보-구조 혼합), `37/39/40`(chapter 04 핵심 도식), `52/53`(chapter 05 statement 밀도) 구조를 우선 패턴으로 둔다.

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
- 3-card row layout은 카드 높이와 폭을 동일하게 맞춘다. 강조 숫자/핵심어는 카드 상단에 배치하고, 카드 하단으로 밀려 내려가면 실패다.
- 카드 label은 의도한 계층을 지켜야 한다. language/category label이 prompt/card 내부 장식으로 빨려 들어가면 실패다.
- dark process card의 stage label은 장식 텍스트가 아니라 읽히는 heading rail이어야 한다. `SPECIFY`, `PLAN`, `TASKS`처럼 단계 의미를 가진 작은 label은 screenshot/PDF에서 즉시 읽혀야 하며, dark surface 위 low-contrast accent text로만 처리하면 실패다.
- native diagram slide는 렌더링된 screenshot/PDF를 승인 reference와 직접 비교한다. contract text가 맞아도 시각 구조, 관계, density, spacing이 reference와 어긋나면 실패다.
- 카드 내부 text는 카드 border 안에 완전히 들어와야 한다. overflow, clipping, border 밖 돌출, footer와 겹침은 실패다.
- 카드 크기와 내부 글자 크기는 서로 맞아야 한다. 큰 카드 안에 작은 글자가 떠 보이거나, 작은 카드 안에서 글자가 과하게 커져 hierarchy가 무너지면 실패다.
- 카드가 담는 정보량이 작으면 카드 자체도 작아져야 한다. 짧은 label/text를 큰 빈 카드에 띄워 놓아 답답한 비례가 생기면 실패다.
- 카드 안에 다시 카드처럼 보이는 `article`/panel/card를 중첩하지 않는다. 한 패널 안의 보조 정보는 rail, row, list, divider, callout text로 처리하고 nested card로 렌더링하면 실패다.
- 인용문은 전용 quote card/block으로 렌더링한다. 표의 callout, 일반 synthesis bar, 흐름 카드 안의 보조 문장처럼 섞어 넣지 않는다.
- 인용구로 바꾸라는 피드백은 단순한 dark bar가 아니라 `blockquote`와 attribution을 갖춘 quote card/block으로 승격 가능한지 먼저 검토한다.
- 결론 slide는 중복 정보를 피한다. 관계식/공식과 핵심 결론이 이미 의미를 전달하면 하단 table이나 반복 설명을 추가하지 않는다.

## Reusable Patterns

- centered single-message prompt/claim page: 한 장에 하나의 자연어 메시지만 남기고, 카드 좌측 상단에는 source 성격 label만 둔다.
- evidence cards without tables: 숫자와 사실만 카드로 압축하고, 해설 열이나 표는 쓰지 않는다.
- role transition flow with right-side analogy: 왼쪽에는 위에서 아래로 이어지는 역할 이동 흐름, 오른쪽에는 비유 블록을 둔다.
- dark quote + factual cards for closing: 어두운 quote 블록 하나와 그 아래 흰 surface + neutral border 사실 카드 두 개로 끝낸다.
- dedicated quote card: 인용문은 `blockquote`와 `figcaption`을 가진 독립 figure/card로 둔다. 출처가 필요한 인용은 카드 안에서 attribution을 함께 보여준다.
- metric card trio: 큰 숫자 / 짧은 label / 보조 문구 / 출처 meta 계층으로 분리하고, metric value는 카드 상단에 둔다.
- example-first native diagram: pattern, architecture, workflow 설명은 이름/정의 나열보다 source-backed 예시와 관계를 보이는 native diagram으로 구성한다.
- loop visual: 네 단계 사이 명시적 arrow로 순환을 보인다. dashed repeat label 또는 `↺ repeat`를 쓰지 않는다.
- tier hierarchy: 좌측 tier label과 계층 row 구조를 유지한다.
- inclusion relationship: 포함관계는 텍스트 관계식으로 노출한다. nested box 그림을 기본값으로 쓰지 않는다.
- reference-derived soft patterns: `main process + rationale card + bottom takeaway`, `axis rows + column headers + final synthesis`, `quote/counter-claim + taxonomy cards + caution takeaway`, `dominant native diagram + outcome cards`, `card row + mini diagram + 1-line meaning`, `dominant system map + side explanation + bottom conclusion`를 후보 grammar로 둔다.
- reference-derived soft patterns는 source-backed content를 배치하는 구조 후보일 뿐이다. source에 없는 문구, 비교 축, label, metric, 해설을 채우는 근거로 쓰지 않는다.
- future source-backed slides는 위 패턴을 먼저 검토하고, source-backed label과 copy만 바꾼다.
- CHAPTER 02 pattern/architecture slides는 approved evolution assets 02-06을 raw image로 붙이지 않고 native diagram으로 재작성한다. `assets/claude-code-seminar-kakao/page-052.png`와 `page-067.png`는 큰 제목, 여백, native diagram, 요약 card 배치의 structure-only reference로만 쓴다.
- CHAPTER 06-07 dark split panel 내부 `small` text는 contrast/readability를 반드시 확보한다. source-backed 보조문구라도 어두운 카드 안에서 묻히면 실패다.
- dark stage rail pattern: dark process card의 step/stage label은 카드 내부 좌상단에 묻힌 작은 accent text가 아니라, 카드 상단 전체 폭을 쓰는 readable rail 또는 같은 수준의 heading treatment로 처리한다.
- CHAPTER 07 artifact/command column은 5개 항목을 모두 footer safe area 안에 넣어야 한다. 항목 수에 맞춘 row sizing 없이 column bottom이 잘리면 실패다.
- CHAPTER 02 S016-S018 기존 화면은 재사용하되 중앙 claim/card typography를 CHAPTER 01 수준으로 낮추고, 카드 내부 줄간격과 footer safe margin을 다시 검증한다.
- CHAPTER 02 rebuild에서는 standalone `Agent = Model + Harness` statement page를 두지 않는다. 이 공식은 S027의 `Prompt ⊂ Context ⊂ Harness` 결론 page 안에서 함께 보여준다.

## Implementation Contract

- deck 구조는 `docs/02-seminar/harness-rebuilt-md` source markdown과 승인된 outline을 따라야 한다.
- chapter별 병렬 작업은 chapter-local staging 구조를 둔다. 예: `docs/03-html/chapters/chapter-03/`, `output/playwright/chapter-03/`, `output/pdf/chapter-03/`처럼 chapter 단위 산출물을 분리하고, 해당 폴더 안에서 local slide number와 source block을 함께 추적한다.
- `docs/03-html/slides/slide-XXX.html`, `docs/03-html/deck/index.html`, global manifest/outline/spec JSON의 전역 번호는 integration artifact다. 여러 worktree가 동시에 작업 중일 때는 이 번호를 고정 계약으로 삼지 않는다.
- 마지막 main 통합에서는 각 작업 브랜치의 chapter-local 산출물과 source-backed slide 정의를 먼저 병합한 뒤, 전역 slide number와 `SXXX`/`slide-XXX` 파일명만 일괄 재계산한다. 이 단계에서 내용, 문구, layout 의미를 함께 바꾸지 않는다.
- 전역 번호 재부여 작업은 content/layout revision과 분리한다. renumbering-only pass에서는 numbering, manifest, outline, deck ordering, generated artifact path만 수정하고 slide copy나 visual structure는 건드리지 않는다.
- CHAPTER 06-07은 combined chapter-local staging으로 관리한다. 리뷰용 PDF와 screenshot/contact-sheet artifact는 6장과 7장 slide만 포함해야 하며, 다른 chapter slide를 섞지 않는다.
- 섹션마다 최소 1장을 둔다. 큰 섹션은 최대 5장까지 허용한다.
- 패턴, 도표, architecture 설명은 시각 요소를 필수로 둔다.
- 같은 인접 주제라도 같은 shell 반복을 금지 검토한다.
- source-sync slide는 source markdown과 generated copy의 drift를 확인한다.
- generated slide HTML과 `deck/index.html`은 artifact다. 실제 slide 구현 단위는 `scripts/jaryo_html_deck/slides/chapter_XX/slide_YYY.py`다.
- HTML deck generator는 얇은 entrypoint를 유지하고, slide source는 chapter package(`chapter_00`~`chapter_09`)로 분리한다. 전체 deck은 한 번의 build에서 chapter package 순서대로 렌더링한다.
- chapter별 파일명은 겹칠 수 있지만 전역 `spec.order`는 중복 없이 contiguous range를 유지해야 한다.
- 실패한 review 결과는 실패 slide id와 수정 범위만 다음 작업자에게 전달한다.

## Validation Contract

- HTML 수정 후에는 작업 범위에 맞게 `check_slide_contract`, `check_slide_korean`, `check_deck_runtime`, 필요한 Playwright screenshot, 필요한 PDF smoke를 이 문서 기준으로 통과시킨다.
- rules-document core only 작업에서는 HTML 검증을 실행하지 않는다. markdown/file scope 검증만 수행한다.
- 규칙 문구가 바뀌면 테스트/contract/visual check 중 하나 이상으로 고정한다. 단, rules-document only 작업에서는 구조 검증과 범위 검증으로 제한한다.
- 구조 검증은 통과해도 label 위치, 카드 내부/외부, font scale, footer와 본문 겹침, dark quote 대비 같은 visual rule은 screenshot review 없이는 놓칠 수 있다.
- nested-card 위험은 contract 단계에서 탐지해야 한다. 렌더 결과만 믿고 넘기지 않는다.
- 전체 deck 검증 기준은 현재 main 통합본의 contiguous deck/manifest/outline/script/spec JSON과 generated HTML 존재 여부를 포함한다.
- 반복 루프(`html 생성 -> pdf 생성 -> 피드백 -> html 수정 -> html 생성`)마다 footer 우하단 page number의 중복/누락/역순 여부를 전역으로 확인한다.

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
- 2026-04-22 feedback round 1: S009 `자연어` label 계층 복귀, S011/S016 3-card equal sizing, S016 metric 상단 배치, S013/S014 body typography CHAPTER 01 scale 통일, S018-S021 approved evolution references와 rendered visual 직접 비교, S024 rule conformance 재검토, S025 card overflow 수정, S027 하단 table 제거, S026 메시지 명확화를 확정했다.
- 2026-04-22 feedback round 2: S018은 Towards AI CoT/ToT/GoT comparison image의 linear-chain 구조를 참고해 전면 개편한다. 정말 필요한 문장만 카드에 담고, 렌더링된 결과를 reference image와 직접 비교한다.
- 2026-04-22 feedback round 3: S018은 `CoT`, `ReAct`, `ToT`를 모두 기재한다. layout은 `assets/claude-code-seminar-kakao/page-064.png`의 card row + mini diagram + 1-line meaning 구조를 따른다. CoT/ToT 그림은 Towards AI comparison의 native structure를 참고하고, ReAct 그림은 사용자 첨부 screenshot의 LM/Env loop, `Reasoning Traces`, `Actions`, `Observations`, `ReAct (Reason + Act)` 구조를 따른다. 산수 예시 `2캔 × 3개`, `11개`는 제거한다.
- 2026-04-22 feedback discipline: 사용자의 모든 피드백은 먼저 문서에 기록하고, fixed rule, reusable pattern, validation rule, Traceability history로 승격 가능한지 검토한다. 규칙화하지 않는 피드백도 보류 사유를 남긴다.
- 2026-04-22 feedback governance reinforcement: 사용자가 피드백은 항상 문서에 기록하고 규칙 적용 가능성을 검토해야 한다고 재확인했다. 이 원칙은 deck-wide Workflow Gate로 승격하며, 모든 피드백을 rule-candidate로 분류한다.
- 2026-04-22 S018 Gemini CLI experiment: S018 전체 재구성은 `gemini` CLI의 `gemini-3.1-pro-preview` 모델에 맡겨본다. 이번 pass에서는 사용자 지시에 따라 validation command, Playwright screenshot, PDF export를 실행하지 않는다. 이 검증 생략은 현재 S018 실험에 한정된 one-off exception이다.
- 2026-04-22 chapter 02 final visual pass: S019/S020은 S018과 중복되어 폐기한다. S021은 Andrew Ng 4-pattern reference를 사람/글자 없이 node/arrow native diagram으로 재구성하고, Planning은 사용자가 제시한 fan-out 상태를 따른다. S022는 3개 원인 card + full-width dark quote card만 남긴다. S024는 Cursor architecture 06 asset raw embed 예외를 허용하고, 오른쪽은 source text arrow graph로 둔다. S025는 1/2/3/4 루프를 버리고 context-wall layout으로 둔다.
- 2026-04-23 S026 simplification: 사용자가 S026에 요소가 너무 많다고 지적했다. S026은 기능 목록, control stack, component rail을 제거하고 `코딩 도구는 이제 실행 환경을 품는다` 한 문장과 `자동완성·채팅 -> 작업 환경 전체 -> Harness` 전환만 남긴다. 보조 정보는 `파일 · 셸 · 테스트` 수준으로 제한한다.
- 2026-04-23 current-main S023 refinement: 현재 main의 23페이지 `컨텍스트만으로는 부족하다`는 기존 임시 context-wall 변형을 폐기하고, 이미 deck에서 검증된 `split-compare` family로 재구성한다. source 문장의 세부 실패 예시를 모두 펼치지 말고 `잘못된 결과나 응답 유입`, `느슨한 실행 권한`, `잘못된 검증` 세 축으로 압축한다. 오른쪽은 `허용/차단 범위`, `멈춤 기준`, `검증 경로`를 두고, 하단 한 줄은 `멈춤 기준과 검증 경로를 먼저 설계해야 한다`로 묶는다. body width는 chapter 02 기준에서 과도하게 넓어지지 않게 줄이고, 관계가 보이는 좌->우 흐름이 없으면 실패다.
- 2026-04-23 current-main S023 latest lock: 23페이지는 다시 더 압축한다. 좌측에는 `index.html` 기준 35페이지(`에이전트 루프: 하네스의 심장`)의 diagram part만 축소 재사용하고, loop panel로 둔다. 우측 상단은 `도구 호출 실패`, `목표 망각`, `테스트 오해`, `보안 경계` 4개 card만 둔다. 이 카드들에서 좌측 loop 쪽으로 화살표가 향하고, 중간 레일 label은 `잘못된 응답 주입`으로 둔다. 우측의 해결 카드 열은 제거하고, 하단 dark one-line emphasis card는 유지한다. body는 기존 시안보다 더 줄여 chapter 02 기준에서 대략 75~85% 폭 감각으로 맞춘다.
- 2026-04-23 current-main S024 planning note: 현재 main의 24페이지 `3막: 하네스의 시대` minimal transition은 전달력이 약하다. 이 페이지는 source의 `Claude Code는 터미널 네이티브 워크플로우를 중심에 둡니다`, `Agent = Model + Harness`, `하네스가 결정하는 것 - 무엇을 보는지/할 수 있는지/멈추는지/잘못되었을 때`를 묶는 `context wall` 성격으로 재검토한다. 좌측에는 하네스의 네 결정 축을 세로 책임 카드로 두고, 우측에는 실행 환경 카드 묶음을 둔다. 우측 카드 묶음은 `작업 루프`(`파일 읽기`, `셸 실행`, `테스트 결과`, `다시 수정`), `통제/승인`(`Plan Mode`, `승인 체계`), `프로젝트 규칙`(`CLAUDE.md`, `Skills`, `Hooks`), `연결/확장`(`MCP`, `Plugins`, `Subagents`)의 네 category로 압축한다. `S054`, `S071`, `S072`, `S037` 계열의 검증된 card grammar를 우선 재사용하고, chapter 02 body 폭을 넘는 과밀한 관계도나 source 밖 설명 label 추가는 금지한다.
- 2026-04-23 current-main S024 implementation lock: 사용자는 24페이지 구조 변경에서 자신이 지정한 구성만 적용하라고 명시했다. 따라서 이번 pass에서는 24페이지에 `하네스가 결정하는 것` 4축과 우측 실행 환경 카드 묶음만 반영하고, `Agent = Model + Harness` 하단 dark strip 추가나 25페이지 시대 구분 표 경량화 같은 추가 제안은 적용하지 않는다. formula는 25페이지의 현재 상태를 유지하고, 24페이지에는 formula/equation/결론 strip를 새로 넣지 않는다.
- 2026-04-23 current-main S028 readability fix: `SPECIFY`, `PLAN`, `TASKS`처럼 dark card 상단에 놓인 단계 label이 screenshot/PDF에서 묻히면 blocker로 본다. 이 계열 label은 작은 accent text로 남기지 않고, card top rail 수준의 readable heading treatment로 승격한다.
- 2026-04-22 chapter 03 build start: S028-S033은 `CHAPTER 03`으로 묶고, S029 timeline table, S030 SDD flow, S031 TDD control map, S032 Waterfall split compare, S033 Harness bridge summary로 source-backed copy만 사용하기로 확정했다.
- 2026-04-22 chapter 03 revision 1: S031은 S030과 유사한 process structure로 재구성하되 왼쪽은 수직 3단 `Red`/`Green`/`Refactor`, 오른쪽은 2개 `권한 통제` block으로 둔다. S032는 좌우로 치우친 split compare를 폐기하고 `assets/claude-code-seminar-kakao/page-032.png`의 row-based comparison + bottom synthesis 구조를 따른다. S033은 `assets/claude-code-seminar-kakao/page-033.png`처럼 `Spec + TDD` 두 카드와 하단 결론 구조를 따른다.
- 2026-04-22 chapter 03 revision 2: S031의 `Red`/`Green`/`Refactor`는 카드 안에 source-backed 설명을 둔다. `Refactor`만 전부 대문자로 쓰지 않고 `Red`/`Green`과 같은 title case로 맞춘다. S031의 큰 `AI 시대의 TDD는 권한 통제 기법` statement card는 제거한다. 모든 slide 요소는 원문에 없는 내용이나 문장을 창작해서 넣지 않는 deck-wide source rule을 다시 강화한다. S033은 카드/결론/중앙 thesis가 안전 영역 안에서 균형 있게 정렬되도록 수정한다.
- 2026-04-22 parallel numbering workflow: 병렬 worktree에서는 slide number가 다른 chapter 작업에 따라 조정될 수 있으므로 전역 `SXXX`/`slide-XXX` 번호를 안정된 소유권으로 보지 않는다. chapter별 작업 폴더 아래에서 local slide order와 임시 번호를 관리하고, 마지막 main 통합에서 모든 작업 브랜치의 진행사항을 병합한 뒤 numbering-only pass로 전역 번호만 재계산한다.
- 2026-04-22 chapter 03 revision 3: S031은 카드 크기와 글자 크기 hierarchy를 맞춘다. S032는 번역투/추상 비교 축을 제거하고 원문에 존재하는 표현만 visible copy로 둔다. S033은 `하네스`를 TDD 카드 항목으로 넣지 않는다. `하네스`는 source-backed 결론/synthesis 레벨에만 둘 수 있다.
- 2026-04-22 chapter 03 revision 4: S031의 TDD reference는 사용자가 명시한 `assets/claude-code-seminar-kakao/page-028.png`와 canonical transcription이다. S032는 사용자의 인터넷 검색 지시에 따라 Waterfall/SDD 차이를 Royce 1970 paper와 GitHub Spec Kit official docs로 재정리하되, visible copy는 source markdown, canonical transcription, 또는 해당 검색 근거로 추적 가능한 표현만 쓴다. S033에는 source-backed 소제목을 visible하게 둔다.
- 2026-04-22 chapter 03 revision 5: S031은 `TDD (Test-Driven Development)`와 Page 028 lead를 함께 visible하게 두고, S032는 `Waterfall vs SDD` row comparison을 Royce 1970 paper와 `spec-driven.md` evidence로 다시 적는다. S033은 `SDD + TDD가 Harness로 이어지는 이유` subheading을 `Spec + TDD` 위에 명시한다.
- 2026-04-22 chapter 03 revision 6: S030은 `assets/claude-code-seminar-kakao/page-031.png`의 spec-kit workflow 구조를 reference로 삼고, 출처에 `GitHub Copilot icon`과 `GitHub spec-kit`을 명시한다. S032는 `SDD` column header가 아래 row content column과 정렬되어야 하며 bottom one-line synthesis를 제거한다. S033은 title/subheading을 blue가 아닌 ink 계열로 두고, 중앙 `Spec + TDD` thesis text를 제거하며, `assets/claude-code-seminar-kakao/page-033.png`를 참고해 card size와 card 내부 text scale을 재조정한다.
- 2026-04-22 chapter 03 revision 7: S033은 copy와 구조를 유지하고 카드 크기만 한 단계 줄인다. 카드가 담는 정보량이 작으므로 card width/height는 과하게 커 보이지 않아야 하며, card 내부 text hierarchy와 footer safe area는 유지한다.
- 2026-04-23 current-main S029 title relief: 29페이지 TDD slide는 title을 `TDD`로 줄이고 `Test-Driven Development`를 제목 아래 lead로 둔다. 기존 body 맨 위 요약 한 줄은 제거하고, topmost chapter-label row도 제거해 vertical relief를 확보한다.
- 2026-04-23 current-main S029 scale tune: 29페이지 TDD slide는 28페이지 SDD보다 body가 더 커 보이면 안 된다. subtitle 아래 body start는 SDD와 비슷한 호흡으로 한 단계 더 내려야 하고, flow/control card의 제목·본문 scale도 한 톤 낮춰 subtitle과 body가 서로 달라붙어 보이지 않게 맞춘다.
- 2026-04-23 current-main S029 blue rail: 29페이지 좌측 flow card를 묶는 세로 rail은 neutral line이 아니라 프로젝트 기본 signal blue(`var(--color-signal)`)를 쓴다.
- 2026-04-22 chapter 04 build start: 모든 사용자 피드백은 구현 전에 규칙 적용 가능성을 검토하고 이 문서에 기록한다. CHAPTER 04는 source page 36/37을 별도 slide로 만들지 않고 `Prompt, Context, Harness` 한 장에서 설명한다. `Agent = Model + Harness`, LangChain/Vivek Trivedy 인용구, 6대 구성요소는 한 slide에 함께 배치한다. `책임과 도구는 1:1이 아니다`는 slide title이 아니라 `하네스의 도구` slide 내부 claim이다. `Right Altitude - 지시문의 고도`는 rebuilt 4장 소제목이 아니므로 독립 title로 쓰지 않고 `CLAUDE.md`/도구 운용 보조 원칙으로만 쓴다. Memory slide는 4장에 포함한다.
- 2026-04-22 chapter 04 review 1: S034 keyword chips are blocked if the text is not visibly readable on screenshot/PDF. S039 must not collapse the responsibility/tool N:N relationship into a dense table; it needs a native relationship composition. S043 must not stay as a two-column list table; it needs an external-memory artifact map/card composition.
- 2026-04-22 chapter folder handoff: 병렬 chapter 작업 폴더는 `docs/03-html/chapters/chapter-XX/`로 두며, CHAPTER 04는 `docs/03-html/chapters/chapter-04/`에 provisional S034-S045 인계 manifest를 둔다.
- 2026-04-22 chapter 04 feedback round 2: S034 pill/al약 keyword rendering is rejected. S037 center card overflow is a blocker. S038 one-line statement must be replaced with a better source-backed line. S039 tool mapping is visually crude and needs a new native rendering strategy. S043 one-line claim must move lower. S044 comparison table is insufficient and needs a new rendering strategy.
- 2026-04-22 chapter 04 lock feedback: S039 bottom synthesis uses `책임과 도구는 1:1이 아니다`, not `도구 이름보다 그 도구가 맡는 책임`. S040 one-line claim must use Anthropic's context engineering phrasing and show source as `Anthropic Research`.
- 2026-04-22 chapter 04 feedback round 3: S037 one-line statement must be checked against source before reuse. Current `하네스 엔지니어링 = 이 네 단계의 신뢰성` is not a source sentence; use source-backed `이 네 지점을 신뢰성 있게 만드는 일`. S036 must emphasize the quote `모델이 아닌 것은 전부 하네스입니다.` and show attribution `LangChain, Vivek Trivedy`. S040 Anthropic phrase must not look like an arbitrary oversized string; render it as a quote/source treatment with appropriate typography. S041 must move away from a generic four-step list into a native MCP/Context Hub architecture layout.
- 2026-04-22 chapter 04 feedback round 4: S036 component cards are too large for their copy and must be rearranged into smaller cards with more breathing room. S038 removes the awkward one-line thesis card. S040 quote must use a dedicated quote card/block, following the same quote-card rule as S036. S041 is split into left-side MCP usage structure and right-side Context Hub MCP role/principle explanation. S039 removes the visible `하네스의 책임 ↔ 하네스의 도구` label. S042 must be replaced after internet research, using RAG paper evidence plus MCP/Context Hub documentation rather than the earlier rough table.
- 2026-04-22 chapter 04 feedback round 5: S036 and S043 body content must be optically centered in the slide body, not biased toward the top band. S040's Anthropic one-line phrase must be translated into natural Korean while keeping the source label. S041 nested-card layout is a validation miss and must be fixed with a contract rule that catches card-inside-card structures. S042 must use internet-researched sentences but avoid translationese; automatic Korean checks are necessary but not sufficient. S044 replaces the bottom one-line statement with a Manus source quote rendered as a dedicated quote block.
- 2026-04-22 chapter 04 feedback round 6: S037 one-line synthesis must change again and should not repeat the rejected/unsatisfying phrase. S040 must explain the Anthropic context idea in plain Korean rather than jargon such as `신호가 큰 토큰`. S041 still reads as card-inside-card; remove card-like parent containers and any `card` class from that slide, then validate both DOM and CSS. S042 must become a multi-card layout, with no visible source line and no `선택 기준`/decision strip. S044 Manus quote must use easier Korean grounded in the source sentence about fixed prefix and variable suffix.
- 2026-04-22 chapter 04 feedback round 7: S037 one-line synthesis is fixed to `거의 모든 에이전트가 반복하는 4단계.`. S040 quote is fixed to `Anthropic의 4가지 전략: 필요한 정보만 남기고 잡음은 덜어낸다.`. S041 should again use left/right card-shaped containers, but only one card layer; the right card must explain `Context 7` as the commonly used MCP server for current docs, not `Context Hub`. S042 must show the difference between `RAG` and `Context 7` as a table, without source/footer extras. S044 attribution changes to `Manus Research`.
- 2026-04-22 chapter 04 feedback round 8: S041 must not read as cards inside cards. The two outer sibling cards are the only card-shaped containers; internal MCP steps and Context 7 role/principle/effect lines must be flat typography and arrows, without inner rounded rectangles, borders, shadows, or card-like row blocks. S044 quote text should not churn after every review; replace it once with the source-backed KV-cache sentence `최신 입력과 도구 결과만 뒤에서 갈아 끼워야 KV-cache hit rate가 살아납니다.` and keep the attribution `Manus Research`.
- 2026-04-22 final main integration: 전역 번호는 main 통합본에서 S001-S094로 확정한다. 기존 1-4장은 S001-S045를 유지하고, 5장은 S046-S055, 6장은 S056-S068, 7장은 S069-S081, 8장은 S082-S090, 9장은 S091-S094로 배치한다. 이 통합은 numbering/registry/generator/validation 확장 작업이며 slide copy와 visual meaning을 함께 수정하지 않는다.
- 2026-04-23 chapter 06-07 main merge: CHAPTER 06-07 worktree의 provisional S046-S071을 main 통합본의 S056-S081로 재번호화한다. main의 최신 source heading을 기준으로 S057은 `하나의 에이전트 = 하나의 역할`, S067은 `멀티 모델과 멀티 에이전트`, S072는 `필요없는 도구는 덜어내라`를 title fixed value로 둔다.
- 2026-04-23 chapter 06-07 reference merge: 사용자가 지정한 page-062~068 reference 문법과 QA blocker를 main 규칙으로 흡수한다. dark split panel `small` contrast와 5-item artifact column clipping은 main 통합 후에도 blocker다.
- 2026-04-23 design/workflow freeze: 사용자가 선호한 page `1-18`, `21`, `24`, `37`, `39`, `40`, `52`, `53`을 deck-wide baseline으로 고정한다. 향후 HTML 피드백 루프에서는 이 묶음을 우선 비교군으로 유지한다.
- 2026-04-23 chapter source split: slide Python source를 chapter folder(`scripts/jaryo_html_deck/slides/chapter_XX/`)로 분리하고, 전체 deck은 one-pass build로 유지한다. 번호 충돌 방지는 파일 경로 분리 + 전역 `spec.order` contiguous 검증으로 강제한다.

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
- S028-S033 chapter label fixed value: `CHAPTER 03`; banned auxiliary labels include `SECTION 3`. 단, 2026-04-23 current-main S029는 사용자 지시에 따라 chapter-label row 제거 예외를 둔다.
- S029 visible copy must stay source-backed timeline evidence only; `Harness`, `Agent`, `Prompt`, `Model`, `Waterfall` topic words are not visible labels on that slide.
- S030 must show `SDD`, `Spec-Driven Development`, `WHAT`, `WHY`, `HOW`, `/speckit.specify`, `/speckit.plan`, `/speckit.tasks`, `[NEEDS CLARIFICATION]`, and `Constitution Check` without turning into a Harness summary page.
- S030 latest layout: 사용자가 명시한 `assets/claude-code-seminar-kakao/page-031.png`의 spec-kit workflow 구조를 참고한다. Three command workflow must read as `SPECIFY` -> `PLAN` -> `TASKS` or equivalent staged command flow, with supporting principle/outcome cards where space permits. 출처에는 `GitHub Copilot icon`과 `GitHub spec-kit`을 visible하게 명시한다. Reference의 warm palette/section pill은 복사하지 않고 minimal-light native layout으로 재구성한다.
- S031 must show `권한 통제`, `Red`, `Green`, `Refactor`, `테스트 코드 임의 수정 금지`, `assert 조건 약화`, and `실패 확인 전 구현 금지` as the TDD control surface.
- S031 latest layout: 사용자가 명시한 `assets/claude-code-seminar-kakao/page-028.png`와 `docs/01-sources/local-canonical/claude-code-seminar-kakao.md` Page 028 transcription을 TDD reference로 쓴다. current-main 29페이지에서는 title을 `TDD`, lead를 `Test-Driven Development`로 두고, 기존 body 맨 위 한 줄과 chapter-label row를 제거한다. `Red`/`Green`/`인간 리뷰 → AI가 리팩토링`, `왜 AI에게 특히 중요한가`, `AI의 치팅에 주의`, `테스트 수정 금지 규칙 필수`는 reference-backed copy로 유지할 수 있다. reference의 warm palette/section pill/character styling은 복사하지 않고 minimal-light native layout으로 재구성한다.
- S031 latest spacing/scale rule: current-main 29페이지의 subtitle-to-body gap은 28페이지 SDD와 비슷한 breathing room을 유지해야 한다. body가 title/lead를 밀어내거나 subtitle 바로 아래에 과밀하게 붙으면 실패다. left flow card와 right control card typography는 SDD page body보다 더 무겁게 보이지 않도록 조정한다.
- S031 latest accent rule: current-main 29페이지 left flow stack의 세로 rail은 프로젝트 기본 blue rule을 사용한다. gray divider로 낮추지 않는다.
- S032 compares `Waterfall` against AI 시대 `SDD + TDD` and does not bridge to Harness.
- S032 latest layout: 좌우로 치우친 sparse split compare를 쓰지 않는다. `assets/claude-code-seminar-kakao/page-032.png`의 column headers + horizontal comparison rows + bottom synthesis 구조를 native layout으로 재구성한다.
- S032 latest copy rule: 사용자가 인터넷 검색을 지시한 revision에서는 Waterfall/SDD 차이를 `Royce 1970 Managing the Development of Large Software Systems`와 GitHub `spec-kit/spec-driven.md` official docs로 보강한다. Waterfall은 요구사항/설계/코딩/테스트가 단계적으로 이어지고 testing이 개발 후반에 실제 제약을 드러낸다는 점, SDD는 specification이 primary artifact가 되고 `/speckit.specify` → `/speckit.plan` → `/speckit.tasks`로 spec/plan/tasks를 실행 기준으로 만든다는 점을 중심으로 압축한다. `문서의 성격`, `검증 타이밍`, `작동 방식`, `검증 루프`처럼 source/search 근거 밖으로 보이는 추상 label은 쓰지 않는다.
- S032 latest alignment/content rule: `SDD` header는 아래 SDD row content column과 같은 column start/center에 맞춘다. Bottom one-line synthesis/dark bar는 제거한다.
- S033 must include `스펙 템플릿`, `계획 문서`, `TDD 루프`, `Skills`, `Hooks`, and `하네스` as the bridge into chapter 4.
- S033 latest layout: `assets/claude-code-seminar-kakao/page-033.png`의 conclusion/card scale 감각을 참고하되, 최신 지시에 따라 중앙 `Spec + TDD` thesis text는 제거한다. Two large cards and bottom synthesis 구조는 유지하고, card size와 내부 글자 크기는 reference처럼 카드 안에서 충분히 읽히도록 재조정한다. warm brown palette와 원본 문구 직접 복사는 금지한다.
- S033 latest size adjustment: copy와 의미 구조는 유지하고 card size만 줄인다. 정보량이 작은 `Spec`/`TDD` 카드는 slide width를 과하게 점유하지 않아야 하며, plus sign과 bottom synthesis의 중심 정렬은 유지한다.
- S033 latest alignment rule: two card columns and bottom synthesis must sit inside the footer safe area without vertical crowding, clipping, or off-center imbalance.
- S033 latest copy rule: `하네스`는 TDD 카드의 종류나 항목으로 배치하지 않는다. TDD card에는 `TDD 루프`, `Skills`, `Hooks`까지만 둔다. `하네스`는 source line의 결론 의미에 따라 bottom synthesis 또는 bridge conclusion에서만 쓴다. S033에는 `SDD + TDD가 Harness로 이어지는 이유`처럼 source-backed 소제목을 visible하게 둔다. 이 소제목/title은 blue accent가 아니라 ink/neutral heading color로 렌더링한다.
- S034-S045 chapter label fixed value: `CHAPTER 04`; banned label: `SECTION 4`.
- S034 visible keywords `Prompt`, `Context`, `Harness` must be readable against the section divider background in screenshot/PDF, not merely present in HTML.
- S034 must not render `Prompt`, `Context`, `Harness` as pill/chip/al약 elements. Use plain text grouping or a non-pill structural treatment on the divider.
- S035 must absorb source page 36/37 meaning into one page: `Prompt`, `Context`, `Harness`, `무엇을/어떻게 말할 것인가`, `무엇을/어떻게 보여줄 것인가`, `무엇을/어떻게 통제할 것인가`, and `Prompt ⊂ Context ⊂ Harness`.
- S036 must combine `Agent = Model + Harness`, `모델이 아닌 것은 전부 하네스입니다.`, and six components: `Context Engineering`, `Tool Orchestration`, `State & Memory`, `Verification Loop`, `Error Recovery`, `Human-in-the-Loop Control`.
- S036 quote fixed value: `모델이 아닌 것은 전부 하네스입니다.`. The quote must be visually emphasized and attributed to `LangChain, Vivek Trivedy`; do not leave it as an unattributed table callout.
- S036 component cards must not be large empty rectangles. Use a quote card plus compact component card arrangement; card size, title size, and body size must read as the same visual scale.
- S036 body group must sit at the optical center of the slide body. If the quote/components group reads as pulled toward the top band, lower the group or center the `table-wrap` content vertically.
- S037 center loop card must keep all text inside the card border at 720pt x 405pt screenshot/PDF size. Any escaped or clipped center-card text blocks acceptance.
- S037 bottom synthesis must stay source-backed. `하네스 엔지니어링 = 이 네 단계의 신뢰성` is rejected because it is not in the source; use the source phrase `이 네 지점을 신뢰성 있게 만드는 일` or a direct source-preserving compression.
- S037 latest rule: visible one-line synthesis fixed value is `거의 모든 에이전트가 반복하는 4단계.`.
- S038 one-line statement is not fixed; choose a stronger source-backed line from rebuilt chapter 4 that clarifies Harness responsibility without adding new semantics.
- S038 latest rule: remove the bottom one-line thesis card. The five responsibility cards are enough; do not add an awkward synthesis sentence on this slide.
- S039 title fixed value: `하네스의 도구`; banned title: `책임과 도구는 1:1이 아니다`. The 1:1 statement may appear only as an internal claim.
- S039 must show the N:N relation between `하네스의 책임` and `하네스의 도구` as a native relationship composition. A dense 9-row table is not acceptable even if copy contract passes.
- S039 rendering strategy must make the tool mapping feel deliberate: grouped responsibility side, grouped tool side, clear many-to-many connector paths, and a visible synthesis claim. Crude table-like mapping or tangled connector density is a blocker.
- S039 bottom synthesis fixed value: `책임과 도구는 1:1이 아니다`. Do not use `도구 이름보다 그 도구가 맡는 책임` as the bottom synthesis on S039.
- S039 must not show the standalone label `하네스의 책임 ↔ 하네스의 도구`. The relationship should be carried by layout and the bottom synthesis, not by a redundant top label.
- S040 one-line claim must be an Anthropic context engineering quote/paraphrase from `Effective context engineering for AI agents`: `smallest set of high-signal tokens`. Visible source label fixed value: `Anthropic Research`.
- S040 Anthropic phrase must be rendered as a quote/source line with restrained typography, not as an oversized bottom slogan that looks visually detached from the Korean slide.
- S040 quote must use the reusable dedicated quote card/block pattern with `blockquote` and `figcaption`; do not render it as a generic flow thesis or plain table/card text.
- S040 visible quote may translate the Anthropic phrase into Korean, but must preserve the meaning of keeping only the smallest high-signal context. Avoid literal translation that reads like machine translation.
- S040 visible quote fixed value is `Anthropic의 4가지 전략: 필요한 정보만 남기고 잡음은 덜어낸다.`. Do not use `Antrophic` spelling, and do not leave `신호가 큰 토큰` in visible copy.
- S041 must not remain a plain process list. Render MCP/Context Hub as a native architecture composition: Agent -> MCP Client -> MCP Server -> connected tools, with Context Hub shown as the current-doc/source side of the same context infrastructure.
- S041 latest rule: left side explains how an agent uses MCP; right side explains what `Context Hub MCP` does and why it works. Avoid a tool-chip pile or generic architecture strip that looks like decoration.
- S041 must not place cards inside cards. Use one flat architecture surface with lanes/rows/arrows and one explanation surface with text blocks, not nested `article` cards inside a parent card.
- S041 latest rule: use two sibling cards, one for MCP 원리 and one for `Context 7`. Nested cards inside either card are forbidden. Rename visible copy from `Context Hub` to `Context 7`.
- S041 internal layout rule: the outer sibling cards are the only card-shaped containers. Internal MCP stages and Context 7 role/principle/effect entries must be flat text/arrows only, with no inner rounded rectangle, inner border, shadow, muted card background, or `article` element.
- S042 latest evidence rule: internet-researched replacement uses `Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks` for RAG and MCP/Context Hub or Context7 official docs for the current-doc side. Visible copy should distinguish indexed retrieval over a broad corpus from selected/current/versioned documentation injected into context.
- S042 copy must be Korean-native. Phrases like `passage 검색`, `retriever 품질`, or stiff translated decision labels are not acceptable unless the English term is necessary and explained by the surrounding Korean rhythm.
- S042 latest layout rule: render a table comparing `RAG` and `Context 7` across source-backed axes: 대상, 강점, 기대, 문제점. Do not show source lines, `선택 기준`, or card-grid remnants.
- `지시문의 고도` / `Right Altitude` is not a rebuilt chapter 4 heading. Do not use it as a slide title; if used, trace it to rebuilt line 115 and local-canonical Page 042 as a compact tool-writing principle.
- CHAPTER 04 must include `Memory: 세션을 넘어서는 기억`; do not drop the Memory section when reducing slide count.
- S043 must render Memory as an external artifact map/card composition around the claim `대화창을 기억 저장소로 착각하지 않는다`. A two-column list table is not acceptable.
- S043 one-line claim must sit lower than the title band and read as a bottom or lower-middle synthesis, not as a crowded top subtitle.
- S043 body group must be optically centered in the slide body while preserving the lower-middle synthesis position of the one-line claim.
- S044 comparison table is not sufficient. Re-render Stable Prefix vs Variable Suffix as a deliberate comparison composition with stronger visual hierarchy than a plain table.
- S044 Manus example must use a source quote, not a loose paraphrase. The quote should be rendered with the reusable dedicated quote card/block pattern and attributed to `Manus 사례`.
- S044 latest attribution fixed value: `Manus Research`.
- S044 latest quote fixed value: `최신 입력과 도구 결과만 뒤에서 갈아 끼워야 KV-cache hit rate가 살아납니다.`. Do not keep changing this quote unless the user explicitly replaces the fixed value.
- Parallel chapter worktree traceability: S034-S045 numbering is provisional for the current CHAPTER 04 worktree. If another chapter changes the final deck length, keep CHAPTER 04 content grouped and only change global numbering during final main integration.
- CHAPTER 04 folder-scoped handoff lives at `docs/03-html/chapters/chapter-04/README.md`; final integration may change `S034`-`S045` to another contiguous range, but content order and chapter-local references should remain stable.
- Final main merge rule: chapter-local worktree outputs may have provisional page numbers. During main integration, first map chapter-local ids to the final contiguous global range, then regenerate flat global `SXXX` slides. Do not overwrite another chapter's flat page paths with provisional output.
- Scoped preview artifact rule: chapter-local decks/data/slides such as `ch06`, `ch07`, or `chapter-08-09` must stay under chapter-scoped paths. They may be copied into main only when the path remains namespaced and cannot collide with `docs/03-html/slides/slide-XXX.html`.
- CHAPTER 06-07 folder-scoped handoff lives at `docs/03-html/chapters/chapter-06-07/README.md`; final integration maps the worktree's provisional `S046`-`S071` to `S056`-`S081`, but content order, source-backed title, and chapter-only QA artifacts remain stable.
- CHAPTER 06-07 invalid titles: `멀티 에이전트 활용`, `실전 워크플로우 & 도구 세팅`, `핵심 패턴 5가지`, `실전 세팅 - 다중 세션 병렬`, `병렬화보다 분해가 먼저다`, `멀티 모델은 멀티 에이전트와 다르다`, `다다익선? 과유불급` are not current rebuilt markdown subheadings, so they must not be final slide titles.
- S016 metric fixed values: `2주`, `1~2일`, `불가능하던 작업 실현`; source에 없는 tool label `Augment Code + Vertex AI`는 visible copy로 쓰지 않는다.
- S017 standalone formula page rule은 CHAPTER 02 rebuild에서 폐기됐다. `Agent = Model + Harness`는 S027 결론 page의 fixed value로 이동한다.
- S017 title fixed value after rebuild: `1막: Copilot과 ChatGPT, 프롬프트의 시대`; `2022~2024`는 generated title이 아니라 body metadata/era badge/rail에 둔다.
- S018 title fixed value after latest feedback: `CoT / ReAct / ToT`; required visible pattern names are `CoT`, `ReAct`, `ToT`, `Chain-of-Thought`, `Tree-of-Thought`. Required ReAct diagram labels are `LM`, `Env`, `Reasoning Traces`, `Actions`, `Observations`, `ReAct (Reason + Act)`.
- S018 latest layout: page-064 style 3-card row, each card same width/height, mini native diagram centered, and one-line meaning only. Required source-backed meaning lines are `중간 추론 단계`, `추론과 행동 반복`, `여러 추론 경로`. Forbidden S018 visible copy includes `2캔 × 3개`, `11개`, `Graph-of-Thought`, `GoT`.
- S018 Gemini CLI experiment scope: Gemini may restructure only S018 implementation/generator artifact. It must not run validation, screenshot, PDF export, deck-wide build, or touch chapter 3 work during this one-off experiment.
- S019 title fixed value after rebuild: `ReAct / Tree-of-Thought`; required pattern names are `ReAct`, `Tree-of-Thought`; raw asset embeds are forbidden.
- S020 title fixed value after rebuild: `Self-Refine / Reflexion`; required pattern names are `Self-Refine`, `Reflexion`; feedback-loop native diagram structure is required.
- S021 Andrew Ng pattern visual은 네 패턴 관계가 보이는 native 2x2 diagram으로 남긴다. `assets/evolution-of-ai-agentic-patterns/05-andrew-ng-agentic-design-patterns.png`의 2x2 pattern panel, mini workspace, node/arrow 구조를 존중하되 raw image embed, 사람 아이콘, diagram 내부 visible text label, source 밖 label 생성은 금지한다. 제목 하위 설명은 `자기 결과를 비판하고 반복 개선`, `외부 도구로 정보 수집과 실행`, `목표를 실행 순서로 나눠 추진`, `전문 역할로 나눠 복잡한 작업 수행`으로 둔다. Planning은 workspace 밖 input node, 내부 accent node에서 세 planning node로 갈라지는 fan-out, 세 output node로 이어지는 병렬 실행 흐름을 구분한다.
- S022 Blind Prompting은 3개 원인 card + 1개 full-width dark quote card 구조로 남긴다. gradient 배경은 금지하고 neutral surface와 border, dark quote card는 `--color-dark-surface`와 white text 대비를 사용한다. 하단 dark card는 `모델은 컨텍스트 창 안에 들어온 지식만 다룰 수 있다.`와 `Vivek Trivedy, LangChain` attribution만 visible로 유지하고, `모델은 보지 못한 것을 알 수 없음`, `문제는 지시문이 아니라 모델이 소비하는 정보`는 visible one-line 문구로 쓰지 않는다.
- S023 title fixed value after rebuild: `2막: Cursor와 컨텍스트의 시대`; 초기 Copilot과 Cursor 계열 도구 비교 구조를 유지한다.
- S024 Cursor architecture는 예외적으로 `assets/evolution-of-ai-agentic-patterns/06-cursor-ai-code-editor-architecture.png` raw asset을 그대로 사용한다. 오른쪽 설명은 source markdown의 `text` 화살표 흐름을 세로 그래프로 재구성하고, raw asset 위에 overlay text를 얹거나 이미지를 crop하지 않는다.
- S025 no-loop fixed values: `좋은 입력만으로는 루프를 통제할 수 없다`, `도구 호출 실패`, `테스트 오해`, `비용 폭주`, `위험 명령`, `보안 경계`, `목표 망각`, `무엇을 하게 할 것인가`, `무엇을 못 하게 막을 것인가`, `어디서 멈출 것인가`, `어떻게 검증할 것인가`. Banned visible values/classes include `gather context`, `take action`, `verify`, `repeat`, `loop-cycle-body`, `loop-cycle-arrow`, `loop-repeat-arc`, `↺ repeat`.
- Current-main S023는 former S025 no-loop/context-wall 의도를 승계하지만, visible copy는 더 압축한다. 현재 main 기준 visible fixed values include `폭주를 만드는 것`, `잘못된 결과나 응답 유입`, `느슨한 실행 권한`, `잘못된 검증`, `먼저 고정할 것`, `허용/차단 범위`, `멈춤 기준`, `검증 경로`, `멈춤 기준과 검증 경로를 먼저 설계해야 한다`. Forbidden S023 structure/class includes `context-wall-body`, `context-wall-grid`, `context-wall-risk-strip`, `context-failure-body`.
- Current-main S023 visible fixed values include `루프`, `도구 호출 실패`, `목표 망각`, `테스트 오해`, `보안 경계`, `잘못된 응답 주입`, `멈춤 기준과 검증 경로를 먼저 설계해야 한다`. Forbidden S023 structure/class includes `context-wall-body`, `context-wall-grid`, `context-wall-risk-strip`, `context-failure-body`, `cache-sequence-body`.
- S026 fixed minimal values: `코딩 도구는 이제 실행 환경을 품는다`, `자동완성·채팅`, `작업 환경 전체`, `파일 · 셸 · 테스트`, `Harness`. Forbidden S026 values/classes include `Plan Mode`, `승인 체계`, `CLAUDE.md`, `Skills`, `Hooks`, `MCP`, `Plugins`, `Subagents`, `허용`, `차단`, `기록`, `harness-era-actor-body`, `harness-era-control-stack`, `harness-era-actor-rail`, `harness-era-signs-body`, `harness-era-bridge-body`.
- S027 relationship fixed value: `Prompt ⊂ Context ⊂ Harness`; banned structure/class: `era-native-nesting`.
- S027 formula fixed value after rebuild: `Agent = Model + Harness`; relationship fixed value: `Prompt ⊂ Context ⊂ Harness`; both must appear on the same conclusion page.
- Current-main S025 title fixed value: `하네스의 시대로`. The long source heading is reduced to keep the title on one line, and the former bottom one-line statement is removed so the page keeps only the era cards plus the two relationship lines.
- S009 `자연어`는 prompt card 내부 장식 label이 아니라 language/category label이다. 카드 안으로 들어오면 실패다.
- S011/S016 3-card layout은 카드 width/height를 동일하게 유지한다.
- S016 metric fixed values `2주`, `1~2일`, `불가능하던 작업 실현`은 카드 상단 핵심 값으로 배치한다.
- S013/S014 body copy는 CHAPTER 01 일반 본문 size와 맞춘다. CHAPTER 02 rebuild 과정의 oversized body는 실패다.
- S018-S021 native diagrams는 approved evolution assets `02-chain-of-thought.png`부터 `05-andrew-ng-agentic-design-patterns.png`와 rendered screenshot/PDF를 직접 비교한다.
- S024 Cursor architecture는 raw 06 asset + source-backed arrow graph로 구성한다. 이전 3-card explanation layout과 fixed native redraw flow는 이 예외 이후 폐기한다.
- S025 context-wall text는 card/chip border 안에 완전히 들어와야 한다.
- S026 latest layout은 one sparse transition page다. Required structure is one large centered claim and a 3-node flow: `자동완성·채팅 -> 작업 환경 전체 -> Harness`. Do not render the earlier action-loop/control-stack/component-rail layout.
- S027은 하단 table을 제거한다. conclusion page는 `Agent = Model + Harness`와 `Prompt ⊂ Context ⊂ Harness` 중심으로 압축한다.
