class ElfAssignment:
    def __init__(self, assignment_code : str) -> None:
        section_codes = assignment_code.split("-")
        if len(section_codes) != 2:
            raise ValueError(f"Assignment code: {assignment_code} has incorrect format.")

        self.lower_bound, self.upper_bound = [int(bound) for bound in section_codes]

    def overlaps(self, elf_assignment: object) -> bool:
        def _value_in_bounds(value: int, lower_bound: int, upper_bound: int):
            return value >= lower_bound and value <= upper_bound

        if not isinstance(elf_assignment, ElfAssignment):
            return False

        return _value_in_bounds(value=self.lower_bound, lower_bound=elf_assignment.lower_bound, upper_bound=elf_assignment.upper_bound) or \
            _value_in_bounds(value=self.upper_bound, lower_bound=elf_assignment.lower_bound, upper_bound=elf_assignment.upper_bound)

    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, ElfAssignment):
            return False

        return self.lower_bound == __value.lower_bound and self.upper_bound == __value.upper_bound

    def __ge__(self, __value: object) -> bool:
        if not isinstance(__value, ElfAssignment):
            return False

        return self.lower_bound <= __value.lower_bound and self.upper_bound >= __value.upper_bound

    def __hash__(self):
        return hash((self.lower_bound, self.upper_bound))


def is_pair_assignment_range_overlapped(pair_assignment : str) -> bool:
    elfs_assignments = pair_assignment.split(",")
    if len(elfs_assignments) != 2:
        raise ValueError(f"Elfs assignements: {pair_assignment} not valid, incorrect format!")

    assignment_one, assignment_two = [ElfAssignment(assignment_code=assignment_code) for assignment_code in elfs_assignments]

    return assignment_one.overlaps(assignment_two) or assignment_one >= assignment_two


def calculate_solution(file_name :str = "input"):
    total_ranges_overlapped_assignments = 0
    with open(file_name, "r") as file:
        for line in file:
            total_ranges_overlapped_assignments += 1 if is_pair_assignment_range_overlapped(pair_assignment = line.strip()) else 0

    return total_ranges_overlapped_assignments


print(calculate_solution())

