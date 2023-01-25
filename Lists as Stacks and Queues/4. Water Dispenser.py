from collections import deque

people = deque()
quantity = int(input())
while True:
    names = input()
    if names == "Start":
        break
    people.append(names)

while True:
    command = input()
    if command == 'End':
        break
    command = command.split()
    if len(command) == 1:

        if quantity < int(command[0]):
            print(f"{people.popleft()} must wait")

        else:
            print(f'{people.popleft()} got water')
            quantity -= int(command[0])
    else:
        quantity += int(command[1])


print(f'{quantity} liters left')