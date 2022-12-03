with open("./day1.input") as calories_input:
    raw_calories= [line.strip() for line in calories_input]

cals = []
c = []
for cal in raw_calories:
    if cal == "":
        cals.append(c)
        c = []
        continue

    c.append(int(cal))

largest = [0]

for inx, elf_cal in enumerate(cals):
    if sum(elf_cal) > largest[-1:][0]:
        largest.append(sum(elf_cal))

print(sum(largest[-3:]))