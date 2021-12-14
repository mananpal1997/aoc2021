from collections import defaultdict, Counter
from typing import Dict
from aoc_base import BaseSolution, BaseTest


class Solution(BaseSolution):
    _path = __package__

    def solve(self, s: str) -> int:
        polymer = s.split("\n\n")[0]
        conversions = {
            c.split(" -> ")[0]: c.split(" -> ")[1]
            for c in s.split("\n\n")[1].splitlines()
        }
        pairs: Dict[str, int] = defaultdict(int)
        for i in range(len(polymer) - 1):
            pairs[polymer[i : i + 2]] += 1
        for _ in range(10):
            new_pairs: Dict[str, int] = defaultdict(int)
            for pair, freq in pairs.items():
                if pair in conversions:
                    addition = conversions[pair]
                    new_pairs[pair[0] + addition] += freq
                    new_pairs[addition + pair[1]] += freq
            pairs = new_pairs
        c = Counter({polymer[0]: 1, polymer[-1]: 1})
        for pair, freq in pairs.items():
            c[pair[0]] += freq
            c[pair[1]] += freq
        frequencies = c.most_common()
        return (frequencies[0][1] - frequencies[-1][1]) // 2


class TestSolution(Solution, BaseTest):
    _SAMPLES = (
        (
            (
                "NNCB\n\nCH -> B\nHH -> N\nCB -> H\nNH -> C\nHB -> C\nHC -> B\n"
                "HN -> C\nNN -> C\nBH -> H\nNC -> B\nNB -> B\nBN -> B\nBB -> N\n"
                "BC -> B\nCC -> N\nCN -> C"
            ),
            1588,
        ),
    )


if __name__ == "__main__":
    raise SystemExit(Solution().main())
