# users = int(input())
#
# usernames = set(input() for x in range(users))
#
#
# for user in usernames:
#     print(user)


print(*{input() for i in range(int(input()))}, sep="\n")