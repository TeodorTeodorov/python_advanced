def naughty_or_nice_list(list, *arg, **kwargs):
    # args = list(str(x) for x in args)
    nice = []
    naughty = []
    not_found =  []
    for i in list:
        # list_i = list(i)
        for k, v in kwargs.items():
            if i[1] in k and v == 'Nice':
                nice.append(i[1])
            elif i[1] in k and v == 'Naughty':
                naughty.append(i[1])
            elif i[1] in k:
                not_found.append(i[1])
    print(nice, naughty, not_found)









print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))
