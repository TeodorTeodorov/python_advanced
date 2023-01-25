from collections import deque

skobi = deque(input())
open_skobi = deque()


while skobi:
    left_koba = skobi.popleft()
    if left_koba in '[{(':
        open_skobi.append(left_koba)
    elif not open_skobi:
        print('NO')
        break
    else:
        if f'{open_skobi.pop() + left_koba}' not in '[](){}':
            print('NO')
            break
else:
    print('YES')
