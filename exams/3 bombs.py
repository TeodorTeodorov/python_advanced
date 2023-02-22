from collections import deque

bomb_effects = deque(int(x) for x in input().split(', '))
bomb_casings = deque(int(x) for x in input().split(', '))


bombs = {
    40: 'Datura Bombs',
    60: 'Cherry Bombs',
    120: 'Smoke Decoy Bombs'
}

created_bombs = []

while bomb_casings and bomb_effects:
    first_effect = bomb_effects.popleft()
    last_casing = bomb_casings.pop()
    bomb_sum = first_effect + last_casing
    if bomb_sum in bombs.keys():
        created_bombs.append(bombs[bomb_sum])
        if created_bombs.count('Datura Bombs') >= 3 and created_bombs.count('Cherry Bombs') >= 3 and created_bombs.count('Smoke Decoy Bombs') >=3:
            break
    else:
        bomb_effects.appendleft(first_effect)
        bomb_casings.append(last_casing - 5)

if 'Datura Bombs' in created_bombs and 'Cherry Bombs' in created_bombs and 'Smoke Decoy Bombs' in created_bombs:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")
if bomb_effects:
    print(f"Bomb Effects: {', '.join(str(x) for x in bomb_effects)}")
else:
    print("Bomb Effects: empty")
if bomb_casings:
    print(f"Bomb Casings: {', '.join(str(x) for x in bomb_casings)}")
else:
    print("Bomb Casings: empty")
created_bombs = sorted(created_bombs)

print(f"Cherry Bombs: {created_bombs.count('Cherry Bombs')}")
print(f"Datura Bombs: {created_bombs.count('Datura Bombs')}")
print(f"Smoke Decoy Bombs: {created_bombs.count('Smoke Decoy Bombs')}")