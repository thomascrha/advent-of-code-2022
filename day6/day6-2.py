"""
TEST INPUT
mjqjpqmgbljsphdztnvjfqwrcgsmlb
"""

from rich import print


def get_input():
    with open("./day6.input") as packet:
        return packet.read().strip()

def get_marker(packet, marker_index=14):
    marker_set = list()
    for inx, character in enumerate(packet):

        if inx in list(range(marker_index - 1)):
            marker_set.append(character)
            continue

        marker_set.append(character)

        if len(marker_set) > marker_index:
            # remove the first item
            marker_set = marker_set[1:]

        # check if all chars are unique
        if len(marker_set) == len(set(marker_set)):
            return inx + 1



print(get_marker(get_input()))

