# Ask user to input their age.
age = int(input("Please write your age: "))

if age < 13:
    # If user younger than 13.
    print("You are qualify for the kiddie discount.")

elif age == 21:
    # If user is 21.
    print("Congrats on your 21st!")

elif age > 100:
    # If user is over 100.
    print("Sorry, you're dead.")

elif age >= 65:
    # If user older than 64. 
    print("Enjoy your retirement.")

elif age >= 40:
    # If user's age between 39 and 65
    print("You're over the hill.")

else:
    # All others.
    print("Age is but a number.")