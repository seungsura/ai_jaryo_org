# CHAPTER 08-09 HTML Handoff

이 폴더는 CHAPTER 08-09 HTML slide 작업의 chapter-local handoff다. 원본 main worktree의 branch는 절대 옮기지 않고, 이 작업은 `/Users/seungsu/Code/jaryo-ch08-09-html` detached worktree에서만 진행한다.

## Scope

- worktree: `/Users/seungsu/Code/jaryo-ch08-09-html`
- source 08: `docs/02-seminar/harness-rebuilt-md/08-이 글과 발표가 만들어진 과정.md`
- source 09: `docs/02-seminar/harness-rebuilt-md/09-우리가 다음에 해야 할 일.md`
- canonical reference: `docs/01-sources/local-canonical/claude-code-seminar-kakao.md` Page 076-086 transcription
- visual reference: `assets/claude-code-seminar-kakao/page-076.png` through `page-086.png`, structure-only
- chapter-local deck: `docs/03-html/deck/chapter-08-09.html`
- chapter-local data: `docs/03-html/data/chapter-08-09-slide-specs.json`
- generated slides: `docs/03-html/slides/chapter-08-09/`
- screenshot artifacts: `output/playwright/chapter-08-09/`
- PDF artifact: `output/pdf/harness-chapter-08-09-current-720x405.pdf`
- final main range: `S082`-`S094`
- final main source modules: `scripts/jaryo_html_deck/slides/chapter_08/slide_082.py`-`slide_094.py`

## Integration Rule

- 이 작업의 local id는 최종 전역 `SXXX`가 아니다.
- global `docs/03-html/deck/index.html`, `docs/03-html/manifest.md`, `docs/03-html/outline/slide-outline.md`, `docs/03-html/data/slide-specs.json`는 이번 chapter-only preview의 구현 source가 아니다.
- 최종 main 통합에서는 chapter-local source-backed slide definitions를 먼저 병합하고, 별도 numbering-only pass에서 global slide number를 재계산한다.
- numbering-only pass에서는 slide copy, source mapping, visual structure를 바꾸지 않는다.
- main에 반영된 전역 manifest/outline/deck에서는 `CH08-00`-`CH08-08`을 `S082`-`S090`, `CH09-00`-`CH09-03`을 `S091`-`S094`로 사용한다.

## Fixed User Decisions

- 08 챕터 전환 slide를 둔다.
- 09 챕터 전환 slide를 둔다.
- `speaker notes를 맨 뒤로 밀었다` source section은 이번 HTML slice에서 visible slide로 만들지 않는다.
- `이 제작 과정이 보여 주는 하네스 원리`와 `이 제작 과정이 보여 준 것`은 `이 발표가 증거` slide로 합친다.
- 원문에 존재하지 않는 문장, 비교축, label, metric, 예시, 해설을 창작하지 않는다.
- slide title은 사용자 확정 제목 또는 source/canonical transcription 근거가 있는 제목만 사용한다.

## Detailed Slide Plan

| local id | title | source range | visual structure | visible copy boundary |
| --- | --- | --- | --- | --- |
| `CH08-00` | `이 글과 발표가 만들어진 과정` | source 08 title; canonical Page 076-077 | dark chapter divider | `CHAPTER 08`, title only |
| `CH08-01` | `이 글과 발표가 만들어진 과정` | source 08 lines 1-3; canonical Page 076 | Page 076 native memory/proof layout | `기억하시나요`, `이 발표를`, `코드 한 줄 없이 만든 방법`, `한 것은 하나 - 하네스 설계`, `지금부터 그 증거` |
| `CH08-02` | `이 발표를 만든 방법` | source 08 lines 5-30; canonical Page 077 | pipeline rail with layer cards | `source`, `prose`, `outline`, `html`, `pdf`, `markdown`, `html`, `규칙 문서`, `Spec`, `Harness`, `Skills`; no bottom one-line strip |
| `CH08-03` | `재료 1 source 수집` | source 08 lines 32-38; canonical Page 078 | distinct source boundary cards | `자료 수집`, `유튜브 · 링크드인 · 인터넷 커뮤니티`, `공식 사이트 · 공개 문헌`, `직접 수집한 마크다운 · PDF`, `서로 다른 계층`, `서로 다른 중요도`, `불확실한 부분을 억지로 메우지 않는 구분` |
| `CH08-04` | `재료 2 단일 진실원 만들기` | source 08 lines 40-53; canonical Page 079 for rule consistency only | prose-centered source-of-truth flow | `prose`, `블로그 글처럼 작성`, `source of truth`, `논리 순서`, `주장 강도`, `한국어 문체`, `원본 소스의 누락 방지`, `본문을 벗어날 수 없습니다` |
| `CH08-05` | `재료 3- slides-grab, Skill 경계로 박힌 분리` | source 08 lines 55-67, 83-96; canonical Page 080 | PLAN / DESIGN / EXPORT gate diagram without overlapping arrows | `slides-grab`, `Skill`, `PLAN`, `DESIGN`, `EXPORT`, `slide-outline.md`, `slide-XX.html`, `PDF 변환`, `사용자 승인`; no bottom one-line strip |
| `CH08-06` | `재료 4 규칙 세우기` | source 08 lines 69-96; canonical Page 079 | rule table plus compact tool card | `design contract`, `톤과 분위기`, `색상 팔레트`, `타이포그래피`, `여백과 레이아웃 규칙`, `금지해야 할 표현과 과한 장식`, `slide contract 점검`, `한국어 문장 점검`, `사용 도구: MS의 슬라이드 디자인 규칙 · Google Stitch의 Design.md · Kuneosu/make-slide` |
| `CH08-07` | `생성과 검증을 같은 손에 쥐지 않았다` | source 08 lines 83-96; canonical Page 081 | generation lane and validation lane | `생성자가 자기 결과를 스스로 통과시키게 두면`, `HTML generation`, `기계적 검증`, `사람 검토`, `source와 주장 매핑`, `디자인 계약 위반`, `생성과 검증 분리`; no bottom one-line strip |
| `CH08-08` | `이 발표가 증거` | source 08 lines 102-121; canonical Page 081-082 | merged proof formula without overlapping arrows | `원하는 것을`, `글로 작성`, `규칙을`, `문서로 작성`, `결과를`, `사람이 검증`; no bottom one-line strip |
| `CH09-00` | `우리가 다음에 해야 할 일` | source 09 chapter entry | dark chapter divider | `CHAPTER 09`, title only |
| `CH09-01` | `시작하며: FOMO 와 피로` | source 09 lines 1-7; canonical Page 084 | quote/fear/evidence composition | `AI FoMO`, `지식이 쌓이는 속도보다 감가상각되는 속도가 더 빠르다`, `Simon Willison, 2025`, `뒤처지는 두려움`, `좋은 도구를 못 쓸까`, `남들만 이득 볼까`, `직접 써 보는 일`, `무엇을 남기고 무엇을 버릴지`; no `축소가 아니라 증폭` |
| `CH09-02` | `증폭되는 경험 - 세 개의 증언` | source 09 lines 9-17; canonical Page 085 | three testimony cards plus bottom summary band | `Kent Beck`, `Simon Willison`, `Martin Fowler`, `AI 시대의 경험 - 축소가 아니라 증폭`, `Spec-first`, `TDD`, `Plan-Critic`, `검증 분리` |
| `CH09-03` | `내일부터` | source 09 lines 35-43; canonical Page 086 | stacked action layout plus quote/source line | `글로 먼저`, `CLAUDE.md 1페이지 작성, 또는 반복 업무 1개를 글로 명세`, `직접 써보기`, `터미널 열고 Claude Code 3~4창 - 토큰을 일부러라도 소비`, `도구`, `Oh My Claude Code 설치 - 원리의 자동화`, `박종천` |

## Builder Acceptance Criteria

- Every visible phrase must trace to the source range, canonical transcription, or direct user title decision in this handoff.
- `재료 3` title stays source-backed: `재료 3- slides-grab, Skill 경계로 박힌 분리`.
- No warm brown palette, section pill, character image, or raw screenshot copy from the reference assets.
- No standalone visible `speaker notes` slide.
- CHAPTER 09 maturity slide is replaced in this slice by canonical Page 085 unless the user asks to add it back elsewhere.
- Generated HTML and PDF must fit `720pt x 405pt` with footer safe area intact.
