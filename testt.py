def vig():


    message = "THRSNNEGYRTHNRSSNTHPLNT"
    #expected = "OYQCMHKSVCM"
    key = "R" 
    #newEncryption = ""
    keyLength = len(key)
    messageLength = len(message)

    message =  list(message)
    print(message)
    listCharVal =[]
    for i in range(len(message)):
        charVal = ord(message[i])-65
        #print(message[i], charVal)
        listCharVal += [charVal]
    print(listCharVal)
    #now we have all the character values of the message
    key = list(key)
    listKeyVal = []
    for i in range(len(key)):
        keyVal = ord(key[i])-65
        listKeyVal += [keyVal]
    print(listKeyVal)

    encryptedValList = []
    for i in range(messageLength):
        newVal = ((listCharVal[i]+listKeyVal[i%keyLength])%26)
        print(newVal)
        encryptedValList += [newVal]
    print(encryptedValList)

    encryptedMessage= ""
    for i in range(len(encryptedValList)):
        encryptedMessage += chr(encryptedValList[i]+65)
    print(encryptedMessage)
    
##
##    for i in range(messageLength):
##        charvalue = message[i]+
##        






vig()
