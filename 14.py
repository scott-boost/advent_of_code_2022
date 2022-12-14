import dataclasses
from enum import Enum
from pathlib import Path


@dataclasses.dataclass
class Coord:
    x: int
    y: int


RockSegment = tuple[Coord, Coord]
RockSnake = list[RockSegment]


class GridItem(str, Enum):
    air = "."
    rock = "#"
    source = "+"
    sand = "o"


RIGHT_SHIFT = 500


def contents_to_rock_snakes(contents: str) -> list[RockSnake]:
    result = []
    for line in contents.split("\n"):
        coords: list[str] = line.split(" -> ")
        previous_coord = None
        rock_snake = []
        for coord in coords:
            x, y = coord.split(",")
            x = int(x) + RIGHT_SHIFT
            y = int(y)
            current_coord = Coord(x=x, y=y)
            if previous_coord is None:
                previous_coord = current_coord
                continue
            rock_snake.append((previous_coord, current_coord))
            previous_coord = current_coord
        result.append(rock_snake)

    return result


def part_a(contents: str) -> int:
    rock_snakes = contents_to_rock_snakes(contents)
    grid = get_starting_grid(rock_snakes)
    lowest_y_rock = get_lowest_rock_y(rock_snakes)
    counter = 0

    while True:
        sand = Coord(x=500+RIGHT_SHIFT, y=0)
        while True:
            if sand.y > lowest_y_rock:
                return counter
            if grid[sand.y+1][sand.x] == GridItem.air:
                sand.y += 1
            elif grid[sand.y+1][sand.x-1] == GridItem.air:
                sand.y += 1
                sand.x -= 1
            elif grid[sand.y+1][sand.x+1] == GridItem.air:
                sand.y += 1
                sand.x += 1
            else:
                break
        grid[sand.y][sand.x] = GridItem.sand
        counter += 1


def get_lowest_rock_y(rock_snakes):
    lowest_y_rock = -1
    for rock_snake in rock_snakes:
        for rock_segment in rock_snake:
            a, b = rock_segment
            lowest_y_rock = max(lowest_y_rock, a.y, b.y)
    return lowest_y_rock


def get_starting_grid(rock_snakes):
    max_coords = Coord(-1, -1)
    for rock_snake in rock_snakes:
        for coords in rock_snake:
            max_coords.x = max(max_coords.x, coords[0].x, coords[1].x)
            max_coords.y = max(max_coords.y, coords[0].y, coords[1].y)
    grid: list[list[GridItem]] = []
    for _ in range(max_coords.y+2):
        grid.append([GridItem.air for __ in range(max_coords.x+500)])

    for rock_snake in rock_snakes:
        for rock_segment in rock_snake:
            a, b = rock_segment
            if a.x == b.x:
                for y in range(min(a.y, b.y), max(a.y, b.y)+1):
                    grid[y][a.x] = GridItem.rock
                continue
            for x in range(min(a.x, b.x), max(a.x, b.x) + 1):
                grid[a.y][x] = GridItem.rock

    grid[0][500+RIGHT_SHIFT] = GridItem.source

    return grid


def part_b(contents: str) -> int:
    rock_snakes = contents_to_rock_snakes(contents)
    grid = get_starting_grid(rock_snakes)
    lowest_y_rock = get_lowest_rock_y(rock_snakes)
    counter = 0

    while grid[0][500+RIGHT_SHIFT] == GridItem.source:
        sand = Coord(x=500+RIGHT_SHIFT, y=0)
        while True:
            if sand.y == lowest_y_rock + 1:
                break
            row = grid[sand.y+1]
            if row[sand.x] == GridItem.air:
                sand.y += 1
            elif row[sand.x - 1] == GridItem.air:
                sand.y += 1
                sand.x -= 1
                assert sand.x > 0
            elif row[sand.x + 1] == GridItem.air:
                sand.y += 1
                sand.x += 1
            else:
                break
        grid[sand.y][sand.x] = GridItem.sand
        counter += 1
    return counter


def main():
    contents = Path("14_input.txt").read_text().strip()
    print(part_a(contents))
    print(part_b(contents))


if __name__ == "__main__":
    main()
