# Jaryo Design Rules

이 문서는 Jaryo HTML 발표 자료의 디자인 규칙을 한 파일로 압축한 작업용 요약본이다. 최상위 authority는 항상 `docs/03-html/shared/slide-quality-rules.md`이며, 이 문서는 그 규칙을 대체하지 않는다.

## 읽기 순서

1. `AGENTS.md`
2. `docs/03-html/shared/slide-quality-rules.md`
3. `docs/03-html/shared/decision-log.md`
4. `docs/03-html/shared/design.md`
5. `docs/03-html/shared/layout-shell-reference.md`
6. `docs/03-html/shared/minimal-light-adaptation.md`
7. `docs/03-html/shared/make-slide-adoption.md`

## 디자인 원칙

- 디자인은 source 의미를 더 잘 읽히게 만드는 장치다. source markdown이나 사용자가 명시한 reference 밖에서 새 의미, 비교 축, label, metric, 예시를 만들지 않는다.
- reference는 composition, layout rhythm, diagram density, spatial hierarchy를 참고하는 soft reference다. content source가 아니다.
- `Kuneosu/make-slide`에서는 outline-first, theme/layout 분리, shell reuse, standalone deck, keyboard/touch, print/PDF 친화 구조를 가져온다.
- 장식보다 정보 위계, 여백, 대비, typography scale로 설득한다.
- 모든 slide는 발표자가 보는 artifact이자 PDF export 대상이다. browser와 PDF에서 모두 읽혀야 한다.

## Theme

- active theme는 `theme-minimal-light` 하나다.
- slide size는 `720pt × 405pt`다.
- font는 Pretendard CDN을 기준으로 한다.
- footer는 좌하단 `Harness 잘 사용하기`, 우하단 page number를 유지한다.
- 일반 deck 화면에 footer 외 visible UI chrome을 두지 않는다.

## Palette

| role | value |
| --- | --- |
| background | `#fafafa` |
| surface | `#ffffff` |
| border | `#e0e0e0` |
| primary text | `#1a1a1a` |
| secondary text | `#555555` |
| tertiary text | `#444444` |
| accent | `#0066cc` |
| highlight | `#0a84ff` |
| code background | `#f5f5f5` |

- 색은 역할로 사용한다. 새로운 palette를 slide별로 만들지 않는다.
- warm brown palette, copper/brown accent, ivory/paper/beige 계열 token은 금지한다.
- decorative gradient, section pill, character image 복사는 금지한다.
- depth는 강한 shadow보다 fill, border, spacing으로 만든다.

## Typography

- title은 한 줄 고정이다. 2줄이 예상되면 생성 또는 구현을 멈추고 확인한다.
- subtitle/lead는 기본 금지다. source 의미를 잃지 않기 위해 꼭 필요한 경우에만 최소 문구로 둔다.
- body는 긴 paragraph보다 scan-friendly block을 우선한다.
- slide copy는 명사형, 구, 짧은 clause 중심으로 압축한다.
- 공손체, 서술형 장문, 명령형, 보고서식 연결어를 피한다.
- English term, product name, API name, command, path, protocol은 정밀도가 떨어질 때 번역하지 않는다.
- code syntax는 원문을 보존한다. slide를 위해 code block에 새 주석을 넣거나 source-visible 예시를 임의 축약하지 않는다.

## Korean Copy

- 자연스러운 한국어는 English term을 모두 없애는 일이 아니다. 정확한 English term을 한국어 어순과 호흡 안에 놓는 것이다.
- 번역투와 어색한 한국어 표현은 디자인 실패로 본다.
- 금지 후보: `상류/하류`, `강하게 호출된다`, `핵심은 ~ 데 있다`, `~의 측면에서`, `~라고 볼 수 있다`.
- 한국문학적 어휘는 허용한다. 다만 source 의미를 선명하게 압축하고 발표 가독성을 살릴 때만 쓴다.
- 과한 문예체, 감상적 수사, source 밖 은유는 금지한다.

## Layout Grammar

- active shell은 `title-hero-shell`, `agenda-list-shell`, `section-divider-shell`, `statement-editorial-shell`, `process-flow-shell`, `split-compare-shell`, `evidence-table-shell`이다.
- `title`: cover 전용. 첫 장 tool mark는 우상단 실제 asset icon만 허용한다.
- `agenda`: compact agenda. subtitle 없이 전체 흐름을 빠르게 훑을 수 있어야 한다.
- `section`: chapter 진입용 dark divider다. 일반 요약 slide에 남용하지 않는다.
- `statement`: 강한 선언, quote, 짧은 thesis에 사용한다.
- `process`: 단계, loop, architecture, workflow, source-backed diagram에 사용한다.
- `comparison`: 좌우 대비, 층위 비교, 두 축 비교에 사용한다.
- `table`: 실제 표뿐 아니라 evidence card, metric card, source fact card까지 포함한다.

## Cards And Surfaces

- nested card는 금지한다.
- 기본 card radius는 8px 이하로 둔다.
- slide당 핵심 card는 보통 1~3개다.
- reference가 구조적으로 요구하는 경우에만 4-card grid를 허용한다.
- card는 의미 단위가 있을 때만 쓴다. 단순 장식 surface를 늘리지 않는다.
- tool card나 identity card는 실제 icon asset을 우선한다. generic document/file glyph를 쓰지 않는다.
- 일반 본문 slide에서 pill chip, text pill 형태 tool 표기, 일반 tool mark는 금지한다.

## Visual Reference

- current preferred baseline은 `output/pdf/harness-full-main-94-current-720x405.pdf` 기준 page `1-18`, `21`, `24`, `37`, `39`, `40`, `52`, `53`이다.
- current disliked baseline은 같은 PDF 기준 page `41`, `54`, `57-68`이다.
- `assets/claude-code-seminar-kakao`는 가장 원하는 slide style reference다. 특히 page `062-068`은 structure/style baseline이다.
- baseline은 composition, layout rhythm, diagram density, spatial hierarchy만 참고한다.
- baseline의 문구, 비교 축, label, metric, 사례, 해설 의미를 새 content로 가져오지 않는다.
- baseline의 warm brown palette, section pill, character image는 복사하지 않는다.

## Reusable Patterns

- statement page는 한 문장 중심으로 둔다.
- evidence/metric slide는 source-backed 근거 묶음이 보이도록 설계한다.
- 숫자, 근거, 구조, 비교, process, architecture를 보여줘야 하는 slide는 statement 하나로 과하게 압축하지 않는다.
- 검토 후보 layout family: `metric card trio`, `evidence cards without tables`, `evidence table`, `process`, `native diagram`, `split comparison`.
- quote는 dedicated quote card/block으로 처리하고 source label을 함께 둔다.
- architecture는 generic strip보다 관계가 보이는 native diagram으로 구성한다.
- process/loop는 단계와 검증 지점이 보이게 만든다.

## 금지 항목

- source 밖 의미 생성
- reference 문구 직접 차용
- generated slide HTML을 source처럼 직접 수정
- warm brown, copper, ivory, beige palette 도입
- decorative gradient, watermark 숫자 장식, demo chrome
- progress bar, fullscreen UI, slide counter UI, keyboard hint UI, notes popup UI
- title 2줄 방치
- subtitle/lead 남발
- card 안 card
- pill/chip 남발
- body paragraph 장문화
- 자동 검사를 통과했다는 이유로 어색한 한국어를 승인

## 품질 기준

- visible text는 source markdown, 승인 reference, 또는 사용자 직접 지시와 연결되어야 한다.
- slide는 browser screenshot과 PDF export에서 모두 읽혀야 한다.
- 제목, 본문, footer가 서로 겹치거나 clipping되면 실패다.
- body group은 footer safe area 안에 있어야 한다.
- 정보량이 작은 card가 slide 폭을 과하게 점유하면 재조정한다.
- 자동 검증과 reviewer 판단을 함께 통과해야 한다.

## 관련 Source

- `AGENTS.md`
- `docs/03-html/shared/slide-quality-rules.md`
- `docs/03-html/shared/decision-log.md`
- `docs/03-html/shared/design.md`
- `docs/03-html/shared/layout-shell-reference.md`
- `docs/03-html/shared/minimal-light-adaptation.md`
- `docs/03-html/shared/make-slide-adoption.md`
