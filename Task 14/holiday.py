# calculate holiday total cost

#get user inputs
city_flight = input("The city where you are flying to: ")
num_nights = int(input("Number of nights at a hotel: "))
rental_days = int(input("Number of days you hiring a car: "))

#calculate total cost for the hotel stay
def hotel_cost(num_nights):
    return num_nights * 300

#return flight cost depends of where flight is
def plane_cost(city_flight):

    if city_flight == "Lisbon":
        return 300
    elif city_flight == "Paris":
        return 100
    elif city_flight == "Dubai":
        return 800
    else:
        return 200
    
#calculate the total cost of car rental
def car_rental(rental_days):
    return rental_days * 80

# calculate holiday total cost
def holiday_cost(hotel_cost, plane_cost, car_rental):
    return(hotel_cost + plane_cost + car_rental)

holiday_cost_total = holiday_cost(hotel_cost(num_nights),plane_cost(city_flight),car_rental(rental_days))

#print all details about the holiday
print(f"Your holiday details:\nCity: {city_flight}, Number of nights: {num_nights}, Number of car rental days: {rental_days}.\nTotal cost: {holiday_cost_total}")
