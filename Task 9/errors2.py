# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

#SyntaxError: NameError as name 'Lion' is not defined, string must have ""
animal = "Lion"
animal_type = "cub"
number_of_teeth = 16

#SyntaxError: Missing parentheses in call to 'print' and missing f for f-string
#Logical: swap type and number of teeth   

full_spec = (f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth")

#SyntaxError: Missing parentheses in call to 'print'.
print(full_spec)

