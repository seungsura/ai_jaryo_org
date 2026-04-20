# Slide Outline

- status: 132-slide make-slide rebuild
- canonical prose source: `docs/02-seminar/prose/`
- output deck: `docs/03-html/deck/index.html`
- output script: `docs/03-html/deck/script.md`
- theme: `minimal-light`
- runtime policy: single-file deck, keyboard navigation, active slide switching, print CSS, `data-notes`

## Section Targets

| section | source | target slides |
| --- | --- | --- |
| 00 | `docs/02-seminar/prose/00-overview.md` | 6 |
| 01 | `docs/02-seminar/prose/01-where-coding-is-going.md` | 14 |
| 02 | `docs/02-seminar/prose/02-why-claude-code.md` | 14 |
| 03 | `docs/02-seminar/prose/03-ai-era-methodology.md` | 13 |
| 04 | `docs/02-seminar/prose/04-harness-and-context-engineering.md` | 15 |
| 05 | `docs/02-seminar/prose/05-limitations-and-failure-patterns.md` | 12 |
| 06 | `docs/02-seminar/prose/06-multi-agent-patterns.md` | 14 |
| 07 | `docs/02-seminar/prose/07-practical-workflow-and-tooling.md` | 15 |
| 08 | `docs/02-seminar/prose/08-how-this-presentation-was-made.md` | 10 |
| 09 | `docs/02-seminar/prose/09-what-we-should-do-next.md` | 11 |
| 90 | `docs/02-seminar/prose/90-appendix-references.md` | 8 |

## Slide Registry

### S001. Harness를 설계하는 법
- file: `docs/03-html/slides/slide-001.html`
- slide type: `title`
- layout: `centered`
- shell: `title-hero-shell`
- source section: `00`
- source paragraph block: `00-00`
- key claim: 좋은 모델보다 좋은 하네스가 앞에 선다
- notes intent: 문제의식과 발표 범위를 한 번에 고정
- notes status: `ready`

### S002. 전체 구조
- file: `docs/03-html/slides/slide-002.html`
- slide type: `agenda`
- layout: `wide`
- shell: `agenda-list-shell`
- source section: `00`
- source paragraph block: `00-00`
- key claim: 이 덱은 이동, 수렴, 방법, 구조, 실패, 분해, 운영, 사례, 실천, 출처 순으로 읽힌다
- notes intent: 청중이 132장 전체 지도를 먼저 잡게 만든다
- notes status: `ready`

### S003. 개발의 중심축이 옮겨가고 있다
- file: `docs/03-html/slides/slide-003.html`
- slide type: `bullets`
- layout: `wide`
- shell: `wide-bullets-shell`
- source section: `00`
- source paragraph block: `00-01`
- key claim: 개발의 중심축이 옮겨가고 
- notes intent: opening narrative를 짧은 리듬으로 쪼갠다
- notes status: `ready`

### S004. 운영 구조가 앞선다
- file: `docs/03-html/slides/slide-004.html`
- slide type: `statement`
- layout: `editorial`
- shell: `statement-editorial-shell`
- source section: `00`
- source paragraph block: `00-02`
- key claim: 코딩보다 운영 구조가 앞선다
- notes intent: opening narrative를 짧은 리듬으로 쪼갠다
- notes status: `ready`

### S005. 앞으로 다룰 이야기
- file: `docs/03-html/slides/slide-005.html`
- slide type: `process`
- layout: `wide`
- shell: `process-flow-shell`
- source section: `00`
- source paragraph block: `00-03`
- key claim: 앞으로 다룰 이야기
- notes intent: opening narrative를 짧은 리듬으로 쪼갠다
- notes status: `ready`

### S006. 더 나은 Harness
- file: `docs/03-html/slides/slide-006.html`
- slide type: `statement`
- layout: `editorial`
- shell: `statement-editorial-shell`
- source section: `00`
- source paragraph block: `00-03`
- key claim: 경쟁력은 더 좋은 모델보다 더 나은 하네스에서 갈린다
- notes intent: opening chapter를 한 문장으로 봉합
- notes status: `ready`

### S007. 코딩은 어디로 가고 있는가
- file: `docs/03-html/slides/slide-007.html`
- slide type: `section`
- layout: `centered`
- shell: `section-divider-shell`
- source section: `01`
- source paragraph block: `01-00`
- key claim: 코딩은 어디로 가고 있는가
- notes intent: 01장의 질문을 챕터 단위로 고정
- notes status: `ready`

### S008. 코딩이 사라지는가
- file: `docs/03-html/slides/slide-008.html`
- slide type: `bullets`
- layout: `wide`
- shell: `wide-bullets-shell`
- source section: `01`
- source paragraph block: `01-01`
- key claim: 코딩이 사라지는가
- notes intent: 코딩이 사라지는가, 질문이 잘못됐다를 slide 단위 주장으로 분해
- notes status: `ready`

### S009. 우리는 늘 직접 하던 일을 줄여왔다
- file: `docs/03-html/slides/slide-009.html`
- slide type: `table`
- layout: `wide`
- shell: `evidence-table-shell`
- source section: `01`
- source paragraph block: `01-02`
- key claim: 우리는 늘 직접 하던 일을 줄여왔다
- notes intent: 우리는 늘 직접 하던 일을 줄여왔다를 slide 단위 주장으로 분해
- notes status: `ready`

### S010. 전환이 일어날 때마다
- file: `docs/03-html/slides/slide-010.html`
- slide type: `bullets`
- layout: `wide`
- shell: `wide-bullets-shell`
- source section: `01`
- source paragraph block: `01-02`
- key claim: 우리는 늘 직접 하던 일을 줄여왔다
- notes intent: 우리는 늘 직접 하던 일을 줄여왔다를 slide 단위 주장으로 분해
- notes status: `ready`

### S011. 자연어는 진짜 개발이 아니다!
- file: `docs/03-html/slides/slide-011.html`
- slide type: `bullets`
- layout: `wide`
- shell: `wide-bullets-shell`
- source section: `01`
- source paragraph block: `01-02`
- key claim: 우리는 늘 직접 하던 일을 줄여왔다
- notes intent: 우리는 늘 직접 하던 일을 줄여왔다를 slide 단위 주장으로 분해
- notes status: `ready`

### S012. 이번에도 다르지 않을 것
- file: `docs/03-html/slides/slide-012.html`
- slide type: `bullets`
- layout: `wide`
- shell: `wide-bullets-shell`
- source section: `01`
- source paragraph block: `01-02`
- key claim: 우리는 늘 직접 하던 일을 줄여왔다
- notes intent: 우리는 늘 직접 하던 일을 줄여왔다를 slide 단위 주장으로 분해
- notes status: `ready`

### S013. C Java
- file: `docs/03-html/slides/slide-013.html`
- slide type: `bullets`
- layout: `wide`
- shell: `wide-bullets-shell`
- source section: `01`
- source paragraph block: `01-02`
- key claim: 우리는 늘 직접 하던 일을 줄여왔다
- notes intent: 우리는 늘 직접 하던 일을 줄여왔다를 slide 단위 주장으로 분해
- notes status: `ready`

### S014. 타이핑은 더 이상 실력을 설명하지 못
- file: `docs/03-html/slides/slide-014.html`
- slide type: `bullets`
- layout: `wide`
- shell: `wide-bullets-shell`
- source section: `01`
- source paragraph block: `01-03`
- key claim: 타이핑은 더 이상 실력을 설명하지 못
- notes intent: 타이핑은 더 이상 실력을 설명하지 못한다를 slide 단위 주장으로 분해
- notes status: `ready`

### S015. 문서가 결과를 바꾸는 세계
- file: `docs/03-html/slides/slide-015.html`
- slide type: `bullets`
- layout: `wide`
- shell: `wide-bullets-shell`
- source section: `01`
- source paragraph block: `01-04`
- key claim: 문서가 결과를 바꾸는 세계
- notes intent: 문서가 결과를 바꾸는 세계를 slide 단위 주장으로 분해
- notes status: `ready`

### S016. 개발자의 새로운 역할
- file: `docs/03-html/slides/slide-016.html`
- slide type: `bullets`
- layout: `wide`
- shell: `wide-bullets-shell`
- source section: `01`
- source paragraph block: `01-05`
- key claim: 개발자의 새로운 역할
- notes intent: 개발자의 새로운 역할를 slide 단위 주장으로 분해
- notes status: `ready`

### S017. 그래도 기본기는 더 무거워진다
- file: `docs/03-html/slides/slide-017.html`
- slide type: `bullets`
- layout: `wide`
- shell: `wide-bullets-shell`
- source section: `01`
- source paragraph block: `01-06`
- key claim: 그래도 기본기는 더 무거워진다
- notes intent: 그래도 기본기는 더 무거워진다를 slide 단위 주장으로 분해
- notes status: `ready`

### S018. 데모 수준의 간단한 앱을 만드는 일은
- file: `docs/03-html/slides/slide-018.html`
- slide type: `bullets`
- layout: `wide`
- shell: `wide-bullets-shell`
- source section: `01`
- source paragraph block: `01-06`
- key claim: 그래도 기본기는 더 무거워진다
- notes intent: 그래도 기본기는 더 무거워진다를 slide 단위 주장으로 분해
- notes status: `ready`

### S019. 결론
- file: `docs/03-html/slides/slide-019.html`
- slide type: `statement`
- layout: `editorial`
- shell: `statement-editorial-shell`
- source section: `01`
- source paragraph block: `01-07`
- key claim: 코딩이라는 행위 자체가 끝난다는 말은 틀렸습니다.
- notes intent: 결론를 slide 단위 주장으로 분해
- notes status: `ready`

### S020. AI가 코딩을 대체하는가?”가 아니라
- file: `docs/03-html/slides/slide-020.html`
- slide type: `statement`
- layout: `editorial`
- shell: `statement-editorial-shell`
- source section: `01`
- source paragraph block: `01-07`
- key claim: AI가 코딩을 대체하는가?”가 아니라 “개발자의 숙련은
- notes intent: 결론를 slide 단위 주장으로 분해
- notes status: `ready`

### S021. 왜 Claude Code인가
- file: `docs/03-html/slides/slide-021.html`
- slide type: `section`
- layout: `centered`
- shell: `section-divider-shell`
- source section: `02`
- source paragraph block: `02-00`
- key claim: 왜 Claude Code인가
- notes intent: 02장의 질문을 챕터 단위로 고정
- notes status: `ready`

### S022. 왜 하필 Claude Code인가
- file: `docs/03-html/slides/slide-022.html`
- slide type: `bullets`
- layout: `wide`
- shell: `wide-bullets-shell`
- source section: `02`
- source paragraph block: `02-01`
- key claim: 왜 하필 Claude Code인가
- notes intent: 왜 하필 Claude Code인가를 slide 단위 주장으로 분해
- notes status: `ready`

### S023. 우리가 보려는 것은 단일 제품의 장점
- file: `docs/03-html/slides/slide-023.html`
- slide type: `bullets`
- layout: `wide`
- shell: `wide-bullets-shell`
- source section: `02`
- source paragraph block: `02-01`
- key claim: 왜 하필 Claude Code인가
- notes intent: 왜 하필 Claude Code인가를 slide 단위 주장으로 분해
- notes status: `ready`

### S024. 코딩 에이전트 패러다임 진화 연대기
- file: `docs/03-html/slides/slide-024.html`
- slide type: `table`
- layout: `wide`
- shell: `evidence-table-shell`
- source section: `02`
- source paragraph block: `02-02`
- key claim: 코딩 에이전트 패러다임 진화 연대기
- notes intent: 코딩 에이전트 패러다임 진화 연대기 (2022-2026)를 slide 단위 주장으로 분해
- notes status: `ready`

### S025. 코딩 에이전트 패러다임 진화 연대기
- file: `docs/03-html/slides/slide-025.html`
- slide type: `process`
- layout: `wide`
- shell: `process-flow-shell`
- source section: `02`
- source paragraph block: `02-02`
- key claim: 코딩 에이전트 패러다임 진화 연대기
- notes intent: 코딩 에이전트 패러다임 진화 연대기 (2022-2026)를 slide 단위 주장으로 분해
- notes status: `ready`

### S026. GitHub Copilot
- file: `docs/03-html/slides/slide-026.html`
- slide type: `bullets`
- layout: `wide`
- shell: `wide-bullets-shell`
- source section: `02`
- source paragraph block: `02-03`
- key claim: GitHub Copilot
- notes intent: GitHub Copilot, 프롬프트(Prompt)의 시대를 slide 단위 주장으로 분해
- notes status: `ready`

### S027. 모델이 의도를 정확히 이해하도록 명확한
- file: `docs/03-html/slides/slide-027.html`
- slide type: `bullets`
- layout: `wide`
- shell: `wide-bullets-shell`
- source section: `02`
- source paragraph block: `02-03`
- key claim: GitHub Copilot
- notes intent: GitHub Copilot, 프롬프트(Prompt)의 시대를 slide 단위 주장으로 분해
- notes status: `ready`

### S028. Cursor
- file: `docs/03-html/slides/slide-028.html`
- slide type: `bullets`
- layout: `wide`
- shell: `wide-bullets-shell`
- source section: `02`
- source paragraph block: `02-04`
- key claim: Cursor
- notes intent: Cursor, 컨텍스트(Context)의 시대를 slide 단위 주장으로 분해
- notes status: `ready`

### S029. 컨텍스트 시대가 개념적으로 공식화된 것은
- file: `docs/03-html/slides/slide-029.html`
- slide type: `bullets`
- layout: `wide`
- shell: `wide-bullets-shell`
- source section: `02`
- source paragraph block: `02-04`
- key claim: Cursor
- notes intent: Cursor, 컨텍스트(Context)의 시대를 slide 단위 주장으로 분해
- notes status: `ready`

### S030. 에이전트 루프와 Tool Use
- file: `docs/03-html/slides/slide-030.html`
- slide type: `process`
- layout: `wide`
- shell: `process-flow-shell`
- source section: `02`
- source paragraph block: `02-05`
- key claim: 에이전트 루프와 Tool Use
- notes intent: 에이전트 루프와 Tool Use를 slide 단위 주장으로 분해
- notes status: `ready`

### S031. 쓰레기 데이터가 섞이면 컨텍스트가 오염되고
- file: `docs/03-html/slides/slide-031.html`
- slide type: `process`
- layout: `wide`
- shell: `process-flow-shell`
- source section: `02`
- source paragraph block: `02-05`
- key claim: 에이전트 루프와 Tool Use
- notes intent: 에이전트 루프와 Tool Use를 slide 단위 주장으로 분해
- notes status: `ready`

### S032. Claude Code가 대표 사례가 된 이유
- file: `docs/03-html/slides/slide-032.html`
- slide type: `bullets`
- layout: `wide`
- shell: `wide-bullets-shell`
- source section: `02`
- source paragraph block: `02-06`
- key claim: Claude Code가 대표 사례가 된 이유
- notes intent: Claude Code가 대표 사례가 된 이유를 slide 단위 주장으로 분해
- notes status: `ready`

### S033. 파일을 분석하고 셸을 실행하며 결과를
- file: `docs/03-html/slides/slide-033.html`
- slide type: `bullets`
- layout: `wide`
- shell: `wide-bullets-shell`
- source section: `02`
- source paragraph block: `02-06`
- key claim: Claude Code가 대표 사례가 된 이유
- notes intent: Claude Code가 대표 사례가 된 이유를 slide 단위 주장으로 분해
- notes status: `ready`

### S034. 결론
- file: `docs/03-html/slides/slide-034.html`
- slide type: `statement`
- layout: `editorial`
- shell: `statement-editorial-shell`
- source section: `02`
- source paragraph block: `02-07`
- key claim: 최근의 코딩 도구 경쟁은 특정 제품 한두 개의 우열
- notes intent: 결론를 slide 단위 주장으로 분해
- notes status: `ready`

### S035. AI 시대의 개발 방법론
- file: `docs/03-html/slides/slide-035.html`
- slide type: `section`
- layout: `centered`
- shell: `section-divider-shell`
- source section: `03`
- source paragraph block: `03-00`
- key claim: AI 시대의 개발 방법론
- notes intent: 03장의 질문을 챕터 단위로 고정
- notes status: `ready`

### S036. 방법론이 다시 전면에 나온다
- file: `docs/03-html/slides/slide-036.html`
- slide type: `bullets`
- layout: `wide`
- shell: `wide-bullets-shell`
- source section: `03`
- source paragraph block: `03-01`
- key claim: 방법론이 다시 전면에 나온다
- notes intent: 방법론이 다시 전면에 나온다를 slide 단위 주장으로 분해
- notes status: `ready`

### S037. 왜 지금 방법론
- file: `docs/03-html/slides/slide-037.html`
- slide type: `statement`
- layout: `editorial`
- shell: `statement-editorial-shell`
- source section: `03`
- source paragraph block: `03-02`
- key claim: 왜 지금 방법론
- notes intent: 왜 지금 방법론를 slide 단위 주장으로 분해
- notes status: `ready`

### S038. AI 코딩 방법론 재부상 연대기
- file: `docs/03-html/slides/slide-038.html`
- slide type: `table`
- layout: `wide`
- shell: `evidence-table-shell`
- source section: `03`
- source paragraph block: `03-03`
- key claim: AI 코딩 방법론 재부상 연대기
- notes intent: AI 코딩 방법론 재부상 연대기 (2025-2026)를 slide 단위 주장으로 분해
- notes status: `ready`

### S039. 업계의 고민은 자연스럽게 진화
- file: `docs/03-html/slides/slide-039.html`
- slide type: `process`
- layout: `wide`
- shell: `process-flow-shell`
- source section: `03`
- source paragraph block: `03-03`
- key claim: AI 코딩 방법론 재부상 연대기
- notes intent: AI 코딩 방법론 재부상 연대기 (2025-2026)를 slide 단위 주장으로 분해
- notes status: `ready`

### S040. 구현 전에 방향을 고정하는 규율과
- file: `docs/03-html/slides/slide-040.html`
- slide type: `process`
- layout: `wide`
- shell: `process-flow-shell`
- source section: `03`
- source paragraph block: `03-03`
- key claim: AI 코딩 방법론 재부상 연대기
- notes intent: AI 코딩 방법론 재부상 연대기 (2025-2026)를 slide 단위 주장으로 분해
- notes status: `ready`

### S041. AI에게 가장 거친 가드레일
- file: `docs/03-html/slides/slide-041.html`
- slide type: `bullets`
- layout: `wide`
- shell: `wide-bullets-shell`
- source section: `03`
- source paragraph block: `03-04`
- key claim: AI에게 가장 거친 가드레일
- notes intent: AI에게 가장 거친 가드레일를 slide 단위 주장으로 분해
- notes status: `ready`

### S042. 중요한 것은 에이전트가 제멋대로 테스트를
- file: `docs/03-html/slides/slide-042.html`
- slide type: `bullets`
- layout: `wide`
- shell: `wide-bullets-shell`
- source section: `03`
- source paragraph block: `03-04`
- key claim: AI에게 가장 거친 가드레일
- notes intent: AI에게 가장 거친 가드레일를 slide 단위 주장으로 분해
- notes status: `ready`

### S043. 구현 전에 방향을 못 박는다
- file: `docs/03-html/slides/slide-043.html`
- slide type: `bullets`
- layout: `wide`
- shell: `wide-bullets-shell`
- source section: `03`
- source paragraph block: `03-05`
- key claim: 구현 전에 방향을 못 박는다
- notes intent: 구현 전에 방향을 못 박는다를 slide 단위 주장으로 분해
- notes status: `ready`

### S044. 요점은 하나
- file: `docs/03-html/slides/slide-044.html`
- slide type: `bullets`
- layout: `wide`
- shell: `wide-bullets-shell`
- source section: `03`
- source paragraph block: `03-05`
- key claim: 구현 전에 방향을 못 박는다
- notes intent: 구현 전에 방향을 못 박는다를 slide 단위 주장으로 분해
- notes status: `ready`

### S045. Waterfall과는 무엇이 다른가
- file: `docs/03-html/slides/slide-045.html`
- slide type: `comparison`
- layout: `split`
- shell: `split-compare-shell`
- source section: `03`
- source paragraph block: `03-06`
- key claim: Waterfall과는 무엇이 다른가
- notes intent: Waterfall과는 무엇이 다른가를 slide 단위 주장으로 분해
- notes status: `ready`

### S046. 스펙은 출발선이자
- file: `docs/03-html/slides/slide-046.html`
- slide type: `comparison`
- layout: `split`
- shell: `split-compare-shell`
- source section: `03`
- source paragraph block: `03-06`
- key claim: Waterfall과는 무엇이 다른가
- notes intent: Waterfall과는 무엇이 다른가를 slide 단위 주장으로 분해
- notes status: `ready`

### S047. 결론
- file: `docs/03-html/slides/slide-047.html`
- slide type: `statement`
- layout: `editorial`
- shell: `statement-editorial-shell`
- source section: `03`
- source paragraph block: `03-07`
- key claim: TDD와 SDD는 취향 문제가 아닙니다.
- notes intent: 결론를 slide 단위 주장으로 분해
- notes status: `ready`

### S048. 에이전트를 움직이는 기술
- file: `docs/03-html/slides/slide-048.html`
- slide type: `section`
- layout: `centered`
- shell: `section-divider-shell`
- source section: `04`
- source paragraph block: `04-00`
- key claim: 에이전트를 움직이는 기술
- notes intent: 04장의 질문을 챕터 단위로 고정
- notes status: `ready`

### S049. 이제 병목은 문장보다 운영 구조다
- file: `docs/03-html/slides/slide-049.html`
- slide type: `bullets`
- layout: `wide`
- shell: `wide-bullets-shell`
- source section: `04`
- source paragraph block: `04-01`
- key claim: 이제 병목은 문장보다 운영 구조다
- notes intent: 이제 병목은 문장보다 운영 구조다를 slide 단위 주장으로 분해
- notes status: `ready`

### S050. 진짜 차이를 만드는 것은 따로 
- file: `docs/03-html/slides/slide-050.html`
- slide type: `bullets`
- layout: `wide`
- shell: `wide-bullets-shell`
- source section: `04`
- source paragraph block: `04-01`
- key claim: 이제 병목은 문장보다 운영 구조다
- notes intent: 이제 병목은 문장보다 운영 구조다를 slide 단위 주장으로 분해
- notes status: `ready`

### S051. Prompt
- file: `docs/03-html/slides/slide-051.html`
- slide type: `table`
- layout: `wide`
- shell: `evidence-table-shell`
- source section: `04`
- source paragraph block: `04-02`
- key claim: Prompt
- notes intent: Prompt, Context, Harness는 서로 다른 질문에 답한다를 slide 단위 주장으로 분해
- notes status: `ready`

### S052. 하네스는 둘이 언제
- file: `docs/03-html/slides/slide-052.html`
- slide type: `bullets`
- layout: `wide`
- shell: `wide-bullets-shell`
- source section: `04`
- source paragraph block: `04-02`
- key claim: Prompt
- notes intent: Prompt, Context, Harness는 서로 다른 질문에 답한다를 slide 단위 주장으로 분해
- notes status: `ready`

### S053. Context Engineering은 주입이
- file: `docs/03-html/slides/slide-053.html`
- slide type: `bullets`
- layout: `wide`
- shell: `wide-bullets-shell`
- source section: `04`
- source paragraph block: `04-03`
- key claim: Context Engineering은 주입이 아니라 선별
- notes intent: Context Engineering은 주입이 아니라 선별이다를 slide 단위 주장으로 분해
- notes status: `ready`

### S054. 끝난 시도의 잔해
- file: `docs/03-html/slides/slide-054.html`
- slide type: `bullets`
- layout: `wide`
- shell: `wide-bullets-shell`
- source section: `04`
- source paragraph block: `04-03`
- key claim: Context Engineering은 주입이 아니라 선별
- notes intent: Context Engineering은 주입이 아니라 선별이다를 slide 단위 주장으로 분해
- notes status: `ready`

### S055. Agent = Model + Harness
- file: `docs/03-html/slides/slide-055.html`
- slide type: `bullets`
- layout: `wide`
- shell: `wide-bullets-shell`
- source section: `04`
- source paragraph block: `04-04`
- key claim: Agent = Model + Harness
- notes intent: Agent = Model + Harness를 slide 단위 주장으로 분해
- notes status: `ready`

### S056. 하네스의 5대 해부학
- file: `docs/03-html/slides/slide-056.html`
- slide type: `table`
- layout: `wide`
- shell: `evidence-table-shell`
- source section: `04`
- source paragraph block: `04-05`
- key claim: 하네스의 5대 해부학
- notes intent: 하네스의 5대 해부학를 slide 단위 주장으로 분해
- notes status: `ready`

### S057. 특히 장시간 작업일수록 State
- file: `docs/03-html/slides/slide-057.html`
- slide type: `process`
- layout: `wide`
- shell: `process-flow-shell`
- source section: `04`
- source paragraph block: `04-05`
- key claim: 하네스의 5대 해부학
- notes intent: 하네스의 5대 해부학를 slide 단위 주장으로 분해
- notes status: `ready`

### S058. 기능 블록과 도구 레이어를 섞지 말자
- file: `docs/03-html/slides/slide-058.html`
- slide type: `bullets`
- layout: `wide`
- shell: `wide-bullets-shell`
- source section: `04`
- source paragraph block: `04-06`
- key claim: 기능 블록과 도구 레이어를 섞지 말자
- notes intent: 기능 블록과 도구 레이어를 섞지 말자를 slide 단위 주장으로 분해
- notes status: `ready`

### S059. 규칙 파일은 상시 기준선을 고정
- file: `docs/03-html/slides/slide-059.html`
- slide type: `bullets`
- layout: `wide`
- shell: `wide-bullets-shell`
- source section: `04`
- source paragraph block: `04-07`
- key claim: 규칙 파일은 상시 기준선을 고정
- notes intent: 규칙 파일은 상시 기준선을 고정한다를 slide 단위 주장으로 분해
- notes status: `ready`

### S060. Skills
- file: `docs/03-html/slides/slide-060.html`
- slide type: `bullets`
- layout: `wide`
- shell: `wide-bullets-shell`
- source section: `04`
- source paragraph block: `04-08`
- key claim: Skills
- notes intent: Skills, Hooks, MCP, Plugins는 책임이 다르다를 slide 단위 주장으로 분해
- notes status: `ready`

### S061. 도구 이름을 곧 하네스로 오해하지 말아야 
- file: `docs/03-html/slides/slide-061.html`
- slide type: `bullets`
- layout: `wide`
- shell: `wide-bullets-shell`
- source section: `04`
- source paragraph block: `04-08`
- key claim: Skills
- notes intent: Skills, Hooks, MCP, Plugins는 책임이 다르다를 slide 단위 주장으로 분해
- notes status: `ready`

### S062. 정리 좋은 하네스는 잘 시키는 구조가 아니라
- file: `docs/03-html/slides/slide-062.html`
- slide type: `statement`
- layout: `editorial`
- shell: `statement-editorial-shell`
- source section: `04`
- source paragraph block: `04-09`
- key claim: 정리 좋은 하네스는 잘 시키는 구조가 아니라 잘 멈추는 구조다
- notes intent: 정리 좋은 하네스는 잘 시키는 구조가 아니라 잘 멈추는 구조다를 slide 단위 주장으로 분해
- notes status: `ready`

### S063. 코딩 에이전트 한계와 실패 패턴
- file: `docs/03-html/slides/slide-063.html`
- slide type: `section`
- layout: `centered`
- shell: `section-divider-shell`
- source section: `05`
- source paragraph block: `05-00`
- key claim: 코딩 에이전트 한계와 실패 패턴
- notes intent: 05장의 질문을 챕터 단위로 고정
- notes status: `ready`

### S064. 실패는 부작용이 아니라 운영 설계의 본문
- file: `docs/03-html/slides/slide-064.html`
- slide type: `bullets`
- layout: `wide`
- shell: `wide-bullets-shell`
- source section: `05`
- source paragraph block: `05-01`
- key claim: 실패는 부작용이 아니라 운영 설계의 본문
- notes intent: 실패는 부작용이 아니라 운영 설계의 본문이다를 slide 단위 주장으로 분해
- notes status: `ready`

### S065. 실패는 대개 조용히 누적
- file: `docs/03-html/slides/slide-065.html`
- slide type: `bullets`
- layout: `wide`
- shell: `wide-bullets-shell`
- source section: `05`
- source paragraph block: `05-02`
- key claim: 실패는 대개 조용히 누적
- notes intent: 실패는 대개 조용히 누적된다를 slide 단위 주장으로 분해
- notes status: `ready`

### S066. 시간이 갈수록 실패의 기원을 추적하기는
- file: `docs/03-html/slides/slide-066.html`
- slide type: `bullets`
- layout: `wide`
- shell: `wide-bullets-shell`
- source section: `05`
- source paragraph block: `05-02`
- key claim: 실패는 대개 조용히 누적
- notes intent: 실패는 대개 조용히 누적된다를 slide 단위 주장으로 분해
- notes status: `ready`

### S067. Long Context의 적은 길이가 아니라
- file: `docs/03-html/slides/slide-067.html`
- slide type: `bullets`
- layout: `wide`
- shell: `wide-bullets-shell`
- source section: `05`
- source paragraph block: `05-03`
- key claim: Long Context의 적은 길이가 아니라 조성
- notes intent: Long Context의 적은 길이가 아니라 조성이다를 slide 단위 주장으로 분해
- notes status: `ready`

### S068. Clash는 목표
- file: `docs/03-html/slides/slide-068.html`
- slide type: `bullets`
- layout: `wide`
- shell: `wide-bullets-shell`
- source section: `05`
- source paragraph block: `05-03`
- key claim: Long Context의 적은 길이가 아니라 조성
- notes intent: Long Context의 적은 길이가 아니라 조성이다를 slide 단위 주장으로 분해
- notes status: `ready`

### S069. 세션이 길어질수록 기준은 흐려진다
- file: `docs/03-html/slides/slide-069.html`
- slide type: `bullets`
- layout: `wide`
- shell: `wide-bullets-shell`
- source section: `05`
- source paragraph block: `05-04`
- key claim: 세션이 길어질수록 기준은 흐려진다
- notes intent: 세션이 길어질수록 기준은 흐려진다를 slide 단위 주장으로 분해
- notes status: `ready`

### S070. 오히려 길게 유지할수록 drift를
- file: `docs/03-html/slides/slide-070.html`
- slide type: `bullets`
- layout: `wide`
- shell: `wide-bullets-shell`
- source section: `05`
- source paragraph block: `05-04`
- key claim: 세션이 길어질수록 기준은 흐려진다
- notes intent: 세션이 길어질수록 기준은 흐려진다를 slide 단위 주장으로 분해
- notes status: `ready`

### S071. 실패 신호는 하네스 공백의 이름
- file: `docs/03-html/slides/slide-071.html`
- slide type: `bullets`
- layout: `wide`
- shell: `wide-bullets-shell`
- source section: `05`
- source paragraph block: `05-05`
- key claim: 실패 신호는 하네스 공백의 이름
- notes intent: 실패 신호는 하네스 공백의 이름이다를 slide 단위 주장으로 분해
- notes status: `ready`

### S072. 어떤 상태가 기록되지 않았는가.
- file: `docs/03-html/slides/slide-072.html`
- slide type: `bullets`
- layout: `wide`
- shell: `wide-bullets-shell`
- source section: `05`
- source paragraph block: `05-05`
- key claim: 실패 신호는 하네스 공백의 이름
- notes intent: 실패 신호는 하네스 공백의 이름이다를 slide 단위 주장으로 분해
- notes status: `ready`

### S073. 신뢰는 감정이 아니라 배치다
- file: `docs/03-html/slides/slide-073.html`
- slide type: `bullets`
- layout: `wide`
- shell: `wide-bullets-shell`
- source section: `05`
- source paragraph block: `05-06`
- key claim: 신뢰는 감정이 아니라 배치다
- notes intent: 신뢰는 감정이 아니라 배치다를 slide 단위 주장으로 분해
- notes status: `ready`

### S074. 정리 실패를 줄이는 길은 더 오래 붙드는
- file: `docs/03-html/slides/slide-074.html`
- slide type: `statement`
- layout: `editorial`
- shell: `statement-editorial-shell`
- source section: `05`
- source paragraph block: `05-07`
- key claim: 정리 실패를 줄이는 길은 더 오래 붙드는 것이 아니라 더
- notes intent: 정리 실패를 줄이는 길은 더 오래 붙드는 것이 아니라 더 잘 끊는 것이다를 slide 단위 주장으로 분해
- notes status: `ready`

### S075. 멀티 에이전트 활용 패턴
- file: `docs/03-html/slides/slide-075.html`
- slide type: `section`
- layout: `centered`
- shell: `section-divider-shell`
- source section: `06`
- source paragraph block: `06-00`
- key claim: 멀티 에이전트 활용 패턴
- notes intent: 06장의 질문을 챕터 단위로 고정
- notes status: `ready`

### S076. 병렬화보다 분해가 먼저다
- file: `docs/03-html/slides/slide-076.html`
- slide type: `bullets`
- layout: `wide`
- shell: `wide-bullets-shell`
- source section: `06`
- source paragraph block: `06-01`
- key claim: 병렬화보다 분해가 먼저다
- notes intent: 병렬화보다 분해가 먼저다를 slide 단위 주장으로 분해
- notes status: `ready`

### S077. 병렬화는 결과일 수 있어도 본질은 아닙니다.
- file: `docs/03-html/slides/slide-077.html`
- slide type: `bullets`
- layout: `wide`
- shell: `wide-bullets-shell`
- source section: `06`
- source paragraph block: `06-01`
- key claim: 병렬화보다 분해가 먼저다
- notes intent: 병렬화보다 분해가 먼저다를 slide 단위 주장으로 분해
- notes status: `ready`

### S078. 같은 일을 다섯 방식으로 쪼개기
- file: `docs/03-html/slides/slide-078.html`
- slide type: `process`
- layout: `wide`
- shell: `process-flow-shell`
- source section: `06`
- source paragraph block: `06-02`
- key claim: 같은 일을 다섯 방식으로 쪼개기
- notes intent: 같은 일을 다섯 방식으로 쪼개기를 slide 단위 주장으로 분해
- notes status: `ready`

### S079. 중간 노동을 메인 컨텍스트 밖으로 격리
- file: `docs/03-html/slides/slide-079.html`
- slide type: `bullets`
- layout: `wide`
- shell: `wide-bullets-shell`
- source section: `06`
- source paragraph block: `06-03`
- key claim: 중간 노동을 메인 컨텍스트 밖으로 격리
- notes intent: 중간 노동을 메인 컨텍스트 밖으로 격리한다를 slide 단위 주장으로 분해
- notes status: `ready`

### S080. 긴 작업에서 이 단순한 분리가 생각보다
- file: `docs/03-html/slides/slide-080.html`
- slide type: `bullets`
- layout: `wide`
- shell: `wide-bullets-shell`
- source section: `06`
- source paragraph block: `06-03`
- key claim: 중간 노동을 메인 컨텍스트 밖으로 격리
- notes intent: 중간 노동을 메인 컨텍스트 밖으로 격리한다를 slide 단위 주장으로 분해
- notes status: `ready`

### S081. 계획자가 전체 분해를 쥔다
- file: `docs/03-html/slides/slide-081.html`
- slide type: `bullets`
- layout: `wide`
- shell: `wide-bullets-shell`
- source section: `06`
- source paragraph block: `06-04`
- key claim: 계획자가 전체 분해를 쥔다
- notes intent: 계획자가 전체 분해를 쥔다를 slide 단위 주장으로 분해
- notes status: `ready`

### S082. 같은 목표를 동시에 벌리되 서로를 더럽히지
- file: `docs/03-html/slides/slide-082.html`
- slide type: `bullets`
- layout: `wide`
- shell: `wide-bullets-shell`
- source section: `06`
- source paragraph block: `06-05`
- key claim: 같은 목표를 동시에 벌리되 서로를 더럽히지 않는다
- notes intent: 같은 목표를 동시에 벌리되 서로를 더럽히지 않는다를 slide 단위 주장으로 분해
- notes status: `ready`

### S083. 생성자와 평가자를 갈라 자기최면을 끊는다
- file: `docs/03-html/slides/slide-083.html`
- slide type: `bullets`
- layout: `wide`
- shell: `wide-bullets-shell`
- source section: `06`
- source paragraph block: `06-06`
- key claim: 생성자와 평가자를 갈라 자기최면을 끊는다
- notes intent: 생성자와 평가자를 갈라 자기최면을 끊는다를 slide 단위 주장으로 분해
- notes status: `ready`

### S084. 양방향 대화 자체가 일인 경우에만 쓴다
- file: `docs/03-html/slides/slide-084.html`
- slide type: `bullets`
- layout: `wide`
- shell: `wide-bullets-shell`
- source section: `06`
- source paragraph block: `06-07`
- key claim: 양방향 대화 자체가 일인 경우에만 쓴다
- notes intent: 양방향 대화 자체가 일인 경우에만 쓴다를 slide 단위 주장으로 분해
- notes status: `ready`

### S085. 이런 경우에는 단방향 심부름보다 양방향
- file: `docs/03-html/slides/slide-085.html`
- slide type: `bullets`
- layout: `wide`
- shell: `wide-bullets-shell`
- source section: `06`
- source paragraph block: `06-07`
- key claim: 양방향 대화 자체가 일인 경우에만 쓴다
- notes intent: 양방향 대화 자체가 일인 경우에만 쓴다를 slide 단위 주장으로 분해
- notes status: `ready`

### S086. 패턴 이름보다 handoff 설계가 먼저다
- file: `docs/03-html/slides/slide-086.html`
- slide type: `process`
- layout: `wide`
- shell: `process-flow-shell`
- source section: `06`
- source paragraph block: `06-08`
- key claim: 패턴 이름보다 handoff 설계가 먼저다
- notes intent: 패턴 이름보다 handoff 설계가 먼저다를 slide 단위 주장으로 분해
- notes status: `ready`

### S087. 패턴 선택은 이 질문에 대한 답
- file: `docs/03-html/slides/slide-087.html`
- slide type: `process`
- layout: `wide`
- shell: `process-flow-shell`
- source section: `06`
- source paragraph block: `06-08`
- key claim: 패턴 이름보다 handoff 설계가 먼저다
- notes intent: 패턴 이름보다 handoff 설계가 먼저다를 slide 단위 주장으로 분해
- notes status: `ready`

### S088. 더 많은 AI가 아니라 더 좁은 책임이 필요하다
- file: `docs/03-html/slides/slide-088.html`
- slide type: `bullets`
- layout: `wide`
- shell: `wide-bullets-shell`
- source section: `06`
- source paragraph block: `06-09`
- key claim: 더 많은 AI가 아니라 더 좁은 책임이 필요하다
- notes intent: 더 많은 AI가 아니라 더 좁은 책임이 필요하다를 slide 단위 주장으로 분해
- notes status: `ready`

### S089. 실전 워크플로우와 도구 세팅
- file: `docs/03-html/slides/slide-089.html`
- slide type: `section`
- layout: `centered`
- shell: `section-divider-shell`
- source section: `07`
- source paragraph block: `07-00`
- key claim: 실전 워크플로우와 도구 세팅
- notes intent: 07장의 질문을 챕터 단위로 고정
- notes status: `ready`

### S090. 원리를 잊어도 버티는 구조가 필요하다
- file: `docs/03-html/slides/slide-090.html`
- slide type: `bullets`
- layout: `wide`
- shell: `wide-bullets-shell`
- source section: `07`
- source paragraph block: `07-01`
- key claim: 원리를 잊어도 버티는 구조가 필요하다
- notes intent: 원리를 잊어도 버티는 구조가 필요하다를 slide 단위 주장으로 분해
- notes status: `ready`

### S091. 실전 워크플로우는 네 동사로 굴러간다 Write
- file: `docs/03-html/slides/slide-091.html`
- slide type: `process`
- layout: `wide`
- shell: `process-flow-shell`
- source section: `07`
- source paragraph block: `07-02`
- key claim: 실전 워크플로우는 네 동사로 굴러간다 Write
- notes intent: 실전 워크플로우는 네 동사로 굴러간다 Write, Select, Compress, Isolate를 slide 단위 주장으로 분해
- notes status: `ready`

### S092. command가 먼저이고 tool은 그 뒤다
- file: `docs/03-html/slides/slide-092.html`
- slide type: `bullets`
- layout: `wide`
- shell: `wide-bullets-shell`
- source section: `07`
- source paragraph block: `07-03`
- key claim: command가 먼저이고 tool은 그 뒤다
- notes intent: command가 먼저이고 tool은 그 뒤다를 slide 단위 주장으로 분해
- notes status: `ready`

### S093. Plan-Critic-Build
- file: `docs/03-html/slides/slide-093.html`
- slide type: `bullets`
- layout: `wide`
- shell: `wide-bullets-shell`
- source section: `07`
- source paragraph block: `07-04`
- key claim: Plan-Critic-Build
- notes intent: Plan-Critic-Build를 slide 단위 주장으로 분해
- notes status: `ready`

### S094. 무엇을 끝으로 볼 것인지
- file: `docs/03-html/slides/slide-094.html`
- slide type: `bullets`
- layout: `wide`
- shell: `wide-bullets-shell`
- source section: `07`
- source paragraph block: `07-04`
- key claim: Plan-Critic-Build
- notes intent: Plan-Critic-Build를 slide 단위 주장으로 분해
- notes status: `ready`

### S095. 좋은 워크플로우는 pass/fail보다
- file: `docs/03-html/slides/slide-095.html`
- slide type: `process`
- layout: `wide`
- shell: `process-flow-shell`
- source section: `07`
- source paragraph block: `07-05`
- key claim: 좋은 워크플로우는 pass/fail보다 gate와
- notes intent: 좋은 워크플로우는 pass/fail보다 gate와 Observability를 먼저 세운다를 slide 단위 주장으로 분해
- notes status: `ready`

### S096. pass/fail은 결과를 말하지만
- file: `docs/03-html/slides/slide-096.html`
- slide type: `process`
- layout: `wide`
- shell: `process-flow-shell`
- source section: `07`
- source paragraph block: `07-05`
- key claim: 좋은 워크플로우는 pass/fail보다 gate와
- notes intent: 좋은 워크플로우는 pass/fail보다 gate와 Observability를 먼저 세운다를 slide 단위 주장으로 분해
- notes status: `ready`

### S097. 컨텍스트를 덜어내고 반복 규칙을 자산으로 올린다
- file: `docs/03-html/slides/slide-097.html`
- slide type: `bullets`
- layout: `wide`
- shell: `wide-bullets-shell`
- source section: `07`
- source paragraph block: `07-06`
- key claim: 컨텍스트를 덜어내고 반복 규칙을 자산으로 올린다
- notes intent: 컨텍스트를 덜어내고 반복 규칙을 자산으로 올린다를 slide 단위 주장으로 분해
- notes status: `ready`

### S098. 반복 지시는 Skills로 올리고
- file: `docs/03-html/slides/slide-098.html`
- slide type: `bullets`
- layout: `wide`
- shell: `wide-bullets-shell`
- source section: `07`
- source paragraph block: `07-06`
- key claim: 컨텍스트를 덜어내고 반복 규칙을 자산으로 올린다
- notes intent: 컨텍스트를 덜어내고 반복 규칙을 자산으로 올린다를 slide 단위 주장으로 분해
- notes status: `ready`

### S099. core workflow가 선 뒤에 시야를
- file: `docs/03-html/slides/slide-099.html`
- slide type: `bullets`
- layout: `wide`
- shell: `wide-bullets-shell`
- source section: `07`
- source paragraph block: `07-07`
- key claim: core workflow가 선 뒤에 시야를 교차시킨다
- notes intent: core workflow가 선 뒤에 시야를 교차시킨다를 slide 단위 주장으로 분해
- notes status: `ready`

### S100. cmux와 Git Worktree
- file: `docs/03-html/slides/slide-100.html`
- slide type: `bullets`
- layout: `wide`
- shell: `wide-bullets-shell`
- source section: `07`
- source paragraph block: `07-08`
- key claim: cmux와 Git Worktree
- notes intent: cmux와 Git Worktree를 slide 단위 주장으로 분해
- notes status: `ready`

### S101. 세션이 아니라 이슈가 상태를 들고 간다
- file: `docs/03-html/slides/slide-101.html`
- slide type: `bullets`
- layout: `wide`
- shell: `wide-bullets-shell`
- source section: `07`
- source paragraph block: `07-09`
- key claim: 세션이 아니라 이슈가 상태를 들고 간다
- notes intent: 세션이 아니라 이슈가 상태를 들고 간다를 slide 단위 주장으로 분해
- notes status: `ready`

### S102. 이슈가 작업의 목적과 기준과 증거를 붙들고
- file: `docs/03-html/slides/slide-102.html`
- slide type: `bullets`
- layout: `wide`
- shell: `wide-bullets-shell`
- source section: `07`
- source paragraph block: `07-09`
- key claim: 세션이 아니라 이슈가 상태를 들고 간다
- notes intent: 세션이 아니라 이슈가 상태를 들고 간다를 slide 단위 주장으로 분해
- notes status: `ready`

### S103. 결론 좋은 workflow는 생성 능력이
- file: `docs/03-html/slides/slide-103.html`
- slide type: `statement`
- layout: `editorial`
- shell: `statement-editorial-shell`
- source section: `07`
- source paragraph block: `07-10`
- key claim: 결론 좋은 workflow는 생성 능력이 아니라 운영
- notes intent: 결론 좋은 workflow는 생성 능력이 아니라 운영 구조를 설계한다를 slide 단위 주장으로 분해
- notes status: `ready`

### S104. Codex를 어디에 넣었는가
- file: `docs/03-html/slides/slide-104.html`
- slide type: `section`
- layout: `centered`
- shell: `section-divider-shell`
- source section: `08`
- source paragraph block: `08-00`
- key claim: Codex를 어디에 넣었는가
- notes intent: 08장의 질문을 챕터 단위로 고정
- notes status: `ready`

### S105. 우리는 slide부터 열지 않았다
- file: `docs/03-html/slides/slide-105.html`
- slide type: `bullets`
- layout: `wide`
- shell: `wide-bullets-shell`
- source section: `08`
- source paragraph block: `08-01`
- key claim: 우리는 slide부터 열지 않았다
- notes intent: 우리는 slide부터 열지 않았다를 slide 단위 주장으로 분해
- notes status: `ready`

### S106. source를 입력층에 가둔 이유
- file: `docs/03-html/slides/slide-106.html`
- slide type: `bullets`
- layout: `wide`
- shell: `wide-bullets-shell`
- source section: `08`
- source paragraph block: `08-02`
- key claim: source를 입력층에 가둔 이유
- notes intent: source를 입력층에 가둔 이유를 slide 단위 주장으로 분해
- notes status: `ready`

### S107. prose를 canonical source로
- file: `docs/03-html/slides/slide-107.html`
- slide type: `bullets`
- layout: `wide`
- shell: `wide-bullets-shell`
- source section: `08`
- source paragraph block: `08-03`
- key claim: prose를 canonical source로 세웠다
- notes intent: prose를 canonical source로 세웠다를 slide 단위 주장으로 분해
- notes status: `ready`

### S108. outline과 manifest가 계획을
- file: `docs/03-html/slides/slide-108.html`
- slide type: `bullets`
- layout: `wide`
- shell: `wide-bullets-shell`
- source section: `08`
- source paragraph block: `08-04`
- key claim: outline과 manifest가 계획을 세션 밖으로 끌어냈다
- notes intent: outline과 manifest가 계획을 세션 밖으로 끌어냈다를 slide 단위 주장으로 분해
- notes status: `ready`

### S109. design contract를 먼저 잠그고
- file: `docs/03-html/slides/slide-109.html`
- slide type: `bullets`
- layout: `wide`
- shell: `wide-bullets-shell`
- source section: `08`
- source paragraph block: `08-05`
- key claim: design contract를 먼저 잠그고 Codex를 넣었다
- notes intent: design contract를 먼저 잠그고 Codex를 넣었다를 slide 단위 주장으로 분해
- notes status: `ready`

### S110. 반대로 progress bar
- file: `docs/03-html/slides/slide-110.html`
- slide type: `bullets`
- layout: `wide`
- shell: `wide-bullets-shell`
- source section: `08`
- source paragraph block: `08-05`
- key claim: design contract를 먼저 잠그고 Codex를 넣었다
- notes intent: design contract를 먼저 잠그고 Codex를 넣었다를 slide 단위 주장으로 분해
- notes status: `ready`

### S111. 생성과 검증을 같은 손에 쥐지 않았다
- file: `docs/03-html/slides/slide-111.html`
- slide type: `bullets`
- layout: `wide`
- shell: `wide-bullets-shell`
- source section: `08`
- source paragraph block: `08-06`
- key claim: 생성과 검증을 같은 손에 쥐지 않았다
- notes intent: 생성과 검증을 같은 손에 쥐지 않았다를 slide 단위 주장으로 분해
- notes status: `ready`

### S112. speaker notes를 맨 뒤로 밀었다
- file: `docs/03-html/slides/slide-112.html`
- slide type: `bullets`
- layout: `wide`
- shell: `wide-bullets-shell`
- source section: `08`
- source paragraph block: `08-07`
- key claim: speaker notes를 맨 뒤로 밀었다
- notes intent: speaker notes를 맨 뒤로 밀었다를 slide 단위 주장으로 분해
- notes status: `ready`

### S113. 우리가 만든 것은 slide보다 파이프라인
- file: `docs/03-html/slides/slide-113.html`
- slide type: `bullets`
- layout: `wide`
- shell: `wide-bullets-shell`
- source section: `08`
- source paragraph block: `08-08`
- key claim: 우리가 만든 것은 slide보다 파이프라인
- notes intent: 우리가 만든 것은 slide보다 파이프라인이다를 slide 단위 주장으로 분해
- notes status: `ready`

### S114. 우리가 다음에 해야 할 일
- file: `docs/03-html/slides/slide-114.html`
- slide type: `section`
- layout: `centered`
- shell: `section-divider-shell`
- source section: `09`
- source paragraph block: `09-00`
- key claim: 우리가 다음에 해야 할 일
- notes intent: 09장의 질문을 챕터 단위로 고정
- notes status: `ready`

### S115. 방금 본 사례를 습관으로 바꿔야 
- file: `docs/03-html/slides/slide-115.html`
- slide type: `bullets`
- layout: `wide`
- shell: `wide-bullets-shell`
- source section: `09`
- source paragraph block: `09-01`
- key claim: 방금 본 사례를 습관으로 바꿔야 
- notes intent: 방금 본 사례를 습관으로 바꿔야 한다를 slide 단위 주장으로 분해
- notes status: `ready`

### S116. 암묵지를 문서와 규칙으로 밖에 꺼내라
- file: `docs/03-html/slides/slide-116.html`
- slide type: `bullets`
- layout: `wide`
- shell: `wide-bullets-shell`
- source section: `09`
- source paragraph block: `09-02`
- key claim: 암묵지를 문서와 규칙으로 밖에 꺼내라
- notes intent: 암묵지를 문서와 규칙으로 밖에 꺼내라를 slide 단위 주장으로 분해
- notes status: `ready`

### S117. Thought Partner라는 표현도
- file: `docs/03-html/slides/slide-117.html`
- slide type: `bullets`
- layout: `wide`
- shell: `wide-bullets-shell`
- source section: `09`
- source paragraph block: `09-02`
- key claim: 암묵지를 문서와 규칙으로 밖에 꺼내라
- notes intent: 암묵지를 문서와 규칙으로 밖에 꺼내라를 slide 단위 주장으로 분해
- notes status: `ready`

### S118. 숙련의 중심은 사라지지 않고 이동
- file: `docs/03-html/slides/slide-118.html`
- slide type: `bullets`
- layout: `wide`
- shell: `wide-bullets-shell`
- source section: `09`
- source paragraph block: `09-03`
- key claim: 숙련의 중심은 사라지지 않고 이동
- notes intent: 숙련의 중심은 사라지지 않고 이동한다를 slide 단위 주장으로 분해
- notes status: `ready`

### S119. 모델보다 하네스를 봐야 
- file: `docs/03-html/slides/slide-119.html`
- slide type: `bullets`
- layout: `wide`
- shell: `wide-bullets-shell`
- source section: `09`
- source paragraph block: `09-04`
- key claim: 모델보다 하네스를 봐야 
- notes intent: 모델보다 하네스를 봐야 한다를 slide 단위 주장으로 분해
- notes status: `ready`

### S120. 작은 규칙 파일과 결정론적 문부터 세워라
- file: `docs/03-html/slides/slide-120.html`
- slide type: `bullets`
- layout: `wide`
- shell: `wide-bullets-shell`
- source section: `09`
- source paragraph block: `09-05`
- key claim: 작은 규칙 파일과 결정론적 문부터 세워라
- notes intent: 작은 규칙 파일과 결정론적 문부터 세워라를 slide 단위 주장으로 분해
- notes status: `ready`

### S121. Hooks
- file: `docs/03-html/slides/slide-121.html`
- slide type: `bullets`
- layout: `wide`
- shell: `wide-bullets-shell`
- source section: `09`
- source paragraph block: `09-05`
- key claim: 작은 규칙 파일과 결정론적 문부터 세워라
- notes intent: 작은 규칙 파일과 결정론적 문부터 세워라를 slide 단위 주장으로 분해
- notes status: `ready`

### S122. Build to Delete를 잊지 말자
- file: `docs/03-html/slides/slide-122.html`
- slide type: `bullets`
- layout: `wide`
- shell: `wide-bullets-shell`
- source section: `09`
- source paragraph block: `09-06`
- key claim: Build to Delete를 잊지 말자
- notes intent: Build to Delete를 잊지 말자를 slide 단위 주장으로 분해
- notes status: `ready`

### S123. Harness Engineer라는 역할이
- file: `docs/03-html/slides/slide-123.html`
- slide type: `bullets`
- layout: `wide`
- shell: `wide-bullets-shell`
- source section: `09`
- source paragraph block: `09-07`
- key claim: Harness Engineer라는 역할이 또렷해진다
- notes intent: Harness Engineer라는 역할이 또렷해진다를 slide 단위 주장으로 분해
- notes status: `ready`

### S124. 그 세 가지만 해도 하네스는 추상 개념이
- file: `docs/03-html/slides/slide-124.html`
- slide type: `bullets`
- layout: `wide`
- shell: `wide-bullets-shell`
- source section: `09`
- source paragraph block: `09-07`
- key claim: Harness Engineer라는 역할이 또렷해진다
- notes intent: Harness Engineer라는 역할이 또렷해진다를 slide 단위 주장으로 분해
- notes status: `ready`

### S125. 출처와 후속 읽기를 위한 가이드
- file: `docs/03-html/slides/slide-125.html`
- slide type: `section`
- layout: `centered`
- shell: `section-divider-shell`
- source section: `90`
- source paragraph block: `90-00`
- key claim: 출처와 후속 읽기를 위한 가이드
- notes intent: 90장의 질문을 챕터 단위로 고정
- notes status: `ready`

### S126. 무엇을 어디까지 믿고
- file: `docs/03-html/slides/slide-126.html`
- slide type: `bullets`
- layout: `wide`
- shell: `wide-bullets-shell`
- source section: `90`
- source paragraph block: `90-01`
- key claim: 무엇을 어디까지 믿고
- notes intent: 무엇을 어디까지 믿고, 어디서부터 전진할 것인가를 slide 단위 주장으로 분해
- notes status: `ready`

### S127. 근거의 세 층위
- file: `docs/03-html/slides/slide-127.html`
- slide type: `comparison`
- layout: `split`
- shell: `split-compare-shell`
- source section: `90`
- source paragraph block: `90-02`
- key claim: 근거의 세 층위
- notes intent: 근거의 세 층위를 slide 단위 주장으로 분해
- notes status: `ready`

### S128. 이 층은 공개 1차 근거와 같은 무게로
- file: `docs/03-html/slides/slide-128.html`
- slide type: `comparison`
- layout: `split`
- shell: `split-compare-shell`
- source section: `90`
- source paragraph block: `90-02`
- key claim: 근거의 세 층위
- notes intent: 근거의 세 층위를 slide 단위 주장으로 분해
- notes status: `ready`

### S129. 로컬 source-to-section map
- file: `docs/03-html/slides/slide-129.html`
- slide type: `process`
- layout: `wide`
- shell: `process-flow-shell`
- source section: `90`
- source paragraph block: `90-03`
- key claim: 로컬 source-to-section map
- notes intent: 로컬 source-to-section map를 slide 단위 주장으로 분해
- notes status: `ready`

### S130. 후속 읽기 순서
- file: `docs/03-html/slides/slide-130.html`
- slide type: `process`
- layout: `wide`
- shell: `process-flow-shell`
- source section: `90`
- source paragraph block: `90-04`
- key claim: 후속 읽기 순서
- notes intent: 후속 읽기 순서를 slide 단위 주장으로 분해
- notes status: `ready`

### S131. 외부 reference repo를 다루는 법
- file: `docs/03-html/slides/slide-131.html`
- slide type: `bullets`
- layout: `wide`
- shell: `wide-bullets-shell`
- source section: `90`
- source paragraph block: `90-05`
- key claim: 외부 reference repo를 다루는 법
- notes intent: 외부 reference repo를 다루는 법를 slide 단위 주장으로 분해
- notes status: `ready`

### S132. 다시 열어볼 로컬 지도
- file: `docs/03-html/slides/slide-132.html`
- slide type: `closing`
- layout: `centered`
- shell: `closing-shell`
- source section: `90`
- source paragraph block: `90-06`
- key claim: 근거의 층위를 섞지 않는 읽기 습관이 마지막 안전장치다
- notes intent: 다시 열어볼 로컬 지도를 slide 단위 주장으로 분해
- notes status: `ready`
