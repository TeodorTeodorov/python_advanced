from collections import deque

bowls = deque(int(x) for x in input().split(', '))
customers = deque(int(x) for x in input().split(', '))

while bowls and customers:
    last_bowls = bowls.pop()
    first_cust = customers.popleft()
    if last_bowls == first_cust:
        continue
    elif last_bowls > first_cust:
        last_bowls -= first_cust
        bowls.append(last_bowls)
    elif first_cust > last_bowls:
        first_cust -= last_bowls
        customers.appendleft(first_cust)

if not customers:
    print("Great job! You served all the customers.")

if bowls:
    print(f"Bowls of ramen left: {', '.join(str(x) for x in bowls)}")

if not bowls:
    print("Out of ramen! You didn't manage to serve all customers.")

if customers:
    print(f"Customers left: {', '.join(str(x) for x in customers)}")