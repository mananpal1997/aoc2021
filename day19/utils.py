import itertools
from typing import Callable, Generator, List, NewType, Optional, Tuple

POINT = NewType("POINT", Tuple[int, int, int])

manhattan_distance: Callable[[POINT, POINT], int] = lambda p1, p2: sum(
    abs(c1 - c2) for c1, c2 in zip(p1, p2)
)


def get_rotations(x: int, y: int, z: int) -> List[POINT]:
    return [POINT((x, y, z)), POINT((-y, x, z)), POINT((-x, -y, z)), POINT((y, -x, z))]


def get_z_orientations(x: int, y: int, z: int) -> List[POINT]:
    return [
        POINT((x, y, z)),
        POINT((x, z, -y)),
        POINT((x, -y, -z)),
        POINT((x, -z, y)),
        POINT((-z, y, x)),
        POINT((z, y, -x)),
    ]


def get_orientations(point: POINT) -> Generator[POINT, None, None]:
    for xi, yi, zi in get_z_orientations(*point):
        yield from get_rotations(xi, yi, zi)


def pt_hash(beacon1: POINT, beacon2: POINT) -> str:
    min_delta = min(abs(c1 - c2) for c1, c2 in zip(beacon1, beacon2))
    max_delta = max(abs(c1 - c2) for c1, c2 in zip(beacon1, beacon2))
    return f"{manhattan_distance(beacon1, beacon2)},{min_delta},{max_delta}"


def add_point(point: POINT, offset: POINT) -> POINT:
    return POINT((point[0] + offset[0], point[1] + offset[1], point[2] + offset[2]))


def sub_point(point: POINT, offset: POINT) -> POINT:
    return POINT((point[0] - offset[0], point[1] - offset[1], point[2] - offset[2]))


class Scanner:
    def __init__(self, sid: int, beacons: List[POINT]):
        self.sid = sid
        self.beacons = tuple(beacons)
        self.hashes = {
            pt_hash(beacon1, beacon2)
            for beacon1, beacon2 in itertools.permutations(beacons, 2)
        }
        self.pos: Optional[POINT] = None

    @classmethod
    def from_str(cls, s: str, sid: int) -> "Scanner":
        beacons: List[POINT] = []
        for line in s.splitlines()[1:]:
            x, y, z = map(int, line.split(","))
            beacons.append(POINT((x, y, z)))
        return cls(sid, beacons)
