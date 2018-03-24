import math
def series():

    numTerms = eval(input("How many terms in the sequence?" ))
    total = 0
    for i in range(numTerms):

        numerator = i*2
        denominator = (i*5)+5
        print(numerator, " / ", denominator)
        total += numerator/denominator
    print(total)
        
