from queue import Queue
from typing import Tuple

from aoc_base import BaseSolution, BaseTest
from day3.util import TreeNode, Tree


class Solution(BaseSolution):
    _path = __package__

    def get_rates(self, root: TreeNode, num_bits: int) -> Tuple[int, int]:
        epsilon, gamma, bit_pos = 0, 0, num_bits - 1

        q: Queue[TreeNode] = Queue()
        q.put(root)

        def qpush(node: TreeNode):
            q.put(node)
            return node.val

        while not q.empty():
            nodes = [q.get() for _ in range(q.qsize())]
            set_bits = sum(qpush(node.right) for node in nodes if node.right)
            unset_bits = sum(qpush(node.left) for node in nodes if node.left)

            if set_bits > unset_bits:
                epsilon |= 1 << bit_pos
            elif set_bits < unset_bits:
                gamma |= 1 << bit_pos
            bit_pos -= 1

        return epsilon, gamma

    def solve(self, s: str) -> int:
        binary_strings = s.splitlines()

        tree = Tree()
        num_bits = len(binary_strings[0])
        for binary_string in binary_strings:
            tree.add(binary_string)

        epsilon_rate, gamma_rate = self.get_rates(tree.root, num_bits)

        return epsilon_rate * gamma_rate


class TestSolution(Solution, BaseTest):
    _SAMPLES = (
        (
            (
                "00100\n11110\n10110\n10111\n10101\n01111\n00111\n11100\n"
                "10000\n11001\n00010\n01010\n"
            ),
            198,
        ),
    )


if __name__ == "__main__":
    raise SystemExit(Solution().main())
