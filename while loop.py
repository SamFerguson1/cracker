def loop():
#no negatives no 100
    #~(negatives or 100)
    #~negatives & ~100
    total = 0
    count = 0
    scoreA = eval(input("What's the score family"))
    total+=scoreA
    
    while scoreA >= 0 and scoreA != 100:
        
        
        count+=1
        scoreA = eval(input("What's the score family"))
        total+=scoreA
        print(total)
    avg = scoreA/count
    print(avg)



loop()
