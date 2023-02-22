n = int(input())

matrix = []
battle_cruisers_pos = []

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}
dash_cointer = 0
c_couter = 0

for row in range(n):
    rows = list(input())
    matrix.append(rows)
    if 'S' in matrix[row]:
        battle_cruisers_pos = [row, matrix[row].index('S')]
        matrix[row][matrix[row].index('S')] = '-'



while True:
    command = input()
    r, c = battle_cruisers_pos[0] + directions[command][0], battle_cruisers_pos[1] + directions[command][1]

    battle_cruisers_pos = [r, c]

    if matrix[r][c] == '*':
        dash_cointer += 1
        matrix[r][c] = '-'
        if dash_cointer == 3:
            matrix[r][c] = 'S'
            print(f"Mission failed, U-9 disappeared! Last known coordinates [{r}, {c}]!")
            [print(*matrix[r], sep='') for r in range(n)]
            break

    elif matrix[r][c] == 'C':
        matrix[r][c] = '-'
        c_couter += 1
        if c_couter == 3:
            matrix[r][c] = 'S'
            print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
            [print(*matrix[r], sep='') for r in range(n)]
            break

