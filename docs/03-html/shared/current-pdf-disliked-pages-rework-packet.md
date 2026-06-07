# Current PDF 비선호 페이지 재작업 PM Packet

작성일: 2026-04-25

이 문서는 `output/pdf/harness-full-main-94-current-720x405.pdf` 기준 사용자 비선호 page `41`, `54`, `57-68`을 HTML source 작업으로 옮기기 위한 PM packet이다.

## 0. 먼저 잡아야 할 핵심

- 사용자가 말한 page number는 `output/pdf/harness-full-main-94-current-720x405.pdf`의 1-based PDF page다.
- 이 PDF는 94page이고, 현재 `docs/03-html/manifest.md`는 92-slide deck을 가리킨다. 그래서 current PDF page number를 곧바로 `Sxxx`로 보면 안 된다.
- 작업 대상은 PDF page number가 아니라, PDF에서 추출한 title을 현재 source file title과 대조해 확정한다.
- `57-68` 묶음은 단순히 예쁘게 바꾸는 일이 아니다. 현재 prose/target-map 기준으로 보면 `Advisor`, `Parallel`, `멀티 모델`처럼 위치가 흔들리거나 source에서 빠진 항목이 섞여 있다. 먼저 source-alignment를 통과해야 한다.
- 특히 `docs/02-seminar/prose/목표-지도.md`는 `docs/02-seminar/harness-rebuilt-md/90-advisor.md`를 source map에서 제외한다. 따라서 `Advisor 전략` slide는 그대로 살려 꾸미면 안 된다.

## 1. Scope Map

| current PDF page | PDF title | source slide | editable file | generated artifact | source/prose 기준 |
| --- | --- | --- | --- | --- | --- |
| 41 | MCP와 Context 7 | S039 | `scripts/jaryo_html_deck/slides/chapter_04/slide_039.py` | `docs/03-html/slides/slide-039.html` | target-map 최신 구조와 충돌 가능. MCP/Context 7은 새 target-map에서 02/07 쪽 맥락으로 다시 확인 필요 |
| 54 | 결정 제어와 확률 제어를 분리하라 | S052 | `scripts/jaryo_html_deck/slides/chapter_05/slide_052.py` | `docs/03-html/slides/slide-052.html` | `docs/02-seminar/prose/05-기계가-막을-수-있는-것은-앞에서-막는다.md`의 `결정론적 제어와 확률적 제어를 분리한다`와 직접 대응 |
| 57 | 하나의 에이전트 = 하나의 역할 | S055 | `scripts/jaryo_html_deck/slides/chapter_06/slide_055.py` | `docs/03-html/slides/slide-055.html` | `docs/02-seminar/prose/06-하나의-AI에게-다-맡기지-않는다.md` `하나의 에이전트는 하나의 역할을 맡아야 한다` |
| 58 | 1. Sub-Agent: 중간 작업을 격리하는 기본형 | S056 | `scripts/jaryo_html_deck/slides/chapter_06/slide_056.py` | `docs/03-html/slides/slide-056.html` | prose 06 `Sub-Agent는 중간 작업을 격리한다` |
| 59 | Advisor 전략: 작은 실행자, 큰 자문 | S057 | `scripts/jaryo_html_deck/slides/chapter_06/slide_057.py` | `docs/03-html/slides/slide-057.html` | source drift. target-map에서 `90-advisor.md` 제외. 유지 금지 후보 |
| 60 | 2. Orchestrator: 계획자 하나가 여러 실행자를 배치한다 | S058 | `scripts/jaryo_html_deck/slides/chapter_06/slide_058.py` | `docs/03-html/slides/slide-058.html` | prose 06 `Orchestrator는 작업을 나누고 수렴시킨다` |
| 61 | 3. Parallel: 같은 목표를 평면으로 벌리고 나중에 합친다 | S059 | `scripts/jaryo_html_deck/slides/chapter_06/slide_059.py` | `docs/03-html/slides/slide-059.html` | source drift 가능. 최신 prose 06에는 standalone Parallel section 없음 |
| 62 | 4. GAN-Style: 생성자와 평가자를 분리한다 | S060 | `scripts/jaryo_html_deck/slides/chapter_06/slide_060.py` | `docs/03-html/slides/slide-060.html` | prose 06 `생성자와 평가자를 같은 손에 쥐지 않는다` |
| 63 | 5. Agent Teams: 양방향 대화가 가능한 팀을 만든다 | S061 | `scripts/jaryo_html_deck/slides/chapter_06/slide_061.py` | `docs/03-html/slides/slide-061.html` | prose 06 `Agent Team은 토론이 필요할 때만 쓴다` |
| 64 | Sub-Agent와 Agent Team은 다르다 | S062 | `scripts/jaryo_html_deck/slides/chapter_06/slide_062.py` | `docs/03-html/slides/slide-062.html` | prose 06의 Sub-Agent/Agent Team 대비와 대응 |
| 65 | 설계 원칙: 패턴보다 경계가 중요하다 | S063 | `scripts/jaryo_html_deck/slides/chapter_06/slide_063.py` | `docs/03-html/slides/slide-063.html` | prose 06 `패턴보다 경계가 중요하다`의 5원칙 |
| 66 | 설계 원칙: 패턴보다 경계가 중요하다 | S064 | `scripts/jaryo_html_deck/slides/chapter_06/slide_064.py` | `docs/03-html/slides/slide-064.html` | prose 06의 SOLID 재해석 문단 |
| 67 | 멀티 모델과 멀티 에이전트 | S065 | `scripts/jaryo_html_deck/slides/chapter_06/slide_065.py` | `docs/03-html/slides/slide-065.html` | 위치 drift 가능. target-map 07에는 `한 모델에만 기대지 않는다`가 있으나 최신 prose 06에는 없음 |
| 68 | 결론: 더 많은 AI가 아니라 더 좁은 역할의 AI 여럿 | S066 | `scripts/jaryo_html_deck/slides/chapter_06/slide_066.py` | `docs/03-html/slides/slide-066.html` | prose 06 정리 문단과 직접 대응 |

## 2. Problem Hypothesis

### 공통 문제

- 현재 비선호 묶음은 카드/표/하단 검정 바가 반복되어 장표마다 하는 일이 달라 보이지 않는다.
- 본문 카드가 비슷한 무게로 늘어서 있어, 한 장에서 무엇을 기억해야 하는지 바로 잡히지 않는다.
- `Sub-Agent`, `Orchestrator`, `GAN-Style`, `Agent Teams`는 관계와 흐름이 핵심인데, 현재는 박스 나열에 가까워 동작 방식이 약하게 보인다.
- Kakao reference의 장점은 색이나 장식이 아니라 `도입 -> 분류 -> 목록화 -> 비교 -> 상세화 -> 확장 -> 원칙화` 리듬이다. 현재 `57-68`은 이 리듬보다 패턴 설명 카드 묶음처럼 보인다.

### page별 문제 가설

- p41/S039: MCP/Context 7의 관계도 자체보다 설명 카드의 성격이 강하다. 새 target-map에서는 이 위치가 맞는지도 의심해야 한다.
- p54/S052: 내용은 source-backed지만 좌우 비교가 표처럼 딱딱하고, 결정론/확률론의 차이가 한눈에 들어오는 구조가 약하다.
- p57/S055: `하나의 에이전트 = 하나의 역할`이어야 하는데 현재는 5패턴 카탈로그처럼 읽힐 위험이 있다. 핵심은 패턴명이 아니라 `보는 정보 / 할 수 있는 행동 / 통과 기준`의 분리다.
- p59/S057: `Advisor`는 현재 target-map에서 제외된 source에 기대는 항목이다. 디자인 개선 대상이 아니라 삭제/대체/보류 판단 대상이다.
- p61/S059: `Parallel`도 최신 prose 06의 standalone section이 아니다. worktree/병렬성은 07장 운영 구조 쪽으로 보내는 편이 자연스럽다.
- p67/S065: `멀티 모델`은 사용자가 Gemini/Codex 활용을 허용한 최신 피드백과 연결될 수 있지만, 현재 위치가 06장 결론 앞이면 논지가 흐릴 수 있다. 07장 또는 workflow gate로 이동하는 편이 더 맞을 수 있다.

## 3. Reference Obligations

### Kakao page 062-068에서 가져올 것

- page 062: dark chapter divider의 리듬. 단, Jaryo theme 규칙상 warm palette와 장식은 복사하지 않는다.
- page 063: 3개 분류 card + 하단 conclusion bar. `컨텍스트 / 역할 / 신뢰 경계` 같은 3축 설명에 적합.
- page 064: 5개 패턴 card row + mini native diagram + 짧은 caption. 단, 5개를 모두 살릴 때만 사용한다.
- page 065: 좌우 비교형. `Sub-Agent vs Agent Team`, `결정론적 제어 vs 확률적 제어`에 적합.
- page 066: dominant diagram + side explanation cards + bottom conclusion. `Sub-Agent`, `Orchestrator`, `GAN-Style`처럼 구조가 중요한 slide에 적합.
- page 067: network/system map + side explanation + bottom conclusion. `Agent Teams`에 적합.
- page 068: 2x2 또는 4원칙 정리 + bottom conclusion. 설계 원칙/정리 slide에 적합.

### 금지할 것

- Kakao의 warm brown/ivory palette, section pill, character/illustration mood 복사 금지.
- reference의 content claim, label, metric, 예시 복사 금지.
- source에 없는 패턴명, 비교 축, 결론 문구 생성 금지.
- current PDF page number를 바로 `Sxxx`로 매핑 금지. 항상 title/source file 대조.
- `Advisor`처럼 target-map에서 제외된 source를 꾸며서 살리는 작업 금지.

## 4. Batch Plan

### Batch 0. Source-alignment gate

목표: 비선호 page를 꾸미기 전에, 최신 target-map/prose에 맞는 slide만 남긴다.

- 대상: current PDF p41, p54, p57-68 전체
- 할 일:
  - p41/S039가 새 target-map의 어느 장으로 가야 하는지 확인한다. 현 위치 유지가 아니라 이동/삭제/재구성 후보로 본다.
  - p59/S057 `Advisor`는 target-map exclusion 때문에 삭제/대체 후보로 분류한다.
  - p61/S059 `Parallel`은 최신 prose 06에 standalone section이 없으므로 07장 worktree/작업 환경 분리와 합칠지 판단한다.
  - p67/S065 `멀티 모델`은 06장 결론 직전이 아니라 07장 `한 모델에만 기대지 않는다` 또는 workflow reviewer rule로 이동할지 판단한다.
- 산출물:
  - updated outline/manifest proposal only. 구현 source 수정은 다음 batch부터.
  - STOP: Batch 0 결과는 PM gate 산출물이다. orchestrator가 source-alignment 결정을 명시 승인하기 전까지 builder는 Batch 1~3으로 넘어가지 않는다.

### Batch 1. p54/S052 단독 개선

목표: source-backed 내용이 명확한 slide를 먼저 작은 단위로 고친다.

- editable: `scripts/jaryo_html_deck/slides/chapter_05/slide_052.py`
- reference: Kakao page 065 좌우 비교형
- 방향:
  - `결정론적 제어`와 `확률적 제어`를 좌우 큰 panel로 둔다.
  - 항목은 prose 05의 source-backed comparison items와 supporting sentence만 사용한다. 새 비교 축을 만들지 않는다.
  - 결론은 source-backed `AI가 잘하는 판단에 집중할 수 있도록, 기계가 막을 수 있는 일을 먼저 치워 주는 구조`를 압축한다.

### Batch 2. Chapter 06 spine 재구성

목표: `57-68`을 `패턴 설명회`가 아니라 `역할/컨텍스트/검증 책임을 나누는 장`으로 다시 묶는다.

- primary source: `docs/02-seminar/prose/06-하나의-AI에게-다-맡기지-않는다.md`
- editable candidates:
  - `scripts/jaryo_html_deck/slides/chapter_06/slide_055.py`
  - `scripts/jaryo_html_deck/slides/chapter_06/slide_056.py`
  - `scripts/jaryo_html_deck/slides/chapter_06/slide_058.py`
  - `scripts/jaryo_html_deck/slides/chapter_06/slide_060.py`
  - `scripts/jaryo_html_deck/slides/chapter_06/slide_061.py`
  - `scripts/jaryo_html_deck/slides/chapter_06/slide_062.py`
  - `scripts/jaryo_html_deck/slides/chapter_06/slide_063.py`
  - `scripts/jaryo_html_deck/slides/chapter_06/slide_064.py`
  - `scripts/jaryo_html_deck/slides/chapter_06/slide_066.py`
- hold/delete/move candidates:
  - `slide_057.py` Advisor: hold/delete unless target-map changes.
  - `slide_059.py` Parallel: hold/move to 07 unless prose 06 is updated.
  - `slide_065.py` Multi model: hold/move to 07 unless prose 06 is updated.
- suggested flow:
  1. 문제: 한 에이전트에게 다 맡기면 컨텍스트/역할/신뢰 경계가 흐려진다. Kakao p063형 3-card.
  2. 기준: 하나의 에이전트는 하나의 역할. `보는 정보 / 할 수 있는 행동 / 통과 기준` 3축.
  3. Sub-Agent: 격리된 워커 구조. Kakao p066형 dominant diagram + side cards.
  4. Orchestrator: 분해와 수렴. Kakao p066형 diagram.
  5. 생성자/평가자 분리: GAN-Style은 이름보다 원리 중심. feedback loop diagram.
  6. Agent Team: 토론이 필요할 때만. Kakao p067형 network.
  7. Sub-Agent vs Agent Team: Kakao p065형 좌우 비교.
  8. 패턴보다 경계: Kakao p068형 원칙 grid.
  9. 결론: 더 많은 AI가 아니라 더 좁은 역할. statement/closing card.

### Batch 3. p41/S039 위치 판단 후 재작업

목표: MCP/Context 7 slide를 무리하게 현재 위치에서 고치지 않는다.

- editable: `scripts/jaryo_html_deck/slides/chapter_04/slide_039.py`
- 먼저 판단할 것:
  - 새 target-map에서 MCP/Context 7이 02장 Harness 구성요소인지, 07장 실전 파일/명령어 구조인지 확인한다.
  - 현 위치가 유지될 때만 visual rebuild를 진행한다.
- reference: Kakao page 066 or 067의 system map + side explanation 구조.

## 5. Validation and Reviewer Criteria

### build/check commands

Batch 0 source-alignment 이후 실제로 남은 slide list를 다시 산출한 뒤 아래 명령의 targeted file list를 갱신한다. `Advisor`, `Parallel`, `멀티 모델`을 삭제/이동했다면 stale `slide-057.html`, `slide-059.html`, `slide-065.html`를 그대로 검증 목록에 남기지 않는다.

```bash
PYTHONDONTWRITEBYTECODE=1 python3 scripts/build_jaryo_html_deck.py
PYTHONDONTWRITEBYTECODE=1 python3 scripts/check_slide_contract.py
PYTHONDONTWRITEBYTECODE=1 python3 scripts/check_slide_korean.py <post-alignment-target-slide-html-files>
PYTHONDONTWRITEBYTECODE=1 python3 scripts/check_deck_runtime.py docs/03-html/deck/index.html
PYTHONDONTWRITEBYTECODE=1 python3 -m pytest -q tests/test_build_jaryo_html_deck.py
```

최소 targeted file list의 시작점은 다음과 같다. 단, Batch 0 결과에 따라 반드시 갱신한다.

```text
docs/03-html/slides/slide-039.html
docs/03-html/slides/slide-052.html
docs/03-html/slides/slide-055.html ... docs/03-html/slides/slide-066.html
```

### visual QA artifact requirement

이번 문제는 copy/contract 문제가 아니라 visual rhythm 문제이므로 QA report에는 아래 artifact가 반드시 있어야 한다.

- post-build HTML screenshot contact sheet: `output/playwright/disliked-pages-rework/current-target-contact-sheet.png`
- Kakao reference contact sheet: `output/playwright/disliked-pages-rework/kakao-062-068-contact-sheet.png`
- PDF smoke contact sheet after export: `output/playwright/disliked-pages-rework/pdf-smoke-target-contact-sheet.png`
- QA report에는 Playwright screenshot command와 PDF export/render command를 그대로 적는다. repository에 고정 script가 없으면 QA agent가 사용한 one-off command를 report에 남긴다.
- contact sheet 비교는 `p57-68`이라는 예전 PDF handle이 아니라 post-alignment target slide set 기준으로 한다. 단, 사용자가 지적한 실패 원인은 current PDF `p57-68`에서 왔음을 report에 남긴다.

### reviewer criteria

- target-map/prose/source markdown과 visible copy가 모두 추적 가능해야 한다.
- `Advisor`, `Parallel`, `멀티 모델`의 위치/존재가 target-map과 충돌하면 visual polish 전에 block한다.
- Kakao reference는 구조만 닮아야 한다. 색/캐릭터/장식/문구를 닮으면 실패다.
- 한 slide는 하나의 역할만 해야 한다. `설명 + 표 + 결론 + 예시`를 한꺼번에 넣으면 실패다.
- 카드 반복은 줄이고, 관계/흐름이 중요한 slide는 native diagram으로 보여준다.
- 한국어 문구는 구 단위로 짧게 두고, 번역투나 보고서식 연결어를 제거한다.
- generated HTML 직접 수정 금지. source python만 수정한다.
- screenshot/PDF smoke에서는 post-alignment target 묶음이 하나의 장 호흡으로 보이는지 contact sheet로 확인한다.

## 6. Gemini Reviewer Use

Gemini는 builder가 아니라 reviewer/visual analyst로만 쓴다. 단, Gemini 검토는 보조 의견이다. PM, QA, reviewer gate를 대체하거나 다음 gate로 자동 진행시키지 않는다.

권장 사용 위치:

1. Batch 0 이후: source-alignment 제안이 target-map과 충돌하는지 다른 시각으로 검토. 이 결과는 PM 첨부 의견일 뿐이며, orchestrator가 PM gate를 명시 승인하기 전에는 builder가 시작하지 않는다.
2. Batch 2 build 이후와 QA 전/후: current chapter 06 contact sheet와 Kakao page 062-068 contact sheet를 함께 보고 구조만 비교. 단, QA evidence와 final reviewer 판단을 대체하지 않는다.
3. 최종 reviewer 전: 선호 current PDF pages `1-18`, `21`, `24`, `37`, `39`, `40`, `52`, `53`와 새 chapter 06 묶음의 rhythm 차이를 요약. 최종 승인 권한은 `html-slide-reviewer` gate에 있다.

Gemini prompt 핵심:

```text
이 이미지는 Jaryo HTML deck의 chapter 06 후보와 Kakao reference page 062-068입니다.
역할: read-only visual/reference reviewer.
Reasoning budget: high. 구조 충돌, gate 위반, source 밖 의미 생성 가능성을 우선 검토하세요.
한국어 품질 기준: `.codex/skills/local/natural-korean-prose/SKILL.md`를 적용한 상태로, 번역투/어색한 한국어/보고서식 연결어를 함께 잡으세요.
content를 복사하지 말고 structure-only로 비교하세요.
검토 기준은 여백, 정보 위계, diagram density, 한 slide의 역할, 하단 결론 처리입니다.
source에 없는 문구나 새 비교 축은 제안하지 마세요.
```

## 7. Blocking Questions

없음. 다만 구현 전에 PM gate에서 아래 판단은 반드시 내려야 한다.

1. `Advisor`는 target-map에서 제외된 source이므로 유지하지 않는 것이 기본값이다.
2. `Parallel`은 최신 prose 06에 standalone section이 없으므로 07장 worktree/작업 환경 분리로 보내는 것이 기본값이다.
3. `멀티 모델`은 사용자 최신 피드백과 연결되지만 06장 본문에는 없으므로 07장 또는 reviewer workflow 규칙으로 보내는 것이 기본값이다.

## 8. Output / Feedback Loop Policy

- 현재 이미 생성된 PDF 기준으로 재사용할 HTML은 별도 재사용 후보로 기록한다. 재사용 판단은 PDF page number가 아니라 `current PDF page -> stable slide id -> source file -> generated artifact` mapping으로 한다.
- 새 HTML/PDF feedback artifact는 기준 PDF와 기존 generated directory에 섞지 않는다. 구현 세션 권장 출력 root는 다음과 같다.
  - single-slide feedback: `output/html-feedback/<run-id>/chapter_XX/SYYY/`
  - chapter mini-batch review: `output/html-feedback/<run-id>/chapter_XX/mini-batch/`
  - full PDF milestone: `output/pdf-milestones/<build-id>/`
- feedback loop에서는 전체 deck HTML rebuild, 전체 screenshot sweep, 전체 PDF export를 하지 않는다. 한 slide 피드백은 해당 slide HTML/screenshot만 새로 만든다.
- 전체 렌더링은 PDF를 구성하는 milestone에서만 쓴다. chapter freeze, 큰 구조 변경 후, 최종 QA 직전이 기본 trigger다.
- mini-batch는 각 chapter별로 진행한다. chapter 안에서 S-id 범위를 나눌 수는 있지만, 사용자 승인/보류 기록은 chapter rhythm 기준으로 남긴다.
- page number는 매 PDF build마다 바뀔 수 있으므로 영구 식별자로 쓰지 않는다. 모든 feedback item에는 PDF build id, PDF page, stable slide id, source file을 함께 적는다.

## 9. Agent Spawn Note

- Codex CLI는 `codex-cli 0.125.0`, Gemini CLI는 `0.39.1`로 확인됐다.
- 사용자 지정 우선 model은 Codex/OpenAI 계열 `gpt-5.5`, `gpt-5.4`, `gpt-5.3-codex`, Gemini 계열 `gemini-3-flash-preview`다.
- 정확한 model명이 CLI/provider에서 거부되면 같은 Gemini 3 preview/flash 계열의 가장 가까운 사용 가능 model을 쓰되, handoff에 `requested model`, `actual model`, `command`, `fallback reason`을 남긴다.
- Codex CLI, Gemini CLI, project-local subagent를 띄울 때는 모두 `.codex/skills/local/natural-korean-prose/SKILL.md`를 적용한 상태로 둔다. prompt에는 자연스러운 한국어, 번역투 제거, 보고서식 연결어 회피, 필요한 English term 보존을 명시한다.
- reasoning effort는 역할별로 명시한다. PM/reviewer/final source-alignment는 high 또는 xhigh, builder는 high, QA는 high, quick visual sanity/목록화는 medium 이하를 기본값으로 둔다.
- Codex rules/review pass 예시는 read-only sandbox를 기본으로 한다.

```bash
codex exec -m gpt-5.5 -c model_reasoning_effort='"high"' -s read-only -C /Users/seungsu/Code/jaryo - < prompt.md
```

- Gemini rules/review pass 예시는 plan approval mode를 기본으로 한다.

```bash
gemini -m gemini-3-flash-preview --approval-mode plan -p "<prompt>"
```

- 현재 세션은 rules/planning 세션이므로 HTML 생성, PDF export, generated HTML 수정, slide source 수정, CSS/generator/test 수정, build/check 실행을 하지 않는다. orchestrator rules-edit mode에서는 이 packet/규칙/decision/handoff 문서만 수정할 수 있고, CLI/subagent reviewer를 read-only review mode로 띄운 경우에는 그 reviewer가 파일을 수정하지 않는다. 실제 구현 agent는 별도 구현 세션에서 이 packet과 `html-slide-pm -> html-slide-builder -> html-slide-qa -> html-slide-reviewer` gate를 그대로 준수한다.
