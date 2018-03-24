## Sam Ferguson
## lab3.py

#Calculates the power of some base raised to some exponent.
#inputs number and raised to what power
#output power of that number
def power():
    print("Calculates the power of some base raised to some exponent.")
    
    numBase = eval(input("What is the base number?:" ))
    numPower = eval(input("What are you raising the number to?:" ))
    total = 1
    for i in range (numPower):

        total=  numBase * total

    print(numBase, "^ ", numPower, "=", total)
        
#inputs number of grades
#outputs ask for each grade and output average
def average():

    numGrades = eval(input("How many grades to input?: "))

    total = 0
    for i in range(1, numGrades+1):
        numOfGrade =  eval(input("Enter your grade on HW" +str(i) + ":"))

        total = numOfGrade + total
    averageHW = total/numGrades
    print("Your homework average is:", averageHW)

def multiplicationTable():

    print ("    1  2   3   4   5   6   7   8   9   10")
    for i in range(1,11):
       
        print(i,": ", end = "")
        for j in range(1,11):
            print(i*j, end = " ")
        
        print()


def newton():
    import math
    #inputs what number x is and how many times to improve the appriximation
    x = eval(input("What is the number you want to take root of?:" ))
    guess = eval(input("How many approximations do you want to make?: "))

    total = 1
    for i in range(guess):

        guess = (guess + x/guess)/2
        realRoot = math.sqrt(x)
    print("the appoximate root is:", guess)
    print("the real root is:", realRoot)



#inputs: number of terms in a series
#outputs: following patter for the appropriate number of terms
    
def sequence():

    numValues = eval(input("How many terms in the series?: "))
    for i in range(1,numValues):
        print(i+1-i%2, end ="")    

            
            
    
def main():
    power()
    #average()
    #multiplicationTable()
    #newton()
    #sequence()

main()
