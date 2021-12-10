from aoc_base import BaseSolution, BaseTest

BRACKET_MAP = {"(": ")", "[": "]", "{": "}", "<": ">"}
POINTS = {")": 3, "]": 57, "}": 1197, ">": 25137}


class Solution(BaseSolution):
    _path = __package__

    def solve(self, s: str) -> int:
        total = 0
        for line in s.splitlines():
            stack = []
            for c in line:
                if c in BRACKET_MAP.keys():
                    stack.append(c)
                elif c == BRACKET_MAP.get(stack[-1]):
                    stack.pop()
                else:
                    total += POINTS[c]
                    break
        return total


class TestSolution(Solution, BaseTest):
    _SAMPLES = (
        (
            (
                "[({(<(())[]>[[{[]{<()<>>\n"
                "[(()[<>])]({[<{<<[]>>(\n"
                "{([(<{}[<>[]}>{[]{[(<()>\n"
                "(((({<>}<{<{<>}{[]{[]{}\n"
                "[[<[([]))<([[{}[[()]]]\n"
                "[{[{({}]{}}([{[{{{}}([]\n"
                "{<[[]]>}<{[{[{[]{()[[[]\n"
                "[<(<(<(<{}))><([]([]()\n"
                "<{([([[(<>()){}]>(<<{{\n"
                "<{([{{}}[<[[[<>{}]]]>[]]\n"
            ),
            26397,
        ),
    )


if __name__ == "__main__":
    raise SystemExit(Solution().main())
