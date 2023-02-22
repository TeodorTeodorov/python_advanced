def shopping_cart(*args):
    dict = {'Pizza': [],'Dessert': [], 'Soup': []}
    result = ''
    for index in range(len(args)):
        if args[index] == "Stop":
            break

        if args[index][1] in dict[args[index]]:
            break
        if args[index][0] == 'Pizza' and not len(dict['Pizza']) == 4:
            dict[args[index][0]].append(args[index][1])

        elif args[index][0] == 'Soup' and not len(dict["Soup"]) == 3:
            dict[args[index][0]].append(args[index][1])
        elif args[index][0] == 'Dessert' and not len(dict["Dessert"]) == 2:
            dict[args[index][0]].append(args[index][1])
    if not dict.values():

        print("No products in the cart!")
    sorted_dict = sorted(dict.items(), key=lambda x: (-len(x[1]), x[0]))


    for tuple_ in sorted_dict:
        result += f"{tuple_[0]}:\n"
        sorted_product = sorted(tuple_[1])
        for product in sorted_product:
            result += f" - {product}\n"

    return result

print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))
