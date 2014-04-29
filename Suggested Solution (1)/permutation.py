from formatInput import formatInput
from fileHandler import fileReader
from fileHandler import fileWriter

def main():
    myMessage = list("")                
    fileReader("input.txt", myMessage)  #read the message from file
    permutation = [2,4,1,3,5]           #permutation
    myKey = len(permutation)            #key length    
    formatInput(myMessage, 1, 1, myKey) #padding needed, CHANGE
                                        #second argument to 0 to skip spaces in output cipher(Part-2)
    permutationCipher(myKey, permutation, myMessage) #encrypt the message    

def permutationCipher(key, permutation, message):
    startIndex = 0;                         #pointer to character of "message" to be scanned next
    while message[startIndex] != '&':       # & : End of "message" marker   
        temp1 = []                          #temporary file to store a block of oriinal "message" of length "key" 
        temp2 = []                          #temporary file to store permutation of the msg in temp1
        space = []                          #stores indices of spaces within a block
        while len(temp1) < key:             #scanning the msg blockwise
            if message[startIndex] == ' ':  #if scanned symbol is a space keep track of the index
                space.append(len(temp1))
            else:
                temp1.append(message[startIndex])   #enter the scanned character to temp1
            startIndex = startIndex + 1

        for index in range(key):
            temp2.insert(permutation[index] - 1,temp1[index])   #permute the characters in temp1 and store in temp2

        fileWriter("output.txt", temp2, key, space)
    print("ciphertext written to output.txt")        
    
if __name__ == '__main__':
     main()
