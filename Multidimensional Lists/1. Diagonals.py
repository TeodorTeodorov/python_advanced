# rows = int(input())
# matrix = [input().split(', ') for i in range(rows)]
# print(matrix)
# pr_diagonal = []
# sec_diagonal = []
# for index in range(rows):
#
#     pr_diagonal.append(matrix[index][index])
#     sec_diagonal.append(matrix[index][rows - index - 1])
#
# print(f"Primary diagonal: {', '.join(pr_diagonal)}. Sum: {sum(map(int, pr_diagonal))}")
# print(f"Primary diagonal: {', '.join(sec_diagonal)}. Sum: {sum(map(int, sec_diagonal))}")

n = int(input())
matrix = [input().split(', ') for x in range(n)]

primary = [int(matrix[r][r]) for r in range(n)]
secondary = [int(matrix[r][n - r - 1]) for r in range(n - 1, -1, -1)]
sum_pr = sum(primary)
sum_sec = sum(secondary)


print(f"Primary diagonal: {', '.join(str(x) for x in primary)}. Sum: {sum_pr}")
print(f"Secondary diagonal: {', '.join(str(x) for x in secondary[::-1])}. Sum: {sum_sec}")