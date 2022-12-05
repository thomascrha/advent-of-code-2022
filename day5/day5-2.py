"""
    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""

from rich import print

import numpy as np

def delete(lst, to_delete):
    return [element for element in lst if element != to_delete]

def parse_stacks(stacks):
    """
    [0, "N", "Z"], ["D", "C", "M"], [0, 0, "P"]
    """
    _stacks = []
    _s = stacks.split("\n")

    number_of_stacks = int(_s[-1:][0].split(" ")[-1:][0])
    for line in _s:
        _line = ""
        for inx, c in enumerate(list(line)):
            if (inx + 1) % 4 == 0:
                _line += "#"
            else:
                _line += c
        _stacks.append(''.join(_line))

    stacks = np.zeros((10, 10), dtype=np.int32).tolist()
    for xinx, stack in enumerate(_stacks[:-1]):
        for yinx, i in enumerate(stack.split("#")):
            if " " not in list(i):
                stacks[yinx][xinx] = i.strip('[').strip(']')

    # assert [[0, "N", "Z"], ["D", "C", "M"], [0, 0, "P"]] == stacks
    return [delete(stack, 0) for stack in stacks], number_of_stacks

def parse_moves(moves):
    _moves = []
    for move in moves.split("\n"):
        move = move.strip().split(" ")
        _moves.append([int(move[1]), int(move[3]), int(move[5])])

    return _moves

def move_creates(stacks, moves):
    for move in moves:
        # move 1 from 2 to 1
        move_list = stacks[move[1] - 1][0:move[0]]
        stacks[move[2] - 1] = move_list + stacks[move[2] - 1]

        # remove the value(s) from initial stack
        stacks[move[1] - 1] = stacks[move[1] - 1][move[0]:]

    return stacks

def get_score(stacks):
    score = ""
    for s in stacks:
        try:
            score += s[0]
        except:
            pass

    return score

def get_input():
    with open("./day5.input") as input_file:
        stacks, moves = input_file.read().split("\n\n")

    return stacks, moves

stacks, moves = get_input()

stacks, number_of_stacks = parse_stacks(stacks)
moves = parse_moves(moves)

stacks = move_creates(stacks, moves)
print(get_score(stacks))