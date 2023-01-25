row, col = map(int, input().split(', '))
matrix = []

for i in range(row):
    row_nums = list(map(int, input().split()))
    matrix.append(row_nums)

total = []
rows = len(matrix)
cols = len(matrix[0])
for i in range(cols):
    sums = 0
    for j in range(rows):
        sums += matrix[j][i]
    total.append(sums)

print(total)
for i in total:
    print(i)