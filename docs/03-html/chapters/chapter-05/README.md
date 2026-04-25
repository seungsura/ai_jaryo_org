# Chapter 05 HTML Staging

이 폴더는 병렬 worktree에서 만든 5장 HTML 작업의 chapter-local staging root다.

- staging slide id `S034`-`S043`은 chapter worktree의 provisional numbering이다.
- final main integration range는 `S046`-`S055`다.
- global generator source는 `scripts/jaryo_html_deck/slides/chapter_05/slide_046.py`부터 `slide_055.py`까지다.
- review와 피드백 식별자는 `chapter-05 + local order + source heading`을 우선한다.
- flat `docs/03-html/slides/`, `docs/03-html/deck/index.html`, global manifest/outline/spec JSON은 QA용 generated artifact이며 최종 통합 시 일괄 재번호화 대상이다.

## Contents

- `manifest.md`: chapter-local slide registry and source mapping
- `slides/`: generated chapter 05 slide HTML copies with provisional worktree numbers
- `screenshots/`: Playwright visual QA screenshots, contact sheets, and PDF-rendered PNGs
- `pdf/`: chapter-05-only PDF export
