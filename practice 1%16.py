#problem:need to find volume of cylinder
#specifications: take inputs of radius and height to find volume
#design: ask user for radius and height, plug into fomula, get result
#implement design
def volume():
    print("This program calculates the volume of a cylinder")

    radius = eval(input("Please enter the radius: "))
    height = eval(input("Please enter the height: "))

    import math
    PI = math.pi
    
    volume = PI*(radius**2)*height

    print("Your volume is", volume, "units cubed")

def loopPractice():
    print("printing numbers 0-10")
    for i in range(11):
        print(i)

def loopPracticeTwo():
    print("Printing numbers 0-10")
    for i in range(11):
        print(i, end = " ")

def loopPracticeThree():
    for i in range(16):
        print(i+5)
        
