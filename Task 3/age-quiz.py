age = int(input("Please write your age: "))

if age < 13:
    print("Youa are qualify for the kiddie discount.")
elif age == 21:
    print("Congrats on your 21st!")
elif age > 100:
    print("Sorry, you're dead.")
elif age >= 65:
    print("Enjoy your retirement.")
elif age >= 40:
    print("You're over the hill.")
else:
    print("Age is but a number.")