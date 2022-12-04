"""
TEST INPUT
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""
from rich import print
import numpy as np

def lists_overlap(a, b):
    return set(a).issubset(b) or set(b).issubset(a)

def get_input():
    assignments = []
    with open("./day4.input") as pairings:
        for assignment in pairings:
            elf1, elf2 = assignment.strip().split(",")
            elf1 = [int(i) for i in elf1.split("-")]
            elf2 = [int(i) for i in elf2.split("-")]

            elf1 = np.arange(elf1[0], elf1[1] + 1 , 1).tolist()
            elf2 = np.arange(elf2[0], elf2[1] + 1, 1).tolist()
            assignments.append([elf1, elf2])

    return assignments

assignments = get_input()

overlaps = 0
for assignment in assignments:
    if lists_overlap(assignment[0], assignment[1]):
        overlaps += 1

print(overlaps)