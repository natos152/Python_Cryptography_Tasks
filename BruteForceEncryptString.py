import _string


def BruteForceEncryptText(originSt):
    newStr = ""
    key = 1
    for key in range(key, 27):
        for letter in originSt:
            if letter.islower():
                save = ((ord(letter) + key - 97) % 26 + 97)
                newStr += chr(save)
            if letter.isupper():
                save = ((ord(letter) + key - 65) % 26 + 65)
                newStr += chr(save)
            if letter.isdigit():
                newStr += letter
            if not letter.islower() and not letter.isupper() and not letter.isdigit():
                newStr += letter
        print(newStr + '\n')
        newStr = ''
        key += 1


# originSt = input("Enter a string to decrypt:")

with open("text_to_decrypt.txt", "r") as dec_text:
    encoding_txt = dec_text.read()
BruteForceEncryptText(encoding_txt)
