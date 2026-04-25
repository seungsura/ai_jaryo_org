# Chapter 05 Manifest

- chapter: `05`
- source: `docs/02-seminar/harness-rebuilt-md/05-이렇게 하면 망한다: 한계와 실패 패턴.md`
- worktree: `/Users/seungsu/Desktop/project/jaryo-ch05-html`
- numbering: provisional, subject to final main integration
- final main range: `S046`-`S055`
- final main source modules: `scripts/jaryo_html_deck/slides/chapter_05/slide_046.py`-`slide_055.py`
- review artifact: `pdf/harness-chapter-05-current-720x405.pdf`

| local order | provisional slide id | file | source heading | source block | status |
| --- | --- | --- | --- | --- | --- |
| 05-00 | `S034` | `slides/slide-034.html` | 이렇게 하면 망한다 | page-056 / chapter opener | feedback-round-1-applied |
| 05-01 | `S035` | `slides/slide-035.html` | 오류의 나비효과 | `05-01` | feedback-round-1-applied |
| 05-02 | `S036` | `slides/slide-036.html` | 작업이 길어질 때 특히 위험한 이유 | `05-02` | feedback-round-6-applied |
| 05-03 | `S037` | `slides/slide-037.html` | 컨텍스트가 길수록 항상 좋은 것은 아니다 | `05-03` | feedback-round-4-applied |
| 05-04 | `S038` | `slides/slide-038.html` | 대표 실패 패턴 네 가지 | `05-04` | feedback-round-3-applied |
| 05-05 | `S039` | `slides/slide-039.html` | 현실에서 보이는 증상들 | `05-05` | feedback-round-6-applied |
| 05-06 | `S040` | `slides/slide-040.html` | Context Rot: 길어진 기억은 조용히 썩는다 | `05-06` | feedback-round-4-applied |
| 05-07 | `S041` | `slides/slide-041.html` | 신뢰는 조율되어야 한다 | `05-07` | feedback-round-4-applied |
| 05-08 | `S042` | `slides/slide-042.html` | 결정 제어와 확률 제어를 분리하라 | `05-08` | feedback-round-4-applied |
| 05-09 | `S043` | `slides/slide-043.html` | 더 긴 컨텍스트보다 더 좋은 게이트 | `05-09` | feedback-round-6-audited-no-edit |

## Validation

- `python3 scripts/check_slide_contract.py`: passed for 43 slides
- `python3 scripts/check_slide_korean.py docs/03-html/slides`: passed for 43 files, unrelated warnings on S007/S008 only
- `python3 scripts/check_deck_runtime.py docs/03-html/deck/index.html`: passed for 43 slides
- `python3 -m pytest -q tests/test_build_jaryo_html_deck.py`: passed, 6 tests
- Playwright screenshot QA: regenerated after feedback round 6; see `screenshots/contact-sheet-034-043.png` and `screenshots/contact-sheet-036-043.png`
- PDF smoke: regenerated from the HTML deck print path after feedback round 6; 10 pages, `720.0pt x 404.88pt`; rendered with PyMuPDF; see `screenshots/pdf-contact-sheet-034-043.png`
- S040 no-photo contract: round 4 removed the external photo exception. S040 is rendered as a native diagram only; no external photo asset, image data URI, or photo provenance remains in the slide output.
- S043 round 6 audit: no source/CSS edit. Contract, screenshot, and PDF show no clipping or footer collision, but reviewer marked the slide conditional rather than final-quality approved because the composition remains airy and slightly top-heavy.
- Main integration smoke: local `S034`-`S043` maps to global `S046`-`S055`. Final 94-slide deck validation passed after remapping, with latest feedback applied to global `S048`, `S049`, and `S051`.
