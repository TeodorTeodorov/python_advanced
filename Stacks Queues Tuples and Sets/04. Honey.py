from collections import deque

working_bee = deque(int(x) for x in input().split())
nectar = deque(int(x) for x in input().split())
symbols = deque(x for x in input().split())

total_honey = 0

operators = {
    '*': lambda x, y:x * y,
    '/': lambda x, y:x / y,
    '-': lambda x, y:x - y,
    '+': lambda x, y:x + y,
}

while working_bee and nectar:
    current_bee = working_bee.popleft()
    current_nectar = nectar.pop()
    if current_nectar < current_bee:
        working_bee.appendleft(current_bee)
    elif current_nectar > current_bee:
        total_honey += abs(operators[symbols.popleft()](current_bee, current_nectar))

print(f"Total honey made: {total_honey}")

if working_bee:
    print(f"Bees left: {', '.join(str(x) for x in working_bee)}")

if nectar:
    print(f"Nectar left: {', '.join(str(x) for x in nectar)}")