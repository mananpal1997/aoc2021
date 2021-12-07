from aoc_base import BaseSolution, BaseTest


class Solution(BaseSolution):
    _path = __package__

    def solve(self, s: str) -> int:
        crabs = sorted(map(int, s.split(",")))
        num_crabs = len(crabs)
        median = (crabs[num_crabs // 2] + crabs[num_crabs // 2 - 1]) // 2
        return sum(abs(c - median) for c in crabs)


class TestSolution(Solution, BaseTest):
    _SAMPLES = (("16,1,2,0,4,2,7,1,2,14", 37),)


if __name__ == "__main__":
    raise SystemExit(Solution().main())
