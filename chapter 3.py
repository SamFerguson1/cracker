
def volumeSphere():
    #input radius
    #output surface area and volume
    #purpose statement
    print("This program computes the SA and volume of a sphere given radius.")

    radius = eval(input("Enter the radius of the sphere: "))

    PI = 3.14
    volume = (4/3)*PI*(radius**3)
    surfaceArea= 4*PI*(radius**2)

    print("cool shit ur SA and volume are " +str(round(volume,2))+ "units cubed and" + str(round(surfaceArea,2))+".")


def pizzaCalculator():
    print(" this program calculates the cost per square inch of a circular pizza given its diamter and price.")
    
    #inputs diameter and price
    #outputs cost per square ince
    #take the half of diameter then find area
    diameter = eval(input("What is the diameter of the pizza?"))
    price = eval(input("What is the price of the pizza?"))
    PI = 3.14
    area = (1/2*diameter)**2*PI
    priceSQInch = price/area

    print("the price per square is", priceSQInch)


    





















def chapterThree():

    #volumeSphere()
    pizzaCalculator()
chapterThree()
