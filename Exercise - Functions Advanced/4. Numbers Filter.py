def even_odd_filter(**kwargs):
    if 'odd' in kwargs:
        kwargs['odd'] = [n for n in kwargs['odd'] if int(n) % 2 != 0]

    if 'even' in kwargs:
        kwargs['even'] = [n for n in kwargs['even'] if int(n) % 2 == 0]
        # kwargs['even'] = filter(lambda x: x % 2 == 0, kwargs['even'])
    return kwargs


print(even_odd_filter(

    odd=[1, 2, 3, 4, 10, 5],

    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],

))
