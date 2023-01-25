def read_matrix():
    row, col = map(int, input().split(', '))
    current_matrix = []

    for i in range(row):
        row_nums = list(map(int, input().split(', ')))
        current_matrix.append(row_nums)
    return current_matrix


matrix = read_matrix()
print(matrix)

matrix = [list(map(int, input().split(', '))) for x in range(int(input()))]  # ---само за ред

matrix2 = [[int(el) for el in input().split(', ')] for _ in range(int(input()))]  # --  за ред

# sum of primery diagonal:
sum_of_primary_diagonal = sum([matrix[i][i] for i in range(len(matrix))])

# sum secondary diagonal:
sum_sec_diagonal = 0
for i in range(len(matrix) - 1, -1, -1):
    sum_sec_diagonal += matrix[i][(len(matrix) - 1) - i]


# sum of left half

sums = 0
matrix_size = len(matrix)
for row in range(matrix_size):
    for col in range(row + 1):
        sums += matrix[row][col]