# Layout Shell Reference

이 문서는 132장 `make-slide` 기반 상세본에서 사용하는 shell catalog입니다. 이번 버전은 `minimal-light`의 layout rhythm을 그대로 가져오되, Jaryo deck에 필요한 slide type만 좁혀서 고정합니다.

`docs/03-html/shared/slide-quality-rules.md`가 최상위 authority입니다. 이 catalog는 shell 구조를 보조하며, 최신 규칙이나 `decision-log.md`의 보충 결정과 충돌하면 `slide-quality-rules.md`를 따릅니다.

## Shell Registry

| shell id | slide type | layout | use when | required core structure |
| --- | --- | --- | --- | --- |
| `title-hero-shell` | `title` | `centered` | cover와 opening statement | `cover-main`, `cover-rule`, `title-placeholder`, `hero-points`, `footer` |
| `agenda-list-shell` | `agenda` | `wide` | deck map, chapter inventory | `agenda-header`, `agenda-list`, `agenda-item`, `footer` |
| `section-divider-shell` | `section` | `centered` | chapter 진입, appendix 전환 | `section-main`, `chapter-marker`, `title-placeholder`, `section-keywords`, `footer` |
| `statement-editorial-shell` | `statement` | `editorial` | 강한 선언, 결론, short thesis | `statement-panel`, `statement-tag`, `statement-text`, `statement-support`, `footer` |
| `wide-bullets-shell` | `bullets` | `wide` | 일반 본문, 주장-근거, checklist | `top-band`, `body-area`, `callout-card`, `bullet-list`, `footer` |
| `process-flow-shell` | `process` | `wide` | 단계, 연대기, 원칙 묶음, workflow | `top-band`, `process-track`, `process-step`, `footer` |
| `split-compare-shell` | `comparison` | `split` | 대비, 층위, 두 축 비교, map | `top-band`, `compare-grid`, `compare-col`, `footer` |
| `evidence-table-shell` | `table` | `wide` | 표, source map, reference matrix | `top-band`, `table-wrap`, `data-table`, `footer` |
| `closing-shell` | `closing` | `centered` | 마지막 takeaway, appendix closing | `closing-main`, `cover-rule`, `title-placeholder`, `closing-points`, `footer` |

## Shell Rules

- 모든 slide는 `data-slide-id`, `data-shell`, `family-*`, `layout-*`, `density-*`를 같이 선언합니다.
- `minimal-light` theme는 전 deck에서 고정하고, shell만 slide type에 따라 교체합니다.
- `centered`는 title, section, closing만 사용합니다.
- `wide`는 표, 연대기, workflow, 일반 bullets에 사용합니다.
- `split`은 비교와 대조에만 사용합니다.
- `editorial`은 강한 statement slide에만 제한적으로 씁니다.

## Root Contract

```html
<main
  class="slide family-content layout-wide density-medium"
  data-slide-id="S042"
  data-shell="wide-bullets-shell"
  data-notes="..."
  data-footer="default"
>
```

`data-slide-id`, `data-shell`, `family-*`, `layout-*`, `density-*`는 manifest와 같아야 합니다.
