from aoc_base import BaseSolution, BaseTest


class Solution(BaseSolution):
    _path = __package__

    def solve(self, s: str) -> int:
        matrix = [list(map(int, list(line))) for line in s.splitlines()]
        n, m = len(matrix), len(matrix[0])
        total = 0
        DX, DY = [-1, 0, 0, 1], [0, -1, 1, 0]
        for x in range(n):
            for y in range(m):
                for dx, dy in zip(DX, DY):
                    newx, newy = x + dx, y + dy
                    if (
                        newx < 0
                        or newx >= n
                        or newy < 0
                        or newy >= m
                        or matrix[x][y] < matrix[newx][newy]
                    ):
                        continue
                    break
                else:
                    total += 1 + matrix[x][y]
        return total


class TestSolution(Solution, BaseTest):
    _SAMPLES = (("2199943210\n3987894921\n9856789892\n8767896789\n9899965678", 15),)


if __name__ == "__main__":
    raise SystemExit(Solution().main())
