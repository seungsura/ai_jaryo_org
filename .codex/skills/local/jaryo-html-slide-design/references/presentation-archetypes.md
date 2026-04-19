# PowerPoint Layout Families

이 문서는 Jaryo HTML slide 작업에서 사용할 `PowerPoint template / layout family` 기준을 정리한 reference입니다. 이 문서는 자유로운 시각 실험을 위한 메모가 아니라, `design.md`, `SKILL.md`, `slide-XX.html`이 따라야 하는 구조적 기준입니다.

## Normative Sources

- Microsoft Support, `Keep your presentation on-brand with Copilot`
  - https://support.microsoft.com/en-us/topic/keep-your-presentation-on-brand-with-copilot-046c23d5-012e-49e0-8579-fe49302959fc
- Microsoft Support, `What is a slide layout?`
  - https://support.microsoft.com/en-us/office/what-is-a-slide-layout-99da5716-92ee-4b6a-a0b5-beea45150f3a
- Microsoft Support, `Apply a slide layout`
  - https://support.microsoft.com/en-us/office/apply-a-slide-layout-158e6dba-e53e-479b-a6fc-caab72609689
- Anthropic official skill, `frontend-design`
  - https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md
- `tfriedel/claude-office-skills`
  - https://github.com/tfriedel/claude-office-skills

## Working Principles Extracted From Sources

1. Slide는 theme만 맞춘다고 presentation이 되지 않습니다.
   - Microsoft 기준에서 Copilot은 `sample slides`, `layouts`, `objects`, `prompt`를 함께 봅니다.
   - 따라서 deck는 `한 장씩 예쁘게`가 아니라 `layout family가 반복되는 template`로 설계해야 합니다.

2. 모든 slide는 `명확한 intent`를 가져야 합니다.
   - slide를 보면 바로 `Title`, `Agenda`, `Section`, `Content`, `Conclusion` 중 무엇인지 읽혀야 합니다.
   - intent가 흐리면 generic output이 나옵니다.

3. 각 slide는 이름 붙은 `layout family` 하나를 선택해야 합니다.
   - `layout family`는 PowerPoint의 slide layout과 같은 개념입니다.
   - slide마다 새로운 composition을 만들지 않습니다.

4. `placeholder role`이 먼저이고, decoration은 나중입니다.
   - title, body, media, caption, footer 같은 역할이 먼저 정해져야 합니다.
   - helper label, badge, pill, eyebrow, decorative chrome은 기본값이 아닙니다.

5. sample slide는 `완결된 예시`여야 합니다.
   - Microsoft 기준에서도 fragment library보다 complete slide example이 더 잘 작동합니다.
   - 따라서 reusable layout class와 실제 sample slide를 함께 유지합니다.

6. density도 layout 선택의 일부입니다.
   - light, medium, heavy 중 하나를 정하고 slide를 만듭니다.
   - heavy content를 light layout에 억지로 밀어 넣지 않습니다.

7. theme consistency는 layout consistency와 함께 가야 합니다.
   - colors, fonts, spacing, footer, background는 theme 층입니다.
   - layout family는 content placement 층입니다.
   - 이 둘을 섞어서 즉흥적으로 바꾸지 않습니다.

8. rendered output 검증은 필수입니다.
   - `claude-office-skills`가 강조하듯 reusable assets와 generated output을 분리하고, 실제 render를 검증해야 합니다.
   - HTML/CSS 역시 브라우저 screenshot 없이 끝내지 않습니다.

9. `frontend-design`에서 빌릴 것은 미감이 아니라 태도입니다.
   - 분명한 aesthetic direction 하나를 고르고 끝까지 밀어붙입니다.
   - generic AI web UI처럼 보이는 타협형 화면을 만들지 않습니다.

## Required Jaryo Layout Families

이 프로젝트는 아래 7개 family만 기본값으로 사용합니다.

### 1. `title`

- opening slide
- strongest title hierarchy
- subtitle 또는 metadata 허용
- footer는 optional
- body module grid 금지

### 2. `agenda`

- deck 구조 안내
- section list 또는 map 중심
- dense paragraph 금지
- 빠른 scan 우선

### 3. `section`

- section divider
- 한 문장 또는 짧은 clause 중심
- whitespace 크게 사용
- 본문형 module 금지

### 4. `content`

- 가장 일반적인 본문형 family
- title + optional lead + one main content placeholder
- list, process, simple diagram, progression, key points에 사용

### 5. `comparison`

- title + 2~3 comparison columns
- column heading과 body가 명확해야 함
- 차이를 만드는 한 축만 강조

### 6. `visual`

- image, screenshot, diagram이 주인공
- text는 title, caption, short callout만 허용
- visual이 argument를 수행해야 함

### 7. `conclusion`

- 요약, next step, takeaway
- title + short summary body
- closing rhythm 유지

## Placeholder Roles

아래 역할만을 기본 placeholder vocabulary로 사용합니다.

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

- non-title slide는 기본적으로 `title` placeholder를 가집니다.
- `content`, `comparison`, `visual`, `conclusion`은 footer placeholder를 가집니다.
- placeholder text는 styling 참고용일 뿐, instruction layer가 아닙니다.
- content가 placeholder에 맞지 않으면 layout family를 바꾸고, 임시 장식을 추가하지 않습니다.

## Density Bands

모든 slide는 아래 중 하나를 선택합니다.

- `light`
  - title와 짧은 supporting text 중심
- `medium`
  - title + lead + 1개 main content block
- `heavy`
  - title + structured body + multiple aligned placeholders

Rules:

- `title`, `section`은 보통 `light`
- `agenda`, `content`, `comparison`은 주로 `medium`
- `comparison`, `visual`만 예외적으로 `heavy` 허용

## HTML Implementation Mapping

- `docs/03-html/shared/tokens.css`
  - PowerPoint theme에 해당
- `docs/03-html/shared/slide-base.css`
  - Slide Master / layout family class에 해당
- `docs/03-html/slides/slide-XX.html`
  - sample slide에 해당
- `docs/03-html/outline/slide-outline.md`
  - slide intent, layout family, density 기록
- `docs/03-html/manifest.md`
  - 구현 상태 bookkeeping

## Jaryo Skill Implications

`jaryo-html-slide-design`는 다음 순서를 강제해야 합니다.

1. source section과 slide intent 확인
2. layout family 선택
3. density 선택
4. placeholder plan 작성
5. shared layout class 사용 또는 확장
6. slide 구현
7. browser render 검증
8. outline / manifest 동기화

## Prohibited Patterns

- slide마다 다른 시각 문법 발명
- decorative pill, eyebrow, helper label을 기본값처럼 남용
- dashboard card, landing page hero, browser chrome 사용
- title이 없는 content slide
- footer alignment drift
- layout family 없이 one-off composition 작성
- render 검증 없이 종료
