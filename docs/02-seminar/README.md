# 세미나 문서 구성

이 디렉터리는 source를 종합해 만든 canonical seminar prose 계층입니다. `docs/01-sources/`가 입력층이라면, 이곳은 이후 `03-html`, `04-pdf`, `05-speaker-notes`가 모두 참조해야 하는 기준 문장을 보관합니다.

## 현재 파일 구성

- `prose/목표-지도.md`
- `prose/00-코딩은-사라지는가.md`
- `prose/01-챗봇과-싸우지-않기.md`
- `prose/02-하네스는-무엇인가.md`
- `prose/03-이렇게-하면-망한다.md`
- `prose/04-먼저-방향을-잡는다.md`
- `prose/05-기계가-막을-수-있는-것은-앞에서-막는다.md`
- `prose/06-하나의-AI에게-다-맡기지-않는다.md`
- `prose/07-실전-하네스는-파일과-명령어로-남는다.md`
- `prose/08-이-발표-자체가-하네스였다.md`
- `prose/09-하네스-엔지니어.md`

## 편집 원칙

- 문서는 한국어를 기본으로 작성합니다.
- `Harness`, `Prompt`, `Context`, `Spec` 같은 핵심 term은 canonical English 표기를 유지합니다.
- prose는 주장, 논리 순서, 용어 정의, 문단 전개를 책임집니다.
- source provenance와 section mapping은 `docs/01-sources/`에서 관리합니다.
- 근거가 부족하거나 source만으로 확정할 수 없는 내용은 `docs/01-sources/intake/open-questions.md`로 보냅니다.
- 이 계층은 slide copy나 발표 대본을 직접 겸하지 않습니다.

## 다듬기 루프

- canonical prose는 `docs/00-process/seminar-refinement-plan.md`의 per-document loop를 기본값으로 다듬습니다.
- 각 chapter는 `목표-지도.md`, 인접 chapter, source map, open questions를 묶은 reference shell을 먼저 읽고 수정합니다.
- review는 `PASS`, `REVISE`, `BLOCK`으로만 반환하고, `REVISE` 또는 `BLOCK`이면 exact rework scope를 남깁니다.
- 진행 상태와 다음 패스 목표는 `docs/00-process/seminar-refinement-manifest.md`에 live sync로 기록합니다.
