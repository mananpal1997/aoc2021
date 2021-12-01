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
