n = int(input())
car_number = input()
matrix = []

for row in range(n):
    rows = input().split()
    matrix.append(rows)


car_position = [0, 0]
kilometers = 0
directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

while True:
    command = input()
    if command == "End":
        matrix[r][c] = 'C'
        print(f"Racing car {car_number} DNF.")
        break

    r, c = car_position[0] + directions[command][0], car_position[1] + directions[command][1]
    car_position = [r, c]
    if matrix[r][c] == '.':
        kilometers += 10
    elif matrix[r][c] == 'F':
        kilometers += 10
        print(f"Racing car {car_number} finished the stage!")
        matrix[r][c] = 'C'
        break

    elif matrix[r][c] == 'T':
        kilometers += 30
        matrix[r][c] = '.'
        for roww in range(len(matrix)):
            # exit = [el for el in roww if el == 'T' and roww.index(el) != matrix[r][c]]
            for index in range(len(matrix[roww])):
                if matrix[roww][index] == 'T':
                    if[roww, index] != [r, c]:
                        car_position[0], car_position[1] = roww, index
                        matrix[roww][index] = '.'





print(f"Distance covered {kilometers} km.")

[print(*matrix[r], sep='') for r in range(n)]