# Layout Shell Reference

이 문서는 현재 Jaryo HTML deck에서 승인된 active shell catalog입니다. `make-slide`의 layout rhythm은 참고하지만, 실제 shell id는 manifest와 generator model에 존재하는 값만 둡니다.

`docs/03-html/shared/slide-quality-rules.md`가 최상위 authority입니다. 이 catalog는 shell 구조를 보조하며, 최신 규칙이나 `decision-log.md`의 보충 결정과 충돌하면 `slide-quality-rules.md`를 따릅니다.

## Shell Registry

| shell id | slide type | layout | use when | required core structure |
| --- | --- | --- | --- | --- |
| `title-hero-shell` | `title` | `centered` | cover | cover body, title, presenter/meta, footer |
| `agenda-list-shell` | `agenda` | `wide` | deck map, chapter inventory | agenda header/side, ordered item list, footer |
| `section-divider-shell` | `section` | `centered` | chapter 진입, appendix 전환 | chapter marker, title, optional keyword list, footer |
| `statement-editorial-shell` | `statement` | `editorial` | 강한 선언, 결론, short thesis | top band, source-backed claim/quote body, footer |
| `process-flow-shell` | `process` | `wide` | 단계, 연대기, 원칙 묶음, workflow | top band, process/diagram body, footer |
| `split-compare-shell` | `comparison` | `split` | 대비, 층위, 두 축 비교, map | top band, split comparison body, footer |
| `evidence-table-shell` | `table` | `wide` | evidence card, metric card, source fact card, 표 | top band, table/card body, footer |

## Shell Rules

- 모든 slide는 `data-slide-id`, `data-shell`, `family-*`, `layout-*`, `density-*`를 같이 선언합니다.
- `minimal-light` theme는 전 deck에서 고정하고, shell만 slide type에 따라 교체합니다.
- `centered`는 title과 section에서만 사용합니다.
- `wide`는 표, 연대기, workflow, 일반 bullets에 사용합니다.
- `split`은 비교와 대조에만 사용합니다.
- `editorial`은 강한 statement slide에만 제한적으로 씁니다.
- reference-derived soft patterns는 shell을 대체하지 않습니다. source-backed content를 active shell 안에 배치하는 구조 후보로만 씁니다.

## Root Contract

```html
<main
  class="slide family-content layout-wide density-medium chapter-02"
  data-slide-id="S024"
  data-shell="process-flow-shell"
  data-notes="..."
  data-footer="default"
>
```

`data-slide-id`, `data-shell`, `family-*`, `layout-*`, `density-*`는 manifest와 같아야 합니다.
