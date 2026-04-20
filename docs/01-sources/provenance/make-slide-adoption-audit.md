# make-slide Adoption Audit

- repo: `Kuneosu/make-slide`
- audit date: `2026-04-19`
- role: approved external design/process reference

## Repo Status

- `make-slide`는 Jaryo의 canonical source가 아닙니다.
- 이번 저장소에서는 `docs/03-html/` 단계의 design/process reference로만 채택합니다.
- 채택 대상은 shell reuse, `minimal-light` theme 감각, 최소 deck runtime입니다.

## Files Checked

- `README.md`
- `SKILL.md`
- `references/layouts.md`
- `references/html-spec.md`
- `references/core-features.md`
- `themes/minimal-light/README.md`
- `themes/minimal-light/reference.html`

## Adopt / Adapt / Reject

### Adopt

- reference-driven build discipline
- theme와 layout을 분리해서 보는 사고
- `minimal-light` 기반의 palette, typography, spacing rhythm
- keyboard navigation과 print/PDF 대응
- `data-notes` 같은 note storage slot

### Adapt

- 자유 layout 조합은 Jaryo의 `layout family + reference shell` 체계로 좁혀 번역
- single HTML output은 final deck artifact로만 제한
- speaker notes는 runtime UI가 아니라 `data-notes` 저장과 후속 문서 생성으로 분리

### Reject

- progress bar
- fullscreen button
- slide counter
- keyboard hint
- notes popup / inline panel
- theme gallery 식 multi-theme 운영
- auto image search
- generic English demo labels

## Local Target Map

- `docs/01-sources/approved-external/make-slide.md`
- `docs/03-html/shared/make-slide-adoption.md`
- `docs/03-html/shared/design.md`
- `docs/03-html/shared/minimal-light-adaptation.md`
- `docs/03-html/shared/layout-shell-reference.md`
- `docs/02-seminar/prose/08-how-this-presentation-was-made.md`
- `docs/02-seminar/prose/90-appendix-references.md`
