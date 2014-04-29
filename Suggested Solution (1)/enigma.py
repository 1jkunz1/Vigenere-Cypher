import random
from formatInput import formatInput
from fileHandler import fileReader
from fileHandler import fileWriter
MINSMALL = 97

def main():
    myMessage = list("")
    fileReader("input.txt", myMessage)          #read the message from file
    formatInput(myMessage, 1, 0, 0)             #format the message, no need of padding, CHANGE
                                                #second argument to 0 to skip spaces in output cipher(Part-2)
    rotor = list("thequickbrownfxjmpsvlazydg")          #rotor
    enigmaCipher(rotor, myMessage)
    
def enigmaCipher(rotor, message):    
    index = 0;                         #pointer to character of "message" to be scanned next
    while message[index] != '&':       # & : End of "message" marker           
        if message[index] == " ":       #if there is a space in message print it 
            fileWriter("output.txt", " ", 1, [])
            index = index + 1
            continue

        opRotor = rotor[ord(message[index])-MINSMALL]       #apply rotor to the current "message" symbol
        fileWriter("output.txt", [opRotor], 1, [])
        fChar = rotor.pop(0)                #perform rotation by first deleting the first character of rotor
        rotor.append(fChar)                 #and then appending it to the last
        index = index + 1
    print("ciphertext written to output.txt")                
    
if __name__ == '__main__':
     main()
