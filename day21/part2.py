from collections import Counter
from functools import lru_cache
import itertools
import re
from typing import Tuple

from aoc_base import BaseSolution, BaseTest

DIRAC_ROLLS = Counter(sum(roll) for roll in itertools.product(range(1, 4), repeat=3))


class Solution(BaseSolution):
    _path = __package__

    @lru_cache(maxsize=None)
    def multiverse(
        self, p1_pos: int, p2_pos: int, p1_score: int, p2_score: int
    ) -> Tuple[int, int]:
        p1_wins = p2_wins = 0
        for roll, cnt in DIRAC_ROLLS.items():
            new_p1_pos = (p1_pos + roll) % 10
            if new_p1_pos == 0:
                new_p1_pos = 10
            new_p1_score = p1_score + new_p1_pos
            if new_p1_score >= 21:
                p1_wins += cnt
            else:
                w2, w1 = self.multiverse(p2_pos, new_p1_pos, p2_score, new_p1_score)
                p1_wins += w1 * cnt
                p2_wins += w2 * cnt
        return p1_wins, p2_wins

    def solve(self, s: str) -> int:
        p1_pos, p2_pos = map(int, re.findall(r": (\d+)", s))
        return max(self.multiverse(p1_pos, p2_pos, 0, 0))


class TestSolution(Solution, BaseTest):
    _SAMPLES = (
        (
            "Player 1 starting position: 4\nPlayer 2 starting position: 8",
            444356092776315,
        ),
    )


if __name__ == "__main__":
    raise SystemExit(Solution().main())
