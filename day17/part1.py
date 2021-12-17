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
        for candidate_y in range(200, abs(y_min) * -1 - 1, -1):
            for velocity_x in range(x_max, -1, -1):
                velocity_y = candidate_y
                max_h_achieved, x, y = 0, 0, 0
                for _ in range(300):
                    y += velocity_y
                    x += velocity_x
                    velocity_y -= 1
                    if velocity_x > 0:
                        velocity_x -= 1
                    elif velocity_x < 0:
                        velocity_x += 1
                    max_h_achieved = max(max_h_achieved, y)
                    if x_min <= x <= x_max and y_min <= y <= y_max:
                        return max_h_achieved
                    if y < y_min:
                        break
        raise ValueError("No solution found")


class TestSolution(Solution, BaseTest):
    _SAMPLES = (("target area: x=20..30, y=-10..-5", 45),)


if __name__ == "__main__":
    raise SystemExit(Solution().main())
