first_sequences = set(int(x) for x in input().split())
second_sequences = set(int(x) for x in input().split())

functions = {
    'Add First': lambda x: [first_sequences.add(el) for el in x],
    'Add Second': lambda x: [second_sequences.add(el) for el in x],
    'Remove First': lambda x: [first_sequences.discard(el) for el in x],
    'Remove Second': lambda x: [second_sequences.discard(el) for el in x],
    "Check Subset": lambda: print(True) if first_sequences.issubset(second_sequences) or
                                           second_sequences.issubset(first_sequences) else print(False)
}

for _ in range(int(input())):
    first, *second = input().split()

    command = first + ' ' + second.pop(0)
    if second:
        functions[command]([int(x) for x in second])
    else:
        functions[command]()

print(*sorted(first_sequences), sep=', ')
print(*sorted(second_sequences), sep=', ')