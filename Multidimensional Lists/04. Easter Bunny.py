size = int(input())

matrix = []
bunny_pos = []
best_path = []

best_direction = None
max_collect_eggs = 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for row in range(size):
    matrix.append(input().split())
    if "B" in matrix[row]:
        bunny_pos = [row, matrix[row].index('B')]

for direction, positions in directions.items():  # движим заека
    row, col = [
        bunny_pos[0] + positions[0],
        bunny_pos[1] + positions[1]
    ]

    path = []
    collect_eggs = 0

    while 0 <= row < size and 0 <= col < size:  # dali e v matricata
        if matrix[row][col] == 'X':
            break

        collect_eggs += int(matrix[row][col])
        path.append([row, col])
        # движим заека
        row += positions[0]
        col += positions[1]

    if collect_eggs >= max_collect_eggs: # най-добър път
        max_collect_eggs = collect_eggs
        best_direction = direction
        best_path = path

print(best_direction)
print(*best_path, sep="\n")
print(max_collect_eggs)