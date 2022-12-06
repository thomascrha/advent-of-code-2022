"""
TEST INPUT
mjqjpqmgbljsphdztnvjfqwrcgsmlb
"""

from rich import print


def get_input():
    with open("./day6.input") as packet:
        return packet.read().strip()

print(get_input())