from collections import deque

nums1 = deque(map(int, input().split(', ')))
nums2 = deque(int(x) for x in input().split(', '))

boxes = 0

while nums1 and nums2:
    current_egg = nums1.popleft()
    if current_egg <= 0:
        current_egg = nums1.popleft()

    elif current_egg == 13:
        last_paper = nums2.pop()
        first_paper = nums2.popleft()
        nums2.append(first_paper)
        nums2.appendleft(last_paper)
        continue
    current_paper = nums2.pop()
    if current_paper + current_egg <= 50:
        boxes += 1

if boxes > 0:
    print(f"Great! You filled {boxes} boxes.")

else:
    print("Sorry! You couldn't fill any boxes!")

if nums1:
    print(f"Eggs left: {', '.join(str(x) for x in nums1)}")
if nums2:
    print(f"Pieces of paper left: {', '.join(str(x) for x in nums2)}")
