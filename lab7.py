# Lab7.py
# Name 1: Sam Ferguson
# Name 2: Adam Robertson



#main() should be the only file executed when you are checked off for this lab
#thus add code to main() to call any functions you write.

    

def encodeBetter():
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

    
def numberWords():
    file = open("rawWords.txt","r")

    fileWords =""
    for line in file:
        fileWords+= line
    

    fileWords = fileWords.split("\n")
    
    fileWordsTwo = ""
    for i in range( len(fileWords)):
        fileWordsTwo += fileWords[i] + " "

    
    fileWords = fileWordsTwo.split(" ")

    for i in range(1, len(fileWords)):

        print((i) , ". " , fileWords[i-1])


def hourlyWages():

    file = open("hourlyWages.txt","r")
    

    fileWords =""
    for line in file:
        fileWords+= line
    

    fileWords = fileWords.split("\n")
    
    fileWordsTwo = ""
    for i in range( len(fileWords)):
        fileWordsTwo += fileWords[i] + " "

    
    fileWords = fileWordsTwo.split(" ")
   # print(fileWords)

    wageVal =[]
    for i in range(len(fileWords)//4):
        wageVal.append(fileWords[((i+1)*4)-2])

    #print(wageVal)


    wageValTwo = []
    for i in range(len(wageVal)):
        wageValRaised = float(wageVal[i])+1.65
        wageValTwo.append(wageValRaised)

    #print(wageValTwo)

    hours = []
    for i in range(len(fileWords)//4):
        hours.append(fileWords[((i*4)+3)])
    #print(hours)

    weeklyWage= []
    for i in range(len(hours)):
        thing = wageValTwo[i] * eval(hours[i])
        thing = round(thing,1)
        thing = str(thing)
        weeklyWage.append(thing)

    #print(weeklyWage)

    
    wageValFixed = []
    for i in range(len(wageVal)):
        wageValFixed.append("${0:.2f}".format(float(weeklyWage[i])))

    #print(wageValFixed)

    firstName = []
    for i in range(len(fileWords)//4):
        firstName.append(fileWords[(i*4)])
    #print(firstName)

    lastName = []
    for i in range(len(fileWords)//4):
        lastName.append(fileWords[((i*4)+1)])
    #print(lastName)

    for i in range(len(fileWords)//4):
        print(firstName[i]+ " "+ lastName[i] + " " +str(wageValFixed[i]), ".")
        
    
def thirds():

    sentence = input("what's the thing you want us to output; ")
    

    for i in range(len(sentence)//3):
        print(sentence[((i+1)*3)-1], end = "")
    
    
def wordCount():

    sentence = input("what's the thing you want us to output; ")
    sentence = sentence.split(" ")

    print("There are ", len(sentence), "words.")
    
def characterCount():
    
    sentence = input("what's the thing you want us to output; ")

    print(len(sentence),"characters in setence.")

def wordAverage():

    
    numStrings = eval(input("how many strings to process:"))
    total = 0
    for i in range (numStrings):
        sentence = input("what's the thing you want us to output;")
        sentence = sentence.split(" ")
        for j in range(len(sentence)):
            total+= len(sentence[j])
            #print(total)
        
        average = total/(len(sentence))
        total = 0
        print(average)
    

def formatPractice():

    print("It's raining {1} and {0}.".format("dogs", "cats"))
    print("{0:.2f} {1:6.3f} ".format(2.3, .4567))
    print("{0:0>2}:{1:0>5.2f}".format(3,7.4589))
    print(("{0} {1}: {2:.2f}".format("Steph", "Curry", 43.75432)))
def main():


    #hourlyWages()
    #thirds() 
    #numberWords()
    #wordCount()
    #characterCount()
    #encodeBetter()
    #wordAverage()
    formatPractice()        

    
main()

    
