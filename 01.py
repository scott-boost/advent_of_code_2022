from pathlib import Path


def parse(input_contents: str) -> list[list[int]]:
    inventories: list[str] = input_contents.strip().split("\n\n")
    inventories_split: list[list[str]] = [inventory.split("\n") for inventory in inventories]
    to_int = [list(map(int, inventory)) for inventory in inventories_split]
    return to_int


def part_a(input_contents: str):
    summed = [sum(inventory) for inventory in parse(input_contents)]
    return max(summed)


def part_b(input_contents: str):
    summed = [sum(inventory) for inventory in parse(input_contents)]
    return sum(sorted(summed, reverse=True)[:3])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    contents = Path("01_input.txt").read_text()
    print(part_a(contents))
    print(part_b(contents))
