number_total = 0
sum_of_numbers = 0

while True:
    #ask user to input a number
    number = float(input("Please enter a number: "))


    if number == -1:
        if number_total!= 0:
            #calculating average
            numbers_average = sum_of_numbers / number_total

            print(f"Average of entered numbers excluding -1: {numbers_average}")
            
        else: 
            numbers_average = 0
            print("There are no numbers excluding -1.")
            
        break

    # adding/plus new number
    sum_of_numbers += number

    # counting total number of numbers, increasing by 1 every step
    number_total += 1


