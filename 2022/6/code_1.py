class Buffer:
    def __init__(self, buffer: str) -> None:
        self.buffer_raw = buffer
        self.description = {}
        
        for character in self.buffer_raw:
            self.description[character] = self.description[character] + 1 if character in self.description else 1

    def shifft(self, character: str) -> None:
        if len(character) != 1:
            raise ValueError(f"Buffer cannot be resized, you try to add {len(character)} elements to it!")

        self._remove_first_character()
        self.buffer_raw += character

        self.description[character] = self.description[character] + 1 if character in self.description else 1

    @property
    def contains_only_unique_characters(self) -> bool:
        for volume in self.description.values():
            if volume > 1:
                return False

        return True

    def _remove_first_character(self) -> None:
        first_character = self.buffer_raw[0]
        self.buffer_raw = self.buffer_raw[1:]
        self.description[first_character] -= 1


def get_start_of_packat_marker_index(input: str, unique_buffer_length : int = 4) -> int:
    if len(input) < unique_buffer_length:
        raise ValueError(f"Provided input string is shorter ({len(input)} characters) than the unique buffer's length ({unique_buffer_length}).")

    buffer = Buffer(buffer=input[:unique_buffer_length])
    
    if buffer.contains_only_unique_characters:
        return unique_buffer_length

    for index, character in enumerate(input[unique_buffer_length:]):
        buffer.shifft(character=character)
        if buffer.contains_only_unique_characters:
            return unique_buffer_length + index + 1
        
    return -1


def calculate_solution(file_name: str = "input") -> str:
    input = ''

    with open(file_name, "r") as file:
        input = file.readline()

    return str(get_start_of_packat_marker_index(input=input))


print(calculate_solution())
