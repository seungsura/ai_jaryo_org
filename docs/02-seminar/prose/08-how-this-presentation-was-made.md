# 이 발표가 만들어진 과정: Codex를 어디에 넣었는가

## 시작하며: 우리는 장표부터 만들지 않았다

이 발표를 만든 방식도 앞에서 설명한 원리를 그대로 따랐습니다. 처음부터 slide 툴을 열고 문장을 채운 것이 아닙니다. 먼저 source를 잠그고, 그 source를 prose로 정리하고, 그 prose를 outline으로 압축한 뒤, 마지막에 `Codex`가 HTML/CSS를 만들게 했습니다. `PDF`와 speaker notes는 그 다음이었습니다. 순서를 바꾸면 결과물은 나올 수 있습니다. 다만 어떤 판단이 어디서 이뤄졌는지, 무엇을 근거로 다음 단계로 넘겼는지는 훨씬 흐려집니다.

중요한 것은 “AI가 대신 만들었다”는 표면적인 인상이 아닙니다. 더 중요한 것은 어떤 층을 사람이 붙들고, 어떤 층을 에이전트에게 맡겼는가입니다. 이 저장소에서 먼저 만든 것은 개별 slide가 아니라, slide가 생겨나는 경로였습니다.

## source를 입력층으로 가뒀다

이 프로젝트의 가장 바깥 구조는 이미 파일 트리에 박혀 있습니다. `README.md`와 `docs/README.md`가 선언하듯, 전체 파이프라인은 `source -> seminar prose -> html -> pdf -> speaker notes`입니다. 여기서 입력층은 `docs/01-sources/` 하나뿐입니다. `docs/02-seminar/prose/`는 입력층이 아니라 종합된 기준 문장이고, 그 뒤의 `docs/03-html/`, `docs/04-pdf/`, `docs/05-speaker-notes/`는 모두 파생 산출층입니다.

이 분리가 중요한 이유는 단순합니다. source와 해석을 같은 장소에 섞어 놓는 순간, 나중에는 무엇이 근거이고 무엇이 편집 판단인지 구분할 수 없게 되기 때문입니다. 그래서 이 저장소는 local markdown만 authoritative source로 취급하고, 불확실한 내용은 억지로 메우지 않고 `docs/01-sources/intake/open-questions.md`로 보냅니다. 이 단계에서 사람이 붙든 것은 입력층의 경계였고, 다음 단계로 넘긴 산출물은 정리된 source set이었습니다.

## prose를 canonical source로 세웠다

source를 모았다고 곧바로 장표로 가지는 않았습니다. 먼저 `docs/02-seminar/prose/`를 canonical source로 세웠습니다. `00-overview.md`부터 `09-what-we-should-do-next.md`까지가 발표의 main narrative spine이고, `90-appendix-references.md`는 별도 appendix입니다. 이 계층은 slide bullet 모음이 아니라, 논리 순서와 주장 강도를 책임지는 본문입니다.

이 결정이 의미하는 바는 분명합니다. 이후 단계는 이 prose를 요약하고 압축할 수는 있어도, 논지 바깥으로 뛰어넘을 수는 없습니다. HTML slide도, speaker notes도, 나중의 PDF도 모두 이 계층을 따라가야 합니다. 이 단계에서 사람이 붙든 것은 논리 순서와 주장 강도였고, 다음 단계로 넘긴 산출물은 canonical prose였습니다.

## 계획은 outline과 manifest가 들고 간다

prose가 준비되면 곧바로 HTML을 만들지 않습니다. 먼저 `docs/03-html/outline/slide-outline.md`에서 발표를 slide 단위로 자릅니다. 이 파일은 단순한 메모가 아니라 승인 게이트입니다. slide 제목, 핵심 주장, source section, layout family, visual need가 여기서 먼저 정해져야 합니다. 이 단계에서 사람이 붙든 것은 slide 단위의 주장 배치였고, 다음 단계로 넘긴 산출물은 승인된 outline이었습니다.

그 다음 `docs/03-html/manifest.md`가 상태를 들고 갑니다. 이 문서는 작업이 끝난 뒤 쓰는 회고가 아닙니다. slide id allocation, source section mapping, html path, build status를 계속 동기화하는 live sync 문서입니다. 어떤 prose 파일이 어떤 slide들로 풀렸는지, 무엇이 built이고 무엇이 pending인지, 현재 deck이 어디까지 왔는지를 세션 밖 파일이 기억합니다.

## design contract를 먼저 고정하고 `Codex`는 그 안에서 움직였다

이 저장소에서 `Codex`가 맡은 핵심 일은 HTML/CSS generation입니다. 하지만 더 중요한 사실은 따로 있습니다. 그 HTML이 아무 데서나 튀어나오지 않는다는 점입니다. `docs/03-html/shared/design.md`가 먼저 tone, palette, typography, spacing, layout family, reference shell, placeholder contract를 고정합니다. `outline`과 `manifest`가 무엇을 만들어야 하는지 정하고, `design.md`가 어떻게 보여야 하는지 정한 뒤에야 `Codex`가 `slide-XX.html`을 작성합니다. 이 단계에서 사람이 붙든 것은 시각 문법이었고, `Codex`가 맡은 것은 그 문법 안에서 HTML을 생산하는 일이었습니다.

이 구조에서는 매 slide를 영감으로 그리지 않습니다. `title`, `agenda`, `section`, `content`, `comparison`, `visual`, `conclusion` 같은 family를 먼저 고르고, 그 안에서 approved shell을 씁니다. 그래서 `Codex`가 하는 일은 디자인을 즉흥적으로 발명하는 것이 아니라, 이미 잠근 문법 안에서 산출물을 생산하는 일에 가깝습니다. agent를 잘 쓰는 방식은 자유를 최대화하는 것이 아니라, 자유가 작동할 좌표계를 먼저 만드는 것입니다.

## 생성과 검증을 같은 손에 쥐지 않았다

이 프로젝트는 생성과 검증을 한 덩어리로 다루지 않도록 설계돼 있습니다. `AGENTS.md`와 `.codex/subagents/README.md`를 보면, global outline gate, chapter planning, Korean copy, pre-HTML gate, `Codex` HTML build, automated check, post-HTML gate, final deck gate, `PDF`, speaker notes 순서가 분명하게 나뉘어 있습니다. HTML generation과 HTML validation도 다른 역할로 분리돼 있습니다.

이 분리는 형식이 아니라 안전장치입니다. 생성자가 자기 결과를 스스로 통과시키게 두면, 그럴듯한 오류가 가장 오래 살아남습니다. 그래서 이 저장소는 `python3 scripts/check_slide_contract.py`, `python3 scripts/check_slide_korean.py docs/03-html/slides` 같은 기계적 점검을 먼저 걸고, 그 다음에 deck-level consistency와 slide-level validation을 따로 보게 만들었습니다. 이 단계에서 사람이 붙든 것은 통과 기준이었고, 다음 단계로 넘긴 산출물은 검증을 통과한 deck 상태였습니다.

## speaker notes를 맨 뒤로 밀었다

많은 발표 작업이 대본부터 길어지면서 무너집니다. 설명하고 싶은 욕심이 먼저 커지고, 아직 굳지 않은 slide 구조를 말이 덮어버리기 때문입니다. 이 저장소는 그 순서를 거꾸로 잡습니다. `docs/05-speaker-notes/`는 deck이 안정된 뒤에야 들어가는 마지막 단계입니다. notes는 canonical prose를 대체하지 않고, 새로운 factual claim도 추가하지 않습니다. slide order가 바뀌면 먼저 `slide-to-script-map.md`를 고치고, 그 다음 대본을 손봅니다.

이 순서 덕분에 발표 대본은 설계의 주인이 아니라 결과의 해설자가 됩니다. 먼저 prose가 주장하고, 다음으로 slide가 압축하고, 맨 마지막에 notes가 말로 풀어냅니다. 이 세 층의 주객이 바뀌지 않게 만드는 것이 생각보다 중요합니다. 발표는 말로 끝나지만, 말이 먼저 앞서 나가면 구조는 무너집니다.

## 결론: 우리가 만든 것은 slide보다 파이프라인이다

이 발표가 보여 주는 진짜 포인트는 간단합니다. `Codex`가 HTML을 만들었다는 사실 자체가 아닙니다. 우리가 `Codex`에게 맡길 층과 맡기지 않을 층을 먼저 갈라놓았다는 점입니다. source boundary는 사람이 잠갔고, prose spine도 사람이 고정했고, outline과 manifest와 design contract도 파일로 박아 두었습니다. 그 위에서 `Codex`는 HTML/CSS generation을 맡았습니다.

그래서 이 발표의 제작 과정은 앞 장들의 주장을 그대로 증명합니다. 좋은 결과를 만든 것은 한 번의 프롬프트가 아니라, 입력층을 좁히고, 기준 문장을 세우고, 계획을 파일에 남기고, 디자인 계약을 먼저 잠그고, 생성과 검증을 분리한 구조였습니다. `Codex`가 들어간 정확한 위치도 분명합니다. prose와 outline, design contract가 잠긴 뒤 HTML/CSS generation을 맡는 위치입니다. 이 발표에서 `Codex`는 모든 층을 대신한 것이 아니라, 이미 잠근 경계 안에서 생산을 담당했습니다.
