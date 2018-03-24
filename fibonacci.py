def fibonacci(numFib):
    firstOne = 1
    secondOne = 1
    total = 0
    if numFib <= 2:
        return 1

    else:
        for i in range(numFib-2):
            total = firstOne + secondOne
            firstOne = secondOne
            secondOne = total
def doubleInterest(principal, rate):
#inputs: investment amount interest rate
#outputss: number of years to double
#purpose duh
    originalPrincipal = principal
    earnedAmount = 0
    timeCounter = 2
    while principal <=originalPrincipal *2:
        earnedAmount = principal * rate 
        principal +=earnedAmount
        timeCounter += 1
    return timeCounter

def 





def main():
##    numFib = eval(input("What number of the sequence do you want?: "))
##    result = fibonacci(numFib)
##    print("sick fam the result is", result)
##    amount = eval(input(" What is the oringal investment?: "))
##    rate = eval(input("What is the interest rate ex: '.06': "))
##    doubleTime = doubleInterest(amount, rate)
##    print("It'll take, ", doubleTime, " years.")
    

main()
