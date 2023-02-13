# def positive_negative(numbers):
#     positive = [n for n in numbers if int(n) > 0]
#     negative = [n for n in numbers if int(n) < 0]
#     return negative, positive
#
# num = [int(x) for x in input().split()]
# sum_pos = sum(positive_negative())
# positive_negative()
#

nums = input().split(' ')
positive_sum = sum([int(n) for n in nums if int(n) > 0])
negative_sum = sum([int(n) for n in nums if int(n) < 0])

print(negative_sum)
print(positive_sum)
if abs(negative_sum) > positive_sum:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")