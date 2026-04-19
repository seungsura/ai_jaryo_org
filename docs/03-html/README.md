# HTML Stage

이 디렉터리는 seminar prose를 HTML slide 산출물로 전환하는 단계입니다.

## 구성

- `outline/`: prose를 slide-by-slide outline으로 압축한 계획
- `slides/`: 실제 `slide-XX.html` 파일
- `shared/`: 공용 CSS, JS, 디자인 계약, 이미지 매핑 같은 HTML 전용 자산
- `shared/layout-shell-reference.md`: family보다 더 구체적인 approved shell catalog
- `shared/minimal-light-adaptation.md`: `make-slide` minimal-light theme의 Jaryo 적용 기준
- `manifest.md`: 현재 deck 버전, slide id, section 대응, 진행 상태를 기록하는 live sync 문서

## 원칙

- HTML은 canonical source가 아닙니다.
- deck 구조는 `docs/02-seminar/prose/`와 승인된 outline을 따라야 합니다.
- 시각적 강조를 위해 표현은 바꿔도, 핵심 claim은 prose를 벗어나면 안 됩니다.
- `shared/design.md`는 HTML stage의 design contract입니다.
- `shared/layout-shell-reference.md`는 HTML stage의 reference shell contract입니다.
- `shared/minimal-light-adaptation.md`는 active theme와 core runtime 적용 범위를 설명합니다.
- deck 화면에는 footer 외의 presentation UI chrome를 두지 않습니다.
- `manifest.md`는 slide 제작이 끝난 뒤 작성하는 회고 문서가 아니라, 작업 시작 전에 골격을 만들고 진행 중 계속 갱신하는 운영 문서입니다.
- `slide-outline.md`와 `manifest.md`에는 승인된 결과만 반영합니다. 내부 brief나 gate findings는 `.codex/` 계층에서 운용합니다.
- slide 관련 한국어 작성은 Gemini를 사용하고, HTML/CSS generation은 Codex가 담당합니다.
- chapter batch는 pre-HTML gate를 통과해야 HTML generation으로 넘어갈 수 있습니다.
- built HTML deck는 post-HTML gate와 final deck gate를 통과해야 PDF export와 speaker notes로 넘어갈 수 있습니다.

## 기본 점검 명령

```bash
python3 scripts/check_slide_contract.py
python3 scripts/check_slide_korean.py docs/03-html/slides
```
