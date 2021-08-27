import _string


def newString(originSt, key, flag):
    newStr = ""
    if 1 <= key <= 25:
        # Encrypt str if flag is True
        if flag:
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
            return print(newStr)
        # Decrypt str if flag is False
        else:
            for letter in originSt:
                if letter.islower():
                    save = ((ord(letter) - key - 97) % 26 + 97)
                    newStr += chr(save)
                if letter.isupper():
                    save = ((ord(letter) - key - 65) % 26 + 65)
                    newStr += chr(save)
                if letter.isdigit():
                    newStr += letter
                if not letter.islower() and not letter.isupper() and not letter.isdigit():
                    newStr += letter
            return print(newStr)
    else:
        return print(originSt)


print("Enter a string:")
originSt = input()

print("Choose and write e = encrypt or d = Decrypt")
flag = input()
if "e":
    flag = True
if "d":
    flag = False

print("Enter a key between 1 to 25 to Encrypt or Decrypt:")
key = int(input())
if key < 0:
    print("error key")
    print(originSt)
else:
    newString(originSt, key, flag)
