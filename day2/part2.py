from aoc_base import BaseSolution, BaseTest


class Submarine:
    def __init__(self) -> None:
        self.x = 0
        self.y = 0
        self.aim = 0

    def move(self, direction: str, distance: int) -> None:
        if direction == "up":
            self.aim -= distance
        elif direction == "down":
            self.aim += distance
        elif direction == "forward":
            self.x += distance
            self.y += self.aim * distance
        else:
            raise ValueError("Invalid direction")


class Solution(BaseSolution):
    _path = __package__

    def solve(self, s: str) -> int:
        sub = Submarine()
        for line in s.splitlines():
            direction, distance = line.split(" ")
            sub.move(direction, int(distance))
        return sub.x * sub.y


class TestSolution(Solution, BaseTest):
    _SAMPLES = (("forward 5\ndown 5\nforward 8\nup 3\ndown 8\nforward 2", 900),)


if __name__ == "__main__":
    raise SystemExit(Solution().main())
