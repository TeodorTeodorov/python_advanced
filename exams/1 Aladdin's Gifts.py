from collections import deque

materials = deque(map(int, input().split()))
magic_level = deque(map(int, input().split()))

gifts = {}

while materials and magic_level:
    curr_mat = materials.pop()
    curr_mag = magic_level.popleft()
    sum = curr_mag + curr_mat
    if 100 <= sum <= 199:
        gifts['Gemstone'] = sum
    elif 200 <= sum <= 299:
        gifts['Porcelain Sculpture'] = sum
    elif 300 <= sum <= 399:
        gifts['Gold'] = sum
    elif 400 <= sum <= 499:
        gifts['Diamond Jewellery'] = sum
    elif sum < 100:
        new_sum = curr_mat * 2 + curr_mag * 3
        if new_sum % 2 != 0:
            new_sum *= new_sum
            if 100 <= sum <= 199:
                gifts['Gemstone'] = sum
            elif 200 <= sum <= 299:
                gifts['Porcelain Sculpture'] = sum
            elif 300 <= sum <= 399:
                gifts['Gold'] = sum
            elif 400 <= sum <= 499:
                gifts['Diamond Jewellery'] = sum
    elif sum < 499:
        sum /= 2
        if 100 <= sum <= 199:
            gifts['Gemstone'] = sum
        elif 200 <= sum <= 299:
            gifts['Porcelain Sculpture'] = sum
        elif 300 <= sum <= 399:
            gifts['Gold'] = sum
        elif 400 <= sum <= 499:
            gifts['Diamond Jewellery'] = sum
if gifts:
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")
if materials:
    print(f"Materials left: {', '.join(str(x) for x in materials)}")
if magic_level:
    print(f"Magic left: {', '.join(str(x) for x in magic_level)}")
output = []
for k in gifts.keys():
    output.append(k)
for i in output:
    print(f"{i}: {output.count(i)}")
