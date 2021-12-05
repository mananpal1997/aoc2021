import argparse
import os
import time
from typing import Generator, Tuple, Union

from contextlib import contextmanager


@contextmanager
def timer() -> Generator[None, None, None]:
    start = time.perf_counter()
    yield
    end = time.perf_counter()
    runtime = end - start
    unit = "s"
    if runtime < 10:
        runtime *= 1000
        unit = "ms"
    if runtime < 10:
        runtime *= 1000
        unit = "μs"
    print(f"Time: {runtime} {unit}")


class BaseSolution:
    _path = __package__

    def solve(self, s: str) -> int:
        raise NotImplementedError

    def main(self) -> int:
        with open(os.path.join(self._path, "input.txt")) as f, timer():
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
