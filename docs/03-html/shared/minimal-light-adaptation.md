# Minimal Light Adaptation

이 문서는 `make-slide/themes/minimal-light`를 Jaryo seminar deck에 맞게 변환한 적용 기준입니다. 목표는 원본의 밝고 절제된 인상을 가져오되, Jaryo의 canonical prose, shell contract, 한국어 발표 톤을 깨지 않는 것입니다.

## What We Adopt

- 밝은 background와 높은 text contrast
- Pretendard 중심의 precise typography
- 얇은 border와 매우 약한 shadow
- white surface card와 restrained accent blue
- 장식보다 hierarchy와 spacing으로 읽히는 구성

## What We Reject

- generic English tag label
- decorative overline 남발
- 큰 watermark 숫자 장식
- 범용 demo deck에서 쓰는 카드/flow component의 무분별한 재사용
- 한 장에 설명문이 길게 들어가는 body paragraph

## What We Localize For Jaryo

- 발표용 한국어를 우선하고, `Agenda`, `Content`, `Process` 같은 English UI label은 구조적 필요가 없으면 제거
- speaker notes와 next-slide preview 라벨은 한국어로 고정
- shell 중심 구조를 먼저 정하고 copy가 그 shell 안에 맞게 압축되도록 함
- section 흐름과 chapter label을 Jaryo deck rhythm에 맞춤

## Theme Mapping

| make-slide minimal-light | Jaryo adaptation |
| --- | --- |
| `#fafafa` background | `--color-paper` |
| `#ffffff` surface/card | `--color-surface`, `--color-panel` |
| `#1a1a1a` primary text | `--color-ink` |
| `#555555` secondary text | `--color-mute` |
| `#0066cc`, `#0a84ff` accent | `--color-signal`, `--color-support` |
| subtle shadow | `--shadow-card`, `--shadow-soft` |

## Copy Implications

- title은 한 줄 우선, 핵심 명사와 대비 축만 남김
- lead는 설명문이 아니라 방향 문장으로 축약
- agenda item은 `번호 + 짧은 한국어 topic + 한 줄 phrase` 정도로 맞춤
- card나 comparison의 body는 1~2줄 clause 단위로 제한
- code, chart, process slide는 body보다 caption과 takeaway를 우선

## Shell Implications

### `title-hero-shell`

- minimal-light의 clean cover 감각은 유지
- 불필요한 overline은 기본 제거
- subtitle은 한 줄 또는 두 개 clause 이하

### `agenda-list-shell`

- minimal-light card list의 clarity는 채택
- item 설명은 짧게 유지하고, 장황한 서술은 발표 노트로 이동

### `section-divider-shell`

- whitespace를 크게 유지
- chapter marker만 남기고 범용 tag는 두지 않음

### `content-three-step-shell`

- process 감각은 채택하되, step 수와 title 길이를 엄격히 제한
- accent는 하나의 focus step만 강조

### `content-three-card-shell`

- white card + thin border + subtle shadow를 채택
- 카드 내부 문장은 스캔 위주로 압축

## Core Policy

`make-slide/core`에서 가져오는 것은 deck-level interaction UI가 아니라, theme discipline과 layout consistency 원리입니다.

채택:

- spacing rhythm
- typography scale discipline
- shell 재사용
- PDF/print를 염두에 둔 구조 정리

비채택:

- fullscreen button
- progress bar
- slide counter UI
- speaker notes panel
- generic keyboard hint UI
- theme gallery 식 multi-theme switching
