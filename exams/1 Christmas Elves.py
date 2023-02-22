from collections import deque

elf_energy = deque(map(int, input().split()))
materials = deque(map(int, input().split()))

total_energy = 0
counter = 0
toys_count = 0

while materials and elf_energy:
    material = materials.pop()
    energy = elf_energy.popleft()
    counter += 1
    if energy < 5:
        materials.append(material)
        continue
    if counter % 3 == 0:
        if counter % 5 == 0:
            if energy >= material * 2:
                total_energy += material
            else:
                energy *= 2
                elf_energy.append(energy)
        else:
            if energy >= material * 2:
                toys_count += 2
                energy = energy - material * 2 + 1
                elf_energy.append(energy)
                total_energy += material*2
            else:
                energy *= 2
                elf_energy.append(energy)
                materials.append(material)

    elif counter % 5 ==0:
        if energy >= material:
            total_energy += material
            energy -= material
            elf_energy.append(energy)

        else:
            energy *= 2
            elf_energy.append(energy)
            materials.append(material)

    else:
        if energy >= material:
            toys_count += 1
            energy = energy - material +1
            elf_energy.append(energy)
            total_energy += material
        else:
            energy *= 2
            elf_energy.append(energy)
            materials.append(material)


print(f"Toys: {toys_count}")
print(f"Energy: {total_energy}")
if elf_energy:
    print(f"Elves left: {', '.join(str(x) for x in elf_energy)}")

if materials:
    print(f"Boxes left: {', '.join(str(x) for x in materials)}")