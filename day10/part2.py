from aoc_base import BaseSolution, BaseTest

BRACKET_MAP = {"(": ")", "[": "]", "{": "}", "<": ">"}
POINTS = {")": 1, "]": 2, "}": 3, ">": 4}


class Solution(BaseSolution):
    _path = __package__

    def solve(self, s: str) -> int:
        autocomplete_scores, incomplete_lines = [], 0
        for line in s.splitlines():
            stack = []
            for c in line:
                if c in BRACKET_MAP.keys():
                    stack.append(c)
                elif c == BRACKET_MAP.get(stack[-1]):
                    stack.pop()
                else:
                    break
            else:
                incomplete_lines += 1
                autocomplete_scores.append(
                    sum(POINTS[BRACKET_MAP[c]] * (5 ** i) for i, c in enumerate(stack))
                )
        return sorted(autocomplete_scores)[incomplete_lines // 2]


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
            288957,
        ),
    )


if __name__ == "__main__":
    raise SystemExit(Solution().main())
