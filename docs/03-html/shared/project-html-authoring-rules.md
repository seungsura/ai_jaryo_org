# Jaryo HTML Authoring Rules

이 문서는 Jaryo HTML 발표 자료를 작성하거나 수정할 때 따르는 작업 규칙을 한 파일로 압축한 것이다. 최상위 authority는 `docs/03-html/shared/slide-quality-rules.md`이며, 이 문서는 구현자가 빠르게 확인할 수 있는 authoring checklist다.

## 작업 전 필수 확인

모든 HTML 관련 작업 전 아래 파일을 먼저 읽는다.

1. `AGENTS.md`
2. `.codex/subagents/README.md`
3. `.codex/templates/subagent-task-template.md`
4. `docs/03-html/shared/slide-quality-rules.md`
5. `docs/03-html/shared/decision-log.md`
6. `.codex/skills/local/natural-korean-prose/SKILL.md`
7. 대상 source markdown
8. 필요한 사용자 승인 visual reference page
9. 관련 `scripts/jaryo_html_deck/slides/chapter_XX/slide_YYY.py`
10. 관련 generated `docs/03-html/slides/slide-XXX.html`
11. 관련 `docs/03-html/outline/slide-outline.md` entry
12. 관련 `docs/03-html/manifest.md` row

## Authority

- HTML은 canonical source가 아니다.
- canonical source는 `docs/02-seminar/harness-rebuilt-md` 아래 source markdown이다.
- planning sync는 `docs/03-html/outline/slide-outline.md`와 `docs/03-html/manifest.md`를 따른다.
- 실제 구현 단위는 `scripts/jaryo_html_deck/slides/chapter_XX/slide_YYY.py`다.
- generated `docs/03-html/slides/slide-XXX.html`과 `docs/03-html/deck/index.html`은 artifact다. source처럼 직접 수정하지 않는다.
- 사용자와 대화하며 확정한 최신 규칙은 기존 stage 관례, shared design 문서, generator 관성보다 우선한다.

## 작업 모드

- rules/planning 세션에서는 HTML 생성, PDF export, generated HTML 수정, slide source 수정, CSS/generator/test 수정, build/check 실행을 하지 않는다.
- rules-edit mode에서 허용되는 작업은 규칙 문서, decision log, PM packet, open question, handoff 정리다.
- 구현 세션에서는 규칙 기록을 먼저 끝낸 뒤 source-alignment와 slide contract를 확정한다.
- 새 사용자 피드백은 작업 지시이기 전에 rule-candidate다. 구현 전에 `docs/03-html/shared/slide-quality-rules.md`에 먼저 기록한다.
- 피드백 기록에는 적용 범위를 함께 둔다: deck-wide rule, chapter/slide-specific rule, reusable pattern, validation rule, one-off exception.

## Orchestration

- main session은 HTML orchestrator 역할을 맡는다.
- 일반 작업 흐름은 `html-slide-pm -> html-slide-builder -> html-slide-qa -> html-slide-reviewer`다.
- PM gate와 reviewer gate를 건너뛰지 않는다.
- PM은 source-backed task packet, editable-file list, visual-reference obligations, QA checks, reviewer acceptance criteria를 만든다.
- Builder는 PM scope 이후에만 구현한다.
- QA는 static checks, runtime checks, screenshot checks, PDF smoke checks를 범위에 맞게 보고한다.
- Reviewer는 PM packet, builder notes, QA evidence, source markdown, visual reference, artifact를 함께 보고 최종 수용 여부를 판단한다.

## Source Discipline

- local markdown과 사용자가 명시한 reference만 의미 source로 쓴다.
- source/reference 밖 비교 축, label, 의미, 예시, metric, 해설 문구를 만들지 않는다.
- source에 없는 문구가 필요해 보이면 만들지 말고 제거하거나 open question으로 남긴다.
- 사용자가 지정하지 않은 `assets/`, JPG, PNG, PDF는 content source로 보지 않는다.
- visual reference는 composition/layout/diagram soft reference일 뿐 content source가 아니다.
- source markdown의 최신 문구가 stale generated phrasing보다 우선한다.
- source 의미 보존 압축은 허용한다. source 밖 재해석은 금지한다.
- code block은 source code syntax를 보존한다. 새 주석 추가와 임의 축약을 하지 않는다.

## File Ownership

- slide source: `scripts/jaryo_html_deck/slides/chapter_XX/slide_YYY.py`
- shared token: `docs/03-html/shared/tokens.css`
- shared primitive CSS: `docs/03-html/shared/slide-base.css`
- generated slide artifact: `docs/03-html/slides/slide-XXX.html`
- generated deck artifact: `docs/03-html/deck/index.html`
- outline: `docs/03-html/outline/slide-outline.md`
- manifest: `docs/03-html/manifest.md`

## Slide Root Contract

모든 slide root는 manifest와 일치하는 metadata를 선언해야 한다.

```html
<main
  class="slide family-content layout-wide density-medium chapter-02"
  data-slide-id="S024"
  data-shell="process-flow-shell"
  data-notes="..."
  data-footer="default"
>
```

필수 항목:

- `data-slide-id`
- `data-shell`
- `family-*`
- `layout-*`
- `density-*`
- `data-footer`

## Active Shell

- `title-hero-shell`
- `agenda-list-shell`
- `section-divider-shell`
- `statement-editorial-shell`
- `process-flow-shell`
- `split-compare-shell`
- `evidence-table-shell`

새 shell이 필요하면 먼저 `layout-shell-reference.md`, `outline/slide-outline.md`, `manifest.md`를 갱신하고 authority 문서와 충돌하지 않는지 확인한다.

## Runtime Contract

- deck은 standalone artifact다.
- keyboard/touch navigation과 active slide switching을 유지한다.
- print/PDF friendly 구조를 유지한다.
- `data-notes` 저장 슬롯은 허용하지만 notes UI는 넣지 않는다.
- progress bar, fullscreen button, slide counter UI, keyboard hint UI, popup/inline speaker notes panel은 넣지 않는다.
- deck 화면에는 footer 외 visible UI chrome을 두지 않는다.

## CSS Authoring

- shared CSS와 token은 layout primitive의 source of truth다.
- per-slide inline style과 per-slide color override는 금지한다.
- 색은 `theme-minimal-light` token의 역할 안에서 쓴다.
- 새로운 component가 반복될 때만 shared primitive로 승격한다.
- 한 slide 전용 class는 source 의미와 layout 목적이 분명할 때만 둔다.
- nested card처럼 validation에서 막아야 할 구조는 CSS와 DOM 양쪽에서 제거한다.

## HTML Copy

- slide 문구는 한국어를 기본으로 한다.
- English term, product name, path, command, API name, technical vocabulary는 필요한 경우 그대로 둔다.
- slide copy는 명사형 또는 구 단위 중심이다.
- 공손체, 서술형 장문, 명령형을 피한다.
- subtitle/lead는 기본 금지다.
- title은 한 줄 고정이다. 2줄 예상 시 중단하고 확인한다.
- 한국어 문구는 `.codex/skills/local/natural-korean-prose/SKILL.md` 기준으로 다듬는다.
- `check_slide_korean.py` 통과만으로 승인하지 않는다. reviewer가 어색하다고 보면 실패다.

## Visual Authoring

- `theme-minimal-light`, `720pt × 405pt`, Pretendard CDN, footer 기준을 유지한다.
- reference는 raw crop, raw screenshot, character image 복사로 쓰지 않는다.
- 필요한 경우 native diagram, card, table 구조로 재작성한다.
- 첫 장 tool mark는 우상단 실제 asset icon만 사용한다.
- 일반 slide의 tool mark, text pill tool 표기, 본문 pill chip은 금지한다.
- card는 8px 이하 radius를 유지하고 nested card를 만들지 않는다.

## Numbering And Output

- 병렬 worktree나 chapter 작업에서 slide number는 임시값일 수 있다.
- 안정된 추적 기준은 stable slide id, source file, generated artifact다.
- current PDF page number는 사용자 피드백 handle로만 쓴다.
- `PDF page N == SNNN`으로 가정하지 않는다.
- 새 feedback/output artifact는 기존 기준본과 섞지 않는다.
- 권장 output root:
  - `output/html-feedback/<run-id>/chapter_XX/SYYY/`
  - `output/html-feedback/<run-id>/chapter_XX/mini-batch/`
  - `output/pdf-milestones/<build-id>/`

## Feedback Loop

- 한 slide 피드백은 해당 slide source, 해당 slide HTML, 해당 slide screenshot, 해당 slide 검증만 대상으로 삼는다.
- feedback loop에서 전체 deck HTML rebuild, 전체 screenshot sweep, 전체 PDF export를 기본으로 실행하지 않는다.
- 전체 deck/PDF 렌더링은 chapter freeze나 milestone 검증 때만 실행한다.
- mini-batch는 slide 수 기준이 아니라 chapter별 rhythm 기준으로 진행한다.

## Validation

HTML 수정 후 작업 범위에 맞게 아래 검증을 실행한다.

```bash
python3 scripts/check_slide_contract.py
python3 scripts/check_slide_korean.py docs/03-html/slides
python3 scripts/check_deck_runtime.py docs/03-html/deck/index.html
```

필요하면 Playwright screenshot smoke와 PDF smoke를 추가한다.

검증 기준:

- slide contract 통과
- 한국어 copy 품질 통과
- deck runtime 통과
- screenshot/PDF에서 text overlap, clipping, footer drift 없음
- source-backed visible text 확인
- numbering 중복, 누락, 역순 없음

## 금지 항목

- generated `slide-XXX.html` 직접 수정
- source 밖 문구 창작
- 사용자 미승인 asset/PDF를 content source로 사용
- per-slide inline style 남발
- theme 밖 palette 도입
- notes/progress/fullscreen/keyboard hint UI 추가
- card-inside-card 구조
- title 2줄 방치
- source code block 임의 축약
- 자동 검증 없이 구현 종료

## 관련 Source

- `AGENTS.md`
- `.codex/subagents/README.md`
- `.codex/templates/subagent-task-template.md`
- `docs/03-html/shared/slide-quality-rules.md`
- `docs/03-html/shared/decision-log.md`
- `docs/03-html/shared/design.md`
- `docs/03-html/shared/layout-shell-reference.md`
- `docs/03-html/shared/minimal-light-adaptation.md`
- `docs/03-html/shared/make-slide-adoption.md`
