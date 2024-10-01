from typing import List


def get_badge_priority(teams_rucksack : List[str]) -> int:
    badge = get_teams_badge(teams_rucksack=teams_rucksack)

    if not badge:
        raise ValueError("The provided rucksack doesn't contain a team's badge!")

    return get_element_priority(element=badge)


def get_teams_badge(teams_rucksack: List[str]) -> str:
    if len(teams_rucksack) != 3:
        raise ValueError(f"The team's rucksack length: '{len(teams_rucksack)}' is not supported. A team is a group of exactly 3 members.")

    for element in teams_rucksack[0]:
        if element in teams_rucksack[1] and element in teams_rucksack[2]:
            return element

    return ''


def get_element_priority(element: str) -> int:
    if not element or not validate_element(element):
        raise ValueError(f"Unrecognized element: {element}, not in a..z nor in A..Z.")

    if element >= 'a' and element <= 'z':
        return ord(element) - ord('a') + 1

    if element >= 'A' and element <= 'Z':
       return ord(element) - ord('A') + 27

    raise ValueError(f"Unrecognized element: {element}, not in a..z nor in A..Z.")


def validate_element(element: str) -> bool:
    lower_case_elements = range(ord('a'), ord('z') + 1)
    upper_case_elements = range(ord('A'), ord('Z') + 1)

    return ord(element) in lower_case_elements or ord(element) in upper_case_elements


def calculate_solution(file_name :str = "input"):
    total_badges_priorities = 0
    teams_rucksack = []
    with open(file_name, "r") as file:
        for line in file:
            teams_rucksack.append(line.strip())

            if len(teams_rucksack) == 3:
                total_badges_priorities += get_badge_priority(teams_rucksack)
                teams_rucksack.clear()

    return total_badges_priorities


print(calculate_solution())

