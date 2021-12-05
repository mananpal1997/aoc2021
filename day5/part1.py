from collections import defaultdict
from typing import Dict, Tuple

from aoc_base import BaseSolution, BaseTest


class Solution(BaseSolution):
    _path = __package__

    def solve(self, s: str) -> int:
        points: Dict[Tuple[int, int], int] = defaultdict(int)
        for line in s.splitlines():
            p1, p2 = line.split(" -> ")
            (x1, y1), (x2, y2) = map(int, p1.split(",")), map(int, p2.split(","))
            if x1 == x2 or y1 == y2:
                for x in range(min(x1, x2), max(x1, x2) + 1):
                    for y in range(min(y1, y2), max(y1, y2) + 1):
                        points[(x, y)] += 1

        return sum(1 for overlap in points.values() if overlap >= 2)


class TestSolution(Solution, BaseTest):
    _SAMPLES = (
        (
            "0,9 -> 5,9\n8,0 -> 0,8\n9,4 -> 3,4\n2,2 -> 2,1\n7,0 -> 7,4\n6,4 -> 2,"
            "0\n0,9 -> 2,9\n3,4 -> 1,4\n0,0 -> 8,8\n5,5 -> 8,2",
            5,
        ),
    )


if __name__ == "__main__":
    raise SystemExit(Solution().main())
