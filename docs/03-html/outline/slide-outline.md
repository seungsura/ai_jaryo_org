# Slide Outline

- status: 00/01 14-slide make-slide rebuild
- canonical source: `docs/02-seminar/harness-rebuilt-md/00-overview.md`, `docs/02-seminar/harness-rebuilt-md/01-코딩은 사라지는가.md`
- output deck: `docs/03-html/deck/index.html`
- output script: `docs/03-html/deck/script.md`
- theme: `minimal-light`
- runtime policy: single-file deck, keyboard navigation, touch/swipe, active slide switching, print CSS
- rejected chrome: progress bar, fullscreen UI, slide counter UI, notes UI, keyboard hint

## Section Targets

| section | source | target slides |
| --- | --- | --- |
| 00 | `docs/02-seminar/harness-rebuilt-md/00-overview.md` | 3 |
| 01 | `docs/02-seminar/harness-rebuilt-md/01-코딩은 사라지는가.md` | 11 |

## Slide Registry

### S001. Harness를 설계하는 법
- file: `docs/03-html/slides/slide-001.html`
- slide type: `title`
- layout: `centered`
- shell: `title-hero-shell`
- source section: `00`
- source paragraph block: `00-00`
- key claim: 에이전트가 일할 환경 설계
- notes intent: 첫 장에서 제목, 부제, 발표자만 고정
- notes status: `ready`

### S002. 시작하며
- file: `docs/03-html/slides/slide-002.html`
- slide type: `process`
- layout: `wide`
- shell: `process-flow-shell`
- source section: `00`
- source paragraph block: `00-01`
- key claim: AI에게 무엇을 말할까에서 AI가 일할 환경 설계로 이동
- notes intent: 챗봇 사용 경험과 도구 수렴을 Harness 문제로 연결
- notes status: `ready`

### S003. 전체 목차
- file: `docs/03-html/slides/slide-003.html`
- slide type: `agenda`
- layout: `wide`
- shell: `agenda-list-shell`
- source section: `00`
- source paragraph block: `00-03`
- key claim: Harness 관점으로 읽는 9개 장
- notes intent: 00-overview의 목차 표를 한 장에 압축
- notes status: `ready`

### S004. 코딩은 사라지는가
- file: `docs/03-html/slides/slide-004.html`
- slide type: `section`
- layout: `centered`
- shell: `section-divider-shell`
- source section: `01`
- source paragraph block: `01-00`
- key claim: 개발의 추상화 수준 상승
- notes intent: 01장의 질문을 챕터 단위로 고정
- notes status: `ready`

### S005. 기계어 → 어셈블리
- file: `docs/03-html/slides/slide-005.html`
- slide type: `comparison`
- layout: `split`
- shell: `split-compare-shell`
- source section: `01`
- source paragraph block: `01-01`
- key claim: 이진 코드 직접 작성에서 명령어 기호로
- notes intent: 언어 발전의 첫 추상화 사례
- notes status: `ready`

### S006. 어셈블리 → C/Pascal
- file: `docs/03-html/slides/slide-006.html`
- slide type: `comparison`
- layout: `split`
- shell: `split-compare-shell`
- source section: `01`
- source paragraph block: `01-01`
- key claim: 레지스터와 syscall에서 함수와 컴파일러로
- notes intent: 어셈블리와 C/Pascal의 표현량 차이
- notes status: `ready`

### S007. C → Java
- file: `docs/03-html/slides/slide-007.html`
- slide type: `comparison`
- layout: `split`
- shell: `split-compare-shell`
- source section: `01`
- source paragraph block: `01-01`
- key claim: 수동 메모리 관리에서 GC로
- notes intent: 메모리 관리 책임의 이동
- notes status: `ready`

### S008. Java → Python
- file: `docs/03-html/slides/slide-008.html`
- slide type: `comparison`
- layout: `split`
- shell: `split-compare-shell`
- source section: `01`
- source paragraph block: `01-01`
- key claim: 보일러플레이트 축소와 표현 밀도 상승
- notes intent: Java와 Python의 boilerplate 차이
- notes status: `ready`

### S009. AI 개발
- file: `docs/03-html/slides/slide-009.html`
- slide type: `comparison`
- layout: `split`
- shell: `split-compare-shell`
- source section: `01`
- source paragraph block: `01-01`
- key claim: 자연어 지시에서 작업 위임으로
- notes intent: 언어 발전 사례의 현재형
- notes status: `ready`

### S010. 직접 하던 일의 감소
- file: `docs/03-html/slides/slide-010.html`
- slide type: `table`
- layout: `wide`
- shell: `evidence-table-shell`
- source section: `01`
- source paragraph block: `01-02`
- key claim: 직접 작성 부담의 지속적 위임
- notes intent: 시대별 위임 표와 질문 반전
- notes status: `ready`

### S011. 숫자로 보는 변화
- file: `docs/03-html/slides/slide-011.html`
- slide type: `table`
- layout: `wide`
- shell: `evidence-table-shell`
- source section: `01`
- source paragraph block: `01-03`
- key claim: 타이핑 비중 감소의 현장 신호
- notes intent: 숫자 근거를 대형 카드와 표로 압축
- notes status: `ready`

### S012. 문서의 코드화
- file: `docs/03-html/slides/slide-012.html`
- slide type: `table`
- layout: `wide`
- shell: `evidence-table-shell`
- source section: `01`
- source paragraph block: `01-04`
- key claim: 문서의 실행 경로 편입
- notes intent: 문서 역할 변화와 규칙 파일 예시
- notes status: `ready`

### S013. 컨텍스트를 설계하는 능력
- file: `docs/03-html/slides/slide-013.html`
- slide type: `comparison`
- layout: `split`
- shell: `split-compare-shell`
- source section: `01`
- source paragraph block: `01-05`
- key claim: 개발자의 역할은 환경 설계와 결과 판단으로 이동
- notes intent: Harness Engineer의 핵심 역량
- notes status: `ready`

### S014. 기초의 중요성
- file: `docs/03-html/slides/slide-014.html`
- slide type: `statement`
- layout: `editorial`
- shell: `statement-editorial-shell`
- source section: `01`
- source paragraph block: `01-06`
- key claim: 타이핑은 줄고 시스템 판단은 남는다
- notes intent: 01장 결론 전환
- notes status: `ready`
