# matrix = [string.split() for string in input().split('|')]
# print(*[' '.join(string) for string in matrix[::-1]])

line = input().split('|')
sub_lists = []

for sub_string in line[::-1]:
    sub_lists.extend(sub_string.split())

print(*sub_lists)