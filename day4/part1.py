from aoc_base import BaseSolution, BaseTest
from day4.util import BingoGame


class Solution(BaseSolution):
    _path = __package__

    def solve(self, s: str) -> int:
        data = s.split("\n\n")
        bingo_nums = map(int, data[0].split(","))
        raw_boards = data[1:]

        game = BingoGame(bingo_nums, raw_boards)

        return next(game.start())


class TestSolution(Solution, BaseTest):
    _SAMPLES = (
        (
            "7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1\n\n"
            "22 13 17 11  0\n 8  2 23  4 24\n21  9 14 16  7\n 6 10  3 18  5\n"
            " 1 12 20 15 19\n\n3 15  0  2 22\n 9 18 13 17  5\n19  8  7 25 23\n"
            "20 11 10 24  4\n14 21 16 12  6\n\n14 21 17 24  4\n10 16 15  9 19\n"
            "18  8 23 26 20\n22 11 13  6  5\n 2  0 12  3  7",
            4512,
        ),
    )


if __name__ == "__main__":
    raise SystemExit(Solution().main())
