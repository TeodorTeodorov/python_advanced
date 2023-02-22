def start_spring(**kwargs):
    result = ''
    new_dict = {}
    for names, types in kwargs.items():

        if types not in new_dict:
            new_dict[types] = []
            new_dict[types].append(names)
        else:
            new_dict[types].append(names)
    new_dict = sorted(new_dict.items(), key=lambda x: (-len(x[1]), x[0]))
    print(new_dict)

    for name in new_dict:
        result += f"{name[0]}:\n"
        sorted_product = sorted(name[1])
        for product in sorted_product:
            result += f"-{product}\n"
    return result


example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))
