# Gate Contract

Every evaluator returns:

- `Gate`
- `Scope`
- `Decision`
  - `PASS`
  - `REVISE`
  - `BLOCK`
- `Blocking findings`
- `Required fixes`
- `Recheck scope`
- `Next allowed action`

## Decision Semantics

### PASS

- The target scope may move to the next stage.
- Minor polish notes may exist, but none should block the pipeline.

### REVISE

- The target scope must be revised in the immediately previous stage.
- The pipeline pauses at the current scope only.

### BLOCK

- The issue is structural enough that the scope must move up a level.
- Example:
  - storyline failure that forces outline reconsideration
  - batch allocation failure that invalidates a chapter PM packet

Do not use `BLOCK` for ordinary wording cleanup or single-slide overflow.
