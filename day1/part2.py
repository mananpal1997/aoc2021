from aoc_base import BaseSolution, BaseTest


class Solution(BaseSolution):
    _path = __package__

    def solve(self, s: str) -> int:
        increasing = 0

        depths = list(map(int, s.splitlines()))

        for i, depth in enumerate(depths):
            if i > 2 and depth > depths[i - 3]:
                increasing += 1

        return increasing


class TestSolution(Solution, BaseTest):
    _SAMPLES = (("199\n200\n208\n210\n200\n207\n240\n269\n260\n263", 5),)


if __name__ == "__main__":
    raise SystemExit(Solution().main())
