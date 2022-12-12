"""
30373
25512
65332
33549
35390
"""

from rich import print
import numpy as np


def get_input():
    return np.genfromtxt("./day8.input", delimiter=1, dtype=int)

def get_direction_score(tree_height, view):
    count = 0

    for v in view:
        count += 1
        if v >= tree_height:
            break

    return count


def get_scenic_score(trees):
    rows = len(trees) - 1
    columns = len(trees[0]) - 1
    scores = []
    for x, _ in enumerate(trees):
        for y, _ in enumerate(_):
            # the edge
            if y in [0, columns] or x in [0, rows]:
                continue


            right = get_direction_score(trees[x, y], trees[x][y + 1:])
            left = get_direction_score(trees[x, y], trees[x][:y][::-1])
            up = get_direction_score(trees[x, y], trees[:,y][:x][::-1])
            down = get_direction_score(trees[x, y], trees[:,y][x + 1:])

            score = right * left * up * down
            # print(f"for position {trees[x][y]}[{x}, {y}] score is {score}")
            # print(f"\tright {trees[x][y + 1:]}")
            # print(f"\tleft {trees[x][:y]}")
            # print(f"\tup {trees[:,y][:x]}")
            # print(f"\tdown {trees[:,y][x + 1:]}")
            scores.append(score)

    return max(scores)

trees = get_input()
print(trees)
print(get_scenic_score(trees))