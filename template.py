from aoc_base import BaseSolution, BaseTest


class Solution(BaseSolution):
    _path = __package__

    def solve(self, s: str) -> int:
        ...


class TestSolution(Solution, BaseTest):
    _SAMPLES = ()


if __name__ == "__main__":
    raise SystemExit(Solution().main())
