# HTML Slides

이 폴더는 generated slide HTML artifact를 보관합니다. 실제 구현 단위는 `scripts/jaryo_html_deck/slides/chapter_XX/slide_YYY.py`입니다.

- 현재 규칙: `slide-001.html`-`slide-027.html`
- deck order가 바뀌면 `../manifest.md`와 함께 갱신합니다.
- 공용 색상과 spacing은 `../shared/tokens.css`를 재사용합니다.
- 모든 slide root는 `data-slide-id`와 `data-shell`을 가져야 합니다.
- slide module을 수정해 generated HTML을 갱신한 뒤에는 아래 명령으로 기본 contract를 확인합니다.

```bash
python3 scripts/check_slide_contract.py
python3 scripts/check_slide_korean.py docs/03-html/slides
```
