from typing import Callable, Optional

Operator = Callable[[int, int], bool]


class TreeNode:
    def __init__(self, val: int = 0) -> None:
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None
        self.val = val


class Tree:
    def __init__(self) -> None:
        self.root = TreeNode()

    def add(self, binary: str) -> None:
        curr = self.root
        for bit in binary:
            if bit == "0":
                if curr.left is None:
                    curr.left = TreeNode(1)
                else:
                    curr.left.val += 1
                curr = curr.left
            else:
                if curr.right is None:
                    curr.right = TreeNode(1)
                else:
                    curr.right.val += 1
                curr = curr.right
