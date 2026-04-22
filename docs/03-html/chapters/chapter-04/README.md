# CHAPTER 04 HTML Handoff

이 폴더는 CHAPTER 04 HTML slide 작업의 folder-scoped handoff다. 전역 slide number는 다른 chapter worktree와 main integration 순서에 따라 바뀔 수 있으므로, 여기의 `S034`-`S045`는 provisional id로만 본다.

## Scope

- worktree: `/Users/seungsu/Desktop/project/jaryo-ch04-html`
- chapter: `CHAPTER 04`
- source: `docs/02-seminar/harness-rebuilt-md/04-프롬프트를 넘어서: 에이전트를 움직이는 기술, Harness.md`
- chapter-local order: 12 slides
- current provisional range: `S034`-`S045`
- generated chapter PDF: `output/pdf/harness-chapter-04-current-720x405.pdf`
- screenshot/PDF smoke artifacts: `output/playwright/chapter-04/`

## Integration Rule

- 최종 main integration 전까지 이 chapter의 전역 번호를 확정값처럼 다루지 않는다.
- 다른 chapter worktree와 합칠 때는 모든 작업 진행사항을 먼저 main에 반영한다.
- 그 다음 마지막 integration step에서 global numbering만 조정한다.
- 번호가 바뀌어도 chapter-local order, slide title, source-backed copy, QA evidence는 이 문서를 기준으로 추적한다.

## Provisional Slides

| provisional id | chapter key | title | generated HTML | generator source | QA artifact |
| --- | --- | --- | --- | --- | --- |
| `S034` | `04-00` | 프롬프트를 넘어서 | `docs/03-html/slides/slide-034.html` | `scripts/jaryo_html_deck/slides/slide_034.py` | `output/playwright/chapter-04/current034.png` |
| `S035` | `04-01` | Prompt, Context, Harness | `docs/03-html/slides/slide-035.html` | `scripts/jaryo_html_deck/slides/slide_035.py` | `output/playwright/chapter-04/current035.png` |
| `S036` | `04-02` | Agent = Model + Harness | `docs/03-html/slides/slide-036.html` | `scripts/jaryo_html_deck/slides/slide_036.py` | `output/playwright/chapter-04/current036.png` |
| `S037` | `04-03` | 에이전트 루프: 하네스의 심장 | `docs/03-html/slides/slide-037.html` | `scripts/jaryo_html_deck/slides/slide_037.py` | `output/playwright/chapter-04/current037.png` |
| `S038` | `04-04` | 하네스의 책임 | `docs/03-html/slides/slide-038.html` | `scripts/jaryo_html_deck/slides/slide_038.py` | `output/playwright/chapter-04/current038.png` |
| `S039` | `04-05` | 하네스의 도구 | `docs/03-html/slides/slide-039.html` | `scripts/jaryo_html_deck/slides/slide_039.py` | `output/playwright/chapter-04/current039.png` |
| `S040` | `04-06` | Context Engineering | `docs/03-html/slides/slide-040.html` | `scripts/jaryo_html_deck/slides/slide_040.py` | `output/playwright/chapter-04/current040.png` |
| `S041` | `04-07` | MCP와 Context 7 | `docs/03-html/slides/slide-041.html` | `scripts/jaryo_html_deck/slides/slide_041.py` | `output/playwright/chapter-04/current041.png` |
| `S042` | `04-08` | RAG vs Context 7 | `docs/03-html/slides/slide-042.html` | `scripts/jaryo_html_deck/slides/slide_042.py` | `output/playwright/chapter-04/current042.png` |
| `S043` | `04-09` | Memory: 세션을 넘어서는 기억 | `docs/03-html/slides/slide-043.html` | `scripts/jaryo_html_deck/slides/slide_043.py` | `output/playwright/chapter-04/current043.png` |
| `S044` | `04-10` | Stable Prefix와 Variable Suffix | `docs/03-html/slides/slide-044.html` | `scripts/jaryo_html_deck/slides/slide_044.py` | `output/playwright/chapter-04/current044.png` |
| `S045` | `04-11` | 하네스는 환경 그 자체다 | `docs/03-html/slides/slide-045.html` | `scripts/jaryo_html_deck/slides/slide_045.py` | `output/playwright/chapter-04/current045.png` |

## Current Validation

- `python3 scripts/build_jaryo_html_deck.py`
- `python3 scripts/check_slide_contract.py`
- `python3 scripts/check_slide_korean.py docs/03-html/slides/slide-034.html docs/03-html/slides/slide-035.html docs/03-html/slides/slide-036.html docs/03-html/slides/slide-037.html docs/03-html/slides/slide-038.html docs/03-html/slides/slide-039.html docs/03-html/slides/slide-040.html docs/03-html/slides/slide-041.html docs/03-html/slides/slide-042.html docs/03-html/slides/slide-043.html docs/03-html/slides/slide-044.html docs/03-html/slides/slide-045.html`
- `python3 scripts/check_deck_runtime.py docs/03-html/deck/index.html`
- `PYTHONDONTWRITEBYTECODE=1 python3 -m pytest -q tests/test_build_jaryo_html_deck.py`
- Playwright screenshot/PDF smoke for `output/playwright/chapter-04/`

## Notes

- 현 generator source는 아직 `scripts/jaryo_html_deck/slides/slide_XXX.py` flat module 구조다. 이 handoff는 병렬 worktree 충돌을 줄이기 위한 chapter-local tracking layer이며, generator source folder relocation은 별도 PM -> builder -> QA -> reviewer gate가 필요한 구조 변경으로 본다.
- final integration에서 번호만 바뀌면 `manifest.md`, `slide-outline.md`, `slide-specs.json`, generated HTML filename, deck index, generator import registry, test fixed values를 함께 조정한다.
