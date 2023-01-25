numbers = int(input())
names = {}
for i in range(numbers):
    name, ocenka = input().split()
    if name not in names:
        names[name] = []
        names[name].append(float(ocenka))
    else:
        names[name].append(float(ocenka))

for name,ocenki in names.items():
    avg = sum(names[name]) / len(names[name])
    ocenca2 = ' '.join(str(f"{ocenka:.2}") for ocenka in ocenki)
    print(f"{name} -> {ocenca2} (avg: {avg:.2f})")