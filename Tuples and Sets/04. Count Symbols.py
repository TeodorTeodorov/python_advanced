text = input()
# result = sorted({ch: text.count(ch) for ch in text})
text_dict = dict()

for ch in text:
    if ch not in text_dict:
        text_dict[ch] = 0

    text_dict[ch] += 1

for ch, times in sorted(text_dict.items()):
    print(f"{ch}: {times} time/s")





