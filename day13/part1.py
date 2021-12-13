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
        match = re.match(FOLD_RE, fold_info.splitlines()[0])
        if not match:
            raise ValueError("Invalid fold info")
        axis, value = match.group(1), int(match.group(2))
        value = int(value)
        if axis == "x":
            return len({(y, x if x < value else 2 * value - x) for y, x in dots})
        else:
            return len({(y if y < value else 2 * value - y, x) for y, x in dots})


class TestSolution(Solution, BaseTest):
    _SAMPLES = (
        (
            (
                "6,10\n0,14\n9,10\n0,3\n10,4\n4,11\n6,0\n6,12\n4,1\n0,13\n"
                "10,12\n3,4\n3,0\n8,4\n1,10\n2,14\n8,10\n9,0\n\n"
                "fold along y=7\nfold along x=5"
            ),
            17,
        ),
    )


if __name__ == "__main__":
    raise SystemExit(Solution().main())
