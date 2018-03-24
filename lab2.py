
## lab2.py
## Purpose: Solves problems assigned in Lab 2
## Name: Sam 

# This is a sample function to show how to "comment out" function calls
def helloWorld():
    print("Hello, world!")

# This function calculates the volume of a rectangular solid
def calcVolume():
    print("This function calculates the volume of a rectangular solid.")

    length = eval(input("What is the length of the rectanglular solid?: "))
    width = eval(input("What is the width of the rectanglular solid?: "))
    height = eval(input("What is the height of the rectanglular solid?: "))

    volume = length * width * height

    print("Okay the volume of your rectangular solid is", volume, "Units cubed")

def shootingPercentage():

    #inputs: total shots and shots made
    #output: shooting percentage = shots made / shots total
    print("This function calculates your shooting percentage")

    shotsMade = eval(input("How many shots did you make?: "))
    shotsAttempted = eval(input("How many shots did you attempt?: "))

    shootPercent = (shotsMade/shotsAttempted)*100
    print("You made", shootPercent, "% of the shots that you took!")

def coffee():

    #inputs: pounds of coffee
    #outputs: total cost = 10.50*Pounds + .86 *pounds +1.50

    print("This program computes the cost of shipping a coffee order")

    poundsCoffee = eval(input("How many pounds of coffee did you order?: "))
    priceCoffee = 10.50*poundsCoffee
    priceShipping = .86*poundsCoffee
    priceOverhead = 1.50
    totalCost = priceCoffee + priceShipping + priceOverhead

    print("Your total cost is $", totalCost)

def kilometersToMiles ():

    #inputs: number of kilometers
    #outputs: number of miles

    print("This program converts kilometers to miles.")

    numKilometers = eval(input("How many kilometers are you going to drive?: "))
    numMiles = numKilometers/1.61

    print("You will be driving", numMiles, "miles")

def triangleArea():

    import math
    #inputs:lengths of sides A, B, &C
    #outputs: area

    lengthA = eval(input("What is the length of the first side?: "))
    lengthB = eval(input("What is the length of the second side?: "))
    lengthC = eval(input("What is the length of the third side?: "))

    perimeterTriangle= (lengthA + lengthB + lengthC)/2
    areaTriangle = math.sqrt(perimeterTriangle*(perimeterTriangle-lengthA)*(perimeterTriangle-lengthB)*(perimeterTriangle-lengthC))

    print("The area of your triangle is:", areaTriangle, "unites squared.")

def sumSquares():

    #inputs:starting number and final number
    #output: sum of the squares of each of the numbers

    print("This program calculates the sum of the squares of numbers in a give range")

    total = 0
    lowerBound = eval(input("What is the starting number of your sequence?: "))
    upperBound = eval(input("What is the end number of your sequence?: "))
    for i in range(lowerBound, upperBound+1):

        total = total + (i**2)
    
    print("The sum of the squares is:", total)


#Type each function here then call the function from main() below.
#Once the function is working correctly, you can put a comment symbol
#in front of the call in main() so that you don't have to see it run over
#and over.  An example helloWorld function is above, and a call to this function
#is commented out below.
    
def main():
    #helloWorld()  
    #calcVolume()
    #shootingPercentage()
    #coffee()
    #kilometersToMiles()
    triangleArea()
    #sumSquares()
    
main()



    
    

    

    

