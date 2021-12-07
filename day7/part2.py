from typing import Callable, Counter

from aoc_base import BaseSolution, BaseTest


class Solution(BaseSolution):
    _path = __package__

    def solve(self, s: str) -> int:
        triangle_num: Callable[[int], int] = lambda x: x * (x + 1) // 2
        crabs = Counter(map(int, s.split(",")))
        mean = sum(cpos * cnt for cpos, cnt in crabs.items()) // sum(crabs.values())
        return min(
            sum(
                triangle_num(abs(cpos - (mean + 1))) * cnt
                for cpos, cnt in crabs.items()
            ),
            sum(triangle_num(abs(cpos - mean)) * cnt for cpos, cnt in crabs.items()),
        )


class TestSolution(Solution, BaseTest):
    _SAMPLES = (("16,1,2,0,4,2,7,1,2,14", 168),)


if __name__ == "__main__":
    raise SystemExit(Solution().main())
