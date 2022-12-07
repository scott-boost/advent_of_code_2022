from pathlib import Path
from typing import Union, Optional


class File:
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size


class Directory:
    def __init__(self, name: str, contents: dict[str, Union[File, "Directory"]], parent_dir: Optional["Directory"]):
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


def part_a(contents: str):
    root_dir = parse_directory_tree(contents)

    return sum([
        size
        for size in get_dir_sizes(root_dir)
        if size <= 100000
    ])


def part_b(contents: str):
    root_dir = parse_directory_tree(contents)

    update_size = 30_000_000
    total_size = 70_000_000

    used_space = root_dir.size
    free_space = total_size - used_space

    space_to_delete = update_size - free_space

    return min(size for size in get_dir_sizes(root_dir) if size >= space_to_delete)


def parse_directory_tree(contents):
    root_dir = Directory("/", {}, None)
    current_directory: Directory = root_dir
    for line in contents.split("\n"):
        if line.startswith("$ "):
            # $ cd /
            if line.startswith("$ cd "):
                _, cmd, arg = line.split(" ")
                if cmd == "cd":
                    if arg == "/":
                        current_directory = root_dir
                    elif arg == "..":
                        current_directory = current_directory.parent_dir
                    else:
                        current_directory = current_directory.contents[arg]
        else:
            if line.startswith("dir "):
                # dir potato
                _, name = line.split(" ")
                current_directory.contents[name] = Directory(name, {}, current_directory)
            else:
                # 123 potato
                size, name = line.split(" ")
                current_directory.contents[name] = File(name, int(size))
    return root_dir


def main():
    contents = Path("07_input.txt").read_text().strip()
    print(part_a(contents))
    print(part_b(contents))


if __name__ == "__main__":
    main()
