# Lab6.py 
# Name 1:
# Name 2: 
from graphics import*
def processString():
    #input: a string

    string = str(input("gimme a string: "))
    print("The first character in the string is: ", string[0])
    print("The last character in the string is: ", string[-1])
    print("The characters in positions 2-5 are: ",string[1:5])
    stringFirstLast = string[0]+string[-1]
    print("the concatenation of the first and last character of the string are: ", stringFirstLast) 
    firstThree = string[0:3]*10
    print("The firs tthree characters ten times is: ", firstThree)
    for character in string:
        print(character)
    print("The length of the string is: ", len(string))

def processList():
    pt = Point(5,10)
    values = [5, 'hi', 2.5,'there', pt,'7.2']
    x = values[1]+values[3]
    print(x)
    x= float(values[0])+float(values[2])
    print(x)
    x = values[1]*5
    print(x)
    x = values[2:5]
    print(x)
    x = values[2:4]+[values[0]]
    print(x)
    x = [values[2]]+[values[0]]+[float(values[5])]
    print(x)
    x = float(values[0])+float(values[2])+float(values[5])
    print(x)
    x = len(values)
    print(x)

def nameReverse():
    name = input("Gimme your gosh darn name: ")
    nameList = name.split(" ")
    firstName = nameList[0]
    firstNameTitle = firstName.title()
    lastName = nameList[-1]
    lastNameTitle = lastName.title()
    print(lastNameTitle +", " + firstNameTitle +".")

def companyName():
    domain = input('Enter a domain name:')
    domain = domain.split('.')
    print("Your domain name is: "+domain[1]+'.')

def initials():
    numStudents = eval(input("how many students to enter: "))

    print("now enter the first and last names of each student")
    for i in range(1,numStudents+1):
        nameStudent = input("what is student "+ str(i) + "'s first name?")
        lastName = input("What is " + nameStudent +"'s last name?")
        initialsReal = nameStudent[0]+ lastName[0]
        initialsReal = initialsReal.upper()
        initials = print(nameStudent+ "'s dumb initials are:"+ initialsReal)

def names():
    name = input("give me all of your names first and last, comma seperated: ")
    name = name.title()
    name = name.split(", ")
    
    for i in range(len(name)):
        fullName = name[i]
        fullName = fullName.split(' ')
        firstName = fullName[0]
        lastName = fullName[-1]
        
        initials = firstName[0]+ lastName[0]
        print(initials)

def encode():
    message = input("give me a messag eto encode give me only one word: ")
    shift = eval(input("how much do you wanna shift that by?:"))
    message = message.upper()
    encodedMessage = ""
    for character in message:
        newCharacter = ord(character)-65
        newCharacter = ((newCharacter +shift)%26)+65
        newCharacter = chr(newCharacter)
        encodedMessage += newCharacter
    print(encodedMessage)
        
    
    
        

def main():
    #processString()
    #processList()
    #nameReverse()
    #companyName()
    #initials()
    names()
    #encode()
main()
