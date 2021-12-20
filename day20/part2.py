from collections import defaultdict
from aoc_base import BaseSolution, BaseTest


class Solution(BaseSolution):
    _path = __package__

    def solve(self, s: str) -> int:
        s = s.replace(".", "0").replace("#", "1")
        raw_encoding, raw_image = s.split("\n\n")
        encoding = {idx: int(chr) for idx, chr in enumerate(raw_encoding)}

        image = defaultdict(int)
        for i, raw_row in enumerate(raw_image.splitlines()):
            for j, chr in enumerate(raw_row):
                image[(i, j)] = int(chr)

        min_r = min(r for r, _ in image)
        min_c = min(c for _, c in image)
        max_r = max(r for r, _ in image)
        max_c = max(c for _, c in image)

        kernel_width, kernel_height = 3 // 2, 3 // 2
        for step in range(50):
            enhanced = defaultdict(int)
            for r in range(min_r - 1, max_r + 2):
                for c in range(min_c - 1, max_c + 2):
                    code = 0
                    for dr in range(-kernel_height, kernel_height + 1):
                        for dc in range(-kernel_width, kernel_width + 1):
                            code <<= 1
                            if encoding[0] and not (
                                min_r <= r + dr <= max_r and min_c <= c + dc <= max_c
                            ):
                                code |= step % 2
                            else:
                                code |= image[(r + dr, c + dc)]
                    enhanced[(r, c)] = encoding[code]

            image = enhanced
            min_r, min_c, max_r, max_c = min_r - 1, min_c - 1, max_r + 1, max_c + 1

        return sum(image.values())


class TestSolution(Solution, BaseTest):
    _SAMPLES = (
        (
            (
                "..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#."
                ".#..##..###..######.###...####..#..#####..##..#.#####...##.#.#."
                ".#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####..."
                "..#.#....###..#.##......#.....#..#..#..##..#...##.######.####.#"
                "###.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#.."
                ".##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#"
                "..#..#.##.#....##..#.####....##...##..#...#......#.#.......#...."
                "...##..####..#...#.#.#...##..#.#..###..#####........#..####...."
                "..#..#\n\n#..#.\n#....\n##..#\n..#..\n..###"
            ),
            3351,
        ),
    )


if __name__ == "__main__":
    raise SystemExit(Solution().main())
