from aoc_base import BaseSolution, BaseTest


class Solution(BaseSolution):
    _path = __package__

    def solve(self, s: str) -> int:
        matrix = [list(map(int, list(line))) for line in s.splitlines()]
        n, m = len(matrix), len(matrix[0])
        DX, DY = [-1, 0, 0, 1], [0, -1, 1, 0]

        basin_sizes = []
        for x in range(n):
            for y in range(m):
                for dx, dy in zip(DX, DY):
                    newx, newy = x + dx, y + dy
                    if newx < 0 or newx >= n or newy < 0 or newy >= m:
                        continue
                    if matrix[x][y] >= matrix[newx][newy]:
                        break
                else:
                    matrix[x][y] = -1
                    basin = [(x, y)]
                    basin_size = 1
                    while basin:
                        xx, yy = basin.pop()
                        for dx, dy in zip(DX, DY):
                            newx, newy = xx + dx, yy + dy
                            if (
                                newx < 0
                                or newx >= n
                                or newy < 0
                                or newy >= m
                                or matrix[newx][newy] in (-1, 9)
                                or matrix[newx][newy] <= matrix[xx][yy]
                            ):
                                continue
                            matrix[newx][newy] = -1
                            basin.append((newx, newy))
                            basin_size += 1
                    basin_sizes.append(basin_size)

        basin_sizes.sort()
        return basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3]


class TestSolution(Solution, BaseTest):
    _SAMPLES = (("2199943210\n3987894921\n9856789892\n8767896789\n9899965678", 1134),)


if __name__ == "__main__":
    raise SystemExit(Solution().main())
