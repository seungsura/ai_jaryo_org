# make-slide Adoption

이 문서는 `make-slide`를 Jaryo HTML stage에 어떻게 번역해서 적용할지 고정하는 계약입니다.

## Input Files

- `README.md`
- `SKILL.md`
- `references/layouts.md`
- `references/html-spec.md`
- `references/core-features.md`
- `themes/minimal-light/README.md`
- `themes/minimal-light/reference.html`

## Adopt

- reference-driven shell reuse
- `minimal-light` 기반의 palette, typography, spacing rhythm
- keyboard navigation
- active slide switching
- print / PDF friendly `@media print`
- `data-notes` 저장 슬롯

## Adapt

- 자유 layout 조합은 `layout family + reference shell`로 좁혀 번역
- single-file output은 최종 artifact인 `docs/03-html/deck/index.html`에만 적용
- slide source는 계속 `docs/03-html/slides/slide-XX.html`로 유지
- speaker notes는 runtime UI가 아니라 후속 notes 문서 단계로 분리

## Reject

- progress bar
- fullscreen button
- slide counter UI
- keyboard hint UI
- popup / inline speaker notes panel
- auto image search
- generic English labels
- demo chrome
- theme gallery 식 multi-theme switching

## Output Contract

- canonical source: `docs/02-seminar/prose/`
- planning sync: `docs/03-html/outline/slide-outline.md`, `docs/03-html/manifest.md`
- slide source: `docs/03-html/slides/slide-XX.html`
- final deck artifact: `docs/03-html/deck/index.html`
- every slide root:
  - `data-slide-id="SXX"`
  - `data-shell="shell-id"`
  - `family-*`
  - `density-*`
- `data-notes`는 허용하지만 notes UI는 넣지 않습니다.
