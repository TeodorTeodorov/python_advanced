num = int(input())
cars = [input() for car in range(num)]
set_cars = set()

for car in cars:
    command, plate_number = car.split(', ')
    if command == 'IN':
        set_cars.add(plate_number)

    elif command == 'OUT':

        set_cars.remove(plate_number)

if set_cars:
    for car in set_cars:
        print(car)
else:

    print("Parking Lot is Empty")