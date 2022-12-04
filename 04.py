from pathlib import Path


def part_a(content: str):
    counter = 0
    for assignment_pair in content.split("\n"):
        a, b = assignment_pair.split(",")
        a = a.split("-")
        a = [int(c) for c in a]
        b = b.split("-")
        b = [int(c) for c in b]
        if a[0] <= b[0] and b[1] <= a[1]:
            counter += 1
        elif b[0] <= a[0] and a[1] <= b[1]:
            counter += 1
    return counter


def part_b(content: str):
    counter = 0
    for assignment_pair in content.split("\n"):
        a, b = assignment_pair.split(",")
        a = a.split("-")
        a = [int(c) for c in a]
        b = b.split("-")
        b = [int(c) for c in b]
        if b[0] <= a[0] <= b[1]:
            counter += 1
        elif b[0] <= a[1] <= b[1]:
            counter += 1
        elif a[0] <= b[0] <= a[1]:
            counter += 1
        elif a[0] <= b[1] <= a[1]:
            counter += 1
    return counter


def main():
    content = Path("04_input.txt").read_text().strip()
    print(part_a(content))
    print(part_b(content))


if __name__ == "__main__":
    main()
