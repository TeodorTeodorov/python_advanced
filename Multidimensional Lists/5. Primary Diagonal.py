# size = int(input())
# matrix = []
# for _ in range(size):
#
#     matrix.append([int(x) for x in input().split()])
# suma = 0
# for i in range(size):
#     suma += matrix[i][i]
#
# print(suma)
#


matrix = [list(map(int, input().split())) for x in range(int(input()))]
sum_of_primary_diagonal = sum([matrix[i][i] for i in range(len(matrix))])
print(sum_of_primary_diagonal)
