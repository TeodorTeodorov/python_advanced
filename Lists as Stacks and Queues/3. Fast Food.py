from collections import deque

quantity = int(input())
queue = []
orders = deque(map(int, input().split()))

print(max(orders))

for order in orders.copy():


    if quantity - order >= 0:
        orders.popleft()
        quantity -= order

    else:
        print(f"Orders left: {' '.join(str(i) for i in orders)}")
        break
else:
    print("Orders complete")