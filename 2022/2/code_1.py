total_score = 0
file_name = "input"


class GameRuleGenerator:
    def __init__(self, against_rock_score: int, against_paper_score: int, against_scissors_score: int) -> None:
        self.against_rock_score = against_rock_score
        self.against_paper_score = against_paper_score
        self.against_scissors_score = against_scissors_score

    def __call__(self, move: str) -> int:
        match move:
            case "X":
                return self.against_rock_score
            case "Y":
                return self.against_paper_score
            case "Z":
                return self.against_scissors_score

        raise ValueError(f"Move {move} not recognized as a valid one. Please choose from [X, Y, Z]")


def round_guide_score(round_guide: str) -> int:
    move = round_guide[2]
    base_score = 0
    match round_guide[0]:
        case "A":
            base_score = GameRuleGenerator(against_rock_score=3, against_paper_score=6, against_scissors_score=0)(move)
        case "B":
            base_score = GameRuleGenerator(against_rock_score=0, against_paper_score=3, against_scissors_score=6)(move)
        case "C":
            base_score = GameRuleGenerator(against_rock_score=6, against_paper_score=0, against_scissors_score=3)(move)
        case _:
            raise ValueError(f"Move {base_score} not recognized as a valid one. Please choose from [A, B, C]")

    shape_score = 0
    match move:
        case "X":
            shape_score = 1
        case "Y":
            shape_score = 2
        case "Z":
            shape_score = 3
        case _:
            raise ValueError(f"Move {move} not recognized as a valid one. Please choose from [X, Y, Z]")

    return base_score + shape_score


with open(file_name, "r") as file:
    last_line = False
    while not last_line:
        round_guide = file.readline()

        if len(round_guide):
            total_score += round_guide_score(round_guide)
        else:
            last_line = True

print(total_score)

