from aoc_base import BaseSolution, BaseTest

SEGMENTS = {
    0: "abcefg",
    1: "cf",
    2: "acdeg",
    3: "acdfg",
    4: "bcdf",
    5: "abdfg",
    6: "abdefg",
    7: "acf",
    8: "abcdefg",
    9: "abcdfg",
}
OVERLAPS = {
    num1: {
        num2: len(set(segment1).intersection(segment2))
        for num2, segment2 in SEGMENTS.items()
        if num1 != num2
    }
    for num1, segment1 in SEGMENTS.items()
}


class Solution(BaseSolution):
    _path = __package__

    def solve(self, s: str) -> int:
        res = 0
        for line in s.splitlines():
            signals, encoded_digits = map(
                lambda vals: [frozenset(val) for val in vals.split(" ")],
                line.split(" | "),
            )
            segment_map = {
                1: set(signal for signal in signals if len(signal) == 2).pop(),
                4: set(signal for signal in signals if len(signal) == 4).pop(),
                7: set(signal for signal in signals if len(signal) == 3).pop(),
                8: set(signal for signal in signals if len(signal) == 7).pop(),
            }
            reverse_segment_map = {signal: num for num, signal in segment_map.items()}
            missing = {0, 2, 3, 5, 6, 9}
            for signal in signals:
                if signal in reverse_segment_map:
                    continue
                for num in missing:
                    for num_, segment in segment_map.items():
                        overlap = len(set(signal).intersection(segment))
                        if OVERLAPS[num_][num] != overlap:
                            break
                    else:
                        reverse_segment_map[signal] = num
                        segment_map[num] = signal
                        missing.remove(num)
                        break
                if not missing:
                    break
            res += int(
                "".join(
                    map(str, (reverse_segment_map[digit] for digit in encoded_digits))
                )
            )
        return res


class TestSolution(Solution, BaseTest):
    _SAMPLES = (
        (
            (
                "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | "
                "fdgacbe cefdb cefbgd gcbe\n"
                "edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | "
                "fcgedb cgb dgebacf gc\n"
                "fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | "
                "cg cg fdcagb cbg\n"
                "fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | "
                "efabcd cedba gadfec cb\n"
                "aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | "
                "gecf egdcabf bgf bfgea\n"
                "fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | "
                "gebdcfa ecba ca fadegcb\n"
                "dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | "
                "cefg dcbef fcge gbcadfe\n"
                "bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | "
                "ed bcgafe cdgba cbgef\n"
                "egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | "
                "gbdfcae bgc cg cgb\n"
                "gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | "
                "fgae cfgab fg bagce\n"
            ),
            61229,
        ),
    )


if __name__ == "__main__":
    raise SystemExit(Solution().main())
