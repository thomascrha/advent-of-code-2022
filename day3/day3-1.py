import string
from typing import List

"""
TEST DATA

vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""

PRIORITIES = list(string.ascii_letters)

def get_priority(letter: str):
    return PRIORITIES.index(letter) + 1

def get_item_in_both_conpartments(conpartment1: List[str], conpartment2: List[str]):
    for item in conpartment1:
        if item in conpartment2:
            return item

# create the rugsacks with there 2 conpartments
with open("./day3.input") as inventory:
    rugsacks = []
    for rugsack in inventory:
        both_conpartments = list(rugsack.strip())
        size = int(len(both_conpartments) / 2)
        rugsacks.append(
            (
                both_conpartments[:size],
                both_conpartments[size:]
            )
        )

# work out the prioriteis in each rugsack
priorities = 0
for rugsack in rugsacks:
    priorities += get_priority(
        get_item_in_both_conpartments(rugsack[0], rugsack[1])
    )

print(priorities)