def encode_rail_fence_cipher(txt, n):
    flag = 0
    row = 0
    ciphertext = ''
    enc = [[" " for i in range(len(txt))] for j in range(n)]
    print(enc)
    for i in range(len(txt)):
        enc[row][i] = txt[i]
        if row == 0:
            flag = 0
        elif row == n - 1:
            flag = 1
        if flag == 0:
            row += 1
        else:
            row -= 1
    for i in range(n):
        print(" ".join(enc[i]))
    ct = []
    for i in range(n):
        for j in range(len(txt)):
            if enc[i][j] != ' ':
                ct.append(enc[i][j])
            elif enc[i][j] == ' ':
                ct.append((enc[i][j]))
    ciphertext = "".join(ct)
    return ciphertext


def decode_rail_fence_cipher(cipher, key):
    rail = [['\n' for i in range(len(cipher))]
            for j in range(key)]
    print(rail)
    # find the direction
    dir_down = None
    row, col = 0, 0

    # mark the places with '*'
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False

        # place the marker
        rail[row][col] = '*'
        col += 1

        # find the next row
        # using direction flag
        if dir_down:
            row += 1
        else:
            row -= 1
    print(rail)
    # construct the fill the rail matrix
    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if ((rail[i][j] == '*') and
                    (index < len(cipher))):
                rail[i][j] = cipher[index]
                index += 1

    # read the matrix in zig-zag manner to construct the resultant text
    result = []
    row, col = 0, 0
    for i in range(len(cipher)):
        # check the direction of flow
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False
        # place the marker
        if rail[row][col] != '*':
            result.append(rail[row][col])
            col += 1
        # find the next row using
        # direction flag
        if dir_down:
            row += 1
        else:
            row -= 1
    return "".join(result)


text_to_cipher = input(str('Insert a text to cipher: '))

key = int(input('Enter a key to cipher: '))

print(encode_rail_fence_cipher(text_to_cipher, key))

ciphertxt = input(str('Insert a text to cipher: '))
dec_key = int(input('Enter a key to cipher: '))
print(decode_rail_fence_cipher(ciphertxt, dec_key))
