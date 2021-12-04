from collections import defaultdict
from typing import List, Iterator, Generator, Tuple, Dict


class BingoBoard:
    def __init__(self, board: str) -> None:
        self.board = self.make_board(board)
        self.board_sum = sum(sum(row) for row in self.board)

        self.width = len(self.board[0])
        self.height = len(self.board)

        self.remaining_in_row = [self.width] * self.height
        self.remaining_in_col = [self.height] * self.width

        self.finished = False

    def make_board(self, board: str) -> List[List[int]]:
        return [[int(x) for x in row.split()] for row in board.split("\n")]


class BingoGame:
    def __init__(self, bingo_nums: Iterator[int], raw_boards: List[str]) -> None:
        self.bingo_nums = bingo_nums
        self.boards = [BingoBoard(board) for board in raw_boards]

        self.mapping: Dict[int, List[Tuple[int, int, int]]] = defaultdict(list)

        for board_id, board in enumerate(self.boards):
            for row_id in range(board.height):
                for col_id in range(board.width):
                    self.mapping[board.board[row_id][col_id]].append(
                        (board_id, row_id, col_id)
                    )

    def start(self) -> Generator[int, None, None]:
        for num in self.bingo_nums:
            if num not in self.mapping:
                continue

            for board_id, row_id, col_id in self.mapping.pop(num):
                if self.boards[board_id].finished:
                    continue

                self.boards[board_id].remaining_in_row[row_id] -= 1
                self.boards[board_id].remaining_in_col[col_id] -= 1
                self.boards[board_id].board_sum -= num

                if (
                    self.boards[board_id].remaining_in_row[row_id] == 0
                    or self.boards[board_id].remaining_in_col[col_id] == 0
                ):
                    self.boards[board_id].finished = True
                    yield num * self.boards[board_id].board_sum

            if all(board.finished for board in self.boards):
                return
