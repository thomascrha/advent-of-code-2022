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

def get_visible_trees(trees):
    rows = len(trees) - 1
    columns = len(trees[0]) - 1
    visible = 0
    for x, _ in enumerate(trees):
        for y, _ in enumerate(_):
            # marks anything on the edge as visible
            if y in [0, columns] or x in [0, rows]:
                # print(f"{trees[x, y]} is on the edge and visible")
                visible += 1
                continue

            # print(f"right of {trees[x, y]} is {trees[x][y + 1:]}")
            # print(f"left of {trees[x, y]} is {trees[x][:y]}")
            # print(f"above of {trees[x, y]} is {trees[:,y][:x]}")
            # print(f"bellow of {trees[x, y]} is {trees[:,y][x + 1:]}")
            # check if its visible
            # right - don't include itself
            if trees[x, y] > max(trees[x][y + 1:]):
                # print(f"\t{trees[x, y]} is visible as all the trees to the right are smaller {trees[x][y:]}")
                visible += 1
                continue


            # left
            if trees[x, y] > max(trees[x][:y]):
                # print(f"\t{trees[x, y]} is visible as all the trees to the left are smaller {trees[x][:y]}")
                visible += 1
                continue

            if trees[x, y] > max(trees[:,y][:x]):
                # print(f"\t{trees[x, y]} is visible as all the trees to the above are smaller {trees[:,y][:x]}")
                visible += 1
                continue

            # dont include itself
            if trees[x, y] > max(trees[:,y][x + 1:]):
                # print(f"\t{trees[x, y]} is visible as all the trees to the bellow are smaller {trees[:,y][x:]}")
                visible += 1
                continue

        # print(f"\t{trees[x, y]} is not visible")
    return visible
trees = get_input()
print(get_visible_trees(trees))