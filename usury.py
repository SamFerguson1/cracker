# Name: Sam Ferguson
# usury.py
#
# Problem: How to calculate monthly payement, total interest paid
#               and total payment on a loan
#               
#
# Inputs: Principal, time (in months) & interest (in percent) 
#              
#             
# Outputs: Total payment, the total interest paid & the monthly payment.
# Certicfictation of authenticity
#
#       I certify that this lab is entirely my own work.

def main():
#Step one: Gathering the inputs
    print("Hello! This program is designed to calculate the monthly payment, total payment,")
    print("and total interst of your loan, given the principal, time, and interest rate!")
#Want to be 
    principal = eval(input("Please enter the principal of your loan: "))
    months = eval(input("Please enter the amount of time of the loan (in months): "))
#I'm not sure how to put a percent sign after, want to be clear w/ user
    ratePercent = eval(input("Please enter the interest rate of the loan (in percent without percent sign!): ")) 

#Now that we have the inputs we can start putting them into our formula
#Have to convert percent to raw value
    rate = ratePercent/1200

#With that settled we can plug the variables into the function

    monthlyPayment = (principal*(rate*((1+rate)**months)))/(((1+rate)**months)-1)
#This gives us our first output, the monthly payment.
#total payement is monthly * months
    totalPayment= monthlyPayment * months
#Then finally to get the total interest paid
# we subtract total by the principal
    totalInterestPaid = totalPayment - principal
#Now that we have all of the outputs we should print them back to the user

    print("Your monthly payment is:", monthlyPayment)
    print("Your total payment is:", totalPayment)
    print("The total interest paid is:", totalInterestPaid)
#With all of that our problem is solved
