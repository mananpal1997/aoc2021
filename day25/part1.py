from aoc_base import BaseSolution, BaseTest


class Solution(BaseSolution):
    _path = __package__

    def solve(self, s: str) -> int:
        east_facing = set()
        south_facing = set()
        R, C = len(s.splitlines()), len(s.splitlines()[0])
        for r, row in enumerate(s.splitlines()):
            for c, col in enumerate(row):
                if col == ">":
                    east_facing.add((r, c))
                elif col == "v":
                    south_facing.add((r, c))
                else:
                    continue

        steps = 0
        while True:
            new_east_facing = set()
            new_south_facing = set()
            changed = False
            for (r, c) in east_facing:
                new_c = (c + 1) % C
                if (r, new_c) in south_facing or (r, new_c) in east_facing:
                    new_east_facing.add((r, c))
                else:
                    new_east_facing.add((r, new_c))
                    changed = True
            east_facing = new_east_facing
            for (r, c) in south_facing:
                new_r = (r + 1) % R
                if (new_r, c) in south_facing or (new_r, c) in east_facing:
                    new_south_facing.add((r, c))
                else:
                    new_south_facing.add((new_r, c))
                    changed = True
            south_facing = new_south_facing
            if changed:
                steps += 1
            else:
                break
        return steps + 1


class TestSolution(Solution, BaseTest):
    _SAMPLES = (
        (
            (
                "v...>>.vv>\n.vv>>.vv..\n>>.>v>...v\n>>v>>.>.v.\nv>v.vv.v..\n>.>>..v.."
                ".\n.vv..>.>v.\nv.v..>>v.v\n....v..v.>"
            ),
            58,
        ),
    )


if __name__ == "__main__":
    raise SystemExit(Solution().main())
