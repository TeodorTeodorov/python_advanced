n = int(input())
longest = set()
for _ in range(n):

    first, second = [ch.split(',') for ch in input().split('-')]

    first_range = set(range(int(first[0]), int(first[1]) + 1))
    second_range = set(range(int(second[0]),int(second[1]) + 1))
    current_longest = first_range & second_range
    if len(current_longest) > len(longest):
        longest = current_longest
print(f"Longest intersection is "
      f"[{', '.join(str(x) for x in longest)}] "
      f"with length {len(longest)}"
)