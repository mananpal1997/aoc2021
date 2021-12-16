# AOC 2021
https://adventofcode.com/2021

## Instructions
- `export PATH=$PATH:$PWD`
- `export AOC_COOKIE=<your session cookie>`
- `virtualenv venv --python=python3.8`
- `pip install -r requirements.txt`

```
$ aoc-helper setup --help                                                                                                                                                                                 ✹ ✭
Usage: aoc-helper setup [OPTIONS]

  Setups structue for day

Options:
  -d, --day INTEGER  [required]
  --help             Show this message and exit.

$ aoc-helper get-data --help                                                                                                                                                                              ✹ ✭
Usage: aoc-helper get-data [OPTIONS]

  Downloads input for day

Options:
  -d, --day INTEGER  [required]
  --help             Show this message and exit.

$ aoc-helper autorun --help                                                                                                                                                                               ✹ ✭
Usage: aoc-helper autorun [OPTIONS]

  Runs test, and if test passes, submits solution on prompt confirmation

Options:
  -d, --day INTEGER   [required]
  -p, --part INTEGER  [required]
  --submit
  --help              Show this message and exit.
```

### Runtimes

```
$ find -maxdepth 1 -type d -name 'day*' -printf '%P\n' | sort -V | xargs --replace bash -xc 'python -m {}.part1; python -m {}.part2'

+ python -m day1.part1
1292
Time: 619.3000008352101 μs
+ python -m day1.part2
1262
Time: 626.4440016821027 μs
+ python -m day2.part1
1882980
Time: 536.1639778129756 μs
+ python -m day2.part2
1971232560
Time: 562.4740151688457 μs
+ python -m day3.part1
3958484
Time: 13.67917499737814 ms
+ python -m day3.part2
1613181
Time: 3998.278989456594 μs
+ python -m day4.part1
71708
Time: 2651.207003509626 μs
+ python -m day4.part2
34726
Time: 3338.302980409935 μs
+ python -m day5.part1
7674
Time: 79.80240200413391 ms
+ python -m day5.part2
20898
Time: 131.36322901118547 ms
+ python -m day6.part1
372984
Time: 366.69697146862745 μs
+ python -m day6.part2
1681503251694
Time: 908.6619829759002 μs
+ python -m day7.part1
337833
Time: 360.1649950724095 μs
+ python -m day7.part2
96678050
Time: 659.2950085178018 μs
+ python -m day8.part1
288
Time: 350.56701744906604 μs
+ python -m day8.part2
940724
Time: 8852.74398024194 μs
+ python -m day9.part1
600
Time: 6511.579995276406 μs
+ python -m day9.part2
987840
Time: 15.595114004099742 ms
+ python -m day10.part1
323691
Time: 1190.3709964826703 μs
+ python -m day10.part2
2858785164
Time: 1497.737001045607 μs
+ python -m day11.part1
1747
Time: 11.335678020259365 ms
+ python -m day11.part2
505
Time: 54.84981698100455 ms
+ python -m day12.part1
4304
Time: 12.729883997963043 ms
+ python -m day12.part2
118242
Time: 673.0624650008394 ms
+ python -m day13.part1
790
Time: 1239.84499987273 μs
+ python -m day13.part2
###...##..#..#.####.###..####...##..##..
#..#.#..#.#..#....#.#..#.#.......#.#..#.
#..#.#....####...#..###..###.....#.#....
###..#.##.#..#..#...#..#.#.......#.#....
#....#..#.#..#.#....#..#.#....#..#.#..#.
#.....###.#..#.####.###..#.....##...##..
-1
Time: 1845.1300002197968 μs
+ python -m day14.part1
3247
Time: 489.48199992082664 μs
+ python -m day14.part2
4110568157153
Time: 1600.63600014837 μs
+ python -m day15.part1
553
Time: 26.489511990803294 ms
+ python -m day15.part2
2858
Time: 721.3363759947242 ms
+ python -m day16.part1
901
Time: 547.8700004459824 μs
+ python -m day16.part2
110434737925
Time: 661.8309998884797 μs
```
