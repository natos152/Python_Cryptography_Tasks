import math


def route_encrypt(original_str, key, clock_direction):
    # Remove spaces from the string
    original_str = original_str.replace(" ", "")

    # Check length to set number of rows and missing chars
    rows = int(math.ceil(len(original_str) / key))

    # Adding 'X' for  missing chars
    missing_letters = (key * rows) - len(original_str)
    if missing_letters > 0:
        for i in range(missing_letters):
            original_str = original_str + 'X'

    # Create a table for insert letters
    table = [[""] * key for i in range(rows)]

    # Filling The Table With Text
    index = 0
    for i in range(rows):
        for j in range(key):
            table[i][j] = original_str[index]
            index += 1
    print(table)
    # Start Encryption
    # Initialize default parameters for the route indexes
    current_row = -1
    current_col = key - 1
    # start direction (can be "down", "up", "left", "right")
    direction = "down"
    encrypted_text = ""

    # Borders will define the index for leading the direction correctly
    down_border = rows - 1
    left_border = 0
    up_border = 0
    right_border = key - 1
    indexes_amount = key * rows

    # From top-right corner clockwise to the center
    if clock_direction:
        for j in range(indexes_amount):

            # Go Down, than go left
            if direction == "down":
                current_row += 1  # If the direction is down, add 1 to row index
                # Breaking expression,
                # set a border that stands for max index
                # go downwards and checking if we got there.
                if current_row == down_border:
                    direction = "left"  # if we got here it means we need to shift direction because we hit the border.
                    right_border -= 1  # Finished going down we need to "close" the line

                encrypted_text += table[current_row][current_col]

            # Go left, than go up
            elif direction == "left":
                current_col -= 1
                if current_col == left_border:
                    direction = "up"
                    down_border -= 1

                encrypted_text += table[current_row][current_col]

            # Go up, than go right
            elif direction == "up":
                current_row -= 1
                if current_row == up_border:
                    direction = "right"
                    left_border += 1

                encrypted_text += table[current_row][current_col]

            # Go right,than go down again
            elif direction == "right":
                current_col += 1
                if current_col == right_border:
                    direction = "down"
                    up_border += 1

                encrypted_text += table[current_row][current_col]

        return encrypted_text

    # From top-right corner anticlockwise to the center from the table.
    else:
        direction = "left"
        current_row = 0
        current_col = key
        for j in range(indexes_amount):

            # Go left, than go down
            if direction == "left":
                current_col -= 1
                if current_col == left_border:
                    direction = "down"
                    up_border += 1
                encrypted_text += table[current_row][current_col]

            # Go down, than go right
            elif direction == "down":
                current_row += 1
                if current_row == down_border:
                    direction = "right"
                    left_border += 1
                encrypted_text += table[current_row][current_col]

            # Go right, than go up
            elif direction == "right":
                current_col += 1
                if current_col == right_border:
                    direction = "up"
                    down_border -= 1
                encrypted_text += table[current_row][current_col]

            # Go up and than go left
            elif direction == "up":
                current_row -= 1
                if current_row == up_border:
                    direction = "left"
                    right_border -= 1
                encrypted_text += table[current_row][current_col]

    return encrypted_text


def route_decrypt(encrypted_text, key, clockwise):
    # The only thing that is different here from the encryption is
    # that we are building the table as we go through each index that
    # the route takes us and filling in with the encrypted text.

    # Building and Filling The Table
    rows = int(math.ceil(len(encrypted_text) / key))
    table = [[""] * key for i in range(rows)]
    # Start decrypt
    # Initialize default parameters for the route indexes
    current_row = -1
    current_col = key - 1
    direction = "down"
    decrypted_text = ""
    down_border = rows - 1
    left_border = 0
    up_border = 0
    right_border = key - 1
    indexes_amount = key * rows

    # From top-right corner clockwise to the center
    if clockwise:
        for j in range(indexes_amount):
            if direction == "down":
                current_row += 1
                if current_row == down_border:
                    direction = "left"
                    right_border -= 1
                table[current_row][current_col] = encrypted_text[j]

            elif direction == "left":
                current_col -= 1
                if current_col == left_border:
                    direction = "up"
                    down_border -= 1
                table[current_row][current_col] = encrypted_text[j]

            elif direction == "up":
                current_row -= 1
                if current_row == up_border:
                    direction = "right"
                    left_border += 1
                table[current_row][current_col] = encrypted_text[j]

            elif direction == "right":
                current_col += 1
                if current_col == right_border:
                    direction = "down"
                    up_border += 1
                table[current_row][current_col] = encrypted_text[j]

        # Done filling the table
        # Add each character to a string
        for line in table:
            for char in line:
                decrypted_text += char
        # Remove X from the return text
        decrypted_result = decrypted_text.strip("X")
        return decrypted_result

    # From top-right corner anticlockwise to the center from the table.
    else:
        direction = "left"
        current_row = 0
        current_col = key
        for j in range(indexes_amount):
            if direction == "left":
                current_col -= 1
                if current_col == left_border:
                    direction = "down"
                    up_border += 1
                table[current_row][current_col] = encrypted_text[j]

            elif direction == "down":
                current_row += 1
                if current_row == down_border:
                    direction = "right"
                    left_border += 1
                table[current_row][current_col] = encrypted_text[j]

            elif direction == "right":
                current_col += 1
                if current_col == right_border:
                    direction = "up"
                    down_border -= 1
                table[current_row][current_col] = encrypted_text[j]

            elif direction == "up":
                current_row -= 1
                if current_row == up_border:
                    direction = "left"
                    right_border -= 1
                table[current_row][current_col] = encrypted_text[j]

        for line in table:
            for char in line:
                decrypted_text += char

        # Remove X from the return text
        decrypted_result = decrypted_text.strip("X")

        return decrypted_result


text = input("Enter text to encrypt: ")
key_size = int(input("Choose key between 3-9: "))
clock = bool(input("Type True for clockwise or False for anticlockwise for direction clock: "))

encrypted_message = route_encrypt(text, key_size, clock)
print("The encrypt message: " + encrypted_message)

original_text = route_decrypt(encrypted_message, key_size, clock)
print("The original message: " + original_text)
