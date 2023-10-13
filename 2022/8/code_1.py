from typing import List, Optional, Tuple


def count_visible_trees(trees_line: str, visibility_mask: Optional[List[int]] = None, highest_possible_tree: int = 9) -> Tuple[List[int], int]:
    trees_line_len = len(trees_line)

    sum_of_visible_trees = 0 

    visibility_mask = visibility_mask if visibility_mask else [0] * trees_line_len
    if not visibility_mask[0]:
        sum_of_visible_trees += 1
        visibility_mask[0] = 1
    if not visibility_mask[-1]:
        sum_of_visible_trees += 1
        visibility_mask[-1] = 1

    highest_tree_left_index = 0
    highest_tree_right_index = trees_line_len - 1

    for index in range(1, len(trees_line)-1):
        highest_left_tree = int(trees_line[highest_tree_left_index])
        if highest_left_tree < highest_possible_tree and int(trees_line[index]) > highest_left_tree:
            sum_of_visible_trees += 1 if not visibility_mask[index] else 0
            visibility_mask[index] = 1
            highest_tree_left_index = index

        backward_index = trees_line_len-1-index
        highest_right_tree = int(trees_line[highest_tree_right_index])
        if highest_right_tree < highest_possible_tree and int(trees_line[backward_index]) > highest_right_tree:
            sum_of_visible_trees += 1 if not visibility_mask[backward_index] else 0
            visibility_mask[backward_index] = 1
            highest_tree_right_index = backward_index

        if highest_left_tree == highest_right_tree == highest_possible_tree:
            break

    return (visibility_mask, sum_of_visible_trees)


def solution(file_name: str = "input") -> int:
    forest = []

    forest_visibility_mask = []
    visible_trees = 0

    with open(file_name, "r") as file:
        for horizontal_forest_line in file:
            forest.append(horizontal_forest_line.strip())
            visibility_mask, visible_trees_counter = count_visible_trees(trees_line=horizontal_forest_line.strip()) 
            forest_visibility_mask.append(visibility_mask)
            visible_trees += visible_trees_counter

    for index in range(1, len(forest_visibility_mask[0])-1):
        vertical_forest_line = ''.join([forest_line[index] for forest_line in forest])
        vertical_visibility_mask = [horizontal_mask[index] for horizontal_mask in forest_visibility_mask]
        _, new_visible_trees_counter = count_visible_trees(trees_line=vertical_forest_line, visibility_mask=vertical_visibility_mask)

        visible_trees += new_visible_trees_counter

    return visible_trees


print(solution())

