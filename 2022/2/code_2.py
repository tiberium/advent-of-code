total_score = 0
file_name = "input"


class GameRulesEngine:
    def __init__(self, loose: str, draw: str, win: str) -> None:
        self.loose = loose
        self.draw = draw
        self.win = win

    def __call__(self, round_result: str) -> str:
        match round_result:
            case "X":
                return self.loose
            case "Y":
                return self.draw
            case "Z":
                return self.win

        raise ValueError(f"Move {round_result} not recognized as a valid one. Please choose from [X, Y, Z]")


def round_guide_score(round_guide: str) -> int:
    verdict = round_guide[2]
    shape = ''
    match round_guide[0]:
        case "A":
            shape = GameRulesEngine(loose="C", draw="A", win="B")(verdict)
        case "B":
            shape = GameRulesEngine(loose="A", draw="B", win="C")(verdict)
        case "C":
            shape = GameRulesEngine(loose="B", draw="C", win="A")(verdict)
        case _:
            raise ValueError(f"Move {round_guide[0]} not recognized as a valid one. Please choose from [A, B, C]")

    shape_score = 0
    match shape:
        case "A":
            shape_score = 1
        case "B":
            shape_score = 2
        case "C":
            shape_score = 3
        case _:
            raise ValueError(f"Move {shape} not recognized as a valid one. Please choose from [A, B, C]")

    move_score = 0
    match verdict:
        case "X":
            move_score = 0
        case "Y":
            move_score = 3
        case "Z":
            move_score = 6
        case _:
            raise ValueError(f"Expected round verdict {verdict} not recognized as a valid one. Please choose from [X, Y, Z]")

    return shape_score + move_score


with open(file_name, "r") as file:
    last_line = False
    while not last_line:
        round_guide = file.readline()

        if len(round_guide):
            total_score += round_guide_score(round_guide)
        else:
            last_line = True

print(total_score)

