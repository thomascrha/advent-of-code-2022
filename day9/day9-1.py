"""
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
"""
from rich import print
import numpy as np
PLAY_SIZE = 100

STARTING_POINT_X, STARTING_POINT_Y = 1, PLAY_SIZE - 2


def get_input():
	with open("./day9.input") as input_file:
		return input_file.read().split("\n")

def get_play_area():
    play_area = np.chararray((PLAY_SIZE - 1, PLAY_SIZE))
    play_area[:] = "."
    play_area[STARTING_POINT_X][STARTING_POINT_Y] = "s"

    return play_area
def solve_puzzle(instructions, start_position):
    # Create a dictionary that maps each instruction character to a tuple of offsets for the head and tail
    offsets = {
        "U": (0, -1),
        "D": (0, 1),
        "L": (-1, 0),
        "R": (1, 0)
    }

    # Initialize the head and tail positions
    head_position = start_position
    tail_position = start_position

    # Loop through the instructions
    for instruction in instructions:
        # Split the instruction into a direction character and a distance
        direction, distance = instruction[0], int(instruction[1])

        # Get the offsets for the current direction
        head_offset, tail_offset = offsets[direction]

        # Loop the appropriate number of times to move the head and tail
        for _ in range(distance):
            # Update the head and tail positions
            head_position = (head_position[0] + head_offset, head_position[1] + head_offset)
            tail_position = (tail_position[0] + tail_offset, tail_position[1] + tail_offset)

            # If the head and tail are not adjacent, update the tail position to keep it close to the head
            if abs(head_position[0] - tail_position[0]) > 1 or abs(head_position[1] - tail_position[1]) > 1:
                if head_position[0] == tail_position[0]:
                    # Head and tail are in the same column, move the tail one step up or down
                    if head_position[1] > tail_position[1]:
                        tail_position = (tail_position[0], tail_position[1] + 1)
                    else:
                        tail_position = (tail_position[0], tail_position[1] - 1)
                elif head_position[1] == tail_position[1]:
                    # Head and tail are in the same row, move the tail one step left or right
                    if head_position[0] > tail_position[0]:
                        tail_position = (tail_position[0] + 1, tail_position[1])
                    else:
                        tail_position = (tail_position[0] - 1, tail_position[1])
                else:
                    # Head and tail are not in the same row or column, move the tail one step diagonally
                    if head_position[0] > tail_position[0]:
                        if head_position[1] > tail_position[1]:
                            tail_position = (tail_position[0] + 1, tail_position[1] + 1)
                        else:
                            tail_position = (tail_position[0] + 1, tail_position[1] - 1)
                    else:
                        if head_position[1] > tail_position[1]:
                            tail_position = (tail_position[0] - 1, tail_position[1] + 1)
                        else:
                            tail_position = (tail_position[0] - 1, tail_position[1] - 1)

    # Return the final position of the tail
    return tail_position

# Example usage
instructions = [m.split(" ") for m in get_input()]
start_position = (0, 0)
print(solve_puzzle(instructions, start_position))


# play_area = get_play_area()

# print(play_area)

# for inx, move in enumerate(get_input()):
#     print(move)
#     direction, distance = move.strip().split(" ")
#     distance = int(distance)
#     movement_range = list(range(1, distance + 1))

# 	# starting point
#     if inx == 0:
#         play_area[STARTING_POINT_Y, STARTING_POINT_X] = "H"
#         h_pos_x, h_pos_y = STARTING_POINT_X, STARTING_POINT_Y
#         t_pos_x, t_pos_y = PLAY_SIZE - 2, -1
#         movement_range = list(range(1, distance))
#         print(play_area)

#     for d in movement_range:
#         if direction == "R":
#             play_area = get_play_area()
#             # set the new H
#             play_area[h_pos_y][h_pos_x + 1] = "H"
#             # set the new T if not touching
#             play_area[h_pos_y][h_pos_x] = "T"
#             # set the new value of H
#             h_pos_x, h_pos_y = h_pos_x + 1, h_pos_y
#             print(play_area)
#             continue

#         if direction == "L":
#             play_area = get_play_area()
#             # set the new H
#             play_area[h_pos_y][h_pos_x - 1] = "H"
#             # set the new T
#             play_area[h_pos_y][h_pos_x] = "T"
#             # set the new value of H
#             h_pos_x, h_pos_y = h_pos_x - 1, h_pos_y
#             print(play_area)
#             continue

#         if direction == "U":
#             play_area = get_play_area()
#             # set the new H
#             play_area[h_pos_y - 1][h_pos_x] = "H"
#             # set the new T if is not touching
#             play_area[h_pos_y][h_pos_x] = "T"
#             # set the new value of H
#             h_pos_x, h_pos_y = h_pos_x, h_pos_y - 1
#             print(play_area)
#             continue

#         if direction == "D":
#             play_area = get_play_area()
#             # set the new H
#             play_area[h_pos_y + 1][h_pos_x] = "H"
#             # set the new T
#             play_area[h_pos_y][h_pos_x] = "T"
#             # set the new value of H
#             h_pos_x, h_pos_y = h_pos_x, h_pos_y + 1
#             print(play_area)
#             continue





