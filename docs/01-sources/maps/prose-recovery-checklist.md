# Prose Recovery Checklist

이 문서는 `docs/02-seminar/prose/`를 복구하거나 새로 다듬을 때 쓰는 한국어 prose 점검표다. 첫 적용 범위는 `01-where-coding-is-going.md`지만, 이후 다른 prose 문서에도 같은 기준을 확장할 수 있다.

## Working order

1. canonical transcript와 source map을 먼저 읽는다.
2. claim을 `public / internal / supplemental`로 분리한다.
3. slide의 대비 구조와 목록이 논리의 핵심이면 prose 안에서 다시 풀어 쓴다.
4. supplemental source는 연결과 설명 보강에만 쓴다.
5. current prose는 마지막에 읽고, source를 먼저 덮어쓰지 않도록 한다.

## Korean gate

- 주어와 동사가 보이는 문장을 우선한다.
- 영어식 추상명사를 늘리는 대신, 누가 무엇을 어떻게 바꾸는지 풀어 쓴다.
- slide slogan은 그대로 복붙하지 말고 설명문으로 복원한다.
- canonical English term은 precision이 떨어질 때만 유지한다.
- 같은 뜻이면 더 평이한 한국어를 택한다.

## Avoid

- `층위`
- `입력 계층`
- `독점적 위치`
- `실무 감각`
- `생산 시스템`
- `관성도 있었다`
- `감각이 있었다`
- 설명 없는 `~에 가깝다`
- source에 있던 구체 예시를 지우고 일반론만 남기는 요약

## Acceptance

- 각 문단이 어떤 source block에서 왔는지 역추적할 수 있어야 한다.
- `Java` / `GC` 예시가 살아 있어야 한다.
- `문서를 잘 쓰는 능력`과 `컨텍스트를 설계하는 능력`이 따로 남아 있어야 한다.
- `기본기 없이는 질문조차 불가`에 해당하는 뜻이 prose 안에서 분명해야 한다.
- public / internal signal이 한 문장 안에서 뒤섞이지 않아야 한다.
