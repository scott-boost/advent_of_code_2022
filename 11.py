import dataclasses
from pathlib import Path
from queue import Queue
from typing import Optional, Literal, Union, Callable


@dataclasses.dataclass
class Monkey:
    items: Queue[int]
    mapping_func: Callable[[int, int], int]
    arg: Union[int, Literal["__self__"]]
    test_number: int
    throw_to: dict[bool, Optional["Monkey"]]
    inspection_counter: int


def get_monkeys(contents: str) -> list[Monkey]:
    monkeys = []
    monkey_paragraphs = contents.split("\n\n")
    for mp in monkey_paragraphs:
        _, starting_items_line, operation_line, test_line, _, _ = mp.split("\n")
        starting_items_line = starting_items_line.split(": ")[1]
        items = Queue()
        [items.put(x) for x in list(map(int, starting_items_line.split(", ")))]

        operation_line = operation_line.split("= old ")[1]
        operator, arg = operation_line.split(" ")
        try:
            arg = int(arg)
            if operator == "*":
                mapping_func = multiply
            else:
                mapping_func = add
        except ValueError:
            if operator == "*":
                mapping_func = mult_self
            else:
                mapping_func = add_self

        test_number = int(test_line.split(" ")[-1])
        monkey = Monkey(
            items=items,
            mapping_func=mapping_func, arg=arg,
            test_number=test_number, throw_to={True: None, False: None},
            inspection_counter=0,
        )
        monkeys.append(monkey)

    for index, mp in enumerate(monkey_paragraphs):
        _, _, _, _, true_line, false_line = mp.split("\n")
        monkeys[index].throw_to[True] = monkeys[int(true_line.split(" ")[-1])]
        monkeys[index].throw_to[False] = monkeys[int(false_line.split(" ")[-1])]

    return monkeys


def part_a(contents: str) -> int:
    monkeys = get_monkeys(contents)

    for _ in range(20):
        for index in range(len(monkeys)):
            while not monkeys[index].items.empty():
                monkeys[index].inspection_counter += 1
                item = monkeys[index].items.get()
                item = monkeys[index].mapping_func(item, monkeys[index].arg)
                item = int(item / 3)
                test = (item % monkeys[index].test_number) == 0
                monkeys[index].throw_to[test].items.put(item)

    return get_monkey_business_level(monkeys)


def multiply(a, b):
    return a * b


def mult_self(a, _):
    return a * a


def add(a, b):
    return a + b


def add_self(a, _):
    return a + a


def part_b(contents: str) -> int:
    monkeys = get_monkeys(contents)

    test_number_product = 1
    for monkey in monkeys:
        test_number_product *= monkey.test_number

    for round_num in range(10_000):
        for index in range(len(monkeys)):
            monkey = monkeys[index]
            while not monkey.items.empty():
                monkeys[index].inspection_counter += 1
                item = monkeys[index].items.get()
                item = monkeys[index].mapping_func(item, monkeys[index].arg)
                item = item % test_number_product
                test = item % monkey.test_number == 0
                monkey.throw_to[test].items.put(item)

    result = get_monkey_business_level(monkeys)
    return result


def get_monkey_business_level(monkeys):
    inspection_counters = sorted([m.inspection_counter for m in monkeys])
    top_two_inspection_counters = sorted(inspection_counters)[-2:]
    result = top_two_inspection_counters[0] * top_two_inspection_counters[1]
    return result


def main():
    contents = Path("11_input.txt").read_text().strip()
    test_case_input = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""
    assert part_a(test_case_input) == 10605, part_a(test_case_input)
    print(part_a(contents))
    test_b = part_b(test_case_input)
    assert test_b == 2713310158, test_b
    print(part_b(contents))


if __name__ == "__main__":
    main()
