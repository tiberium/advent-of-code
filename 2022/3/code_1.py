def find_duplicate_element(rucksack: str) -> str:
    if len(rucksack) % 2:
        raise ValueError(f"Rucksack: {rucksack} has a wrong number of elements!")

    compartment_size = int(len(rucksack) / 2)
    for index in range(compartment_size):
        if rucksack[index] in rucksack[compartment_size:]:
            return rucksack[index]

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


def find_solution(file_name :str = "input"):
    total_rearrangement_priorities = 0
    with open(file_name, "r") as file:
        last_line = False
        while not last_line:
            rucksack = file.readline()

            if len(rucksack.strip()):
                duplicate_element = find_duplicate_element(rucksack.strip())
                total_rearrangement_priorities += get_element_priority(duplicate_element)
            else:
                last_line = True

    return total_rearrangement_priorities


print(find_solution())

