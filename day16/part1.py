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

    def parse(self, s: str) -> str:
        version = int(s[:3], 2)
        s = s[3:]
        self.version_total += version

        type_id = int(s[:3], 2)
        s = s[3:]
        if type_id == 4:
            prefix = None
            while prefix != "0":
                prefix = s[0]
                s = s[5:]
        else:
            length_type_id = int(s[0], 2)
            s = s[1:]
            if length_type_id == 1:
                num_packets = int(s[:11], 2)
                s = s[11:]
                for _ in range(num_packets):
                    s = self.parse(s)
            else:
                length_subpackets = int(s[:15], 2)
                s = s[15:]
                subpackets = s[:length_subpackets]
                while subpackets:
                    subpackets = self.parse(subpackets)
                s = s[length_subpackets:]
        return s

    def solve(self, s: str) -> int:
        self.version_total = 0
        self.parse("".join(hex_map[c] for c in s))
        return self.version_total


class TestSolution(Solution, BaseTest):
    _SAMPLES = (
        ("8A004A801A8002F478", 16),
        ("620080001611562C8802118E34", 12),
        ("C0015000016115A2E0802F182340", 23),
        ("A0016C880162017C3686B18A3D4780", 31),
    )


if __name__ == "__main__":
    raise SystemExit(Solution().main())
