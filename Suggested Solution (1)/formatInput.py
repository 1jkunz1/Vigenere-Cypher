import random

MINSMALL = 97       #ASCII of 'a'
MAXSMALL = 122      #ASCII of 'z'
MINCAP = 65         #ASCII of 'A'
MAXCAP = 90         #ASCII of 'Z'

def formatInput(message, withSpace, padding, keyLength):     #format the input message
    index = 0
    count = 0               #stores the count of the alphabets in message
    while index < len(message):     #scan the message one symbol at a time
        if ord(message[index]) <= MAXSMALL and ord(message[index]) >= MINSMALL:     #if current symbol is in small letter
            count = count + 1
            index = index + 1
        elif withSpace == 1 and message[index] == " ":      #if space should be kept withSpace is 1, else 0
            index = index + 1
        elif ord(message[index]) <= MAXCAP and ord(message[index]) >= MINCAP:       #if current symbol is in caps change it to small
            message.insert(index, chr(ord(message[index])+ (MINSMALL-MINCAP)))
            message.pop(index+1)
            count = count + 1
            index = index + 1
        else:                       #if any punctuation symbol
            message.pop(index)
            
    index = 0
##    print(count)
    if padding == 1 and count % keyLength != 0:         #padding = 1 if padding needed, else ignore
        while index < (keyLength - count % keyLength):
            message.append(chr(random.randint(0,25) + MINSMALL))
            index = index + 1
        
    message.append('&')     #append end-marker
    

if __name__ == '__main__':
    main()
                           
        
