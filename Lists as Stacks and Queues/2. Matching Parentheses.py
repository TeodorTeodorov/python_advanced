string = input()
stack = []
for index in range(len(string)):
    if string[index] == '(':
        stack.append(index)
        start_index = string[index]
    elif string[index] == ')':
        last_index = stack.pop()
        print(string[last_index: index + 1])
