from collections import deque

food_portions = deque(int(x) for x in input().split(', '))
stamina = deque(int(x) for x in input().split(', '))

conquered_peaks = []

mountains = {
    80: 'Vihren',
    90: "Kutelo",
    100: "Banski Suhodol",
    60: "Polezhan",
    70: "Kamenitza"
}


while food_portions and stamina:

    daily_food = food_portions.pop()
    daily_stamina = stamina.popleft()

    count = daily_food + daily_stamina

    if mountains.get(count):
        conquered_peaks.append(mountains[count])
        del mountains[count]

    else:
        continue



if len(conquered_peaks) == 5:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
    print(f"Conquered peaks:")
    print(*conquered_peaks, sep='\n')

else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")
