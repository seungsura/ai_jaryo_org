# HTML Stage

이 디렉터리는 seminar prose를 HTML slide 산출물로 전환하는 단계입니다.

## 구성

- `outline/`: prose를 slide-by-slide outline으로 압축한 계획
- `briefs/`: batch별 slide brief packet
- `copy/`: batch별 Korean copy packet
- `slides/`: 실제 `slide-XX.html` 파일
- `deck/`: 최종 standalone deck artifact
- `shared/`: 공용 CSS, JS, 디자인 계약, 이미지 매핑 같은 HTML 전용 자산
- `shared/layout-shell-reference.md`: family보다 더 구체적인 approved shell catalog
- `shared/minimal-light-adaptation.md`: `make-slide` minimal-light theme의 Jaryo 적용 기준
- `shared/make-slide-adoption.md`: `make-slide` 채택 범위와 hybrid output 계약
- `shared/slide-quality-rules.md`: 사용자 대화 기반 slide 품질 규칙과 판단 로그
- `manifest.md`: 현재 deck 버전, slide id, section 대응, 진행 상태를 기록하는 live sync 문서

## 원칙

- HTML slide 작업 전 `shared/slide-quality-rules.md`를 먼저 읽습니다.
- 사용자와 대화하며 확정한 `shared/slide-quality-rules.md`의 규칙은 기존 HTML stage 관례보다 우선합니다.
- HTML은 canonical source가 아닙니다.
- deck 구조는 `docs/02-seminar/prose/`와 승인된 outline을 따라야 합니다.
- 시각적 강조를 위해 표현은 바꿔도, 핵심 claim은 prose를 벗어나면 안 됩니다.
- `shared/design.md`는 HTML stage의 design contract입니다.
- `shared/layout-shell-reference.md`는 HTML stage의 reference shell contract입니다.
- `shared/minimal-light-adaptation.md`는 active theme와 core runtime 적용 범위를 설명합니다.
- `shared/make-slide-adoption.md`는 `make-slide`에서 실제로 채택한 범위와 버린 범위를 고정합니다.
- deck 화면에는 footer 외의 presentation UI chrome를 두지 않습니다.
- `manifest.md`는 slide 제작이 끝난 뒤 작성하는 회고 문서가 아니라, 작업 시작 전에 골격을 만들고 진행 중 계속 갱신하는 운영 문서입니다.
- `slide-outline.md`와 `manifest.md`에는 승인된 결과만 반영합니다. 작업 중 메모와 재작업 범위는 별도 작업 로그로 관리합니다.
- HTML/CSS generation은 Codex가 담당합니다.
- `slides/slide-XX.html`은 source artifact이고, `deck/index.html`은 final standalone artifact입니다.
- chapter batch는 review와 점검을 거친 뒤 HTML generation으로 넘어갑니다.
- built HTML deck는 최종 review와 점검을 거친 뒤 PDF export나 notes 단계로 넘어갑니다.

## 기본 점검 명령

```bash
python3 scripts/check_slide_contract.py
python3 scripts/check_slide_korean.py docs/03-html/slides
python3 scripts/check_deck_runtime.py docs/03-html/deck/index.html
```
