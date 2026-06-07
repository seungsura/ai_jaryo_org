# Korean Slide Copy Rules

이 문서는 Jaryo 프로젝트에서 HTML slide를 만들 때 적용하는 한국어 visible copy 규칙을 한곳에 모은다. 적용 범위는 `docs/03-html/`의 outline, manifest, slide module, generated slide artifact, deck HTML, screenshot/PDF review에서 보이는 slide title, lead, card title, body copy, table label, quote, attribution, footer-adjacent text다.

긴 글, seminar prose, source reconstruction 문서는 `docs/00-process/korean-writing-rules.md`를 따른다. prose가 구어체 기준으로 바뀌어도 slide copy는 발표 대본이 아니다.

## 기본 원칙

- slide 문구는 한국어를 기본으로 쓴다.
- English term, product name, path, command, API name, protocol, framework/library name, method name은 정확도가 필요하면 그대로 둔다.
- 자연스러운 한국어는 English term을 모두 번역하는 것이 아니다. 정확한 English term을 한국어 어순과 호흡 안에 놓는 것이다.
- visible copy의 의미 단위는 source markdown, 사용자가 명시한 reference, 또는 사용자가 직접 지시한 문구로 추적 가능해야 한다.
- source/reference 밖 비교 축, label, 의미, 예시, metric, 해설 문구를 만들지 않는다.
- source에 없는 문구가 필요해 보이면 새로 쓰지 않는다. 요소를 제거하거나 open question으로 남긴다.
- source 의미 보존 압축은 허용한다. source 밖 재해석은 금지한다.

## Slide Copy 표면

- slide copy는 명사형 또는 구 단위 중심이다.
- 공손체, 서술형, 명령형을 피한다.
- slide title, lead, body copy는 압축 문구를 우선한다.
- slide는 발표자가 말할 문장 전체를 옮기는 공간이 아니다.
- 짧아야 한다가 아니라 역할이 선명해야 한다.
- statement slide는 한 문장 중심으로 둘 수 있지만, 모든 slide를 1-2줄 statement page로 만들지 않는다.
- 숫자, 근거, 구조, 비교, process, architecture를 보여줘야 하는 slide는 `metric card trio`, `evidence cards without tables`, `evidence table`, `process`, `native diagram`, `split comparison` 같은 layout family를 우선 검토한다.

## 종결어미 규칙

- 기본 종결은 명사형과 구 단위다.
- `~입니다`, `~습니다`, `~했습니다`, `~되었습니다`, `~하십시오`, `~하세요`, `~드립니다`, `~합니다` 같은 공손체 ending은 금지한다.
- `~이다`, `~한다`, `~된다`, `~있다`, `~없다`, `~보인다`, `~의미한다`, `~설명한다`처럼 prose-like ending은 긴 visible copy에서 피한다.
- 명령형은 금지한다. 예: `확인하세요`, `줄이세요`, `분리하라`.
- full sentence가 꼭 필요한 quote나 source-backed 문장은 예외가 될 수 있다. 단, quote/source treatment로 보이고 attribution이 분명해야 한다.

## 길이와 정보량

- 문구는 scan-friendly해야 한다.
- 긴 설명문은 card body에 그대로 넣지 않는다.
- 한 visible text segment가 길어지면 title, label, value, support text로 나눈다.
- source 문장을 압축할 때 의미를 잃은 slogan으로 만들지 않는다.
- slide title은 장면이나 claim을 이름 붙인다. 본문 전체를 설명하지 않는다.
- 제목 아래 subtitle/lead는 기본 금지다. source 의미를 잃는 경우에만 최소 문구로 둔다.
- 제목은 한 줄 고정이다. 두 줄이 예상되면 생성/수정을 멈추고 확인한다.

## 금지 표현

다음 표현은 slide visible copy에서 금지하거나 강한 REVISE 후보로 본다.

| 금지/주의 표현 | 바꾸는 방향 |
| --- | --- |
| `장표` | `슬라이드`, `발표 자료` |
| `상류`, `하류` | `앞단`, `뒤쪽`, `먼저`, `나중에` |
| `강하게 호출된다` | `자주 필요`, `여기서 중요`, `여기서 사용` |
| `핵심은 ~ 데 있다` | 더 짧은 claim phrase |
| `~의 측면에서` | frame 제거, claim 직접 표기 |
| `~라고 볼 수 있다` | source-backed claim 직접 표기 |
| `또한`, `따라서`, `그러나`, `한편`으로 시작하는 긴 설명 | 구조로 분리하거나 삭제 |
| `통하여`, `위하여`, `기반으로`, `관련하여`가 붙은 장문 | 실제 동사나 짧은 label로 축약 |
| `passage 검색`, `retriever 품질`, `컨텍스트로 주입` | 필요한 English term만 남기고 한국어 리듬으로 재작성 |
| `신호가 큰 토큰` | `필요한 정보`, `잡음`, `맥락`처럼 이해 가능한 표현 |

## 번역투 금지

- 번역체와 어색한 한국어 표현은 구현 금지다.
- source 의미가 맞아도 한국어 리듬이 어색하면 REVISE 대상이다.
- stiff translated decision label은 쓰지 않는다.
- English phrase를 직역해 이상한 한국어 label로 만들지 않는다.
- 전문 용어가 필요한 경우 English term을 남기고 주변 한국어를 자연스럽게 만든다.

## Source-Backed 압축

- 모든 visible slide 요소는 source line, source markdown, 사용자 reference, 또는 사용자 직접 지시로 추적 가능해야 한다.
- source 문장을 그대로 복붙하지 말고 slide 역할에 맞게 압축한다.
- 압축 과정에서 새로운 비교 축, helper label, metric 해석, 예시를 만들지 않는다.
- source에 있는 주장 강도보다 더 세게 쓰지 않는다.
- source에 있는 의미를 너무 흐려 slogan으로 만들지 않는다.
- 최신 source markdown의 문구가 stale generated phrasing보다 우선한다.

## Quote 규칙

- quote는 짧은 구 단위 또는 source-backed 핵심 문장으로 유지한다.
- 부정적 의견 quote는 짧은 구 단위 문구로 둔다.
- 외부 source phrase를 한국어로 옮길 수 있지만 의미를 보존해야 한다.
- literal translation이 machine translation처럼 읽히면 실패다.
- quote는 일반 card body가 아니라 quote/source treatment로 보여야 한다.
- attribution은 source label과 함께 절제해서 표시한다.

## 한국문학적 어휘

- 한국문학적 어휘는 허용한다.
- 단, source 의미를 선명하게 압축하고 발표 리듬을 살릴 때만 쓴다.
- 과한 문예체, 감상적 수사, source 밖 은유는 금지한다.
- 보기 좋게 만들기 위해 source 밖 말맛을 추가하지 않는다.

## Code와 Technical Text

- code syntax는 원문을 보존한다.
- source code block 내부 주석은 slide 표시에서 제거한다.
- slide를 위해 새 code 주석을 추가하지 않는다.
- 예시 code block은 축약하지 않는다. source-visible 전체 예시 내용이 보여야 한다.
- command, path, API name, protocol은 정확한 표기를 유지한다.

## 검증 기준

- 자동 검사와 reviewer 판단을 함께 통과해야 한다.
- 자동 검사가 통과해도 어색한 한국어가 보이면 실패다.
- HTML 수정 후 작업 범위에 맞게 다음 검증을 실행한다.

```bash
python3 scripts/check_slide_contract.py
python3 scripts/check_slide_korean.py docs/03-html/slides
python3 scripts/check_deck_runtime.py docs/03-html/deck/index.html
```

single-slide 작업이면 대상 slide만 좁혀 실행할 수 있다.

```bash
python3 scripts/check_slide_korean.py docs/03-html/slides/slide-XXX.html
```

`check_slide_korean.py`는 공손체 ending, 번역체, slide-specific awkward copy, 과도하게 긴 문구, prose-like ending, 보고서형 연결어, 어색한 서술 동사를 잡는다. 이 결과는 최소 기준이며, 최종 판단은 source alignment와 사람이 보는 한국어 리듬까지 포함한다.
