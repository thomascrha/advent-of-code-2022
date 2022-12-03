import string
from typing import List
from rich import print
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

def get_item_in_all_sacks(sack1: List[str], sack2: List[str], sack3: List[str]):
    for item in sack1:
        if item in sack2 and item in sack3:
            return item

grouped_sacks = []
# create the rugsacks with there 2 conpartments
with open("./day3.input") as inventory:
    rugsacks = []
    for inx, rugsack in enumerate(inventory):
        both_conpartments = list(rugsack.strip())
        size = int(len(both_conpartments) / 2)
        rugsacks.append(both_conpartments)
        if (inx + 1) % 3 == 0:
            grouped_sacks.append(rugsacks)
            rugsacks = []

print(grouped_sacks)
# work out the prioriteis in each rugsack
priorities = 0
for group_sack in grouped_sacks:
    priorities += get_priority(
        get_item_in_all_sacks(group_sack[0], group_sack[1], group_sack[2])
    )

print(priorities)