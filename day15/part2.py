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
            if x == 5 * n - 1 and y == 5 * m - 1:
                return risk
            for dx, dy in zip(DX, DY):
                new_x, new_y = x + dx, y + dy
                if new_x < 0 or new_x >= 5 * n or new_y < 0 or new_y >= 5 * m:
                    continue
                if (new_x, new_y) in seen:
                    continue
                mutation_dist = (new_x) // n + (new_y) // m
                mutated_risk = (grid[(new_x) % n][(new_y) % m] + mutation_dist) % 9
                if mutated_risk == 0:
                    mutated_risk = 9
                seen.add((new_x, new_y))
                heappush(heap, (risk + mutated_risk, new_x, new_y))
        raise ValueError("No path found")


class TestSolution(Solution, BaseTest):
    _SAMPLES = (
        (
            (
                "1163751742\n1381373672\n2136511328\n3694931569\n7463417111\n131912813"
                "7\n1359912421\n3125421639\n1293138521\n2311944581"
            ),
            315,
        ),
    )


if __name__ == "__main__":
    raise SystemExit(Solution().main())
