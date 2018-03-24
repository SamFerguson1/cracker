##def poopFart():
##
##    line = "Bradley Odac,75, 13, 22;Bryan James, 19,22,57,35;Patrick McCabe,35,80"
##
##    perPerson = line.split(";")
##
##    for personData in perPerson:
##        personList = personData.split(",")
##
##        fullName = personList[0]
##
##        values = personList[1:]
##
##        total = 0
##        for num in values:
##            total += eval(num)
##        avg = total/len(values)
##
##        name = fullName.split()
##        firstName = name[0]
##        lastName = name[1]
##
##        print(lastName + ", " + firstName +": " +str(avg))
##
##
##    
##    
##
###poopFart()
##
def fartPoop():

    shift = 3 #the amoun shifted
    message = "ASS" #any message needed to print
    newMessage = "" #empty string

    for character in message: #loop for each character in the message
        newCharacter = ord(character)-65 #for each time in the loop subtract 65 to find alphabet val
        newCharacter = (newCharacter + shift)%26 #mod by 26 to get remainder
        newCharacter+=65 #add by 65 to get back to ASCII value
        newMessage = newMessage + chr(newCharacter) #add 

    print(newMessage)

fartPoop()
