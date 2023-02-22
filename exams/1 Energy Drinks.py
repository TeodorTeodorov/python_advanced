from collections import deque

milligrams_of_caffeine = deque(int(x) for x in input().split(', '))
energy_drinks = deque(int(x) for x in input().split(', '))

maximum_caffeine = 300
coffeine_in_drink = 0
stamat_total_coffeine = 0

while milligrams_of_caffeine and energy_drinks:
    current_coffeine = milligrams_of_caffeine.pop()
    current_energy_drink = energy_drinks.popleft()
    coffeine_in_drink = current_coffeine * current_energy_drink

    if stamat_total_coffeine + coffeine_in_drink < maximum_caffeine:
        stamat_total_coffeine += coffeine_in_drink
        continue
    else:
        energy_drinks.append(current_energy_drink)
        stamat_total_coffeine -= 30
        if stamat_total_coffeine < 0:
            stamat_total_coffeine = 0

if energy_drinks:
    print(f"Drinks left: {', '.join(str(x) for x in energy_drinks)}")


else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")
print(f"Stamat is going to sleep with {stamat_total_coffeine} mg caffeine.")
