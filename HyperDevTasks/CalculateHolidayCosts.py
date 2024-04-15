# Functions to calculate the costs of holiday for different cities
def hotel_cost(num_nights):
    per_night = 75
    return per_night * num_nights

def plane_cost(city_flight):
    if city_flight == "p":
        return 105
    elif city_flight == "c":
        return 130
    elif city_flight == "l":
        return 77
    elif city_flight == "b":
        return 189

def car_rental(rental_days):
    rental_daily_cost = 43.50
    return rental_days * rental_daily_cost

def holiday_cost(num_nights, city_flight, rental_days):
    return hotel_cost(num_nights) + plane_cost(city_flight) + car_rental(rental_days)

# Function for menu
def options():
    print("Options:")
    print("p = Paris")
    print("c = Copenhagen")
    print("l = London")
    print("b = Barcelona")
    print("q = quit")

# Dictionary that pairs STRINGS (city_options) to destinations.       
city_options = {'p': 'Paris', 'c':'Copenhagen', 'l':'London',
    'b':'Barcelona'}

# Get inputs from user
print("This program will calculate the total cost of your holiday.")
city_flight = "x"
options()
while city_flight != "q":
    city_flight = input("Please enter the city you are flying to: ")
    if city_flight in city_options:
        num_nights = int(input("Enter the number of nights you'll stay a hotel:"))
        rental_days = int(input("How many days will you hire a car for?"))
        print("The total cost of your holiday is ", holiday_cost(num_nights, city_flight, rental_days))
        options()
    elif city_flight == "q":
        print("")
    else:
        print("Unrecognized destination.")
        options()
