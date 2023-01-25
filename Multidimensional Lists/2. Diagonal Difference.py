# size = int(input())
# matrix = [input().split() for i in range(size)]
# pr_diagonal = []
# sec_diagonal = []
# for index in range(size):
#     pr_diagonal.append(matrix[index][index])
#     sec_diagonal.append(matrix[index][size - index - 1])
#
# pr_diagonal_sum = sum(map(int, pr_diagonal))
# sec_diagonal_sum = sum(map(int, sec_diagonal))
#
# diff = abs(pr_diagonal_sum - sec_diagonal_sum)
# print(diff)

n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]

primary, secondary = 0,0

for i in range(n):

    primary += matrix[i][i]
    secondary += matrix[n - i - 1][i]

print(abs(primary - secondary))
