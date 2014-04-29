##def main():
##    message = list("")
##    fileReader("input.txt", message)
##    print(message)

def fileReader(fileName, message):
    f = open(fileName,'r')
    data = f.read()
    index = 0
    while index < len(data):
        message.append(data[index])
        index = index + 1
    return f        

def fileWriter(fileName, cipher, key, space):
    f = open(fileName,'a')    
    index2 = 0                          #points to space list
    index = 0
    while index < key:            
        if index2 < len(space):         #if all the spaces are printed or not
            if index == space[index2]:  #if it's the index of a space print one space
                f.write(" ")
                index2 = index2 + 1
        f.write(cipher[index])             #print permuted character
        index = index + 1
    
if __name__ == '__main__':
    main()
                           
        
