import random


# Encryption string
def oneTimePadEnc(string):
    keyStr = []
    # build key array to encrypt text
    for i in string:
        rand_num = random.randint(0, 255)
        keyStr.append(rand_num)

    # Mix key array with the text
    encryptSTR = ""
    for i in range(len(string)):
        encryptSTR += (chr(keyStr[i] ^ ord(string[i])))
    return encryptSTR, keyStr


text = input("Insert text to encrypt\n")
print(oneTimePadEnc(text))


# Decrypt encryption str and key
def oneTimePadDec(enc, myKey):
    decryptSTR = ""
    for i in range(len(enc)):
        decryptSTR += chr((myKey[i] ^ ord(enc[i])))
    return decryptSTR


encrypt, key = oneTimePadEnc(text)
print(oneTimePadDec(encrypt, key))


# Decrypt encryption str from file
def DecryptFromFile():
    encrypt_string = ""
    with open("text.txt", "r", encoding='UTF-8') as dec_text:
        encoding_txt = dec_text.read()

    with open("key.txt", "r") as keys:
        string_keys = keys.read()
        list_keys = string_keys.split(",")

    for i in range(len(encoding_txt)):
        ascii = ord(encoding_txt[i])
        encrypt_string += chr(ascii ^ (int(list_keys[i])))
    return encrypt_string


print(DecryptFromFile())
