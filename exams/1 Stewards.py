from collections import deque

sequence = input().split(", ")
nums1 = deque(int(x) for x in input().split(", "))
nums2 = deque(int(x) for x in input().split(", "))

rotation = 0
matches = 0
matches_nums = []
while True:
    if rotation >= 10:
        break
    if matches >= 3:
        break

    rotation += 1
    first = nums1.popleft()
    last = nums2.pop()
    sums_aski = chr(first + last)
    seat1 = f"{first}{sums_aski}"
    seat2 = f"{last}{sums_aski}"

    if seat1 in sequence:
        matches_nums.append(seat1)
        matches += 1
    elif seat2 in sequence:
        matches_nums.append(seat2)
        matches += 1
    else:
        nums1.append(first)
        nums2.appendleft(last)


print(f"Seat matches: {', '.join(matches_nums)}")

print(f"Rotations count: {rotation}")