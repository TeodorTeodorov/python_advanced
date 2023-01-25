from collections import deque

words = deque(input().split())

colors = {'red', 'yellow', 'blue', 'orange', 'purple', 'green'}
mix_color = {
    'orange': {'red', 'yellow'},
    'purple': {'red', 'blue'},
    'green': {'yellow', 'blue'}
}

result = []

while words:
    first_word = words.popleft()
    sec_word = words.pop() if words else ''  # ----попвай ако има думи, ако не дай празен стр

    for color in (first_word + sec_word, sec_word + first_word):
        if color in colors:
            result.append(color)
            break
    else:
        for el in (first_word[:-1], sec_word[:-1]):
            if el:
                words.insert(len(words) // 2, el)   #инсъртваме el в средата на индекса


for color in set(mix_color.keys()).intersection(result): # дали result ги има в mix_color
    if not mix_color[color].issubset(result): # ako color ги има в result
        result.remove(color)

print(result)