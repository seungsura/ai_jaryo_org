# design.md

## Purpose

이 문서는 `docs/03-html/` 단계에서 HTML slide가 따라야 하는 design contract입니다. 이 계약의 목적은 한 장씩 임의 composition을 만드는 것이 아니라, PowerPoint template처럼 `theme + layout family + placeholder role + verification` 체계를 고정하는 것입니다.

## Normative Sources

- Microsoft Support, [Keep your presentation on-brand with Copilot](https://support.microsoft.com/en-us/topic/keep-your-presentation-on-brand-with-copilot-046c23d5-012e-49e0-8579-fe49302959fc)
- Microsoft Support, [What is a slide layout?](https://support.microsoft.com/en-us/office/what-is-a-slide-layout-99da5716-92ee-4b6a-a0b5-beea45150f3a)
- Microsoft Support, [Apply a slide layout](https://support.microsoft.com/en-us/office/apply-a-slide-layout-158e6dba-e53e-479b-a6fc-caab72609689)
- Kuneosu, [make-slide](https://github.com/Kuneosu/make-slide)
- revfactory, [harness](https://github.com/revfactory/harness)
- Anthropic official skill, [frontend-design](https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md)
- [tfriedel/claude-office-skills](https://github.com/tfriedel/claude-office-skills)

이 문서는 다음 로컬 파일과 함께 읽습니다.

- `docs/03-html/outline/slide-outline.md`
- `docs/03-html/manifest.md`
- `docs/03-html/shared/tokens.css`
- `docs/03-html/shared/layout-shell-reference.md`
- `docs/03-html/shared/minimal-light-adaptation.md`
- `.codex/skills/local/jaryo-html-slide-design/references/presentation-archetypes.md`

## Template Model

이 프로젝트에서 HTML slide는 아래처럼 대응됩니다.

- `tokens.css`
  - PowerPoint `theme`
- `slide-base.css`
  - PowerPoint `slide master / layout family`
- `slide-XX.html`
  - template를 사용하는 actual sample slide
- `outline/manifest`
  - slide intent, layout family, density bookkeeping

HTML은 canonical source가 아닙니다. 문장과 논지는 항상 `docs/02-seminar/prose/`와 approved outline을 따릅니다.

## Reference-Driven Build Model

`make-slide`에서 가져오는 핵심은 매번 새 layout을 발명하지 않고, 승인된 reference를 따라 shell을 고정하는 방식입니다. 이 프로젝트에서는 이를 `layout family + reference shell` 모델로 적용합니다.

- `layout family`
  - 큰 구조 범주
  - `title`, `agenda`, `section`, `content`, `comparison`, `visual`, `conclusion`
- `reference shell`
  - family 안에서 실제 HTML skeleton을 고정하는 더 구체적인 id
  - 예: `title-hero-shell`, `agenda-list-shell`, `content-three-step-shell`

Rules:

- 모든 slide는 `layout family`, `density`, `reference shell`을 함께 선언합니다.
- `reference shell`은 `docs/03-html/outline/slide-outline.md`와 `docs/03-html/manifest.md`에 기록합니다.
- HTML root는 아래 두 attribute를 가져야 합니다.
  - `data-slide-id="SXX"`
  - `data-shell="shell-id"`
- shell이 정해지기 전에는 HTML generation을 시작하지 않습니다.
- shell을 바꾸려면 outline과 manifest를 먼저 수정합니다.

활성 shell 목록과 required structure는 `docs/03-html/shared/layout-shell-reference.md`를 기준으로 합니다.

## Generation Model

- 한국어 slide planning / slide copy / speaker notes 생성 경로: `gemini -m gemini-3.1-pro-preview`
- HTML/CSS 생성 경로: Codex
- Codex 책임: HTML generation, deck consistency auditing, render 검증, outline/manifest 동기화

## Producer-Reviewer Loop

`revfactory/harness`에서 가져오는 핵심은 producer와 reviewer를 분리하고, 재작업 범위를 gate 결과로 고정하는 방식입니다. 이 프로젝트에서는 아래 loop를 deck 운영의 기본값으로 둡니다.

1. `slide-outline-planner`
2. `chapter-slide-pm-ko` / `exception-slide-pm-ko`
3. `korean-slide-copywriter-gemini`
4. `storyline-auditor-ko` + `korean-tone-auditor-ko`
5. `html-slide-builder`
6. `html-deck-consistency-auditor` + `html-slide-designer`
7. final deck gate
8. PDF export / speaker notes

Rules:

- reviewer는 asset을 직접 고치지 않고 `PASS`, `REVISE`, `BLOCK`만 반환합니다.
- `REVISE` 또는 `BLOCK`이면 exact rework scope를 남겨야 합니다.
- approved outcome만 outline/manifest에 반영합니다.
- rework delta는 internal agent output에 남기고, 다음 batch에서 같은 drift가 반복되지 않게 prompt와 template를 갱신합니다.

## Theme Rules

theme는 deck 전체에서 한 번 정하고 유지합니다.

- primary background: `paper`
- primary text: `ink`
- primary emphasis: `signal`
- secondary support: `support`
- muted metadata: `mute`

Theme rules:

- 색은 역할로만 사용합니다.
- 한 slide에서 primary emphasis는 하나만 둡니다.
- 배경은 평면적이어야 하며, decorative gradient를 기본값으로 쓰지 않습니다.
- depth는 shadow보다 fill, border, spacing으로 만듭니다.
- slide마다 theme를 바꾸지 않습니다.

현재 deck의 active theme는 `theme-minimal-light`입니다. 이 테마는 `make-slide`의 `minimal-light`를 Jaryo용으로 정제한 변형이며, `theme-slate`, `theme-warm`, `theme-forest`는 비교용 study로만 유지합니다.

## Palette Candidates

아래 3개 palette를 현재 sample 비교용 후보로 둡니다.

### `theme-minimal-light`

- paper: `#FAFAFA`
- ink: `#1A1A1A`
- signal: `#0066CC`
- support: `#0A84FF`
- character: Apple-style minimal light를 가져오되, Jaryo의 Korean presentation rhythm에 맞게 장식 요소를 줄인 기본 테마

### `theme-warm`

- paper: `#F6F1E8`
- ink: `#0F172A`
- signal: `#E85D2A`
- support: `#0F766E`
- character: warm editorial, 가장 기본값에 가까운 톤

### `theme-slate`

- paper: `#EDF3F7`
- ink: `#111827`
- signal: `#2563EB`
- support: `#0F766E`
- character: cooler and more executive, 기술 세미나 톤에 적합

### `theme-forest`

- paper: `#F1EFE7`
- ink: `#1F2B24`
- signal: `#B45309`
- support: `#3F6212`
- character: research / strategy tone, 묵직하고 절제된 느낌

## Typography Rules

- primary sans: `Pretendard`
- fallback: `Noto Sans KR`, `Apple SD Gothic Neo`, `Malgun Gothic`, `sans-serif`
- title은 항상 가장 강한 위계
- body는 paragraph가 아니라 scan-friendly blocks
- non-title slide는 title placeholder를 기본값으로 가집니다
- English term은 precision이 필요한 경우만 유지
- minimal-light adaptation에서는 얇고 밝은 surface 위에서 rhythm이 무너지기 쉬우므로 body 길이를 더 엄격하게 제한합니다
- standard page의 상단 title band 안 title은 반드시 한 줄 유지
- standard page title은 wrap 금지, 필요하면 font size를 줄이고 line break를 넣지 않음

## Layout Families

slide는 아래 family 중 하나만 선택합니다.

### `title`

- opening slide
- title placeholder 필수
- lead 또는 metadata optional
- footer 사용

### `agenda`

- agenda 또는 deck map
- title placeholder 필수
- body는 list/map 형태
- dense paragraph 금지

### `section`

- section divider
- title placeholder 필수
- short clause 중심
- 큰 whitespace 허용
- footer 사용

### `content`

- 일반 본문형 slide
- title placeholder 필수
- lead optional
- 하나의 main body placeholder 사용
- process, list, simple progression, key-point board 허용

### `comparison`

- title placeholder 필수
- 2~3 aligned columns
- column heading / column body 분리
- 차이를 만드는 한 축만 강조

### `visual`

- title placeholder 필수
- media placeholder 필수
- caption optional
- text는 보조 역할만 수행

### `conclusion`

- title placeholder 필수
- short summary body
- next step 또는 takeaway 허용

## Reference Shell Rules

현재 active deck에서 승인된 shell id는 아래와 같습니다.

- `title-hero-shell`
- `agenda-list-shell`
- `section-divider-shell`
- `content-three-step-shell`
- `content-three-card-shell`

Rules:

- shell id는 kebab-case로 유지합니다.
- shell id는 하나의 family에만 속합니다.
- 같은 shell을 쓸 때는 placeholder hierarchy와 주요 class 이름을 바꾸지 않습니다.
- 새 shell이 필요하면 먼저 `layout-shell-reference.md`와 outline/manifest를 갱신한 뒤 build를 시작합니다.
- `minimal-light`에서 보이는 generic tag, overline, decorative num은 shell 구조상 필요가 있을 때만 제한적으로 채택합니다.

## Placeholder Contract

허용 placeholder role:

- `chapter`
- `title`
- `lead`
- `body`
- `column-heading`
- `column-body`
- `media`
- `caption`
- `footer-left`
- `footer-right`

Rules:

- helper label, eyebrow, pill, badge는 placeholder role이 아닙니다.
- source가 요구하지 않으면 decorative label을 만들지 않습니다.
- placeholder text는 styling guide가 아니라 content container입니다.
- content가 placeholder에 맞지 않으면 layout family를 바꾸고, ad-hoc wrapper를 추가하지 않습니다.

## Standard Page Frame

`content`, `comparison`, `visual`, `conclusion` family는 기본적으로 아래 frame을 공유합니다.

- top title band
  - 고정 위치
  - `chapter` placeholder와 `title` placeholder 포함
  - title은 한 줄 유지
- body area
  - family별 main placeholder
- footer
  - `footer-left`: `Harness 잘 사용하기`
  - `footer-right`: page number

chapter label rules:

- 모든 standard page는 chapter label을 동일한 위치에 둡니다.
- label wording은 deck 전체에서 통일합니다.
- 현재 기본 표기는 `CHAPTER 01` 형식으로 사용합니다.

## Frame Exceptions

아래 family는 standard page frame 예외입니다.

- `title`
- `agenda`
- `section`

이 세 family는 top title band와 chapter label을 다르게 쓰거나 생략할 수 있습니다.
footer는 deck 공통 요소로 유지합니다.

## Density Rules

모든 slide는 density를 선언합니다.

- `light`
  - title와 짧은 supporting text 중심
- `medium`
  - title + optional lead + one structured body
- `heavy`
  - multiple aligned placeholders

Rules:

- `title`, `section`은 주로 `light`
- `content`, `agenda`, `comparison`은 주로 `medium`
- `comparison`, `visual`만 제한적으로 `heavy`

## Copy Rules

- 언어 기본값은 한국어
- 공손체 금지
- 문장보다 짧은 clause 우선
- 정말 필요한 문구만 남기고, 설명문과 부연문은 기본적으로 제거
- slide 한 장에는 한 개의 핵심 목적만 유지
- title은 slide intent를 압축해서 바로 읽히게 작성
- helper translation, English UI label, 장식용 category label 금지
- slide 관련 한국어 작성은 Gemini를 사용하되, 모델명은 항상 `gemini-3.1-pro-preview`로 고정
- line, connector, meter, divider는 의미를 전달할 때만 사용하고, 장식 목적이면 제거
- `minimal-light`의 clean tone을 유지하기 위해 subtitle, lead, card body는 특히 짧게 유지합니다.

## Korean Tone Acceptance

- title, lead, body는 발표용 scan rhythm을 유지해야 합니다.
- 한 줄로 읽히는 clause를 기본값으로 삼고, prose-like 문장 완결은 예외로 취급합니다.
- `습니다`, `입니다` 같은 공손체 ending이 slide copy에 나오면 기본적으로 gate failure 후보입니다.
- 길고 설명적인 문장은 note로 보내고, slide에는 claim과 contrast만 남깁니다.
- English technical term은 유지하되, 한국어 구조를 깨는 직역체 문장은 허용하지 않습니다.

## Footer Rules

- 모든 slide는 footer를 기본값으로 사용
- `footer-left`와 `footer-right`는 shared placement 유지
- footer text는 content보다 약한 위계 유지
- page index 표기는 deck 전체에서 일관되게 유지
- 기본 footer-left는 `Harness 잘 사용하기`

## Review Gates

이 deck는 아래 gate를 통과해야 다음 단계로 넘어갑니다.

### Pre-HTML Gate

- `storyline-auditor-ko`
- `korean-tone-auditor-ko`

둘 다 `PASS`일 때만 HTML generation 허용

### Post-HTML Gate

- `html-deck-consistency-auditor`
- `html-slide-designer`

둘 다 `PASS`일 때만 다음 chapter batch 또는 final deck gate 진행 허용

### Final Deck Gate

- `storyline-auditor-ko`
- `korean-tone-auditor-ko`
- `html-deck-consistency-auditor`
- `html-slide-designer`

이 gate를 통과한 뒤에만 PDF export와 speaker notes 진행 허용

## HTML Implementation Rules

- shared CSS가 layout family의 source of truth입니다.
- slide file은 layout family를 소비해야지 다시 정의하면 안 됩니다.
- slide 안의 structure는 placeholder hierarchy가 먼저 보여야 합니다.
- slide root는 `data-slide-id`와 `data-shell`을 함께 가져야 합니다.
- inline style 사용 금지
- per-slide color override 금지
- render 결과가 겹치거나 잘리면 layout을 고치거나 content를 줄입니다.

## Contract Validation Commands

아래 두 검사는 chapter batch build 이후와 final deck gate 전에 기본으로 실행합니다.

```bash
python3 scripts/check_slide_contract.py
python3 scripts/check_slide_korean.py docs/03-html/slides
```

Rules:

- automated check 통과는 review gate의 필요조건이지 충분조건은 아닙니다.
- script error가 남아 있으면 `PASS`를 줄 수 없습니다.
- warning은 reviewer가 맥락을 보고 해석하되, 반복 warning은 prompt/template 보정 대상으로 봅니다.

## Deck Chrome Policy

`make-slide/core`의 runtime 개념은 참고하되, Jaryo deck에는 발표용 UI chrome를 올리지 않습니다.

Rules:

- fullscreen button, progress bar, slide counter UI, speaker notes panel, keyboard hint UI를 deck 화면에 두지 않습니다.
- deck의 시각적 고정 요소는 footer만 사용합니다.
- footer 기본값:
  - 좌측 하단: `Harness 잘 사용하기`
  - 우측 하단: 현재 페이지 번호
- 예외 페이지가 필요하면 outline과 manifest에 먼저 명시하고, HTML root에 `data-footer="none"`을 선언합니다.
- 예외 footer는 cover나 special divider처럼 구조적으로 필요한 경우만 허용합니다.

## Prohibited Patterns

- floating shell
- browser chrome
- SaaS dashboard card composition
- landing page hero / aside split
- decorative pill / eyebrow / helper label
- 영어 섹션명이나 임시 메타 문구를 slide 상단에 삽입
- title 없는 content slide
- one-off composition
- 과한 shadow
- slide마다 다른 footer 위치
- standard page에서 wrap 되는 top title
- standard page에서 위치가 흔들리는 chapter label

## Review Checklist

- slide intent가 명확한가
- layout family가 outline과 manifest에 기록됐는가
- reference shell이 outline과 manifest, HTML root에 같이 기록됐는가
- title placeholder가 존재하는가
- density가 family와 맞는가
- content가 placeholder를 넘치지 않는가
- footer가 family 규칙에 맞는가
- generic webpage처럼 보이지 않는가
- automated contract / Korean tone check를 실행했는가
- browser render를 실제로 확인했는가
