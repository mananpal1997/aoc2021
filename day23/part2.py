import re

from aoc_base import BaseSolution, BaseTest
from day23.utils import Hallway, Room, State, get_best_path, Amphipod


class Solution(BaseSolution):
    _path = __package__

    def solve(self, s: str) -> int:
        amphipods = [Amphipod[c] for c in re.findall(r"[A-D]", s)]
        state = State(
            0,
            (
                Room(
                    Amphipod.A, 4, (amphipods[4], Amphipod.D, Amphipod.D, amphipods[0])
                ),
                Room(
                    Amphipod.B, 4, (amphipods[5], Amphipod.B, Amphipod.C, amphipods[1])
                ),
                Room(
                    Amphipod.C, 4, (amphipods[6], Amphipod.A, Amphipod.B, amphipods[2])
                ),
                Room(
                    Amphipod.D, 4, (amphipods[7], Amphipod.C, Amphipod.A, amphipods[3])
                ),
            ),
            Hallway(),
        )
        return get_best_path(state)


class TestSolution(Solution, BaseTest):
    _SAMPLES = (
        (
            "#############\n#...........#\n###B#C#B#D###\n  #A#D#C#A#\n  #########",
            44169,
        ),
    )


if __name__ == "__main__":
    raise SystemExit(Solution().main())
