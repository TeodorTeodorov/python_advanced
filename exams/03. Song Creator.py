def add_songs(*args):
    output = []
    dict = {}
    for el in args:

        if el[0] not in dict:
            dict[el[0]] = el[1]
        else:

            dict[el[0]].append(' '.join(el[1]))

    for key, value in dict.items():
        if value:
            n_value = '\n'.join(value)
            output.append(f"- {key}\n{''.join(n_value)}")
        else:
            output.append(f"- {key}")

    return '\n'.join(x for x in output)


print(add_songs(
    ("Bohemian Rhapsody", []),
    ("Just in Time",
     ["Just in time, I found you just in time",
      "Before you came, my time was running low",
      "I was lost, the losing dice were tossed",
      "My bridges all were crossed, nowhere to go"])
))
