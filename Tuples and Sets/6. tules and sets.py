from collections import deque

nums = input().split()
nums = [int(x) for x in nums]
target = int(input())


for i in range(len(nums)):
    if nums[i] == '':
        continue
    for u in range(i + 1, len(nums)):
        if nums[u] == '':
            continue
        if nums[i] + nums[u] == target:
            print(f'{nums[i]} + {nums[u]} = {target}')
            nums[i] = ''
            nums[u] = ''
            break
