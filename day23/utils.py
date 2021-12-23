import enum
import heapq
from typing import FrozenSet, Generator, NamedTuple, Optional, Set, Tuple


class Amphipod(enum.Enum):
    A = 10 ** 0
    B = 10 ** 1
    C = 10 ** 2
    D = 10 ** 3

    def __mul__(self, other: object) -> int:
        if isinstance(other, int):
            return self.value * other
        if isinstance(other, Amphipod):
            return self.value * other.value
        raise TypeError(
            f"Cannot multiply {self.__class__.__name__} by {other.__class__.__name__}"
        )


ROOM_DOORS = {Amphipod.A: 2, Amphipod.B: 4, Amphipod.C: 6, Amphipod.D: 8}
ROOMS = {Amphipod.A: 0, Amphipod.B: 1, Amphipod.C: 2, Amphipod.D: 3}


class Room(NamedTuple):
    type_: Amphipod
    size: int
    amphipods: Tuple[Amphipod, ...]

    def is_final(self) -> bool:
        return len(self.amphipods) == self.size and all(
            amphipod == self.type_ for amphipod in self.amphipods
        )

    def is_enterable(self) -> bool:
        return len(self.amphipods) < self.size and all(
            amphipod == self.type_ for amphipod in self.amphipods
        )

    def __len__(self) -> int:
        return len(self.amphipods)

    def pop(self) -> Tuple[Amphipod, "Room"]:
        if not self.amphipods:
            raise ValueError("Room is empty")

        return self.amphipods[-1], Room(self.type_, self.size, self.amphipods[:-1])

    def append(self, amphipod: Amphipod) -> "Room":
        return Room(self.type_, self.size, self.amphipods + (amphipod,))

    def gap(self) -> int:
        return self.size - len(self.amphipods)


class Hallway(NamedTuple):
    spaces: Tuple[Optional[Amphipod], ...] = (None,) * 11
    DOORS: FrozenSet[int] = frozenset(ROOM_DOORS.values())

    def get_valid_moves(self, start: int) -> Generator[Tuple[int, int], None, None]:
        left_range = range(start - 1, -1, -1)
        right_range = range(start + 1, 11, 1)

        for search_range in [left_range, right_range]:
            for space in search_range:
                if space in self.DOORS:
                    continue

                if self.spaces[space] is not None:
                    break

                distance = abs(start - space)
                yield (space, distance)

    def is_clear(self, start: int, stop: int) -> bool:
        if start < stop:
            search_range = range(start + 1, stop + 1)
        else:
            search_range = range(stop, start)

        return all(self.spaces[space] is None for space in search_range)

    def update_space(self, space: int, amphipod: Optional[Amphipod]) -> "Hallway":
        return Hallway(self.spaces[:space] + (amphipod,) + self.spaces[space + 1 :])


class State(NamedTuple):
    energy: int
    rooms: Tuple[Room, ...]
    hallway: Hallway

    def __hash__(self) -> int:
        return hash((self.rooms, self.hallway))

    def __eq__(self, other: object) -> bool:
        return isinstance(other, State) and hash(self) == hash(other)

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, State):
            return NotImplemented
        return self.energy < other.energy

    def is_final(self) -> bool:
        return all(room.is_final() for room in self.rooms)

    def update_room(self, i: int, new_room: Room) -> Tuple[Room, ...]:
        return self.rooms[:i] + (new_room,) + self.rooms[i + 1 :]


def get_best_path(initial_state: State) -> int:
    heap = [initial_state]
    visited: Set[State] = set()
    while heap:
        state = heapq.heappop(heap)

        if state in visited:
            continue
        visited.add(state)

        for i, room in enumerate(state.rooms):
            if room and not room.is_final():
                curr_amphipod, new_room = room.pop()
                door = ROOM_DOORS[room.type_]

                for space, distance in state.hallway.get_valid_moves(door):
                    new_state = State(
                        state.energy + curr_amphipod * (room.gap() + 1 + distance),
                        state.update_room(i, new_room),
                        state.hallway.update_space(space, curr_amphipod),
                    )
                    if new_state.is_final():
                        return new_state.energy
                    if new_state not in visited:
                        heapq.heappush(heap, new_state)

        for space, amphipod in enumerate(state.hallway.spaces):
            if amphipod is None:
                continue

            door = ROOM_DOORS[amphipod]
            room_idx = ROOMS[amphipod]
            room = state.rooms[room_idx]

            if state.hallway.is_clear(space, door) and room.is_enterable():
                new_room = room.append(amphipod)
                distance = abs(door - space)

                new_state = State(
                    state.energy + amphipod * (distance + room.gap()),
                    state.update_room(room_idx, new_room),
                    state.hallway.update_space(space, None),
                )
                if new_state.is_final():
                    return new_state.energy
                if new_state not in visited:
                    heapq.heappush(heap, new_state)

    raise ValueError("No solution found")
