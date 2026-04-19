# Layout Shell Reference

이 문서는 `make-slide`의 theme/layout reference 개념을 현재 Jaryo deck에 맞게 좁혀서 적용한 shell catalog입니다. 모든 slide는 HTML generation 전에 승인된 `reference shell` 하나를 선택해야 합니다.

## Shell Registry

| shell id | family | default density | use when | required core structure |
| --- | --- | --- | --- | --- |
| `title-hero-shell` | `title` | `light` | cover나 opening statement가 필요할 때 | `cover-main`, `cover-rule`, `title-placeholder`, optional `lead-placeholder`, `footer` |
| `agenda-list-shell` | `agenda` | `medium` | deck map이나 chapter list를 보여 줄 때 | `agenda-header`, `title-placeholder`, `agenda-list`, repeated `agenda-item`, `footer` |
| `section-divider-shell` | `section` | `light` | chapter 진입 또는 구조적 전환을 보여 줄 때 | `section-main`, `chapter-marker`, `title-placeholder`, optional `section-keywords`, `footer` |
| `content-three-step-shell` | `content` | `medium` | 3단계 progression이나 before/after 흐름을 보여 줄 때 | `top-band`, `chapter-label`, `title-placeholder`, `top-band-rule`, `body-area`, `progression-board`, repeated `progress-step`, `footer` |
| `content-three-card-shell` | `content` | `medium` | 3개 핵심 항목을 균형 있게 비교하거나 역할 이동을 보여 줄 때 | `top-band`, `chapter-label`, `title-placeholder`, `top-band-rule`, `body-area`, `role-shift-board`, repeated `role-shift-card`, `footer` |

## Shell Rules

- `reference shell`은 `layout family`보다 더 구체적인 HTML skeleton id입니다.
- 같은 shell을 재사용할 때는 wrapper 계층과 주요 class 이름을 유지합니다.
- 한 slide에서 shell id는 하나만 사용합니다.
- shell drift가 필요해 보이면 기존 shell을 무너뜨리지 말고 outline 단계에서 새 shell을 제안합니다.
- footer는 기본적으로 유지합니다. 예외 페이지는 manifest와 HTML root에서 함께 선언해야 합니다.

## Root Contract

모든 slide root는 아래 형태를 기본값으로 사용합니다.

```html
<main
  class="slide family-content density-medium"
  data-slide-id="S04"
  data-shell="content-three-step-shell"
>
```

`family-*`, `density-*`, `data-slide-id`, `data-shell`은 manifest와 같아야 합니다.

## Shell Notes

### `title-hero-shell`

- cover 메시지를 한 번에 읽히게 하는 shell입니다.
- body를 과도하게 붙이지 않습니다.
- subtitle이 길어지면 shell을 바꾸는 것이 아니라 copy를 줄입니다.

### `agenda-list-shell`

- 구조를 스캔시키는 shell입니다.
- agenda item은 가능한 한 같은 리듬으로 맞춥니다.
- 설명문 대신 chapter label + 핵심 phrase 조합을 우선합니다.

### `section-divider-shell`

- chapter 진입을 분명히 하는 shell입니다.
- section slide를 일반 content slide처럼 채우지 않습니다.
- `chapter-marker`와 title의 위계가 흔들리면 deck rhythm이 무너집니다.

### `content-three-step-shell`

- 흐름과 progression을 보여 주는 shell입니다.
- step 수를 임의로 늘리기보다 supporting point를 줄입니다.
- focus step은 하나만 두는 것을 기본값으로 합니다.

### `content-three-card-shell`

- 비교 가능한 세 항목을 정렬하는 shell입니다.
- 세 카드의 문장 길이와 정보 밀도 차이가 너무 커지면 tone gate에서 수정 대상으로 봅니다.
- card 수를 늘리거나 helper badge를 추가하지 않습니다.

## Review Questions

- 이 slide는 family뿐 아니라 shell까지 승인됐는가
- HTML이 shell의 required structure를 그대로 따르는가
- 이 slide가 shell을 벗어나 one-off composition으로 흘렀는가
- 같은 shell을 쓰는 다른 slide와 rhythm이 맞는가
