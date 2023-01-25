rows, cols = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()] for x in range(rows)]

new_matrix = []
max_sux = float('-inf')

for row in range(rows - 2):
    for col in range(cols - 2):
        first_row = matrix[row][col:col+3]
        sec_row = matrix[row + 1][col:col+3]
        third_row = matrix[row + 2][col:col+3]

        cur_sum = sum(first_row) + sum(sec_row) + sum(third_row)

        if cur_sum > max_sux:
            max_sux = cur_sum
            new_matrix = [first_row,sec_row,third_row]

print(f"Sum = {max_sux}")
[print(*new_matrix[row]) for row in range(3)]