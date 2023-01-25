# from collections import deque
#
# stack = deque()
# num = int(input())
# for i in range(num):
#     query = input().split()
#     if len(query) > 1:
#
#         stack.append(int(query[1]))
#     else:
#         number = int(query[0])
#
#         if number == 2:
#             if stack:
#                 stack.pop()
#
#         elif number == 3:
#             print(max(stack))
#         elif number == 4:
#             print(min(stack))
#
# stack.reverse()
# print(*stack, sep=', ')
from collections import deque

numbers = deque()

map_fun = {
    1: lambda x: numbers.append(x[1]),
    2: lambda x: numbers.pop() if numbers else None,
    3: lambda x: print(max(numbers)) if numbers else None,
    4: lambda x: print(min(numbers)) if numbers else None,
}

for _ in range(int(input())):
    num_data = [int(x) for x in input().split()]
    map_fun[num_data[0]](num_data)

numbers.reverse()
print(*numbers, sep=', ')
