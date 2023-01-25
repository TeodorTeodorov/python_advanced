n = int(input())
commands = input().split()
matrix = []
miner_pos = []
collected_coal, total_coal = 0, 0


directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for row in range(n):
    matrix.append(input().split())
    if 's' in matrix[row]:
        miner_pos = [row, matrix[row].index('s')]
        matrix[row][miner_pos[1]] = '*'

    total_coal += matrix[row].count('c')

for command in commands:
    r, c = miner_pos[0] + directions[command][0], miner_pos[1] + directions[command][1]

    if not (0 <= r < n and 0 <= c < n): #za validni koordinati
        continue

    miner_pos = [r, c]

    if matrix[r][c] == 'c': # proverka dali sme na C
        collected_coal += 1

        if collected_coal == total_coal:
            print(f'total coll collected')
            break

    elif matrix[r][c] == 'e':
        print('game over')
        break

    matrix[r][c] = '*'

else:
    print(f"coal left")
