# Shared HTML Assets

이 폴더는 HTML deck에서 공통으로 사용하는 스타일, 스크립트, 공용 asset 매핑을 보관합니다.

- `slide-quality-rules.md`: HTML slide 최상위 규칙과 preserved Decision Log
- `decision-log.md`: preserved Decision Log를 보충하는 상세 결정 기록
- `design.md`: tone, palette, typography, spacing, slide grammar를 정리한 보조 design contract
- `layout-shell-reference.md`: 승인된 slide shell id와 required structure catalog
- `minimal-light-adaptation.md`: `make-slide` minimal-light를 Jaryo deck으로 변환한 적용 규칙
- `make-slide-adoption.md`: `make-slide` 채택/비채택과 hybrid output contract
- `tokens.css`: 실제 HTML slide에서 재사용할 CSS custom properties
- `slide-base.css`: slide shell, card, title, footer 같은 공용 presentation primitives

## Required Reading

모든 HTML 관련 작업 전 `slide-quality-rules.md`를 먼저 확인하고, 이어서 `decision-log.md`가 있으면 확인한다. 대상은 slide HTML뿐 아니라 outline, manifest, generator, shared CSS, token, deck HTML, screenshot QA, PDF export QA까지 포함한다.

`slide-quality-rules.md`의 대화 기반 규칙은 이 폴더의 다른 shared 문서와 generator 기존 구현보다 우선한다. `decision-log.md`는 preserved Decision Log를 보충하지만 최상위 규칙을 대체하지 않는다. 새 사용자 피드백은 구현 전에 `slide-quality-rules.md`에 먼저 기록한다.

현재 HTML deck source root는 `docs/02-seminar/harness-rebuilt-md`다. shared 문서와 generator 문구가 오래된 source path를 언급하면 이 root를 기준으로 고친다.

HTML 작업은 orchestrator/subagent workflow가 필수다. subagent prompt에는 `slide-quality-rules.md` 사전 확인, source/reference 밖 생성 금지, 필요한 검증 명령을 명시한다.

## Validation

```bash
python3 scripts/check_slide_contract.py
python3 scripts/check_slide_korean.py docs/03-html/slides
python3 scripts/check_deck_runtime.py docs/03-html/deck/index.html
```
