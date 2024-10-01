from enum import Enum
from typing import List, Optional


TOTAL_AVAILABLE_DISK_SPACE = 70000000
MINIMUM_NEEDED_DISK_SPACE = 30000000


class FileSystemNodeType(Enum):
    DIRECTORY = "directory"
    FILE = "file"


class TerminalCommandType(Enum):
    CHANGE_DIRECTORY = "cd"
    LIST = "ls"
    OUTPUT = "output"


class FileSystemNode:
    def __init__(self, node_type: FileSystemNodeType, name: str, size: int = 0, parent_node: Optional['FileSystemNode'] = None) -> None:
        self.type = node_type
        self.name = name

        self.parent_node = parent_node

        self._size = 0
        self.size = size

    @property
    def size(self) -> int:
        return self._size

    @size.setter
    def size(self, value: int) -> None:
        match self.type:
            case FileSystemNodeType.DIRECTORY:
                self._size += value
            case FileSystemNodeType.FILE:
                self._size = value

        if self.parent_node:
            self.parent_node.size = value

    def ancestors(self) -> List['FileSystemNode']:
        ancestors = []
        current = self
        while current.parent_node:
            ancestors.append(current.parent_node)
            current = current.parent_node

        return ancestors

    def __hash__(self) -> int:
        return hash(self.ancestors())


class TerminalCommandParser:
    @staticmethod
    def parse_terminal_line(terminal_line: str) -> TerminalCommandType:
        if not terminal_line.startswith("$"):
            return TerminalCommandType.OUTPUT

        if terminal_line.startswith("$ cd"):
            return TerminalCommandType.CHANGE_DIRECTORY

        if terminal_line.startswith("$ ls"):
            return TerminalCommandType.LIST

        raise ValueError("The provided terminal line is not a supported command, nieghter is it the temrinal's output.")

    @staticmethod
    def get_cd_directory_name(terminal_line: str) -> str:
        return terminal_line.split()[-1:][0]

    @staticmethod
    def get_file_node(terminal_line: str,parent: FileSystemNode) -> FileSystemNode:
        node_type = FileSystemNodeType.DIRECTORY if terminal_line.startswith("dir") else FileSystemNodeType.FILE
        node_information = terminal_line.split(" ")

        node_name = node_information[1]
        node_size = 0 if node_type == FileSystemNodeType.DIRECTORY else int(node_information[0])

        return FileSystemNode(name=node_name, node_type=node_type, size=node_size, parent_node=parent)


class FileSystem:
    def __init__(self, root_node: FileSystemNode) -> None:
        self.root_node = root_node
        self.directories = [self.root_node]        


class Terminal:
    def __init__(self) -> None:
        self.current_node : FileSystemNode = FileSystemNode(node_type=FileSystemNodeType.DIRECTORY, name="/", size=0)
        self.file_system = FileSystem(root_node=self.current_node)

    def process_line(self, terminal_line: str) -> None:
        commandType = TerminalCommandParser.parse_terminal_line(terminal_line=terminal_line)

        match commandType:
            case TerminalCommandType.CHANGE_DIRECTORY:
                self.execute_cd(terminal_line=terminal_line)
            case TerminalCommandType.OUTPUT:
                TerminalCommandParser.get_file_node(terminal_line=terminal_line, parent=self.current_node)
            case TerminalCommandType.LIST:
                pass

    def execute_cd(self, terminal_line: str) -> None:
        directory_name = TerminalCommandParser.get_cd_directory_name(terminal_line=terminal_line)

        if directory_name == ".." and self.current_node.parent_node:
            self.current_node = self.current_node.parent_node
            return

        node = FileSystemNode(node_type=FileSystemNodeType.DIRECTORY, name=directory_name, size=0, parent_node=self.current_node)
        self.current_node = node

        if self.current_node not in self.file_system.directories:
            self.file_system.directories.append(self.current_node)


def solution(file_name: str = "input") -> int:
    terminal = Terminal()
    with open(file_name, "r") as file:
        for line in file:
            terminal.process_line(line.strip())

    free_space = TOTAL_AVAILABLE_DISK_SPACE -terminal.file_system.root_node.size
    space_to_free = MINIMUM_NEEDED_DISK_SPACE - free_space

    if space_to_free <= 0:
        return 0
    
    directories_sorted = sorted(terminal.file_system.directories, key=lambda directory: directory.size)
    for directory in directories_sorted:
        if directory.size >= space_to_free:
            return directory.size
    
    return -1


print(solution())
