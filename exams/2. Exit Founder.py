# tom, jerry = input().split(', ')
# matrix = []
# for r in range(6):
#     row = list(x for x in input().split())
#     matrix.append(row)
#
# turn = 0
# resting = False
# while True:
#     turn += 1
#     direction = input()
#     direct = []
#
#     for i in direction:
#         if i.isdigit():
#             direct.append(i)
#
#     row = int(direct[0])
#     col = int(direct[1])
#     if matrix[row][col] == "E":
#         if turn % 2 == 0:
#             print(f"Jerry found the Exit and wins the game!")
#         else:
#             print(f"Tom found the Exit and wins the game!")
#             break
#     elif matrix[row][col] == "T":
#         if turn % 2 == 0:
#             print(f"Tom is out of the game! The winner is Jerry.")
#
#         else:
#             print(f"Jerry is out of the game! The winner is Tom.")
#             break
#     elif matrix[row][col] == "W":
#         if turn % 2 == 0:
#             resting = True
#             print(f"Jerry hits a wall and needs to rest.")
#         else:
#             resting = True
#             print(f"Tom hits a wall and needs to rest.")


player1, player2 = input().split(', ')
matrix = []
for r in range(6):
    row = list(x for x in input().split())
    matrix.append(row)

turn = 0
resting = False
rest1 = 0
rest2 = 0
while True:
    turn += 1
    direction = input()
    direct = []
    for i in direction:
        if i.isdigit():
            direct.append(i)

    row = int(direct[0])
    col = int(direct[1])

    if turn % 2 != 0:
        if rest1 % 2 == 0:
            resting = False
        # player1
        if resting == True:
            rest1 += 1
            continue
        if matrix[row][col] == "E":
            print(f"{player1} found the Exit and wins the game!")
            break
        elif matrix[row][col] == "T":
            print(f"{player1} is out of the game! The winner is {player2}.")
            break
        elif matrix[row][col] == "W":
            resting = True
            print(f"{player1} hits a wall and needs to rest.")

    elif turn % 2 == 0:
        if rest2 % 2 == 0:
            resting = False
        # player2
        if resting == True:
            rest2 += 1
            continue

        if matrix[row][col] == "E":
            print(f"{player2} found the Exit and wins the game!")
            break
        elif matrix[row][col] == "T":
            print(f"{player2} is out of the game! The winner is {player1}.")
            break
        elif matrix[row][col] == "W":
            resting = True
            print(f"{player2} hits a wall and needs to rest.")
