from collections import deque

clothes = deque(int(x) for x in input().split())
rack_capacity = int(input())
current_rack_capacity = rack_capacity

rack = 1
while clothes:
    cloth = clothes.pop()
    if current_rack_capacity - cloth >= 0:
        current_rack_capacity -= cloth
    else:
        rack += 1
        current_rack_capacity = rack_capacity - cloth


print(rack)