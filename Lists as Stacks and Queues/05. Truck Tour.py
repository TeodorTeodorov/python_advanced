from collections import deque

petrol_stat = int(input())
pumps_data = deque([[int(x) for x in input().split()] for i in range(petrol_stat)])
pumps_data_copy = pumps_data.copy()
index = 0
gas_in_tank = 0
while pumps_data_copy:
    petrol, distance = pumps_data_copy.popleft()
    gas_in_tank += petrol

    if gas_in_tank < distance:

        pumps_data.rotate(-1)
        pumps_data_copy = pumps_data.copy()
        gas_in_tank = 0
        index += 1
    else:
        gas_in_tank -= distance




print(index)