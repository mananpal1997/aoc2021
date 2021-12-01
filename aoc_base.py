import argparse
import os
from typing import Tuple, Union


class BaseSolution:
    _path = __package__

    def solve(self, s: str) -> int:
        raise NotImplementedError

    def main(self) -> int:
        with open(os.path.join(self._path, "input.txt")) as f:
            print(self.solve(f.read().strip()))

        return 0


class BaseTest:
    _SAMPLES: Union[Tuple[()], Tuple[Tuple[str, int]]] = ()

    def solve(self, s: str) -> int:
        raise NotImplementedError

    def pytest_generate_tests(self, metafunc: argparse.Namespace) -> None:
        metafunc.parametrize("s, expected", self._SAMPLES)

    def test_solve(self, s: str, expected: int) -> None:
        output = self.solve(s)
        assert output == expected, f"Expected {expected}, got {output}"
