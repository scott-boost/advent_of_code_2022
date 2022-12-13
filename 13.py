import json
from pathlib import Path
from typing import Union, Optional


class MyList(list):
    def __lt__(self, other):
        assert isinstance(other, self.__class__)
        return compare_list(self, other)


def compare_list(left: list[Union[int, list]], right: list[Union[int, list]]) -> Optional[bool]:
    index = 0

    while True:
        try:
            left_item = left[index]
        except IndexError:
            if len(left) == len(right):
                return None
            return True
        try:
            right_item = right[index]
        except IndexError:
            return False

        if isinstance(left_item, int) and isinstance(right_item, int):
            if left_item != right_item:
                return left_item < right_item

        elif isinstance(left_item, list) and isinstance(right_item, list):
            comparison = compare_list(left_item, right_item)
            if comparison is not None:
                return comparison

        elif isinstance(left_item, int):
            comparison = compare_list([left_item], right_item)
            if comparison is not None:
                return comparison

        else:
            comparison = compare_list(left_item, [right_item])
            if comparison is not None:
                return comparison

        index += 1


def part_a(contents: str) -> int:
    result = 0

    for index, pair in enumerate(contents.split("\n\n")):
        line_one, line_two = pair.split("\n")

        line_one = eval(line_one)
        line_two = eval(line_two)

        comparison = compare_list(line_one, line_two)
        assert comparison is not None

        if comparison:
            result += index + 1

    return result


def list_to_mylist(reg_list: list[Union[int, list]]) -> MyList[Union[int, MyList]]:
    result = MyList()
    for item in reg_list:
        if isinstance(item, int):
            result.append(item)
        else:
            result.append(list_to_mylist(item))
    return result


def part_b(contents: str) -> int:
    lines = contents.replace("\n\n", "\n").split("\n")
    evaled_lines: list[MyList] = [list_to_mylist(eval(line)) for line in lines] + [
        list_to_mylist([[2]]), list_to_mylist([[6]])
    ]
    sorted_lines = sorted(evaled_lines)

    result = 1
    for index, line in enumerate(sorted_lines):
        if json.dumps(line) in {"[[2]]", "[[6]]"}:
            result *= (index+1)

    return result


def main():
    contents = Path("13_input.txt").read_text().strip()
    print(part_a(contents))
    print(part_b(contents))


if __name__ == "__main__":
    main()
