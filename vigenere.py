#Sam Ferguson - CSCI220
#vigenere.py
#purpose: make interface that runs a vigenere cypher
#inputs: message and key
#output: encoded message
#statement of authenticity: The code in this file is my work only



#import things I'll need
from graphics import *


#define code function with asked for parameters
def code(message, keyword):

    #assigns variable to ASCII A
    letterA = ord("A")


    #get message length and key length for mod arithmetic
    messageLength = len(message)
    encryptionKeyLength = len(keyword)

    #turn message into a list
    message = list(message)

    #loop that gives the 0-25 value of each letter in string
    listCharVal = []
    for i in range(messageLength):
        charVal = ord(message[i])-letterA
        listCharVal += [charVal]
    #it outputs it into a list for convenience
    #same thing for the keyword
    keyword = list(keyword)
    listKeyVal = []
    for i in range(encryptionKeyLength):
        keyVal =ord(keyword[i])-letterA
        listKeyVal += [keyVal]
    

    #loop takes the key value and message value
    #and adds them together
    #it mods the encryption key value list by the length
    #to cycle the list index, making the cypher work
    #then it mods by 26 to keep the value on the ASCII alphabet
    #then it adds up the values of the list
    #of encrypted values into a new value list
    encryptedValList = []
    for i in range(messageLength):
        newVal = ((listCharVal[i]+listKeyVal[i%encryptionKeyLength])%26)
        encryptedValList += [newVal]

    #loop to turn the encrypted values back into ASCII
    #and then into a string
    encryptedMessage = ""
    for i in range(len(encryptedValList)):
        encryptedMessage += chr(encryptedValList[i]+letterA)
    
    
    #returns the encrypted message to main
    return encryptedMessage



    
    
    
def main():
#set up the window
    winWidth = 450
    winHeight = 300
    win = GraphWin("Vigenere", winWidth, winHeight)

    #prompt for message and key
    messagePrompt = Text(Point(100,50), "Message to be encoded:")
    messagePrompt.setSize(12)
    messagePrompt.draw(win)

    keyword = Text(Point(65,100), "Enter keyword:")
    keyword.setSize(12)
    keyword.draw(win)

    #allow for entry
    messageEntry = Entry(Point(300,50), 20)
    messageEntry.draw(win)

    encodingEntry = Entry(Point(254,100),10)
    encodingEntry.draw(win)

    #creates an encode "button"
    rectangle = Rectangle(Point(180,140), Point(270,180))
    rectangle.draw(win)

    wordInRectangle = Text(Point(225, 160), "Encode")
    wordInRectangle.draw(win)

    #when they click it undraws
    win.getMouse()
    rectangle.undraw()
    wordInRectangle.undraw()

    #this code gets the entry and delimits on space and capitalizes
    inputMessageStr = messageEntry.getText()
    cappedInputMessage= inputMessageStr.upper()
    spacedCappedMessage= cappedInputMessage.split(" ")

     #this code does the same but rather with key
    encryptionKey = encodingEntry.getText()
    encryptionKey = encryptionKey.upper()
    encryptionKey = encryptionKey.split(" ")

    #this loop turns key back into a string without any input spaces
    encryptionKeyFin = ""
    for i in range(len(encryptionKey)):
        encryptionKeyFin += encryptionKey[i]

    #same as the previous loop but with message not key    
    messageFinal = ""
    for i in range(len(spacedCappedMessage)):
        messageFinal += spacedCappedMessage[i]
    
    #okay now we have the message and the key
    #time to call code()
    code(messageFinal, encryptionKeyFin)
    
    #display the output of the encoded message
    returnMessage = Text(Point(225,180), "Your encoded message is")
    returnMessage.setSize(12)
    returnMessage.draw(win)
    
    displayEncryption = Text(Point(225,225), code(messageFinal, encryptionKeyFin))
    displayEncryption.setSize(12)
    displayEncryption.draw(win)
    
    #create a text box in the program
    #I'm not a fan of click anywhere to close thus is didn't put it
    

main()


