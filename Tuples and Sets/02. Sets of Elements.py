n,m = input().split()

set_n = set(input() for x in range(int(n)))
set_m = set(input() for y in range(int(m)))

repeat = set_m & set_n

for i in repeat:
    print(i)



# за всяко X сортирай от най-голямо към малко
# sorted_by_extending = (sorted(tuple, key = lambda x: -x))
# sorted_by_extending = sorted(tuple)[::-1])) i reverse=True