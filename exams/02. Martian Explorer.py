matrix = []

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}


rover_position = []

for r in range(6):
    row = input().split()
    matrix.append(row)
    if 'E' in row:
        c = row.index('E')
        rover_position = [r, c]
r, c = rover_position[0],rover_position[1]
commands = input().split(", ")
deposite = []
for command in commands:

    if command == 'up' and r == 0:
        r, c = 5, rover_position[1]
    elif command == 'down' and r == 5:
        r, c = 0, rover_position[1]
    elif command == 'left' and c == 0:
        r, c = rover_position[0], 5
    elif command == 'right' and c == 5:
        r, c = rover_position[0], 0
    else:
        r, c = rover_position[0] + directions[command][0], rover_position[1] + directions[command][1]
    rover_position = [r, c]

    if matrix[r][c] == 'W':
        print(f"Water deposit found at ({r}, {c})")
        deposite.append('Water')
    elif matrix[r][c] == 'M':
        print(f"Metal deposit found at ({r}, {c})")
        deposite.append('Metal')
    elif matrix[r][c] == 'C':
        print(f"Concrete deposit found at ({r}, {c})")
        deposite.append('Concrete')
    elif matrix[r][c] == 'R':
        print(f"Rover got broken at ({r}, {c})")

        break

if 'Water' and 'Metal' and 'Concrete' in deposite:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")


