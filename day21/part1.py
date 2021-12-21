import re

from aoc_base import BaseSolution, BaseTest


class Dice:
    def __init__(self):
        self.start = 0
        self.end = 100
        self.throws = 0

    def __iter__(self) -> "Dice":
        return self

    def __next__(self) -> int:
        if self.start > self.end:
            self.start = 1
        self.start += 1
        self.throws += 1
        return self.start


class Solution(BaseSolution):
    _path = __package__

    def solve(self, s: str) -> int:
        p1_pos, p2_pos = map(int, re.findall(r": (\d+)", s))
        p1_score = p2_score = 0

        dice = Dice()
        min_score_to_win = 1000

        while p1_score < min_score_to_win and p2_score < min_score_to_win:
            steps = next(dice) + next(dice) + next(dice)
            p1_pos = (p1_pos + steps) % 10
            if p1_pos == 0:
                p1_pos = 10
            p1_score += p1_pos
            p1_pos, p1_score, p2_pos, p2_score = p2_pos, p2_score, p1_pos, p1_score

        return min(p1_score, p2_score) * dice.throws


class TestSolution(Solution, BaseTest):
    _SAMPLES = (
        ("Player 1 starting position: 4\nPlayer 2 starting position: 8", 739785),
    )


if __name__ == "__main__":
    raise SystemExit(Solution().main())
