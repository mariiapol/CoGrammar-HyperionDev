n = 10

for i in range(0,n):
    # i - is a number of step where we are now
    # add plus one step each time
    i += 1
   
    if i <= n/2: 
        # increasing number of stars
        number_of_stars = "*" * i

    else: 
        #decreasing number of stars  
        number_of_stars = "*" * (n-i)

    print(number_of_stars)

