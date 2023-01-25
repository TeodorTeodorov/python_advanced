def print_func(not_arrived):
    print(len(not_arrived))
    for gest in sorted(not_arrived):
        print(gest)

num = int(input())

set_reserve = [input() for gest in range(num)]

set_gests = []
while True:
    gests = input()

    if gests == "END":
        break
    else:
        set_gests.append(gests)

not_arrived = set(set_reserve).difference(set_gests)

print_func(not_arrived)


