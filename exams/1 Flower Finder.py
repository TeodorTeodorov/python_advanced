from collections import deque
#
# vowels = deque(map(str, input().split()))
# consonants = deque(map(str, input().split()))
#
# words = ['rose','tulip','lotus','daffodil']
# copy_words = words.copy()
# while vowels and consonants:
#     current_vowels = vowels.popleft()
#     current_consonants = consonants.pop()
#     for word in range(len(words)):
#         for el in words[word]:
#             if current_vowels == el:
#                 words[word] = words[word].replace(el, '')
#                 if copy_words[word] == '':
#                     print(f"Word found: {word}")
#             elif current_consonants == el:
#                 words[word] = words[word].replace(el, '')
#                 if copy_words[word] == '':
#                     print(f"Word found: {word}")
#
# print('Cannot find any word!')
# if vowels:
#     print(f"Vowels left: {' '.join(str(x) for x in vowels)}")
# if consonants:
#     print(f"Consonants left: {' '.join(str(x) for x in consonants)}")
#
#

vowels = deque(input().split())
consonants = deque(input().split())

words = ['rose', 'tulip', 'lotus', 'daffodil']
word_copy = words.copy()
while vowels and consonants:
    current_vowels = vowels.popleft()
    current_consonants = consonants.pop()
    for word in word_copy:
        for index in range(len(word)):
            if current_consonants == word[index] or current_vowels == word[index]:
                word[index] = ''

            if word == '':
                print(words.index(word))


        # else:
        #     vowels.append(current_vowels)
        #     consonants.appendleft(current_consonants)
        # for word in words:
        #     if word == '':
        #         print(f"Word found: {word}")
        #         break

print('Cannot find any word!')

if vowels:
    print(f"Vowels left: {' '.join(str(x) for x in vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(str(x) for x in consonants)}")
