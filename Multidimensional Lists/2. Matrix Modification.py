n = int(input())

matrix = [[int(el) for el in input().split()] for _ in range(n)]

command = input().split()

while command[0] != "END":
    # type_command, row, col, num = command
    type_command, row, col, num = command[0], int(command[1]), int(command[2]), int(command[3])
    if not (0 <= row < n and 0 <= col < n):
        print('Invalid coordinates')

    elif type_command == 'Add':
        matrix[row][col] += num
    elif type_command == "Subtract":
        matrix[row][col] -= num

    command = input().split()

[print(*row) for row in matrix]

