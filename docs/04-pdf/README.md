# PDF Stage

이 디렉터리는 HTML deck을 PDF로 고정하는 단계입니다.

## 구성

- `exports/`: 실제 PDF 산출물
- `qa/`: PDF 검수 기록과 수정 메모
- `manifest.md`: 어떤 HTML 버전에서 어떤 PDF가 나왔는지 기록

## 원칙

- PDF는 배포용 고정본이며 편집 source가 아닙니다.
- PDF 검수는 HTML 렌더 결과를 기준으로 수행합니다.
