# Jaryo Seminar Workspace

이 저장소는 세미나 제작을 `source -> seminar prose -> html -> pdf -> speaker notes` 파이프라인으로 관리합니다.

## 주요 경로

- `docs/01-sources/`
  - 원본 markdown source, intake, source map, provenance
- `docs/02-seminar/prose/`
  - canonical seminar prose
- `docs/03-html/`
  - HTML slide outline과 구현
  - 모든 HTML 관련 작업 전 `docs/03-html/shared/slide-quality-rules.md` 확인
- `docs/04-pdf/`
  - PDF export와 QA
- `docs/05-speaker-notes/`
  - 발표 대본과 slide 대응표

## Source Archive

- `docs/01-sources/local-canonical/claude-code-seminar-kakao.md`
- `docs/01-sources/local-supplemental/prompt-context-harness-1-15.md`
- `docs/01-sources/local-supplemental/claude-code-mastery-playbook.md`
- `docs/01-sources/local-supplemental/evolution-of-ai-agentic-patterns.md`

## Asset Folders

- `assets/prompt-context-harness-1-15`
- `assets/claude-code-seminar-kakao`
- `assets/claude-code-mastery-playbook`
- `assets/evolution-of-ai-agentic-patterns`

## Preservation Note

- PDF 기반 아카이브는 page-by-page OCR transcription과 원본 렌더 이미지를 함께 보존합니다.
- 웹 article 기반 아카이브는 원문 Markdown을 기준으로 보존하고, 본문에서 사용한 figure를 로컬 `assets/` 경로로 치환합니다.
