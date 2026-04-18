# HTML Stage

이 디렉터리는 seminar prose를 HTML slide 산출물로 전환하는 단계입니다.

## 구성

- `outline/`: prose를 slide-by-slide outline으로 압축한 계획
- `slides/`: 실제 `slide-XX.html` 파일
- `shared/`: 공용 CSS, JS, 이미지 매핑 같은 HTML 전용 자산
- `manifest.md`: 현재 deck 버전과 주요 산출물 기록

## 원칙

- HTML은 canonical source가 아닙니다.
- deck 구조는 `docs/02-seminar/prose/`와 승인된 outline을 따라야 합니다.
- 시각적 강조를 위해 표현은 바꿔도, 핵심 claim은 prose를 벗어나면 안 됩니다.
