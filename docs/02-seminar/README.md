# 세미나 문서 구성

이 디렉터리는 source를 종합해 만든 canonical seminar prose 계층입니다. `docs/01-sources/`가 입력층이라면, 이곳은 이후 `03-html`, `04-pdf`, `05-speaker-notes`가 모두 참조해야 하는 기준 문장을 보관합니다.

## 현재 파일 구성

- `prose/00-overview.md`
- `prose/01-where-coding-is-going.md`
- `prose/02-why-claude-code.md`
- `prose/03-ai-era-methodology.md`
- `prose/04-harness-and-context-engineering.md`
- `prose/05-limitations-and-failure-patterns.md`
- `prose/06-multi-agent-patterns.md`
- `prose/07-practical-workflow-and-tooling.md`
- `prose/08-how-this-presentation-was-made.md`
- `prose/09-what-we-should-do-next.md`
- `prose/90-appendix-references.md`

## 편집 원칙

- 문서는 한국어를 기본으로 작성합니다.
- `Harness`, `Prompt`, `Context`, `Spec` 같은 핵심 term은 canonical English 표기를 유지합니다.
- prose는 주장, 논리 순서, 용어 정의, 문단 전개를 책임집니다.
- source provenance와 section mapping은 `docs/01-sources/`에서 관리합니다.
- 근거가 부족하거나 source만으로 확정할 수 없는 내용은 `docs/01-sources/intake/open-questions.md`로 보냅니다.
- 이 계층은 slide copy나 발표 대본을 직접 겸하지 않습니다.
