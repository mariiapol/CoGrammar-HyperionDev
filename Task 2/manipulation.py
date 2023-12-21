str_manip = input("Please write a sentence: ")

length_str_manip = len(str_manip)
print(length_str_manip)

last_letter = str_manip[-1]
new_string = str_manip.replace(last_letter,"@")
print(new_string)

last_3_letters = str_manip[-3:]
print(last_3_letters)
last_letters_test = last_3_letters[::-1]
print(last_letters_test)

last_2_letters = str_manip[-2:]
first_3_letters = str_manip[:3]
new_word = first_3_letters + last_2_letters
print(new_word)
