from pathlib import Path


def part_a(contents: str):
    for index in range(len(contents)-4):
        to_be_checked = contents[index:index+4]
        if len(set(to_be_checked)) == 4:
            return index+4


def part_b(contents: str):
    for index in range(len(contents) - 14):
        to_be_checked = contents[index:index + 14]
        if len(set(to_be_checked)) == 14:
            return index + 14


def main():
    contents = Path("06_input.txt").read_text().strip()
    print(part_a(contents))
    print(part_b(contents))


if __name__ == "__main__":
    main()
