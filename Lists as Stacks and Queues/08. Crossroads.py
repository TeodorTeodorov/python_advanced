from collections import deque

green_win = int(input())
free_win = int(input())
total_cars = 0
cars = deque()
info = input()

while info != 'End':
    if info != "green":
        cars.append(info)
    else:
        current_green = green_win

        while current_green > 0 and cars:
            car = cars.popleft()

            time = current_green + free_win

