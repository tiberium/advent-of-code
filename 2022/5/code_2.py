from typing import List


class CargoCraneMoveInstruction:
    def __init__(self, instruction: str) -> None:
        self.volume, self.source, self.destination = [int(tag) for tag in instruction.strip().split(" ") if
                                                      tag.isnumeric()]
        self.source -= 1
        self.destination -= 1
        self.raw = instruction


class StackCratesParser:
    @staticmethod
    def parse_stack_crates_raw(stack_crates_raw: List[str]) -> List[List[str]]:
        stack_indexes_line = stack_crates_raw[-1:][0]
        number_of_stacks = int(stack_indexes_line.split()[-1:][0])

        stack_crates = []
        for _ in range(number_of_stacks):
            stack_crates.append([])

        # iterating over reversed list without the last element
        for index in range(len(stack_crates_raw) - 2, -1, -1):
            for crate in [(i, el) for i, el in enumerate(stack_crates_raw[index]) if i == 1 or (i - 1) % 4 == 0]:
                if crate[1] != ' ':
                    stack_crates[int(crate[0] / 4)].append(crate[1])

        return stack_crates


class CargoCrane:
    def __init__(self, stack_crates: List) -> None:
        self.stack_crates = stack_crates

    def get_top_crates(self) -> str:
        return "".join([stack[-1:][0] for stack in self.stack_crates if stack[-1:][0] != ' '])

    def move(self, move: CargoCraneMoveInstruction) -> None:
        self.validate_move(move=move)

        self.stack_crates[move.source], popped_items = self.stack_crates[move.source][: move.volume * -1], \
                                                       self.stack_crates[move.source][move.volume * -1:]
        self.stack_crates[move.destination].extend(popped_items)

    def validate_move(self, move: CargoCraneMoveInstruction) -> None:
        if move.source > len(self.stack_crates):
            raise ValueError(f"Move: {move.raw} not possible, stack crate no {move.source} doesn't exist.")

        if len(self.stack_crates[move.source]) < move.volume:
            raise ValueError(f"Move: {move.raw} not possible, stack crate no {move.source} doesn't have enough crates.")

        if move.destination > len(self.stack_crates):
            raise ValueError(f"Move: {move.raw} not possible, stack crate no {move.destination} doesn't exist.")


def calculate_solution(file_name: str = "input") -> str:
    stack_crates_raw = []
    cargo_crane = None

    with open(file_name, "r") as file:
        for line in file:
            if not cargo_crane and line == "\n":
                stack_crates = StackCratesParser.parse_stack_crates_raw(stack_crates_raw=stack_crates_raw)
                cargo_crane = CargoCrane(stack_crates=stack_crates)
                continue

            if not cargo_crane:
                stack_crates_raw.append(line.strip())
            else:
                cargo_crane.move(move=CargoCraneMoveInstruction(line.strip()))

    return cargo_crane.get_top_crates() if cargo_crane else ""


print(calculate_solution())
