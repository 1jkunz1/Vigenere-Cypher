###Vigenere Encryption by Joseph Kunzler###

Alphabet = 26
Start = 97
End = 122


def getKey():
    key = input("Please enter a key: ")
    return key.lower()

def getPlaintext():
    plaintext = input("Enter Text: ")
    return plaintext.replace(' ','')
       

def Encrypt(key, plaintext):
    cipher = ''
    for n in range(0, len(plaintext), 1):
        if plaintext[n].islower():
            lower = ord(plaintext[n]) + ord(key[n%len(key)]) - Start
            if (lower> End) or (lower < Start):
                lower -= Alphabet
            cipher += chr(lower)
        else:
            else_new = plaintext[n]
            cipher += else_new
    return cipher



def display(cipher):
    print("Encrypted Text: ", cipher)



def main():
    key = getKey()
    plaintext = getPlaintext()
    cipher = Encrypt(key,plaintext)
    display(cipher)

main()
