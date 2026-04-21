from __future__ import annotations

from .config import ROOT

CODE_MACHINE = "10111000 00000001 00000000 00000000 00000000"

CODE_ASSEMBLY_MOV = "MOV EAX, 1"

CODE_ASSEMBLY_HELLO = """section .data
  msg db "Hello World"

section .text
  global_start

_start:
\tmov rax, 1
\tmov rdi, 1
\tmov rsi, msg
\tmov rdx, 12
\tsyscall
\tmov rax, 60
\tmov rdi, 0
\tsyscall"""

CODE_C_HELLO = """#include <stdio.h>

int main() {
    printf("Hello\\n");
    return 0;
}"""

CODE_C_POINT = """#include <stdio.h>
#include <stdlib.h>

...

int main() {
    Point* p = (Point*)malloc(sizeof(Point));
    p->x = 10;
    p->y = 20;
    printf(
        "Point: %d, %d\\n",
        p->x,
        p->y
    );
    free(p);
    return 0;
}"""

CODE_JAVA_POINT = """        Point p = new Point(10, 20);
        System.out.println(
            "Point: " + p.x + ", " + p.y
        );
        p = null;"""

CODE_JAVA_HELLO = """public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}"""

CODE_PYTHON_HELLO = 'print("Hello, World!")'

PROMPT_AI_REFACTOR = "이 함수를 리펙토링하고 테스트 코드를 작성해줘."
ASSET_AGENTIC_ROOT = ROOT / "assets/evolution-of-ai-agentic-patterns"
ASSET_COT = ASSET_AGENTIC_ROOT / "02-chain-of-thought.png"
ASSET_REACT = ASSET_AGENTIC_ROOT / "03-react-pattern.png"
ASSET_TOT = ASSET_AGENTIC_ROOT / "04-tree-of-thought.png"
ASSET_ANDREW_NG = ASSET_AGENTIC_ROOT / "05-andrew-ng-agentic-design-patterns.png"
ASSET_CURSOR_ARCH = ASSET_AGENTIC_ROOT / "06-cursor-ai-code-editor-architecture.png"
ASSET_THREE_ERA = ASSET_AGENTIC_ROOT / "01-three-era-timeline.png"
