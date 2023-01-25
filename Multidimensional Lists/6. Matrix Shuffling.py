def check_valid_indes(indexes):
    if set(indexes[:2]).issubset(valid_rows) and set(indexes[2:]).issubset(valid_cols):
        return True

    return False

def swap_command(command, indexes):
    if check_valid_indes(indexes) and command == 'swap' and len(indexes) == 4:
        row1, col1, row2, col2 = indexes
        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]

        print(*[' '.join(matrix[r]) for r in range(rows)], sep='\n')
    else:
        print("Invalid input!")



rows, cols = [int(x) for x in input().split()]
matrix = [input().split() for x in range(rows)]

valid_rows = range(rows)
valid_cols = range(cols)

while True:
    command, *info = [int(x) if x.isdigit() else x for x in input().split()]

    if command == 'END':
        break

    swap_command(command, info)




