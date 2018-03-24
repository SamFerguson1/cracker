def fuelEconomy(mpg):

    print("Your care has {0} mpg".format(mpg))

    if mpg>= 24:
        print("yoU HAVE A FUEL EFFICIENT CAR.")
    else:
        print("You are sucking the life out of our environment.")


def isFuelEfficient(mpg):
    if mpg>= 24:
        rtnVal =  True
    else:
        rtnVal = False
    return rtnVal


def total(op1, op2):

    return op1+op2

def findMax(num1, num2, num3):

    if num1 > num2 or num3:
        maxVal = num1
    elif num2 > num1 or num3:
        maxVal = num2
    elif num3 >num1 or num2:
        maxVal = num2
    
def findMaxList(numList):
    
    maxVal = numList[0]
    for i in range(1,len(numList)):
        if numList[i] > maxVal:
            maxVal = numList[i]
    return maxVal
            
    
def main():

    poopfart = [10,30441, 143210 ,1230123402, 13471230971294, 1348123442,12374]
    bigBoy = findMaxList(poopfart)
    print(bigBoy)

##
##    maxVal = findMax(7,15,8)
##    print(maxVal)
##    maxVal = findMax(10,5,7)
##    print(maxVal)
##    maxVal = findMax(12,12,13)
##    print(maxVal)


##    for mpg in [10,24,40]:
##        efficient = isFuelEfficient(mpg)
##        if efficient:
##            print("Thanks for all you do.")
##        else:
##            print("consider buying a different car.")
##        print()
#boolean function returns a boolean result
#will return true if it's fuel efficient and false if not
        


        
main()
