from formatInput import formatInput
from fileHandler import fileReader
from fileHandler import fileWriter

def main():
    myMessage = list("")
    fileReader("input.txt", myMessage)    #read the message from file
    myKey = list("bigdata")                   #keyword
    formatInput(myMessage, 1, 1, len(myKey))    #padding needed, CHANGE
                                                #second argument to 0 to skip spaces in output cipher(Part-2)
    changeKeytoNumber(myKey, myMessage)
    vigenereCipher(myKey, myMessage) #encrypt the message

def changeKeytoNumber(key, message):        #changes character key to alphabetical numbers(0-25) for simplicity of calculation
    index = 0
    while index < len(key):
        key.insert(index,ord(key[index]) - 97)  #97 ASCII of 'a'
        index = index + 1
        key.pop(index)

def vigenereCipher(key, message):           #encrypt "message" using Vigenere Cipher
    startIndex = 0;                         #pointer to character of "message" to be scanned next
    while message[startIndex] != '&':       # & : End of "message" marker   
        temp1 = []                          #temporary file to store a block of oriinal "message" of length "key" 
        temp2 = []                          #temporary file to store ciphertext of the msg in temp1
        space = []                          #stores indices of spaces within a block
        while len(temp1) < len(key):             #scanning the msg blockwise
            if message[startIndex] == ' ':  #if scanned symbol is a space keep track of the index
                space.append(len(temp1))
            else:
                temp1.append(message[startIndex])   #enter the scanned character to temp1
            startIndex = startIndex + 1

        index = 0        
        while index < len(key):
            temp2.insert(index, chr(((ord(temp1[index])-97) + key[index])%26 + 97))   #encrypt the characters in temp1 using "key" and store in temp2
            index = index + 1
            
        fileWriter("output.txt", temp2, len(key), space)
    print("ciphertext written to output.txt")
    
if __name__ == '__main__':
     main()
