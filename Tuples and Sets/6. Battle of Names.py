n = int(input())
row = 0
odd = set()
even = set()
# for row in range(1, int(input()) + 1):
    #ascii_sum = sum(ord(ch) for ch in input() // row
for namee in range(n):
    row += 1
    name= input()
    suma = 0
    result = 0
    for ch in name:
        suma += ord(ch)
        result = suma // row
    if result % 2 == 0:

        even.add(result)

    else:
        odd.add(result)


if sum(odd) == sum(even):
    print(odd & even, sep=', ')
    #print(*odd.union(even), sep=', ')
elif sum(odd) > sum(even):
    print(*odd.difference(even), sep=", ")
else:
    print(*odd.symmetric_difference(even), sep=", ")



