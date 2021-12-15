from heapq import heappop, heappush

from aoc_base import BaseSolution, BaseTest


class Solution(BaseSolution):
    _path = __package__

    def solve(self, s: str) -> int:
        grid = [list(map(int, list(line))) for line in s.splitlines()]
        n, m = len(grid), len(grid[0])
        DX = [0, 1, -1, 0]
        DY = [1, 0, 0, -1]
        heap = [(0, 0, 0)]
        seen = {(0, 0)}
        while heap:
            risk, x, y = heappop(heap)
            if x == n - 1 and y == m - 1:
                return risk
            for dx, dy in zip(DX, DY):
                if x + dx < 0 or x + dx >= n or y + dy < 0 or y + dy >= m:
                    continue
                if (x + dx, y + dy) in seen:
                    continue
                seen.add((x + dx, y + dy))
                heappush(heap, (risk + grid[x + dx][y + dy], x + dx, y + dy))
        raise ValueError("No path found")


class TestSolution(Solution, BaseTest):
    _SAMPLES = (
        (
            (
                "1163751742\n1381373672\n2136511328\n3694931569\n7463417111\n131912813"
                "7\n1359912421\n3125421639\n1293138521\n2311944581"
            ),
            40,
        ),
    )


if __name__ == "__main__":
    raise SystemExit(Solution().main())
