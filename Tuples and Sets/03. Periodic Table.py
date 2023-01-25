n = int(input())
compounds_set =set()
for i in range(n):
    compounds = set(input().split())
    compounds_set = compounds_set | compounds
# compounds = set(input().split() for x in range(n))
# compounds = set(map(str, input().split()))
# orders = deque(map(int, input().split()))
# clothes = deque(int(x) for x in input().split())

for i in compounds_set:
    print(i)

print(*compounds_set, sep="\n")