"""
TEST INPUT
mjqjpqmgbljsphdztnvjfqwrcgsmlb
"""

from rich import print


def get_input():
    with open("./day6.input") as packet:
        return packet.read().strip()

def get_marker(packet):
    marker_set = list()
    for inx, character in enumerate(packet):

        if inx in [0, 1, 2]:
            marker_set.append(character)
            continue

        marker_set.append(character)
        # check if all chars are unique
        if len(marker_set) == len(set(marker_set)):
            return inx

        if len(marker_set) > 4:
            # remove the first item
            marker_set = marker_set[1:]

print(get_marker(get_input()))

