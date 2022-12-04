from pathlib import Path


def part_a(input_content: str):
    rucksacks = input_content.split("\n")
    total = 0
    for rucksack in rucksacks:
        compartment_a = rucksack[:int(len(rucksack)/2)]
        compartment_b = rucksack[int(len(rucksack)/2):]
        common_item = list(set(compartment_a).intersection(compartment_b))[0]
        priority = ord(common_item) - 38
        if 97 <= ord(common_item) <= 122:
            priority = ord(common_item) - 96
        total += priority
    return total


def part_b(input_content: str):
    rucksacks = input_content.split("\n")
    total = 0
    grouped_rucksacks = [rucksacks[i:i + 3] for i in range(0, len(rucksacks), 3)]
    for group_of_rucksacks in grouped_rucksacks:
        common_item = list(set(group_of_rucksacks[0]).intersection(group_of_rucksacks[1]).intersection(group_of_rucksacks[2]))[0]
        priority = ord(common_item) - 38
        if 97 <= ord(common_item) <= 122:
            priority = ord(common_item) - 96
        total += priority
    return total


def main():
    content = Path("03_input.txt").read_text().strip()
    print(part_a(content))
    print(part_b(content))


if __name__ == "__main__":
    main()
