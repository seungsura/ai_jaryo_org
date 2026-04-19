# Shared HTML Assets

이 폴더는 HTML deck에서 공통으로 사용하는 스타일, 스크립트, 공용 asset 매핑을 보관합니다.

- `design.md`: tone, palette, typography, spacing, slide grammar를 고정하는 design contract
- `layout-shell-reference.md`: 승인된 slide shell id와 required structure catalog
- `minimal-light-adaptation.md`: `make-slide` minimal-light를 Jaryo deck으로 변환한 적용 규칙
- `tokens.css`: 실제 HTML slide에서 재사용할 CSS custom properties
- `slide-base.css`: slide shell, card, title, footer 같은 공용 presentation primitives

## Validation

```bash
python3 scripts/check_slide_contract.py
python3 scripts/check_slide_korean.py docs/03-html/slides
```
