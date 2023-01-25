from collections import deque

people = deque()
while True:

    names = input()
    if names == "End":
        break

    if names == "Paid":
        print(('\n'.join(people)))
        people.clear()
    people.append(names)
print(f'{len(people)} people remaining.')