import itertools

from aoc_base import BaseSolution, BaseTest
import day18.utils as utils


class Solution(BaseSolution):
    _path = __package__

    def solve(self, s: str) -> int:
        return max(
            max(
                utils.calculate_magnitude(
                    eval(utils.reduce(f"[{smallfish1},{smallfish2}]"))
                ),
                utils.calculate_magnitude(
                    eval(utils.reduce(f"[{smallfish2},{smallfish1}]"))
                ),
            )
            for (smallfish1, smallfish2) in itertools.combinations(s.splitlines(), 2)
        )


class TestSolution(Solution, BaseTest):
    _SAMPLES = (
        (
            (
                "[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]\n"
                "[[[5,[2,8]],4],[5,[[9,9],0]]]\n"
                "[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]\n"
                "[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]\n"
                "[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]\n"
                "[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]\n"
                "[[[[5,4],[7,7]],8],[[8,3],8]]\n"
                "[[9,3],[[9,9],[6,[4,9]]]]\n"
                "[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]\n"
                "[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]"
            ),
            3993,
        ),
    )


if __name__ == "__main__":
    raise SystemExit(Solution().main())
