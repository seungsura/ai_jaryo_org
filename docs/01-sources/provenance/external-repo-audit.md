# 외부 Reference Repo 검증 기록

이 문서는 `Youngdong2/claude-seminar-references` 저장소가 실제로 존재하는지, 그리고 세미나 문서에 흡수할 가치가 있는 실자료를 담고 있는지 점검한 기록입니다.

## 저장소 상태

- 저장소: [Youngdong2/claude-seminar-references](https://github.com/Youngdong2/claude-seminar-references)
- 공개 여부: `Public`
- 기본 브랜치: `main`
- 확인 시점: `2026-04-17`
- 구조: 루트에 `README.md` 한 개만 있는 curated bibliography
- 사용자 확인 기준으로 `Youngdong2`는 카카오 AI 팀의 인물입니다.

즉, 이 저장소는 원문 자료를 미러링한 archive가 아니라, 카카오 AI 팀 내부 제작자 네트워크와 연결된 참고 링크 index에 가깝습니다.

## 링크 상태 점검

- raw `README.md`에 포함된 고유 URL `46`개를 점검했습니다.
- `43`개는 `HTTP 200`으로 응답했습니다.
- `1`개는 `HTTP 404`였습니다.
- `2`개는 `LinkedIn`의 `999` 응답으로 자동 검증이 차단되었습니다.

### 확인된 예외

- `404`
  - `Claude Code Agent Teams — Subagent를 넘어 팀으로`
- `999`
  - `https://www.linkedin.com/in/gb-jeong/`
  - `https://www.linkedin.com/in/jyoung105/`

따라서 이 저장소를 “모든 링크가 검증된 완전한 자료실”로 보기는 어렵고, “대부분의 링크가 살아 있는 curated list”로 보는 편이 정확합니다.

## docs에 흡수한 판단

- 그대로 미러링하지 않음
  - 현재 저장소는 `docs/01-sources/` 중심 pipeline이라서, 로컬 provenance 문서에 같은 목록을 통째로 복제하면 중복이 커집니다.
- 선별적으로 반영
  - 이미 본문에 직접 연결된 `TechCrunch`, `spec-kit`, `AI FoMO`, `OECD`, `Drew Breunig`, `Chroma`, `Anthropic`, `Claude Code`, `Team Attention`, `Oh My Claude Code`는 로컬 reference 문서에 반영되어 있습니다.
  - 이 외부 repo에서 새로 의미가 있는 부분은 `Anthropic 공식 블로그` 계열의 curated index와 일부 커뮤니티 링크입니다.

## 흡수 가치가 높은 항목

- `Introduction to Agentic Coding`
- `Key Benefits of Transitioning to Agentic Coding`
- `How to Scale Agentic Coding`
- `How Anthropic Teams Use Claude Code`
- `Managing Context on the Claude Developer Platform`
- `Common Workflow Patterns for AI Agents`
- `Introducing Agent Skills`
- `Building Agents with Skills`
- `Customize Claude Code with Plugins`
- `Claude Code Auto Mode`
- `Security Sandbox`
- `Preview, Review, and Merge on Desktop`
- `Bringing Code Review to Claude Code`
- `How Enterprises Are Building AI Agents in 2026`
- `Eight Trends Defining Software in 2026`

이 항목들은 세미나 본문을 다시 쓸 때 1차 source나 추가 reading list로 연결하기 좋습니다.

## 결론

`Youngdong2/claude-seminar-references`는 실제로 존재하는 public repo이며, 세미나용 외부 참고자료 index로는 유효합니다. 다만 원문 자료를 담은 archive는 아니고, 일부 링크는 깨졌거나 플랫폼 차단으로 자동 검증이 어렵습니다. 앞으로는 이 저장소를 상위 카탈로그로만 참조하고, 실제 본문 provenance는 `docs/01-sources/maps/seminar-claims-and-sources.md`와 `docs/01-sources/provenance/people-and-orgs.md` 같은 로컬 문서에서 관리하는 구조를 유지합니다.
