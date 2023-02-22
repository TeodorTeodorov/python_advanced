def shopping_list(budget, **kwargs):
    basket = {}
    if int(budget) < 100:
        return "You do not have enough budget."
    else:

        for k, v in kwargs.items():
            v_list = [float(x) for x in v]
            sum_item = v_list[0]*v_list[1]
            if budget >= sum_item:
                basket[k] = []
                basket[k].append(f"{sum_item:.2f}")
                budget -= sum_item
                if len(basket.keys()) > 4:
                    break
    result = []
    for k, v in basket.items():

        result.append(f"You bought {k} for {''.join(v)} leva.")
    return '\n'.join(x for x in result)






print(shopping_list(20,
                    jeans=(19.99, 1),
                    ))
