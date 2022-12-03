
# ROCK PAPER SISORS
PLAYER_1 = ['A', 'B', 'C']
# LOSE DRAW WIN
PLAYER_2_INDICATOR = ['X', 'Y', 'Z']

MAP = ["ROCK", "PAPER", "SCISSORS"]
# A X == 0 0

with open("./day2.input") as results:
    rounds = [line.strip().split(" ") for line in results]

round_totals = []
for round in rounds:
    player_1_inx = PLAYER_1.index(round[0]) + 1
    if round[1] == 'X':
        player_2_inx = player_1_inx - 1
        if player_2_inx == 0:
            player_2_inx = 3
        print(f"LOSE {MAP[player_1_inx - 1]} vs {MAP[player_2_inx - 1]}")
        round_totals.append(0 + player_2_inx)
    elif round[1] == 'Y':
        player_2_inx = player_1_inx
        print(f"DRAW {MAP[player_1_inx - 1]} vs {MAP[player_2_inx - 1]}")
        round_totals.append(3 + player_2_inx)
    else:
        player_2_inx = player_1_inx + 1
        if player_2_inx == 4:
            player_2_inx = 1
        print(f"WIN {MAP[player_1_inx - 1]} vs {MAP[player_2_inx - 1]}")
        round_totals.append(6 + player_2_inx)

print(f"\nTOTAL {sum(round_totals)}")