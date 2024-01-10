# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.


#Syntax Error: missing parenthese in print
print("Welcome to the error program")

#Syntax Error: unexpected indent +  missing parenthese in print
print("\n")

#Syntax Error: unexpected indent
# Variables declaring the user's age, casting the str to an int, and printing the result
#Syntax Error: NameError: name 'age_Str' is not defined, need to use = and not ==
age_Str = "24" 

#Syntax Error: ValueError because the string you want to convert does not represent any numbers
age = int(age_Str)

#Runtime error: concatenate a string with an integer using the + operator
print("I'm " + age_Str + "years old.")

#Syntax Error: unexpected indent
# Variables declaring additional years and printing the total years of age
years_from_now = "3"

#Runtime error: concatenate a string with an integer using the + operator
total_years = age + int(years_from_now)

#Syntax Error: missing parenthese in print
#Logical Error:  add value not text
print(f"The total number of years: {total_years}" )

# Variable to calculate the total amount of months from the total amount of years and printing the result
#Syntax Error: NameError because name total is not defined
#Logical: add 6 month

total_months = total_years * 12 + 6

#Syntax Error: missing parenthese in print
#TypeError: can only concatenate str (not "int") to str
print("In 3 years and 6 months, I'll be " + str(total_months) + " months old")

#HINT, 330 months is the correct answer

