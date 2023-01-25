# matrix = [list(input() for x in range(int(input())))]
# symbol = input()


# OK e
rows = int(input())
matrix = []
for row in range(rows):
    row_data = list(input())
    matrix.append(row_data)
symbol = input()
print(matrix)

for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        if symbol == matrix[row][col]:

            print((row, col))
        else:
            print(f"{symbol} does not occur in the matrix")