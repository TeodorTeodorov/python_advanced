matrix = []

for i in range(6):
    matrix.append(input().split())

indexes = list(x for x in input() if x.isdigit())

row, col = int(indexes[0]), int(indexes[1])

current_position = [row, col]

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

while True:
    command = input().split(', ')
    if command[0] == 'Stop':
        break
    if command[0] == "Create":
        direction, value = command[1], command[2]
        r, c = current_position[0] + directions[direction][0], current_position[1] + directions[direction][1]
        current_position = [r, c]

        if matrix[current_position[0]][current_position[1]] == '.':
            matrix[current_position[0]][current_position[1]] = value

    elif command[0] == "Update":
        direction, value = command[1], command[2]
        r, c = current_position[0] + directions[direction][0], current_position[1] + directions[direction][1]
        current_position = [r, c]
        matrix[current_position[0]][current_position[1]] = value

    elif command[0] == "Delete":
        direction = command[1]
        r, c = current_position[0] + directions[direction][0], current_position[1] + directions[direction][1]
        current_position = [r, c]
        matrix[current_position[0]][current_position[1]] = '.'
    elif command[0] == "Read":
        direction = command[1]
        r, c = current_position[0] + directions[direction][0], current_position[1] + directions[direction][1]
        current_position = [r, c]
        if matrix[current_position[0]][current_position[1]] != '.':
            print(matrix[current_position[0]][current_position[1]])

[print(*matrix[r], sep=' ') for r in range(6)]

