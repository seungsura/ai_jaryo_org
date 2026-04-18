# 문서 작업 공간

이 디렉터리는 `source -> seminar prose -> html -> pdf -> speaker notes` 생산 파이프라인을 기준으로 정리한 작업 공간입니다. 가장 중요한 기준은 로컬 markdown source이며, 이후 단계의 모든 산출물은 이 source와 세미나 prose에서 파생됩니다.

## 파이프라인 구조

```text
docs/
  README.md
  01-sources/
    README.md
    registry.md
    local-canonical/
    local-supplemental/
    approved-external/
    intake/
    maps/
    provenance/
  02-seminar/
    README.md
    prose/
  03-html/
    README.md
    outline/
    slides/
    shared/
    manifest.md
  04-pdf/
    README.md
    exports/
    qa/
    manifest.md
  05-speaker-notes/
    README.md
    slide-to-script-map.md
    notes/
```

## 계층 규칙

- `01-sources/`만 입력층입니다.
- `02-seminar/`는 source를 종합한 canonical prose 계층입니다.
- `03-html/`, `04-pdf/`, `05-speaker-notes/`는 모두 파생 산출층입니다.
- `assets/`는 별도 보존층이며, 사용자가 명시적으로 허용하지 않는 한 reconstruction source로 보지 않습니다.

## 문서 언어 규칙

- `docs/` 아래의 문서는 한국어를 기본 언어로 작성합니다.
- `term`, 전문용어, product name, service name, library name, framework name, API name, command, file path, protocol처럼 정확한 English 표기가 중요한 항목은 English를 유지합니다.
- 한국어 번역이 오히려 의미를 흐리거나 업계 관용 표현이 English인 경우에는 English를 우선 사용하고, 필요하면 첫 언급에서만 한국어 설명을 덧붙입니다.
- heading과 설명 문장은 한국어를 기본으로 작성합니다.

## 작업 규칙

- 사용자가 명시적으로 허용하지 않는 한 local markdown만 source로 사용합니다.
- 새로운 자료는 먼저 `docs/01-sources/intake/`와 `docs/01-sources/registry.md`에서 분류합니다.
- source provenance와 section mapping은 `docs/01-sources/maps/`와 `docs/01-sources/provenance/`에서 관리합니다.
- 세미나의 main narrative spine은 `docs/02-seminar/prose/00-*.md`부터 `09-*.md`까지에서 유지하고, `docs/02-seminar/prose/90-appendix-references.md`는 별도 appendix로 둡니다.
- 불확실한 내용은 `docs/01-sources/intake/open-questions.md`로 보냅니다.
- 문서의 중심 thesis는 특정 vendor 사용기가 아니라 `Prompt -> Context -> Harness`로 이동해 온 AI coding tool의 흐름과 그 운영 원리를 설명하는 데 둡니다.
- `Claude Code`는 가장 풍부한 local source를 가진 대표 사례로 유지하되, 본문은 `Codex`, `OpenCode`, `Copilot`, `Cursor`를 포함한 broader tool genealogy 위에서 읽히도록 정리합니다.
