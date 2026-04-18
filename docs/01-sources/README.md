# Sources Layer

이 디렉터리는 세미나 제작의 입력층입니다. 원본 markdown source, intake 상태, source map, provenance 문서를 이곳에서 관리합니다.

## 구성

- `local-canonical/`: 세미나의 주된 narrative spine을 제공하는 핵심 source
- `local-supplemental/`: 본문을 보강하는 로컬 supplemental source
- `approved-external/`: 사용자가 명시적으로 승인한 외부 source snapshot
- `intake/`: 신규 source 접수와 미해결 이슈
- `maps/`: source가 seminar 어느 섹션을 지지하는지 정리한 연결 문서
- `provenance/`: 인물, 기관, 외부 repo audit 같은 배경성 provenance
- `registry.md`: 현재 source의 등급과 역할을 한 눈에 보는 인덱스

## 운영 원칙

- canonical 여부는 파일 위치로 구분합니다.
- 새 자료는 곧바로 prose에 넣지 않고 먼저 `intake/`와 `registry.md`에 기록합니다.
- source map은 서술형 본문이 아니라 연결 정보에 집중합니다.
- provenance 문서는 세미나의 근거 경계를 분명히 하기 위한 보조 문서입니다.
