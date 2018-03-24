#fucking fuck bro

#(1+rate) = rateOne | rateTwo = rateOne**months   | rateThree= rate * rateTwo  | rateFour = rateThree * principal
#rateTwo-1

def main():
    principal = 1000
    rate= 5/1200
    months = 36

    rateOne= 1+rate
    rateTwo = rateOne**months
    rateThree=rateTwo* rate
    rateFour = rateThree * principal
    rateFive = rateTwo-1

    finalThing= rateFour/rateFive

    print(finalThing)
