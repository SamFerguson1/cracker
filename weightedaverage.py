#name: Sam Ferguson
#weightedaverage.py
#purpose: read from txt run weighted average, output txt
#input: txt strings
#output:txt file
#cerification of authenticity: I, Sam Ferguson, was the only person who
#                                           wrote this code.




def weightedAverage(inputFileName, outFileName):
    #get what's on the lines

    lineList = ""
    for line in inputFileName:
        lineList +=line
    lineList = lineList.split("\n")
    #make a list of all the names to be indexed later
    nameList =[]
    for i in range(len(lineList)):
        name = lineList[i].split(" ")
        name = name[0] + " " +name [1]
        nameList.append(name)
    #now i have a nice list of names
    weightVals = []
    for i in range(len(lineList)):
        #for each line in the list of lines split on space
        newList = lineList[i].split(" ")
        #this lets me yank out names
        total = 0        
        betterList = []
        for j in range(2,len(newList)):
            betterList.append(newList[j])
        #names officially yanked out
        #this loop adds up the sum of the weights
        for l in range(len(betterList)//2):
            total += eval(betterList[l*2])
            sumOfWeights = total
        #I add the weights to a list for conditional
        weightVals.append(sumOfWeights)
    
    #these conditionals check whether its 100 and which error if not
    avgList =[]
    for i in range(len(nameList)):
        #sends bad files to shadow realm
        if weightVals[i] != 100:
            if weightVals[i] > 100:
                print("Sorry, "+ nameList[i] +" stinks to be you, your weight is too big", file =  outFileName)
            else:
                print("Sorry, "+ nameList[i] +" stinks to be you, your weight is too low", file  = outFileName)
        else:
            #function that makes the number list for the specific
            #lineList value that passed test
            newList = lineList[i].split(" ")
            betterList = []
            for j in range(2,len(newList)):
                betterList.append(newList[j])
            #okay finally the easy part, just a formula
            total = 0
            for l in range(len(betterList)//2):
                total += eval(betterList[l*2])* eval(betterList[(l*2)+1])
            average = total/100
            print("Holy cow, " +nameList[i]+"! You're a real champ, your average was: "+ str(average)+ "!", file = outFileName)
            avgList.append(average)
          
    total = 0     
    for i in range(len(avgList)):
        total +=avgList[i]
    overallAverage = total/ len(avgList)
    print(file = outFileName)
    print("Class average: " + str(overallAverage), file = outFileName)
        
    

def main():

    inFile= open("grades.txt", "r")
    outFile = open("SamFergusonavg.txt", "w")
    weightedAverage(inFile, outFile)


main()
    
    

    
