
# ROCK PAPER SISORS
PLAYER_1 = ['A', 'B', 'C']
PLAYER_2 = ['X', 'Y', 'Z']

# A X == 0 0

with open("./day2.input") as results:
    rounds = [line.strip().split(" ") for line in results]

round_totals = []
for round in rounds:
    player_1_inx = PLAYER_1.index(round[0]) + 1
    player_2_inx = PLAYER_2.index(round[1]) + 1

    # draw
    if player_1_inx == player_2_inx:
        round_totals.append(3 + player_2_inx)
        continue

    player_beaten_inx = player_2_inx - 1

    # if rock - loop round to siscors
    if player_beaten_inx == 0:
        player_beaten_inx = 3

    if player_beaten_inx not in [1, 2, 3]:
        print(player_beaten_inx)

    # player 2 wins
    if player_beaten_inx == player_1_inx:
        round_totals.append(6 + player_2_inx)
        continue
    # player 1 wins
    else:
        round_totals.append(0 + player_2_inx)
        continue

print(sum(round_totals))