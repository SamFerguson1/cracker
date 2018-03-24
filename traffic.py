
#name: Sam Ferguson
#traffic.py

#Problem: Write program to analyze traffic patterns
#inputs: # of roads & # of days of counters & # cars travelled day
#outputs: average number of vehicles per road & per all roads
#statement of authenticity
#   The code used int his script is my own


#



def traffic():

#purpose statement:
    print("This program is designed to give average number of vehicles on roads.")

    #input number of roads surveyed
    roadsSurveyed= eval(input("How many roads were surveyed?: "))
    #loop
    #start loop to got how many times to loop individual road survey
    #initialize total sum accumulator
    totalTwo = 0
    for i in range(1, roadsSurveyed+1):
        #gather number days to get # times to loop
        numDays = eval(input("how many days was road " +str(i)+" surveyed? "))
        #initialize the accumulator for the j loop in i loop so it loops
        total = 0
        #loop
        for j in range(1, numDays+1):
           #ask how many cars traveled 
            carsTraveled = eval(input("How many cars traveled on day "+str(j)+ "?"))
            #add to acccumulator
            total = total + carsTraveled
            #take average
            avgRoad = total/numDays
        #print in i loop so it prints when j loop finished first
        print("Road", i, "had an average of", avgRoad, "vehicles per day.")
        #take total of cars of each road after it loops and add to total
        totalTwo = total + totalTwo
        #avg of total of all cars/ all roads
        avgAllRoad = totalTwo/roadsSurveyed
    #print the final output values outside of the loop
    print("Total number of vehicles traveled on all roads: " +str(totalTwo))
    print("Average number of vehicles per road: "+str(round(avgAllRoad,2)))
    

def main():

    traffic()

main()

    
    
