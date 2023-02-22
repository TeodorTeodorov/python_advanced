matrix = []
for row in range(6):
    matrix.append(input().split())

total_sum = 0
for trow in range(3):
    coordinates = []
    for num in input():
        if num.isdigit():

            coordinates.append(int(num))
    r,c = coordinates[0], coordinates[1]
    if matrix[r][c] == 'B':
        suma = 0
        for nums in range(6):

            suma += int(matrix[nums][c]) if matrix[nums][c].isdigit() else 0
        total_sum += suma
if 100 <= total_sum <= 199:
    print(f"Good job! You scored {total_sum} points, and you've won Football.")
elif 200 <= total_sum <= 299:
    print(f"Good job! You scored {total_sum} points, and you've won Teddy Bear.")
elif 300 <= total_sum:
    print(f"Good job! You scored {total_sum} points, and you've won Lego Construction Set.")
else:
    print(f"Sorry! You need {100- total_sum} points more to win a prize.")