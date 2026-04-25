# Page Number Mapping (Legacy PDF -> Current Index)

## Scope

- legacy 기준: `output/pdf/harness-full-main-94-current-720x405.pdf`
- current 기준: `docs/03-html/deck/index.html` (footer-right 1-based page)
- 변경 이유: legacy page `19`, `20` 제거

## Conversion Rule

- `1 <= legacy_page <= 18`: current_page = legacy_page
- `legacy_page >= 21`: current_page = legacy_page - 2
- `legacy_page in {19, 20}`: removed (no direct page)

## User Favorite Baseline Mapping

| legacy page | current page | status |
| --- | --- | --- |
| 1 | 1 | active |
| 2 | 2 | active |
| 3 | 3 | active |
| 4 | 4 | active |
| 5 | 5 | active |
| 6 | 6 | active |
| 7 | 7 | active |
| 8 | 8 | active |
| 9 | 9 | active |
| 10 | 10 | active |
| 11 | 11 | active |
| 12 | 12 | active |
| 13 | 13 | active |
| 14 | 14 | active |
| 15 | 15 | active |
| 16 | 16 | active |
| 17 | 17 | active |
| 18 | 18 | active |
| 21 | 19 | active |
| 24 | 22 | active |
| 37 | 35 | active |
| 39 | 37 | active |
| 40 | 38 | active |
| 52 | 50 | active |
| 53 | 51 | active |

## Note

- 피드백 루프에서 사용자가 legacy page 번호로 지시하면 먼저 이 매핑을 적용한 뒤 current page 기준으로 구현/검증한다.
