import math
from typing import List, Tuple

from aoc_base import BaseSolution, BaseTest

hex_map = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}


class Solution(BaseSolution):
    _path = __package__

    def parse(self, s: str) -> Tuple[str, int]:
        s = s[3:]
        type_id = int(s[:3], 2)
        s = s[3:]
        if type_id == 4:
            prefix = None
            subpacket = ""
            while prefix != "0":
                subpacket += s[1:5]
                prefix = s[0]
                s = s[5:]
            return s, int(subpacket, 2)
        else:
            subpacket_literals: List[int] = []
            length_type_id = int(s[0], 2)
            s = s[1:]
            if length_type_id == 1:
                num_packets = int(s[:11], 2)
                s = s[11:]
                for _ in range(num_packets):
                    s, subpacket_literal = self.parse(s)
                    subpacket_literals.append(subpacket_literal)
            else:
                length_subpackets = int(s[:15], 2)
                s = s[15:]
                subpackets = s[:length_subpackets]
                while subpackets:
                    subpackets, subpacket_literal = self.parse(subpackets)
                    subpacket_literals.append(subpacket_literal)
                s = s[length_subpackets:]
            if type_id == 0:
                # sum of all literals
                return s, sum(subpacket_literals)
            elif type_id == 1:
                # product of all literals
                return s, math.prod(subpacket_literals)
            elif type_id == 2:
                # minimum of all literals
                return s, min(subpacket_literals)
            elif type_id == 3:
                # maximum of all literals
                return s, max(subpacket_literals)
            elif type_id == 5:
                # first literal greater than the second
                return s, int(subpacket_literals[0] > subpacket_literals[1])
            elif type_id == 6:
                # first literal less than the second
                return s, int(subpacket_literals[0] < subpacket_literals[1])
            elif type_id == 7:
                # first literal equal to the second
                return s, int(subpacket_literals[0] == subpacket_literals[1])
            else:
                raise Exception(f"Unknown type_id: {type_id}")

    def solve(self, s: str) -> int:
        return self.parse("".join(hex_map[c] for c in s))[1]


class TestSolution(Solution, BaseTest):
    _SAMPLES = (
        ("C200B40A82", 3),
        ("04005AC33890", 54),
        ("880086C3E88112", 7),
        ("CE00C43D881120", 9),
        ("D8005AC2A8F0", 1),
        ("F600BC2D8F", 0),
        ("9C005AC2F8F0", 0),
        ("9C0141080250320F1802104A08", 1),
    )


if __name__ == "__main__":
    raise SystemExit(Solution().main())
