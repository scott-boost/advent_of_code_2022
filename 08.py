from pathlib import Path
from typing import Optional, cast


class DirectoryElement:
    name: str
    size: int


class File(DirectoryElement):
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size


class Directory(DirectoryElement):
    def __init__(self, name: str, contents: dict[str, DirectoryElement], parent_dir: Optional["Directory"]):
        self.name = name
        self.contents = contents
        self.parent_dir = parent_dir

    @property
    def size(self):
        return sum([item.size for item in self.contents.values()])


def get_dir_sizes(root_dir: Directory) -> list[int]:
    result = [root_dir.size]
    for content in root_dir.contents.values():
        if isinstance(content, Directory):
            result.extend(get_dir_sizes(content))
    return result


def is_visible_left(x: int, y: int, grid: list[list[int]]) -> bool:
    height = grid[y][x]
    for x_index in range(x):
        if grid[y][x_index] >= height:
            return False
    return True


def is_visible_right(x: int, y: int, grid: list[list[int]]) -> bool:
    height = grid[y][x]
    for x_index in range(x+1, len(grid[y])):
        if grid[y][x_index] >= height:
            return False
    return True


def is_visible_up(x: int, y: int, grid: list[list[int]]) -> bool:
    height = grid[y][x]
    for y_index in range(y):
        if grid[y_index][x] >= height:
            return False
    return True


def is_visible_down(x: int, y: int, grid: list[list[int]]) -> bool:
    height = grid[y][x]
    for y_index in range(y+1, len(grid)):
        if grid[y_index][x] >= height:
            return False
    return True


def part_a(contents: str):
    lines = contents.split("\n")
    lines = [list(line) for line in lines]
    for line_index in range(len(lines)):
        for character_index in range(len(lines[line_index])):
            lines[line_index][character_index] = int(lines[line_index][character_index])

    result = len(lines) * 2
    result += len(lines[0]) * 2
    result -= 4

    for line_index, line in enumerate(lines[1:-1]):
        for character_index, character in enumerate(line[1:-1]):
            if is_visible_left(character_index+1, line_index+1, lines) or\
                    is_visible_right(character_index+1, line_index+1, lines) or \
                    is_visible_up(character_index+1, line_index+1, lines) or\
                    is_visible_down(character_index+1, line_index+1, lines):
                result += 1
    return result


def calculate_scenic_score(x: int, y: int, grid: list[list[int]]) -> int:
    height = grid[y][x]
    num_visible_left = 0
    num_visible_right = 0
    num_visible_up = 0
    num_visible_down = 0

    for x_index in range(x-1, -1, -1):
        num_visible_left += 1
        if grid[y][x_index] >= height:
            break

    for x_index in range(x+1, len(grid[0])):
        num_visible_right += 1
        if grid[y][x_index] >= height:
            break

    for y_index in range(y - 1, -1, -1):
        num_visible_up += 1
        if grid[y_index][x] >= height:
            break

    for y_index in range(y + 1, len(grid)):
        num_visible_down += 1
        if grid[y_index][x] >= height:
            break

    return num_visible_left * num_visible_right * num_visible_down * num_visible_up


def part_b(contents: str):
    lines = contents.split("\n")
    lines = [list(line) for line in lines]
    for line_index in range(len(lines)):
        for character_index in range(len(lines[line_index])):
            lines[line_index][character_index] = int(lines[line_index][character_index])

    result = 0
    for line_index, line in enumerate(lines[1:-1]):
        for character_index, character in enumerate(line[1:-1]):
            result = max(result, calculate_scenic_score(character_index+1, line_index+1, lines))

    return result


def main():
    contents = Path("08_input.txt").read_text().strip()
    print(part_a(contents))
    print(part_b(contents))


if __name__ == "__main__":
    main()
