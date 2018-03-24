def thingy():

    total = 0
    numVal = eval(input("how many numbers in sequence?"))
    for i in range(1, numVal+1):

        total = total + (i /((i*2)+1))

        print(total)

def main():

    thingy()

main()
