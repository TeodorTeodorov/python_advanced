row, col = map(int, input().split(', '))
matrix = []

for i in range(row):
    row_nums = list(map(int, input().split(', ')))
    matrix.append(row_nums)

sums = []
for i in range(2):
    for row in range(len(matrix)):
        max_num = max(matrix[row])
        sums.append(max_num)
        del max_num


print(sums)