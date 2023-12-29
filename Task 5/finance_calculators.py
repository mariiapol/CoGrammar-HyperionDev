import math
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond - to calculate the amount you'll have to pay on a home loan")

user_input = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")
user_input = user_input.lower()

if user_input != "investment" and user_input != "bond":
    print("Error. Please try ones more.")

elif user_input == "investment":

    deposit = float(input("Please enter the amount of money that you are depositing: "))
    rate = float(input("Please enter the interest rate: "))
    years = int(input("Please enter the number of years you plan: "))
    interest = input("Would you like interest 'simple' or 'compaund': ")
    interest = interest.lower()
                     

    if interest == "simple":
        total = deposit * (1+ rate/100 * years)
        print(f"Total is: {total}, {interest} interest formula used.")


    elif interest == "compaund": 
        total = deposit * math.pow((1+rate/100),years)
        print(f"Total is: {total}, {interest} interest formula used.")

    else:
        print("Error in chosing investment formula.")
    
    

else: 
    value = float(input("Please write plesent value of the house: "))
    interest_rate = float(input("Interest rate: "))
    months = int(input("Number of months you plan to take to repay: "))

    repayment = (interest_rate/100/12 * value)/(1 -( 1 + interest_rate/100/12)**(-months))
    print(f"Your repayment each month will be: {repayment}.")


