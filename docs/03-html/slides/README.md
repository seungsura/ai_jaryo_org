# HTML Slides

이 폴더는 실제 발표용 HTML 파일을 보관합니다.

- 권장 규칙: section별 하위 폴더 또는 `slide-XX.html`
- deck order가 바뀌면 `../manifest.md`와 함께 갱신합니다.
- 공용 색상과 spacing은 `../shared/tokens.css`를 재사용합니다.
- 모든 slide root는 `data-slide-id`와 `data-shell`을 가져야 합니다.
- slide를 수정한 뒤에는 아래 명령으로 기본 contract를 확인합니다.

```bash
python3 scripts/check_slide_contract.py
python3 scripts/check_slide_korean.py docs/03-html/slides
```
