# HTML Design Contract

이 문서는 `docs/03-html/`의 active design contract다. 최상위 authority는 항상 `docs/03-html/shared/slide-quality-rules.md`이며, 이 문서는 현재 deck 구현자가 빠르게 읽을 수 있도록 theme, shell, typography, validation 기준만 압축해 둔다.

## 읽기 순서

1. `docs/03-html/shared/slide-quality-rules.md`
2. `docs/03-html/shared/decision-log.md`
3. `docs/03-html/outline/slide-outline.md`
4. `docs/03-html/manifest.md`
5. `docs/03-html/shared/layout-shell-reference.md`
6. `docs/03-html/shared/minimal-light-adaptation.md`
7. `docs/03-html/shared/make-slide-adoption.md`

HTML은 canonical source가 아니다. 문장, claim, 구조 의미는 `docs/02-seminar/harness-rebuilt-md` source markdown과 승인된 outline에서만 온다. `docs/03-html/slides/*.html`과 `docs/03-html/deck/index.html`은 artifact이고, 실제 구현 단위는 `scripts/jaryo_html_deck/slides/chapter_XX/slide_YYY.py`다.

## 현재 Deck 계약

- status: 00/01/02 27-slide deck
- theme: `theme-minimal-light`
- size: `720pt × 405pt`
- font: Pretendard CDN
- footer: 좌하단 `Harness 잘 사용하기`, 우하단 page number
- runtime: standalone deck, keyboard/touch navigation, active slide switching, print/PDF 구조
- rejected chrome: progress bar, fullscreen UI, slide counter UI, notes UI, keyboard hint

## Theme

`theme-minimal-light`만 active theme로 둔다.

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

색은 역할로만 사용한다. warm brown palette, copper/brown accent, ivory/paper/beige 계열 token, decorative gradient, section pill, character image 복사는 금지한다. depth는 shadow보다 fill, border, spacing으로 만든다.

## Shell Model

모든 slide root는 `data-slide-id`, `data-shell`, `family-*`, `layout-*`, `density-*`를 manifest와 맞게 선언한다. 현재 active shell은 아래 7개다.

- `title-hero-shell`
- `agenda-list-shell`
- `section-divider-shell`
- `statement-editorial-shell`
- `process-flow-shell`
- `split-compare-shell`
- `evidence-table-shell`

새 shell이 필요하면 먼저 `layout-shell-reference.md`, `outline/slide-outline.md`, `manifest.md`를 갱신한다. 현재 deck에 없는 shell 이름을 design 문서에서 예시로 쓰지 않는다.

## Layout Grammar

- `title`: cover 전용. tool mark는 첫 장 우상단 실제 icon asset만 허용한다.
- `agenda`: compact agenda. subtitle 없이 전체 흐름을 scan 가능하게 둔다.
- `section`: dark divider 성격의 chapter 전환. 일반 요약 page에 쓰지 않는다.
- `statement`: 중앙 claim, quote, 짧은 thesis에 사용한다.
- `process`: 단계, loop, architecture, workflow, source-backed diagram에 사용한다.
- `comparison`: 좌우 대비와 theme accent arrow에 사용한다.
- `table`: 실제 표보다 evidence card, metric card, source fact card까지 포괄한다.

reference-derived soft patterns는 `slide-quality-rules.md`의 `Reusable Patterns`에만 둔다. 이 문서는 per-slide layout 처방을 늘리지 않는다.

## Typography And Copy

- title은 한 줄 고정이다. 2줄이 예상되면 build를 멈추고 확인한다.
- subtitle/lead는 기본 금지이며, source 의미를 잃는 경우에만 최소 문구로 둔다.
- body는 paragraph가 아니라 scan-friendly block이다.
- slide copy는 한국어 clause와 명사형 중심이다.
- 공손체, 명령형, 번역체, 어색한 한국어, 설명문 냄새가 강한 문장, source 밖 helper label은 gate failure 후보다.
- `~의 측면에서`, `~라고 볼 수 있다`, `핵심은 ~ 데 있다` 같은 직역 리듬은 쓰지 않는다.
- 한국문학적 어휘는 허용하되, source-backed claim을 더 또렷하게 만드는 경우로 제한한다. 문예적 장식, 감상적 은유, 발표 가독성을 해치는 말맛은 쓰지 않는다.
- English term, product name, path, command, API name은 필요한 경우 그대로 둔다.
- code block은 source code syntax를 보존하고, 새 주석이나 축약을 넣지 않는다.

## Frame

`content`, `comparison`, `statement`, `process`, `table` 계열은 top-band, body area, footer를 공유한다. `title`, `agenda`, `section`은 예외 frame을 쓸 수 있지만 footer는 기본 유지한다.

chapter label은 deck 전체에서 통일한다. 현재 고정값은 `OPENING`, `CHAPTER 01`, `CHAPTER 02`다.

## Implementation And Validation

- shared CSS와 token은 layout primitive의 source of truth다.
- slide module은 shell을 소비하고, 공용 renderer/file output을 새로 정의하지 않는다.
- inline style과 per-slide color override는 금지한다.
- generated HTML과 deck은 artifact로 검사하고 직접 수정하지 않는다.
- HTML 수정 후에는 작업 범위에 맞게 아래를 실행한다.

```bash
python3 scripts/check_slide_contract.py
python3 scripts/check_slide_korean.py docs/03-html/slides
python3 scripts/check_deck_runtime.py docs/03-html/deck/index.html
```

rules-document only 작업은 HTML 검증을 실행하지 않고, markdown/file scope와 stale reference만 확인한다.
