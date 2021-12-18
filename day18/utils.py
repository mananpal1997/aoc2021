from typing import Tuple, Union


def can_explode(s: str) -> Tuple[bool, int]:
    nested_level = 0
    for i, c in enumerate(s):
        if c == "[":
            nested_level += 1
            if nested_level == 5:
                return True, i
        elif c == "]":
            nested_level -= 1
    return False, -1


def explode(s: str, explosion_start: int) -> str:
    pair_start = explosion_start
    pair_end = s.find("]", pair_start)

    num1, num2 = map(int, s[pair_start + 1 : pair_end].split(","))
    s = s[:pair_start] + "." + s[pair_end + 1 :]

    left_idx = s.index(".")
    while left_idx >= 0:
        if s[left_idx].isdigit():
            left_end = left_idx + 1
            while s[left_idx].isdigit():
                left_idx -= 1
            left_start = left_idx + 1
            left_val = int(s[left_start:left_end])
            s = f"{s[:left_start]}{num1 + left_val}{s[left_end:]}"
            break
        left_idx -= 1

    right_idx = s.index(".")
    while right_idx < len(s):
        if s[right_idx].isdigit():
            right_start = right_idx
            while s[right_idx].isdigit():
                right_idx += 1
            right_end = right_idx
            right_val = int(s[right_start:right_end])
            s = f"{s[:right_start]}{num2 + right_val}{s[right_end:]}"
            break
        right_idx += 1

    return s.replace(".", "0")


def can_split(s: str) -> Tuple[bool, int]:
    for i, c in enumerate(s):
        if c.isdigit() and i + 1 < len(s) and s[i + 1].isdigit():
            return True, i
    return False, -1


def split(s: str, split_pos: int) -> str:
    start_idx = split_pos
    while s[split_pos].isdigit():
        split_pos += 1
    end_idx = split_pos

    num = int(s[start_idx:end_idx])
    if num % 2 == 0:
        left_num = right_num = num // 2
    else:
        left_num, right_num = num // 2, num // 2 + 1

    return f"{s[:start_idx]}[{left_num},{right_num}]{s[end_idx:]}"


def calculate_magnitude(s: Union[int, list]) -> int:
    if isinstance(s, list):
        return 3 * calculate_magnitude(s[0]) + 2 * calculate_magnitude(s[1])
    return s


def reduce(s: str) -> str:
    while True:
        ret, pos = can_explode(s)
        if ret:
            s = explode(s, pos)
        else:
            ret, pos = can_split(s)
            if ret:
                s = split(s, pos)
            else:
                return s
