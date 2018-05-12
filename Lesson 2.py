#DEFINING FUNCITONS I
# todo: define a function named `population_density` that takes two arguments,
# `population` and `land_area` (in square kilometres), and returns a population
# density calculated from those values.


def population_density(population, land_area):
    '''
    Return population density.

    :param population:
    :param land_area:
    :return: population density.
    '''
    return population / land_area


# Here are test cases to verify that your function works as expected:
test1 = population_density(10, 1)
expected_result1 = 10
print("expected result: {}, actual result: {}".format(expected_result1, test1))

test2 = population_density(864816, 121.4)
expected_result2 = 7123.6902801
print("expected result: {}..., actual result: {}".format(expected_result2, test2))

# DEFINING FUNCTIONS II
# Write your code for readable_timedelta here.


def readable_timedelta(days):
    ''' returns a str of days in delta format.

    days: a int of the total days
    '''
    weeks_delta = days // 7
    days_delta = days % 7
    return "{} week(s) and {} day(s).".format(weeks_delta, days_delta)


# call to test it:
print(readable_timedelta(10))

# CODE WITH BRANCHES I
#First Example - uncomment lines or change values to test the code
phone_balance = 7.62
bank_balance = 104.39
#phone_balance = 12.34
#bank_balance = 25
if phone_balance < 10:
    phone_balance += 10
    bank_balance -= 10


print(phone_balance)
print(bank_balance)

#Second Example
#change the number to experiment!

number = 145346334

if number % 2 == 0:
    print("The number " + str(number) + " is even.")
else:
    print("The number " + str(number) + " is odd.")

#Third Example
#change the age to experiment with the pricing

age = 35

#set the age limits for bus fares
free_up_to_age = 4
child_up_to_age = 18
senior_from_age = 65

#set bus fares
concession_ticket = 1.25
adult_ticket = 2.50

#ticket price logic
if age <= free_up_to_age:
    ticket_price = 0
elif age <= child_up_to_age:
    ticket_price = concession_ticket
elif age >= senior_from_age:
    ticket_price = concession_ticket
else:
    ticket_price = adult_ticket
message = "Somebody who is {} years old will pay ${} to ride the bus.".format(age, ticket_price)
print(message)


def which_prize(points):
    prize = None
    if 0 <= points <= 50:
        prize = "wooden rabbit"
    elif 151 <= points <= 180:
        prize = "wafer-thin mint"
    elif points >= 181:
        prize = "a penguin"

    if prize:
        return "Congratulations! You have won a {}!".format(prize)
    else:
        return "Oh dear, no prize this time."


print(which_prize(58))


# The cylinder_surface_area function calculates the surface area of cylinders that are solid or hollow.
# The has_top_and_bottom argument is True or False depending on whether the cylinder is solid or hollow.
# The surface area of a solid cylinder includes the areas of the top and bottom
# Restructure this function definition so that it has two return statements in its body.
def cylinder_surface_area(radius, height, has_top_and_bottom):
    """
    Calculates the surface area of cylinder given the following
    parameters
    :param radius:
    :param height:
    :param has_top_and_bottom:
    :return:
    """
    side_area = height * 6.28 * radius
    if has_top_and_bottom:
        top_area = 3.14 * radius ** 2
        return 2 * top_area + side_area
    return side_area


cylinder_side_area = cylinder_surface_area(2, 4, True)
print(cylinder_side_area)
