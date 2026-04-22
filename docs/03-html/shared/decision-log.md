# HTML Slide Decision Log

이 문서는 `docs/03-html/shared/slide-quality-rules.md`의 `Decision Log`를 보완하는 append-only future decision log다. 이 파일은 preserved Decision Log를 대체하지 않는다. 최상위 authority와 active rule은 항상 `slide-quality-rules.md`에 먼저 기록한다.

## 2026-04-22

- Approved HTML Slide Rules 재정비 계획 v5를 기준으로 `slide-quality-rules.md`를 top-level HTML slide authority로 재구성하기로 결정했다.
- 최상위 구조는 `Authority`, `Workflow Gate`, `Source Discipline`, `Copy/Tone`, `Design Direction`, `Visual Reference Baseline`, `Reference Analysis Protocol`, `Layout Grammar`, `Reusable Patterns`, `Implementation Contract`, `Validation Contract`, `Decision Log`, `Traceability` 순서로 고정했다.
- 기존 `slide-quality-rules.md`의 Decision Log entries는 문서 안에 verbatim 또는 nearly verbatim으로 보존하고, 외부 파일로 이동하거나 요약하지 않기로 결정했다.
- `Deprecated/Replaced Rules`는 active rules가 아니라 `Traceability` history로 둔다.
- slide-number-specific active rules는 가능한 reusable meaning/design patterns로 일반화하고, S001-S027의 fixed values는 `Traceability`에 보존한다.
- Visual Reference Baseline은 `output/pdf/harness-00-01-current-720x405.pdf`, `assets/claude-code-seminar-kakao/page-028.png`, `assets/claude-code-seminar-kakao/page-032.png`, `assets/claude-code-seminar-kakao/page-037.png`, `assets/claude-code-seminar-kakao/page-053.png`, `assets/claude-code-seminar-kakao/page-064.png`, `assets/claude-code-seminar-kakao/page-067.png`로 둔다.
- Visual Reference Baseline은 composition/layout/diagram soft reference only이며 content source가 아니다.
- warm brown palette, section pill, character images 복사를 금지하고, `theme-minimal-light` blue/neutral palette를 유지한다.
- 이번 작업은 rules-document core only로 제한한다. HTML/CSS/generator/tests/generated slides/deck/PDF는 수정하지 않고, `check_slide_*` 같은 HTML 검증도 실행하지 않는다.
- page-specific reference analysis를 `slide-quality-rules.md`에 반영했다. page-028, page-032, page-037, page-053, page-064, page-067은 structure-only soft guidelines로 쓰며, content source나 palette/character/image copying 근거로 쓰지 않는다.
