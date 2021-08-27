import string

def AtbashEncrypt(OriginStr):
    newStr = ""
    for char in OriginStr:
        if char.islower():
            newStr += chr(abs((ord(char) - 96) - 27) + 96)
        elif char.isupper():
            newStr += chr(abs((ord(char) - 65) - 25) + 65)
        else:
            newStr += char
    return newStr

OriginStr = "hello"
print(AtbashEncrypt(OriginStr))
