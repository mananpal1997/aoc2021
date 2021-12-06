from aoc_base import BaseSolution, BaseTest
from collections import Counter


class Solution(BaseSolution):
    _path = __package__

    def solve(self, s: str) -> int:
        lanterns = Counter((map(int, s.split(","))))
        for _ in range(80):
            lanterns, lanterns[8] = (
                Counter(
                    {
                        k - 1 if k else 6: v + lanterns[0] if k == 7 else v
                        for k, v in lanterns.items()
                    }
                ),
                lanterns[0],
            )
        return sum(lanterns.values())


class TestSolution(Solution, BaseTest):
    _SAMPLES = (("3,4,3,1,2", 5934),)


if __name__ == "__main__":
    raise SystemExit(Solution().main())
