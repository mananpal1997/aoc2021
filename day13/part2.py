import re
from typing import Set, Tuple

from aoc_base import BaseSolution, BaseTest

FOLD_RE = r"fold along (x|y)=(\d+)"


class Solution(BaseSolution):
    _path = __package__

    def solve(self, s: str) -> int:
        n, m = 0, 0
        dots: Set[Tuple[int, int]] = set()
        point_info, fold_info = s.split("\n\n")
        for line in point_info.splitlines():
            x, y = map(int, line.split(","))
            n, m = max(n, y), max(m, x)
            dots.add((y, x))
        for fold_instr in fold_info.splitlines():
            match = re.match(FOLD_RE, fold_instr)
            if not match:
                raise ValueError("Invalid fold info")
            axis, value = match.group(1), int(match.group(2))
            if axis == "x":
                dots = {(y, x if x < value else 2 * value - x) for y, x in dots}
                m = value - 1
            else:
                dots = {(y if y < value else 2 * value - y, x) for y, x in dots}
                n = value - 1
        print(
            "\n".join(
                [
                    "".join(
                        ["#" if (row, col) in dots else "." for col in range(m + 1)]
                    )
                    for row in range(n + 1)
                ]
            )
        )
        return -1


class TestSolution(Solution, BaseTest):
    _SAMPLES = ()


if __name__ == "__main__":
    raise SystemExit(Solution().main())
