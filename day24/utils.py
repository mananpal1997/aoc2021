"""
simplified monad code, each block consists of 18 instructions (14 blocks total)
w, x, y, z = 0, 0, 0, 0
Generic Simplified Block:
    inp w
    x = (((z % 26) + num1) != w)
        z = z / 26 (for blocks 3, 5, 7, 10, 11, 12, 13)
        z = z / 1 for remaining blocks
    z = z * ((25 * x) + 1) + ((w + num2) * x)

num1 and num2 are on line 6 and 16 of each block

x(t) = ((z(t-1) % 26 + num1) != w(t))
z(t) = z(t-1) * (25 * x(t) + 1) + (w(t) + num2) * x(t)
"""

from functools import lru_cache
from typing import List, Tuple

MAX_Z_SUB_FACTOR = 26 ** 3
DIVISIBILITY_BLOCKS = (3, 5, 7, 10, 11, 12, 13)


def find_max_z(pairs: List[Tuple[int, int]]):
    max_z = 0
    for i, pair in enumerate(pairs):
        if i in DIVISIBILITY_BLOCKS:
            max_z //= 26
        max_z = max_z * 26 + (9 + pair[1])
    return max_z // MAX_Z_SUB_FACTOR


def find_model_num(s: str, *, minimize: bool) -> int:
    instructions = s.splitlines()
    pairs = [
        (int(instructions[i * 18 + 5][6:]), int(instructions[i * 18 + 15][6:]))
        for i in range(14)
    ]
    model_num = [-1] * 14
    max_z = find_max_z(pairs)

    @lru_cache(maxsize=None)
    def backtrack(index: int, prev_z: int) -> bool:
        if prev_z > max_z:
            return False
        if index == 14:
            return prev_z == 0
        digits = range(1, 10) if minimize else range(9, 0, -1)
        for i in digits:
            model_num[index] = i
            z_copy = prev_z
            x = int(((prev_z % 26) + pairs[index][0]) != model_num[index])
            if index in DIVISIBILITY_BLOCKS:
                prev_z //= 26
            z = prev_z * (25 * x + 1) + (model_num[index] + pairs[index][1]) * x
            if backtrack(index + 1, z):
                return True
            prev_z = z_copy
        return False

    backtrack(0, 0)
    assert all(i != -1 for i in model_num)
    return int("".join(map(str, model_num)))
