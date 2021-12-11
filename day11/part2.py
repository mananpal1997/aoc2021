from aoc_base import BaseSolution, BaseTest


class Solution(BaseSolution):
    _path = __package__

    def solve(self, s: str) -> int:
        grid = [list(map(int, line)) for line in s.splitlines()]
        n, m = len(grid), len(grid[0])
        DX = [-1, -1, -1, 0, 0, 1, 1, 1]
        DY = [0, -1, 1, -1, 1, -1, 0, 1]
        step = 0
        while True:
            step += 1
            flasher, flashed = [], set()
            for x in range(n):
                for y in range(m):
                    grid[x][y] += 1
                    if grid[x][y] > 9:
                        flasher.append((x, y))
                        flashed.add((x, y))
            while flasher:
                x, y = flasher.pop()
                for dx, dy in zip(DX, DY):
                    if 0 <= x + dx < n and 0 <= y + dy < m:
                        grid[x + dx][y + dy] += 1
                        if grid[x + dx][y + dy] > 9 and (x + dx, y + dy) not in flashed:
                            flasher.append((x + dx, y + dy))
                            flashed.add((x + dx, y + dy))
            if len(flashed) == n * m:
                break
            for (x, y) in flashed:
                grid[x][y] = 0
        return step


class TestSolution(Solution, BaseTest):
    _SAMPLES = (
        (
            "5483143223\n2745854711\n5264556173\n6141336146\n6357385478\n416752464"
            "5\n2176841721\n6882881134\n4846848554\n5283751526",
            195,
        ),
    )


if __name__ == "__main__":
    raise SystemExit(Solution().main())
