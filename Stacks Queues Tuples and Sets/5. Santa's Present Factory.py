from collections import deque

materials = deque(int(x) for x in input().split())
magic_level = deque(int(x) for x in input().split())

crafted = []

magic_needed = {
    150: 'Doll',
    250: 'Wooden train',
    300: 'Teddy bear',
    400: 'Bicycle'
}

while materials and magic_level:

    las_material = materials.pop() #if magic_level[0] or not materials[0] else 0 #--проверка за 0 на магията, като долу
                                        # и проверка на материалите дали са 0
    first_magic = magic_level.popleft() #if materials or not magic_level[0] else 0 # попвай ако има материал и магията не е 0

    if first_magic == 0:
        materials.append(las_material)
        continue
    if las_material == 0:
        magic_level.appendleft(first_magic)

        continue

    current_magic = las_material * first_magic

    if magic_needed.get(current_magic): # get връща ключа, ако го има, ако не none
        crafted.append(magic_needed[current_magic])
    elif current_magic < 0:
        materials.append(las_material + first_magic)

    elif current_magic > 0:
        materials.append(las_material + 15)


if {'Doll', 'Wooden train'}.issubset(crafted) or {'Teddy bear', 'Bicycle'}.issubset(crafted):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if materials:

    print(f"Materials left: {', '.join([str(x) for x in materials][::-1])}")

if magic_level:
    print(f"Magic left: {', '.join(str(x) for x in magic_level)}")

[print(f"{toy}: {crafted.count(toy)}") for toy in sorted(set(crafted))]