# Seminar Refinement Plan

이 문서는 `docs/02-seminar/prose/`를 반복적으로 다듬기 위한 운영 계획이다. `docs/02-seminar/` 안에는 실제 seminar 문서만 남기고, 편집 루프와 상태 추적은 이 계층에서 관리한다.

## 목적

- 초반부 chapter에서 확보된 문장 압력과 논리 리듬을 후반부까지 맞춘다.
- chapter별 품질 편차를 줄인다.
- 편집 판단과 남은 drift를 세션 밖 파일에 남겨 다음 패스가 같은 기준으로 이어지게 한다.

## 루프 원칙

- `revfactory/harness`에서 가져올 것은 producer-reviewer 분리와 gate 기반 재작업 범위 고정이다.
- `make-slide`에서 가져올 것은 reference shell 고정과 live manifest 운영이다.
- local markdown만 source로 사용한다.
- 근거가 비면 채우지 말고 `docs/01-sources/intake/open-questions.md`로 올린다.

## Reference Shell

각 file을 손보기 전에 아래 묶음을 먼저 읽는다.

1. target file
2. `docs/02-seminar/prose/00-overview.md`
3. target file의 직전/직후 chapter
4. 관련 `docs/01-sources/maps/*.md`
5. `docs/01-sources/intake/open-questions.md`

## 반복 루프

1. scope lock
   - 이번 패스에서 다룰 file과 section 목표를 한 줄로 적는다.
2. shell read
   - overview, 인접 chapter, source map을 함께 읽고 chapter 역할을 다시 고정한다.
3. prose pass
   - 설명문 냄새, report-style cadence, translationese, 중복 정의를 먼저 걷어낸다.
4. storyline gate
   - chapter handoff, 논리 점프, 중복 claim을 본다.
   - 결과는 `PASS`, `REVISE`, `BLOCK`만 허용한다.
5. tone gate
   - 한국어 압력, 리듬, 문장 생동감, 과한 해설체를 본다.
   - reviewer는 직접 rewrite하지 않고 exact rework scope만 남긴다.
6. revise
   - `REVISE` 또는 `BLOCK`에서 지적된 범위만 다시 고친다.
7. manifest sync
   - `docs/00-process/seminar-refinement-manifest.md`를 갱신한다.

## Gate 기준

### `PASS`

- chapter 목적이 선명하다
- 앞뒤 chapter와 handoff가 자연스럽다
- 기술 블로그 에세이 톤이 유지된다

### `REVISE`

- 주장 자체는 맞지만 문장 리듬, handoff, 압축도가 약하다
- paragraph 수준의 정확한 재작업 범위를 남겨야 한다

### `BLOCK`

- chapter boundary가 흔들린다
- source support가 부족하다
- 인접 chapter와 구조 충돌이 있다

## 실행 순서

현재 기본 순서는 아래와 같다.

1. `04-harness-and-context-engineering.md`
2. `05-limitations-and-failure-patterns.md`
3. `06-multi-agent-patterns.md`
4. `07-practical-workflow-and-tooling.md`
5. `08-how-this-presentation-was-made.md`
6. `09-what-we-should-do-next.md`
7. `90-appendix-references.md`

초반부 `00`~`03`은 기준선 shell로 계속 참조한다.

## 패스 산출물

각 패스가 끝나면 아래 네 줄을 반드시 남긴다.

1. 무엇이 좋아졌는가
2. 아직 어디가 약한가
3. 어떤 drift가 반복되는가
4. 다음 패스가 어디서 시작되는가

같은 drift가 두 번 반복되면 file만의 문제가 아니라 loop 설정 문제로 보고 prompt, template, reference shell 중 무엇을 보강할지 함께 기록한다.
