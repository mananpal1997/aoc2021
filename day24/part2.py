from aoc_base import BaseSolution, BaseTest
from day24.utils import find_model_num


class Solution(BaseSolution):
    _path = __package__

    def solve(self, s: str) -> int:
        return find_model_num(s, minimize=True)


class TestSolution(Solution, BaseTest):
    _SAMPLES = ()


if __name__ == "__main__":
    raise SystemExit(Solution().main())
