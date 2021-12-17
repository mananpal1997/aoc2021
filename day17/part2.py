import re

from aoc_base import BaseSolution, BaseTest

TARGET_RE = r"target area: x=(-?\d+)\.\.(-?\d+), y=(-?\d+)\.\.(-?\d+)"


class Solution(BaseSolution):
    _path = __package__

    def solve(self, s: str) -> int:
        match = re.match(TARGET_RE, s)
        if not match:
            raise ValueError(f"Invalid input: {s}")
        x_min, x_max, y_min, y_max = map(int, match.groups())
        meet_criteria = 0
        for candidate_y in range(abs(y_min) * -1, 200):
            for velocity_x in range(x_max + 1):
                velocity_y = candidate_y
                x, y = 0, 0
                for _ in range(300):
                    y += velocity_y
                    x += velocity_x
                    velocity_y -= 1
                    if velocity_x > 0:
                        velocity_x -= 1
                    elif velocity_x < 0:
                        velocity_x += 1
                    if x_min <= x <= x_max and y_min <= y <= y_max:
                        meet_criteria += 1
                        break
                    if y < y_min:
                        break
        return meet_criteria


class TestSolution(Solution, BaseTest):
    _SAMPLES = (("target area: x=20..30, y=-10..-5", 112),)


if __name__ == "__main__":
    raise SystemExit(Solution().main())
