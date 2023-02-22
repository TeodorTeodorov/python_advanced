matrix = []


white = {
    'up': (-1, 0),
    'take_right': (-1, 1),
    'take_left': (-1. -1)

}
black = {
    'up': (1, 0),
    'take_right': (1, -1),
    'take_left': (1, 1)
}

r_b= ''
c_b=''
r_w= ''
c_w=''

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

for row in range(8):
    b_index = ''
    w_index =''
    r = input().split()
    matrix.append(r)
    for letter in r:
        if letter == 'b':
            b_index = [row, r.index(letter)]
            r_b, c_b = b_index[0], b_index[1]
        if letter == 'w':
            w_index = [row, r.index(letter)]
            r_w, c_w = w_index[0], w_index[1]

win = False
while not win:

    r_w_take_left, c_w_take_left = r_w - 1 , c_w - 1
    r_w_take_right, c_w_take_right = r_w - 1 , c_w + 1
    if matrix[r_w_take_left][c_w_take_left] == 'b':
        print(f"Game over! White win, capture on square.")
        break
    elif matrix[r_w_take_right][c_w_take_right] == 'b':
        print(f"Game over! White win, capture on square.")
        break
    r_b_take_right, c_b_take_right = r_b + 1 , c_b - 1
    r_b_take_left, c_b_take_left = r_b + 1, c_b + 1
    if matrix[r_b_take_right][c_b_take_right] == 'w':
        print(f"Game over! Black win, capture on square.")
        break
    elif matrix[r_b_take_left][c_b_take_left] == 'w':
        print(f"Game over! Black win, capture on square.")
        break

    r_w, c_w = r_w - 1, c_w
    r_b, c_b = r_b + 1, c_b
    if r_w == 0:
        for letter in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
            if c_w == letters.index(letter):
                square = f"{str(letter)}{str(r_w)}"
                print(f"Game over! White pawn is promoted to a queen at {square}.")
                break

        break
    if r_b == 8:
        print(f"Game over! Black pawn is promoted to a queen at square.")
        break



