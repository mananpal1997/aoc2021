from typing import List, NewType, Optional, Tuple

CUBOID = NewType("CUBOID", Tuple[int, int, int, int, int, int])


def get_overlap(cuboid1: CUBOID, cuboid2: CUBOID) -> Optional[CUBOID]:
    max_x, max_y, max_z = (max(cuboid1[i], cuboid2[i]) for i in (0, 2, 4))
    min_x, min_y, min_z = (min(cuboid1[i], cuboid2[i]) for i in (1, 3, 5))
    if min_x - max_x >= 0 and min_y - max_y >= 0 and min_z - max_z >= 0:
        return CUBOID((max_x, min_x, max_y, min_y, max_z, min_z))
    return None


def run_instructions(instructions: List[Tuple[str, CUBOID]]) -> int:
    on_count = 0
    cuboids: List[CUBOID] = []

    for instruction in reversed(instructions):
        toggle, cuboid = instruction
        if toggle == "on":
            off_cubes = []
            overlapping_cuboids = [get_overlap(cuboid, other) for other in cuboids]
            for overlapping_cuboid in overlapping_cuboids:
                if overlapping_cuboid:
                    off_cubes.append(("on", overlapping_cuboid))
            x_start, x_end, y_start, y_end, z_start, z_end = cuboid
            on_count += (
                (x_end - x_start + 1) * (y_end - y_start + 1) * (z_end - z_start + 1)
            )
            on_count -= run_instructions(off_cubes)
        cuboids.append(cuboid)

    return on_count
