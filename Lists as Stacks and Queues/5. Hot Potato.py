from collections import deque

names = deque(input().split())
num = int(input())
while len(names) > 1:
    counter = 0
    for i in range(num - 1):
        counter += 1
        name = names.popleft()
        names.append(name)

    print(f'{names.popleft()}')
print(''.join(names))