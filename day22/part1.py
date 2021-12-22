import re
from typing import List, Tuple

from aoc_base import BaseSolution, BaseTest
from day22.utils import CUBOID, run_instructions

INSTRUCTION_RE = (
    r"(on|off) x=(-?\d+)\.\.(-?\d+),y=(-?\d+)\.\.(-?\d+),z=(-?\d+)\.\.(-?\d+)"
)


class Solution(BaseSolution):
    _path = __package__

    def solve(self, s: str) -> int:
        instructions: List[Tuple[str, CUBOID]] = []
        for line in s.splitlines():
            match = re.match(INSTRUCTION_RE, line)
            if not match:
                raise ValueError(f"Invalid instruction: {line}")
            instruction, *raw_cuboid = match.groups()
            x_start, x_end, y_start, y_end, z_start, z_end = [
                int(x) for x in raw_cuboid
            ]
            cuboid = CUBOID((x_start, x_end, y_start, y_end, z_start, z_end))
            if not all(cuboid[i] <= 50 for i in (0, 2, 4)) or not all(
                cuboid[i] >= -50 for i in (1, 3, 5)
            ):
                continue
            instructions.append((instruction, cuboid))

        return run_instructions(instructions)


class TestSolution(Solution, BaseTest):
    _SAMPLES = (
        (
            (
                "on x=10..12,y=10..12,z=10..12\non x=11..13,y=11..13,z=11..13\noff "
                "x=9..11,y=9..11,z=9..11\non x=10..10,y=10..10,z=10..10"
            ),
            39,
        ),
        (
            (
                "on x=-20..26,y=-36..17,z=-47..7\non x=-20..33,y=-21..23,z=-26..28"
                "\non x=-22..28,y=-29..23,z=-38..16\non x=-46..7,y=-6..46,z=-50..-1"
                "\non x=-49..1,y=-3..46,z=-24..28\non x=2..47,y=-22..22,z=-23..27\no"
                "n x=-27..23,y=-28..26,z=-21..29\non x=-39..5,y=-6..47,z=-3..44\non"
                " x=-30..21,y=-8..43,z=-13..34\non x=-22..26,y=-27..20,z=-29..19\no"
                "ff x=-48..-32,y=26..41,z=-47..-37\non x=-12..35,y=6..50,z=-50..-2"
                "\noff x=-48..-32,y=-32..-16,z=-15..-5\non x=-18..26,y=-33..15,z=-7"
                "..46\noff x=-40..-22,y=-38..-28,z=23..41\non x=-16..35,y=-41..10,z"
                "=-47..6\noff x=-32..-23,y=11..30,z=-14..3\non x=-49..-5,y=-3..45,z"
                "=-29..18\noff x=18..30,y=-20..-8,z=-3..13\non x=-41..9,y=-7..43,z="
                "-33..15\non x=-54112..-39298,y=-85059..-49293,z=-27449..7877\non x"
                "=967..23432,y=45373..81175,z=27513..53682"
            ),
            590784,
        ),
    )


if __name__ == "__main__":
    raise SystemExit(Solution().main())
