# 이 발표가 만들어진 과정: Codex를 어디에 넣었는가

## 시작하며: 우리는 slide부터 열지 않았다

이 발표를 만든 방식은 앞 장에서 설명한 원리를 그대로 따릅니다. 처음부터 slide 툴을 열고 문장을 채운 것이 아닙니다. 먼저 source를 잠그고, 그 source를 prose로 묶고, 그 prose를 outline으로 압축한 뒤, 마지막에 `Codex`가 HTML/CSS를 만들게 했습니다. `PDF`와 speaker notes는 그 다음이었습니다. 순서를 바꾸면 결과물은 나옵니다. 대신 무엇이 근거이고 무엇이 편집 판단인지, 어떤 기준으로 다음 단계로 넘어갔는지가 금방 흐려집니다.

중요한 것은 “AI가 대신 만들었다”는 표면적 인상 따위가 아닙니다. 더 중요한 것은 어느 층을 사람이 끝까지 붙들고, 어느 층을 에이전트에게 맡겼는가입니다. 이 저장소가 먼저 만든 것도 개별 slide가 아니라 slide가 생겨나는 경로였습니다.

## source를 입력층에 가둔 이유

이 프로젝트의 바깥 경계는 단순합니다. 입력층은 `docs/01-sources/`에 가두고, 그 뒤는 모두 파생 산출층으로 다룹니다. `docs/02-seminar/prose/`는 source를 다시 정리한 canonical text이고, 그 다음 `docs/03-html/`, `docs/04-pdf/`, `docs/05-speaker-notes/`는 이 기준 문장에서 파생됩니다. source와 해석을 한 파일 계층 안에 섞어 두지 않는 이유도 여기 있습니다. 둘이 섞이는 순간, 나중에는 무엇이 근거이고 무엇이 편집인지 분간하기 어려워집니다.

그래서 이 저장소는 local markdown만 authoritative source로 취급하고, 빈 근거는 억지로 메우지 않습니다. 모호한 내용은 `docs/01-sources/intake/open-questions.md`로 올려 둡니다. 핵심은 풍부하게 쓰는 것이 아니라 경계를 먼저 잠그는 일입니다. 입력층이 잠겨야 그 위에서 생기는 prose와 slide도 provenance를 잃지 않습니다.

## prose를 canonical source로 세웠다

source를 모았다고 바로 장표로 가지는 않았습니다. 먼저 `docs/02-seminar/prose/`를 발표의 기준 문장으로 세웠습니다. `00-overview.md`부터 `09-what-we-should-do-next.md`까지가 main narrative spine이고, `90-appendix-references.md`는 그 spine을 받치는 별도 부록입니다. 이 계층은 bullet 원고가 아니라, 발표 전체의 주장 순서와 문장 압력을 고정하는 본문입니다.

이 결정이 중요한 이유는 분명합니다. 뒤 단계는 이 prose를 압축할 수는 있어도, 논지 바깥으로 새 사실과 새 프레이밍을 뛰어넘어서는 안 됩니다. HTML slide도, `PDF`도, speaker notes도 모두 이 문장을 따라가야 합니다. 결국 발표의 중심은 장표가 아니라 본문에 있습니다. slide는 본문을 대신하지 않습니다. 본문을 더 짧고 더 빠르게 읽히는 형태로 바꿀 뿐입니다.

## outline과 manifest가 계획을 세션 밖으로 끌어냈다

prose가 준비되면 다음은 압축입니다. 여기서 곧바로 HTML로 뛰지 않고 먼저 outline을 만드는 이유는, 장표 제작이 시작된 뒤에는 문장 하나를 바꾸는 일도 곧 배치와 디자인을 함께 흔드는 일이 되기 때문입니다. 발표를 slide 단위로 먼저 잘라 놓아야, 뒤 단계는 새 판단을 발명하는 대신 이미 정한 판단을 더 짧고 더 또렷한 형태로 밀어낼 수 있습니다.

이때 `manifest`가 붙드는 것은 세부 목록 자체가 아니라 상태입니다. 어떤 prose가 이미 slide로 풀렸는지, 무엇이 아직 남았는지, 현재 덱이 어디까지 왔는지를 세션 기억이 아니라 파일이 들고 가게 만드는 일입니다. 좋은 파이프라인은 더 많이 기억하는 구조가 아닙니다. 무엇이 끝났고 무엇이 아직 아닌지를 바깥 아티팩트에 남기는 구조입니다.

## design contract를 먼저 잠그고 `Codex`를 넣었다

이 저장소에서 `Codex`가 맡은 핵심 일은 HTML/CSS generation입니다. 하지만 그보다 먼저 잠기는 것이 있습니다. `design.md`가 시각 문법을 먼저 고정한다는 사실입니다. 무엇을 만들지는 `outline`이 잡고, 어디까지 왔는지는 `manifest`가 붙들고, 어떻게 보여야 하는지는 `design.md`가 묶습니다. 그 다음에야 `Codex`가 `slide-XX.html`을 씁니다.

여기서 바깥 참고로 읽은 것이 `make-slide`입니다. 다만 이 저장소는 `make-slide`를 범용 deck generator로 받아들이지 않았습니다. `minimal-light`의 밝은 rhythm, reference shell을 재사용하는 태도, 최종 `deck/index.html`에 필요한 최소 runtime만 선별해서 가져왔습니다. 반대로 progress bar, fullscreen button, notes panel 같은 chrome은 버렸습니다. 외부 reference를 그대로 이식한 것이 아니라, 로컬 design contract 안으로 다시 번역한 셈입니다.

이 순서가 중요합니다. 그래야 `Codex`는 막연한 영감 생성기가 아니라, 이미 잠근 문법 안에서 생산을 맡는 builder가 됩니다. `title`, `agenda`, `section`, `content`, `comparison`, `visual`, `conclusion` 같은 family가 먼저 있고, 그 family 안에서 approved shell을 씁니다. agent를 잘 쓰는 방식은 자유를 끝없이 넓히는 데 있지 않습니다. 자유가 움직일 좌표계를 먼저 만드는 데 있습니다.

## 생성과 검증을 같은 손에 쥐지 않았다

이 프로젝트는 생성과 검증을 한 덩어리로 묶지 않습니다. `AGENTS.md`와 `.codex/subagents/README.md`가 보여 주듯, 계획을 잠그는 문과, 카피를 압축하는 문과, HTML을 만드는 문과, 그것을 다시 거르는 문이 분리돼 있습니다. HTML generation과 HTML validation도 다른 역할로 나뉩니다.

이 분리가 중요한 이유는 단순합니다. 생성자가 자기 결과를 스스로 통과시키게 두면, 그럴듯한 오류가 제일 오래 살아남습니다. 그래서 이 저장소는 `python3 scripts/check_slide_contract.py`, `python3 scripts/check_slide_korean.py docs/03-html/slides` 같은 기계적 점검을 먼저 걸고, 그 다음에 deck-level consistency와 slide-level validation을 따로 봅니다. 중요한 것은 더 많은 리뷰어가 아니라, 어떤 판단을 어느 문에서 끊을지 미리 정해 두는 구조입니다.

## speaker notes를 맨 뒤로 밀었다

발표 작업이 흔히 무너지는 지점도 여기입니다. slide 구조가 아직 흔들리는데 대본부터 길어지기 시작하면, 말이 구조를 덮어버립니다. 이 저장소는 그 순서를 거꾸로 잡습니다. `docs/05-speaker-notes/`는 덱이 안정된 뒤에야 들어가는 마지막 단계입니다. notes는 canonical prose를 대체하지 않고, 새로운 factual claim도 추가하지 않습니다. slide order가 바뀌면 먼저 `slide-to-script-map.md`를 고치고, 그 다음에야 대본을 손봅니다.

덕분에 notes는 설계의 주인이 아니라 설계의 해설자가 됩니다. 먼저 prose가 주장하고, slide가 압축하고, 마지막에 notes가 말로 풉니다. 발표는 결국 말로 끝나지만, 말이 먼저 앞서 나가면 구조는 무너집니다.

## 결론: 우리가 만든 것은 slide보다 파이프라인이다

이 발표의 핵심은 `Codex`가 HTML을 만들었다는 사실이 아닙니다. 더 중요한 것은 `Codex`를 어디에 넣고 어디에는 넣지 않았는가입니다. source boundary는 사람이 잠갔고, prose spine도 사람이 고정했고, outline과 manifest, design contract도 파일로 박아 두었습니다. 그 뒤에야 `Codex`가 HTML/CSS generation을 맡았습니다.

그래서 이 발표의 제작 과정은 앞 장들의 주장을 그대로 증명합니다. 좋은 결과를 만든 것은 한 번의 프롬프트가 아닙니다. 입력층을 좁히고, 기준 문장을 세우고, 계획과 상태를 세션 밖 파일에 남기고, 생성과 검증을 분리한 운영 구조입니다. `Codex`가 들어간 정확한 위치도 여기서 분명해집니다. 모든 층을 대신하는 자리가 아니라, 이미 잠긴 경계 안에서 생산을 맡는 자리입니다. 외부 reference인 `make-slide`도 이 구조 바깥에서 raw로 작동한 것이 아니라, `slide-XX.html`과 `deck/index.html` 계약 안으로 다시 접혀 들어왔을 뿐입니다.

그리고 이 사례가 다음 장의 질문으로도 곧장 이어집니다. 이런 경계와 구조를 일회성 제작 방식으로 끝내지 않으려면, 개인과 팀은 무엇을 습관으로 고정해야 하는가. 이제 그 답을 실천 원칙으로 좁혀 봐야 합니다.
