# make-slide Adoption

이 문서는 `make-slide`를 Jaryo HTML stage에 어떻게 번역해서 적용할지 정리한 보조 계약입니다. 최상위 authority는 `docs/03-html/shared/slide-quality-rules.md`이며, `docs/03-html/shared/decision-log.md`는 preserved Decision Log를 보충합니다.

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
- outline-first, theme/layout 분리, shell reuse, standalone deck artifact 중심 workflow

## Adapt

- 자유 layout 조합은 `layout family + reference shell`로 좁혀 번역
- single-file output은 최종 artifact인 `docs/03-html/deck/index.html`에만 적용
- generated slide HTML은 artifact로 유지하고, 실제 slide 구현 단위는 `scripts/jaryo_html_deck/slides/slide_XXX.py`로 둠
- speaker notes는 runtime UI가 아니라 후속 notes 문서 단계로 분리
- upstream main에는 Jaryo가 그대로 사용할 `make-slide` subagent 파일이 없으므로, workflow/runtime 원칙을 project-local subagents와 prompt template로 번역

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
- implementation unit: `scripts/jaryo_html_deck/slides/slide_XXX.py`
- generated slide artifact: `docs/03-html/slides/slide-XX.html`
- final deck artifact: `docs/03-html/deck/index.html`
- every slide root:
  - `data-slide-id="SXX"`
  - `data-shell="shell-id"`
  - `family-*`
  - `density-*`
- `data-notes`는 허용하지만 notes UI는 넣지 않습니다.
