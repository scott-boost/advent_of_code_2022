import dataclasses
import math
from pathlib import Path
from typing import Optional


def part_a(contents: str):
    cycle_counter = 0
    register_x = 1
    result = 0
    for instruction in contents.split("\n"):
        cycle_counter += 1
        if (cycle_counter - 20) % 40 == 0:
            mult = cycle_counter * register_x
            print(cycle_counter, mult)
            result += mult
        if instruction == "noop":
            continue
        cycle_counter += 1
        if (cycle_counter - 20) % 40 == 0:
            mult = cycle_counter * register_x
            print(cycle_counter, mult)
            result += mult
        register_x += int(instruction.split(" ")[1])
    return result


def part_b(contents: str) -> str:
    cycle_counter = 0
    register_x = 1
    result: list[list[str]] = []

    for instruction in contents.split("\n"):
        cycle_counter += 1
        if (cycle_counter - 1) % 40 == 0:
            result.append([])
        pixel = "#" if register_x - 1 <= (cycle_counter - 1) % 40 <= register_x + 1 else " "
        result[(cycle_counter-1)//40].append(pixel)
        if instruction == "noop":
            continue
        cycle_counter += 1
        if (cycle_counter - 1) % 40 == 0:
            result.append([])
        pixel = "#" if register_x - 1 <= (cycle_counter - 1) % 40 <= register_x + 1 else " "
        result[(cycle_counter - 1) // 40].append(pixel)
        register_x += int(instruction.split(" ")[1])
    return "\n".join(["".join(los) for los in result])


def main():
    contents = Path("10_input.txt").read_text().strip()
    print(part_a(contents))
    print(part_b(contents))


if __name__ == "__main__":
    main()
