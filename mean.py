#Name: Sam Ferguson
#mean.py

#Problem: Need to figure out how to calculate root mean square
#              and harmonic mean
#Inputs: the number of values input & values themselves
#Outputs: Root mean square and Harmonic mean
#Statement of Authenticy:
#   The code used in this script is my own.

#Purpose statement
#input number of values
#initialize accumulator(s)
#loop
#input individual values
#add square values for RMS
#add recipricol values for harmonic mean
#divide sum of squared inputs by number of values
#take square root to get RMS
#divide number of values by recipricol sum for Harmonic mean
#output values


def averageCalculator():
    #Purpose statement
    print("This program is designed to calculate root-mean-square and Harmonic Mean.")
    #input number of values
    numValues = eval(input("How many values in sequence?: "))

    #initialize accumulators
    totalOne = 0
    totalTwo = 0 
    #loop
    for i in range(numValues):
        #Input individual values
        values = eval(input("Enter individual values: "))
        #add squared values
        totalOne = totalOne + (values**2)
        totalTwo = totalTwo + (1/values)

    #divide sum of squared inputs by number of values
    sumSquaredValues = totalOne / numValues
    #take sqrt of values
    valueRMS = sumSquaredValues ** (1/2)
    #divide number of values by recipricol sum for harmonic mean
    valueHarmonicMean = numValues/totalTwo
    #output values
    print("The root-mean-square is:", valueRMS)
    print("The Harmonic mean is:", valueHarmonicMean)

#something I saw in lab that seems pretty neat and convenient
def main():

    averageCalculator()

main()
