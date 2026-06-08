# CHAPTER 03 HTML Handoff

이 폴더는 CHAPTER 03 HTML slide 작업의 folder-scoped handoff다. 전역 slide number는 다른 chapter worktree와 main integration 순서에 따라 바뀔 수 있으므로, 여기의 `S028`-`S033`은 provisional id로만 본다.

## Scope

- worktree: `/Users/seungsu/Code/jaryo`
- branch: `main`
- chapter: `CHAPTER 03`
- source: `docs/02-seminar/harness-rebuilt-md/03-AI 시대의 개발 방법론.md`
- chapter-local order: 6 slides
- current provisional range: `S028`-`S033`
- generated chapter PDF: `output/pdf/harness-chapter-03-current-720x405.pdf`
- screenshot/PDF smoke artifacts: `output/playwright/chapter-03/`

## Integration Rule

- 최종 main integration 전까지 이 chapter의 전역 번호를 확정값처럼 다루지 않는다.
- 다른 chapter worktree와 합칠 때는 모든 작업 진행사항을 먼저 main에 반영한다.
- 그 다음 마지막 integration step에서 global numbering만 조정한다.
- 번호가 바뀌어도 chapter-local order, slide title, source-backed copy, QA evidence는 이 문서를 기준으로 추적한다.
- numbering-only pass에서는 slide copy, visual structure, source-backed meaning을 함께 바꾸지 않는다.

## Provisional Slides

| local order | provisional id | chapter key | title | generated HTML | generator source | QA artifact |
| --- | --- | --- | --- | --- | --- | --- |
| 01 | `S028` | `03-00` | AI 시대의 개발 방법론 | `docs/03-html/slides/slide-028.html` | `scripts/jaryo_html_deck/slides/chapter_03/slide_028.py` | `output/playwright/chapter-03/current028.png` |
| 02 | `S029` | `03-01` | 왜 지금 방법론 | `docs/03-html/slides/slide-029.html` | `scripts/jaryo_html_deck/slides/chapter_03/slide_029.py` | `output/playwright/chapter-03/current029.png` |
| 03 | `S030` | `03-02` | SDD | `docs/03-html/slides/slide-030.html` | `scripts/jaryo_html_deck/slides/chapter_03/slide_030.py` | `output/playwright/chapter-03/current030.png` |
| 04 | `S031` | `03-03` | TDD (Test-Driven Development) | `docs/03-html/slides/slide-031.html` | `scripts/jaryo_html_deck/slides/chapter_03/slide_031.py` | `output/playwright/chapter-03/current031.png` |
| 05 | `S032` | `03-04` | Waterfall vs SDD | `docs/03-html/slides/slide-032.html` | `scripts/jaryo_html_deck/slides/chapter_03/slide_032.py` | `output/playwright/chapter-03/current032.png` |
| 06 | `S033` | `03-05` | SDD + TDD가 Harness로 이어지는 이유 | `docs/03-html/slides/slide-033.html` | `scripts/jaryo_html_deck/slides/chapter_03/slide_033.py` | `output/playwright/chapter-03/current033.png` |

## Current Validation

- `PYTHONDONTWRITEBYTECODE=1 python3 -m pytest -q tests/test_build_jaryo_html_deck.py::BuildJaryoHtmlDeckTest::test_chapter_03_revision_6_focus`
- `PYTHONDONTWRITEBYTECODE=1 python3 scripts/check_slide_contract.py`
- `PYTHONDONTWRITEBYTECODE=1 python3 scripts/check_slide_korean.py docs/03-html/slides/slide-030.html docs/03-html/slides/slide-032.html docs/03-html/slides/slide-033.html`
- `PYTHONDONTWRITEBYTECODE=1 python3 scripts/check_deck_runtime.py docs/03-html/deck/index.html`
- Playwright screenshot/PDF smoke for `output/playwright/chapter-03/`

## Notes

- `S028`-`S033`은 current global numbering일 뿐 final numbering이 아니다.
- final integration에서 번호만 바뀌면 `manifest.md`, `slide-outline.md`, `slide-specs.json`, generated HTML filename, deck index, generator import registry, test fixed values를 함께 조정한다.
