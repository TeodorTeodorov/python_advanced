from collections import deque

chocolates = deque(int(x) for x in input().split(', '))
cups_of_milk = deque(int(x) for x in input().split(', '))

chocolate_count = 0

while chocolate_count != 5 and chocolates and cups_of_milk:

    last_chocolate = chocolates.pop()
    first_cup_milk = cups_of_milk.popleft()
    if last_chocolate <= 0 and first_cup_milk <= 0:
        continue
    elif last_chocolate <= 0:
        cups_of_milk.appendleft(first_cup_milk)
        continue
    elif first_cup_milk <= 0:
        chocolates.append(last_chocolate)
        continue

    if last_chocolate == first_cup_milk:
        chocolate_count += 1
    else:
        cups_of_milk.append(first_cup_milk)
        chocolates.append(last_chocolate - 5)

if chocolate_count == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")


print(f"Chocolate: {', '.join(str(x) for x in chocolates) or 'empty'}")
print(f"Milk: {', '.join(str(x) for x in cups_of_milk) or 'empty'}")