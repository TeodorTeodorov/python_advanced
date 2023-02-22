from collections import deque

# food =deque(map(int, input().split(', ')))
# stamina  =deque(map(int, input().split(', ')))
food = deque(int(x) for x in input().split(', '))
stamina = deque(int(x) for x in input().split(', '))

peaks = {
    'Vihren' : 80,
    'Kutelo': 90,
    'Banski Suhodol': 100,
    'Polezhan': 60,
    'Kamenitza': 70
}

conquered_peaks = []
counter = 0
for name, peak in peaks.items():
    daily_food = food.pop()
    daily_stamina = stamina.popleft()
    daily_sum = daily_food + daily_stamina
    counter += 1


    while True:

        if daily_sum >= peak:
            conquered_peaks.append(name)
            break
        else:
            counter += 1
            daily_food = food.pop()
            daily_stamina = stamina.popleft()
            daily_sum = daily_food + daily_stamina
            if counter == 7:
                break


    if counter == 7:
        break

if len(conquered_peaks) == 5:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if conquered_peaks:
    print("Conquered peaks:")
    print(*conquered_peaks, sep='\n')
