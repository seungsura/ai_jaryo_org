# Chapter-Local HTML Slide Workspace

이 폴더는 병렬 worktree에서 slide number 충돌을 피하기 위한 chapter-local staging 영역이다.

## 원칙

- 전역 `SXXX`와 `slide-XXX` 번호는 마지막 main 통합 전까지 임시값이다.
- 각 chapter 작업은 자기 chapter 폴더 아래에서 local slide order와 임시 번호를 함께 관리한다.
- chapter 작업 중에는 다른 chapter의 전역 번호를 기준으로 파일 소유권을 판단하지 않는다.
- main 통합 시 모든 작업 브랜치의 chapter-local 진행사항을 먼저 합치고, 마지막에 numbering-only pass로 전역 번호만 재계산한다.
- numbering-only pass에서는 slide copy, visual structure, source-backed meaning을 바꾸지 않는다.

## 권장 폴더 형태

```text
docs/03-html/chapters/
  chapter-03/
    README.md
  chapter-04/
    README.md
```

chapter 폴더 안의 문서는 해당 chapter의 local order, 임시 번호, source block, generated artifact 위치를 추적한다.
