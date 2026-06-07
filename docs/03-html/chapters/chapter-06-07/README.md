# CHAPTER 06-07 HTML Handoff

이 폴더는 CHAPTER 06-07 HTML slide 작업의 folder-scoped handoff다. detached worktree의 provisional `S046`-`S071`은 main 통합본에서 `S056`-`S081`로 재번호화했다.

## Scope

- worktree: `/Users/seungsu/Code/jaryo-ch06-07-html`
- chapter: `CHAPTER 06` + `CHAPTER 07`
- source: `docs/02-seminar/harness-rebuilt-md/06-멀티 에이전트 활용 패턴.md`
- source: `docs/02-seminar/harness-rebuilt-md/07-실전 워크플로우와 도구 세팅.md`
- approved reference transcription: `docs/01-sources/local-canonical/claude-code-seminar-kakao.md` Page 063-074
- chapter-local order: 26 slides
- provisional worktree range: `S046`-`S071`
- final main range: `S056`-`S081`
- final main source modules: `scripts/jaryo_html_deck/slides/chapter_06/slide_056.py`-`slide_081.py`
- final generated HTML: `docs/03-html/slides/slide-056.html`-`slide-081.html`
- generated chapter PDF target: `output/pdf/harness-chapter-06-07-current-720x405.pdf`
- screenshot/PDF smoke artifacts: `output/playwright/chapter-06-07/`

## Integration Rule

- 이 chapter의 전역 번호는 final main integration에서 `S056`-`S081`로 확정한다.
- 다른 chapter worktree와 합칠 때도 content order, slide title, source-backed copy, QA evidence는 이 문서를 기준으로 추적한다.
- slide title은 rebuilt markdown 원문 소제목만 사용한다.
- detached worktree의 provisional id에는 `+10`을 적용해 final main id를 얻는다.
- final main source heading drift는 main의 최신 `docs/02-seminar/harness-rebuilt-md`를 우선한다.

## Final Main Slides

| final id | chapter key | title | generated HTML | generator source | QA artifact |
| --- | --- | --- | --- | --- | --- |
| `S056` | `06-01` | 왜 하나의 에이전트만으로는 부족한가 | `docs/03-html/slides/slide-056.html` | `scripts/jaryo_html_deck/slides/chapter_06/slide_056.py` | `output/playwright/chapter-06-07/current056.png` |
| `S057` | `06-02` | 하나의 에이전트 = 하나의 역할 | `docs/03-html/slides/slide-057.html` | `scripts/jaryo_html_deck/slides/chapter_06/slide_057.py` | `output/playwright/chapter-06-07/current057.png` |
| `S058` | `06-03` | 1. Sub-Agent: 중간 작업을 격리하는 기본형 | `docs/03-html/slides/slide-058.html` | `scripts/jaryo_html_deck/slides/chapter_06/slide_058.py` | `output/playwright/chapter-06-07/current058.png` |
| `S059` | `06-04` | Advisor 전략: 작은 실행자, 큰 자문 | `docs/03-html/slides/slide-059.html` | `scripts/jaryo_html_deck/slides/chapter_06/slide_059.py` | `output/playwright/chapter-06-07/current059.png` |
| `S060` | `06-05` | 2. Orchestrator: 계획자 하나가 여러 실행자를 배치한다 | `docs/03-html/slides/slide-060.html` | `scripts/jaryo_html_deck/slides/chapter_06/slide_060.py` | `output/playwright/chapter-06-07/current060.png` |
| `S061` | `06-06` | 3. Parallel: 같은 목표를 평면으로 벌리고 나중에 합친다 | `docs/03-html/slides/slide-061.html` | `scripts/jaryo_html_deck/slides/chapter_06/slide_061.py` | `output/playwright/chapter-06-07/current061.png` |
| `S062` | `06-07` | 4. GAN-Style: 생성자와 평가자를 분리한다 | `docs/03-html/slides/slide-062.html` | `scripts/jaryo_html_deck/slides/chapter_06/slide_062.py` | `output/playwright/chapter-06-07/current062.png` |
| `S063` | `06-08` | 5. Agent Teams: 양방향 대화가 가능한 팀을 만든다 | `docs/03-html/slides/slide-063.html` | `scripts/jaryo_html_deck/slides/chapter_06/slide_063.py` | `output/playwright/chapter-06-07/current063.png` |
| `S064` | `06-09` | Sub-Agent와 Agent Team은 다르다 | `docs/03-html/slides/slide-064.html` | `scripts/jaryo_html_deck/slides/chapter_06/slide_064.py` | `output/playwright/chapter-06-07/current064.png` |
| `S065` | `06-10` | 설계 원칙: 패턴보다 경계가 중요하다 | `docs/03-html/slides/slide-065.html` | `scripts/jaryo_html_deck/slides/chapter_06/slide_065.py` | `output/playwright/chapter-06-07/current065.png` |
| `S066` | `06-11` | 설계 원칙: 패턴보다 경계가 중요하다 | `docs/03-html/slides/slide-066.html` | `scripts/jaryo_html_deck/slides/chapter_06/slide_066.py` | `output/playwright/chapter-06-07/current066.png` |
| `S067` | `06-12` | 멀티 모델과 멀티 에이전트 | `docs/03-html/slides/slide-067.html` | `scripts/jaryo_html_deck/slides/chapter_06/slide_067.py` | `output/playwright/chapter-06-07/current067.png` |
| `S068` | `06-13` | 결론: 더 많은 AI가 아니라 더 좁은 역할의 AI 여럿 | `docs/03-html/slides/slide-068.html` | `scripts/jaryo_html_deck/slides/chapter_06/slide_068.py` | `output/playwright/chapter-06-07/current068.png` |
| `S069` | `07-01` | 시작하며: 두 가지 막다른 길 | `docs/03-html/slides/slide-069.html` | `scripts/jaryo_html_deck/slides/chapter_07/slide_069.py` | `output/playwright/chapter-06-07/current069.png` |
| `S070` | `07-02` | OMC(Oh My Claude Code) | `docs/03-html/slides/slide-070.html` | `scripts/jaryo_html_deck/slides/chapter_07/slide_070.py` | `output/playwright/chapter-06-07/current070.png` |
| `S071` | `07-03` | Plan-Critic-Build | `docs/03-html/slides/slide-071.html` | `scripts/jaryo_html_deck/slides/chapter_07/slide_071.py` | `output/playwright/chapter-06-07/current071.png` |
| `S072` | `07-04` | 필요없는 도구는 덜어내라 | `docs/03-html/slides/slide-072.html` | `scripts/jaryo_html_deck/slides/chapter_07/slide_072.py` | `output/playwright/chapter-06-07/current072.png` |
| `S073` | `07-05` | Approval, Auto-accept, Plan Mode | `docs/03-html/slides/slide-073.html` | `scripts/jaryo_html_deck/slides/chapter_07/slide_073.py` | `output/playwright/chapter-06-07/current073.png` |
| `S074` | `07-06` | 반복의 자산화 | `docs/03-html/slides/slide-074.html` | `scripts/jaryo_html_deck/slides/chapter_07/slide_074.py` | `output/playwright/chapter-06-07/current074.png` |
| `S075` | `07-07` | Ralph Loop | `docs/03-html/slides/slide-075.html` | `scripts/jaryo_html_deck/slides/chapter_07/slide_075.py` | `output/playwright/chapter-06-07/current075.png` |
| `S076` | `07-08` | 암묵지를 파일로 뽑아내라 | `docs/03-html/slides/slide-076.html` | `scripts/jaryo_html_deck/slides/chapter_07/slide_076.py` | `output/playwright/chapter-06-07/current076.png` |
| `S077` | `07-09` | 한 모델에만 기대지 않는다 | `docs/03-html/slides/slide-077.html` | `scripts/jaryo_html_deck/slides/chapter_07/slide_077.py` | `output/playwright/chapter-06-07/current077.png` |
| `S078` | `07-10` | cmux와 Git Worktree | `docs/03-html/slides/slide-078.html` | `scripts/jaryo_html_deck/slides/chapter_07/slide_078.py` | `output/playwright/chapter-06-07/current078.png` |
| `S079` | `07-11` | 세션이 아니라 이슈가 상태를 들고 간다 | `docs/03-html/slides/slide-079.html` | `scripts/jaryo_html_deck/slides/chapter_07/slide_079.py` | `output/playwright/chapter-06-07/current079.png` |
| `S080` | `07-12` | 첫 주에 바로 세울 수 있는 최소 워크플로우 | `docs/03-html/slides/slide-080.html` | `scripts/jaryo_html_deck/slides/chapter_07/slide_080.py` | `output/playwright/chapter-06-07/current080.png` |
| `S081` | `07-13` | 결론: 실전 워크플로우의 중심은 운영 구조다 | `docs/03-html/slides/slide-081.html` | `scripts/jaryo_html_deck/slides/chapter_07/slide_081.py` | `output/playwright/chapter-06-07/current081.png` |

## Current Validation

- `python3 scripts/build_jaryo_html_deck.py`
- `python3 scripts/check_slide_contract.py`
- `python3 scripts/check_slide_korean.py`
- `pytest -q tests/test_build_jaryo_html_deck.py`
- `python3 scripts/check_deck_runtime.py docs/03-html/deck/index.html`
- chapter-local Korean target: `python3 scripts/check_slide_korean.py docs/03-html/slides/slide-056.html docs/03-html/slides/slide-057.html docs/03-html/slides/slide-058.html docs/03-html/slides/slide-059.html docs/03-html/slides/slide-060.html docs/03-html/slides/slide-061.html docs/03-html/slides/slide-062.html docs/03-html/slides/slide-063.html docs/03-html/slides/slide-064.html docs/03-html/slides/slide-065.html docs/03-html/slides/slide-066.html docs/03-html/slides/slide-067.html docs/03-html/slides/slide-068.html docs/03-html/slides/slide-069.html docs/03-html/slides/slide-070.html docs/03-html/slides/slide-071.html docs/03-html/slides/slide-072.html docs/03-html/slides/slide-073.html docs/03-html/slides/slide-074.html docs/03-html/slides/slide-075.html docs/03-html/slides/slide-076.html docs/03-html/slides/slide-077.html docs/03-html/slides/slide-078.html docs/03-html/slides/slide-079.html docs/03-html/slides/slide-080.html docs/03-html/slides/slide-081.html`

## Notes

- generated `docs/03-html/slides/slide-XXX.html` files are artifacts. Source implementation lives in `scripts/jaryo_html_deck/slides/chapter_XX/slide_YYY.py`.
- Page 063-074 canonical transcription was used only within the approved scope. Page 063 numbers and canonical-only OMC claims were not used as slide copy.
- Final main title corrections: `S057` is `하나의 에이전트 = 하나의 역할`, `S067` is `멀티 모델과 멀티 에이전트`, and `S072` is `필요없는 도구는 덜어내라`.
