from functools import reduce

string = input().split()

index = 0

functions = {
    #reduce  взима всички от стринг дo i , и lambda връща a*b, резултата отива в началото на string
    # когато остане един елемент reduce връща само него
    '*': lambda i: reduce(lambda a,b: int(a) * int(b), string[:i]),
    '/': lambda i: reduce(lambda a,b: int(a) / int(b), string[:i]),
    '+': lambda i: reduce(lambda a,b: int(a) + int(b), string[:i]),
    '-': lambda i: reduce(lambda a,b: int(a) - int(b), string[:i])
}



while index < len(string):
    element = string[index]

    if element in '*/+-':
        # element  е символа *,-,+... index отива на i при lambda
        result = functions[element](index)
        [string.pop(1) for i in range(index)]
        string[0] = result
        index = 0
    index += 1

print(int(string[0]))