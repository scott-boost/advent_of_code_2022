from pathlib import Path


def part_a(contents: str):
    starting_stack, instructions = contents.split("\n\n")
    ss_lines: list[str] = starting_stack.split("\n")
    stacks: list[list[str]] = []
    for stack_index in range(9):
        # 1   2   3   4   5   6   7   8   9
        character_index = stack_index*4+1
        stack = [row[character_index:character_index+1] for row in ss_lines[:-1]]
        stack = [character for character in stack if character != " "]
        stack.reverse()
        stacks.append(stack)

    instruction: str
    for instruction in instructions.split("\n"):
        # move 3 from 9 to 7
        _, num_containers, _, from_stack_index, _, to_stack_index = instruction.split(" ")
        num_containers = int(num_containers)
        from_stack_index = int(from_stack_index)
        to_stack_index = int(to_stack_index)

        for _ in range(num_containers):
            container = stacks[from_stack_index-1].pop()
            stacks[to_stack_index-1].append(container)

    result: str = "".join([stack[-1] for stack in stacks])
    return result


def part_b(contents: str):
    starting_stack, instructions = contents.split("\n\n")
    ss_lines: list[str] = starting_stack.split("\n")
    stacks: list[list[str]] = []
    for stack_index in range(9):
        # 1   2   3   4   5   6   7   8   9
        character_index = stack_index * 4 + 1
        stack = [row[character_index:character_index + 1] for row in ss_lines[:-1]]
        stack = [character for character in stack if character != " "]
        stack.reverse()
        stacks.append(stack)

    instruction: str
    for instruction in instructions.split("\n"):
        # move 3 from 9 to 7
        _, num_containers, _, from_stack_index, _, to_stack_index = instruction.split(" ")
        num_containers = int(num_containers)
        from_stack_index = int(from_stack_index)
        to_stack_index = int(to_stack_index)

        containers_to_add = []
        for _ in range(num_containers):
            container = stacks[from_stack_index - 1].pop()
            containers_to_add.append(container)

        containers_to_add.reverse()

        for container in containers_to_add:
            stacks[to_stack_index - 1].append(container)

    result: str = "".join([stack[-1] for stack in stacks])
    return result


def main():
    contents = Path("05_input.txt").read_text().strip()
    print(part_a(contents))
    print(part_b(contents))


if __name__ == "__main__":
    main()
