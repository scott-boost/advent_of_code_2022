import dataclasses
import math
from pathlib import Path
from typing import Optional


@dataclasses.dataclass
class Position:
    x: int
    y: int


@dataclasses.dataclass
class Knot(Position):
    infront: Optional["Knot"]
    behind: Optional["Knot"]
    unique_positions: Optional[set[tuple[int, int]]]

    def move(self, direction: str):
        assert self.infront is None
        if direction == "U":
            self.y += 1
        elif direction == "D":
            self.y -= 1
        elif direction == "L":
            self.x -= 1
        else:
            self.x += 1
        self.behind._update(direction)

    def _update(self, direction: str):
        assert self.infront is not None

        distance_apart = math.sqrt((self.infront.y - self.y) ** 2 + (self.infront.x - self.x) ** 2)

        if distance_apart == 0:
            pass
        elif distance_apart == 1:
            pass
        elif distance_apart == math.sqrt(2):
            pass
        elif distance_apart == 2:
            if self.infront.x == self.x and self.infront.y > self.y:
                self.y += 1
            elif self.infront.x == self.x and self.infront.y < self.y:
                self.y -= 1
            elif self.infront.x > self.x and self.infront.y == self.y:
                self.x += 1
            elif self.infront.x < self.x and self.infront.y == self.y:
                self.x -= 1
        else:
            if self.infront.x > self.x and self.infront.y > self.y:
                self.x += 1
                self.y += 1
            elif self.infront.x < self.x and self.infront.y > self.y:
                self.x -= 1
                self.y += 1
            elif self.infront.x > self.x and self.infront.y < self.y:
                self.x += 1
                self.y -= 1
            elif self.infront.x < self.x and self.infront.y < self.y:
                self.x -= 1
                self.y -= 1

        if self.behind is not None:
            self.behind._update(direction)
            return
        self.unique_positions.add((self.x, self.y))


def part_a(contents: str):
    # 6642
    head_knot = Knot(x=0, y=0, infront=None, behind=None, unique_positions=None)
    tail_knot = Knot(x=0, y=0, infront=head_knot, behind=None, unique_positions={(0, 0)})
    head_knot.behind = tail_knot

    for instruction in contents.split("\n"):
        direction, num_steps = instruction.split(" ")
        num_steps = int(num_steps)
        for _ in range(num_steps):
            head_knot.move(direction)
    return len(tail_knot.unique_positions)


def part_b(contents: str):
    head_knot = Knot(x=0, y=0, infront=None, behind=None, unique_positions=None)
    knot_before = head_knot
    knot: Optional[Knot] = None
    for _ in range(9):
        knot = Knot(x=0, y=0, infront=knot_before, behind=None, unique_positions=None)
        knot_before.behind = knot
        knot_before = knot
    tail_knot = knot
    assert isinstance(tail_knot, Knot)

    tail_knot.unique_positions = {(0, 0)}
    for instruction in contents.split("\n"):
        direction, num_steps = instruction.split(" ")
        num_steps = int(num_steps)
        for _ in range(num_steps):
            head_knot.move(direction)
    print(sorted(tail_knot.unique_positions))
    return len(tail_knot.unique_positions)


def main():
    contents = Path("09_input.txt").read_text().strip()
    print(part_a(contents))
    test_case_1 = part_b(
        """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""
    )
    assert test_case_1 == 1, test_case_1
    test_case_2 = part_b(
        """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""
    )
    assert test_case_2 == 36, test_case_2
    print(part_b(contents))


if __name__ == "__main__":
    main()
