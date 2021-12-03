import operator

from aoc_base import BaseSolution, BaseTest
from day3.util import TreeNode, Tree, Operator


class Solution(BaseSolution):
    _path = __package__

    def find_rating(self, root: TreeNode, num_bits: int, op: Operator) -> int:
        rating, bit_pos = 0, num_bits - 1

        curr = root
        while bit_pos >= 0:
            if curr.left and curr.right and op(curr.right.val, curr.left.val):
                rating |= 1 << bit_pos
                curr = curr.right
            elif curr.left and curr.right:
                curr = curr.left
            elif curr.left:
                curr = curr.left
            elif curr.right:
                rating |= 1 << bit_pos
                curr = curr.right
            else:
                raise Exception("Unbounded")
            bit_pos -= 1
        return rating

    def solve(self, s: str) -> int:
        tree = Tree()
        binary_inputs = s.splitlines()
        num_bits = len(binary_inputs[0])

        for binary_input in binary_inputs:
            tree.add(binary_input)

        oxygen_rating = self.find_rating(tree.root, num_bits, operator.ge)
        co2_rating = self.find_rating(tree.root, num_bits, operator.lt)

        return oxygen_rating * co2_rating


class TestSolution(Solution, BaseTest):
    _SAMPLES = (
        (
            (
                "00100\n11110\n10110\n10111\n10101\n01111\n00111\n11100\n"
                "10000\n11001\n00010\n01010\n"
            ),
            230,
        ),
    )


if __name__ == "__main__":
    raise SystemExit(Solution().main())
