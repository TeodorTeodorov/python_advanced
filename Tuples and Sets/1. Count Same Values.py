numbers = tuple(map(float, input().split()))
uniq = set(numbers)
for num in uniq:
    print(f"{num} - {numbers.count(num)} times")

