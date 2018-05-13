from countries import country_list # Note: since the list is so large, it's tidier
                                   # to put in in a separate file. We'll learn more
                                   # about "import" later on.


#REORGAINIZING CODE
def check_answer(my_answer, actual_answer):
    '''
    Checks rather the answer is correct
    :param my_answer:
    :param actual_answer:
    :return: 1 for correct and 0 for false.
    '''
    if my_answer == actual_answer:
        return 1
    return 0


def get_result(my_answers, actual_answers, pass_rate):
    '''
    Returns true if the score is precnetage is greater than or equal
    to the pass precentage.

    :param my_answers:
    :param actual_answers:
    :param pass_rate:
    :return:
    '''
    correct_answers = 0
    for i in range(len(actual_answers)):
        correct_answers += check_answer(my_answers[i], actual_answers[i])

    passed = correct_answers / len(actual_answers) >= pass_rate

    if passed:
        return "Congratulations, you passed the test! You scored {} out of {}".format(correct_answers), len(actual_answers)
    else:
        return "Unfortunately, you did not pass. You scored {} out of {}".format(correct_answers, len(actual_answers))

def remove_duplicates(elements):
    '''
    Returns a list with with duplicates removed.
    '''
    my_set = []
    for element in elements:
        if element not in my_set:
            my_set.append(element)
    return my_set


squares = set()


# todo: populate "squares" with the set of all of the integers less
# than 2000 that are square numbers


# Note: If you want to call the nearest_square function, you must define
# the function on a line before you call it. Feel free to move this code up!
def nearest_square(limit):
    answer = 0
    while (answer + 1) ** 2 < limit:
        answer += 1
    return answer ** 2

def get_square_numbers(limit):

    square = 0
    i = 2
    limit = nearest_square(limit)

    while square <= limit:
        square = nearest_square(i)
        squares.add(square)
        i += 1

    print(squares)


def get_squares(limit):
    i = 1
    squares = list()
    while (i ** 2) <= limit:
        squares.append(i ** 2)
        i += 1

    return squares


# Users by Country
def get_country_occurrence(country_list):
    country_counts = {}

    for country in country_list:
        # If the country isn't in the dict already, add it and set the value to 1
        # If the country is in the dict, increment its value by one to keep count
        if country_counts.get(country) is None:
            country_counts[country] = 1
        else:
            country_counts[country] += 1
    return country_counts

#Quiz: Prolific Year
def most_prolific(discography):

    count_list = dict()
    years = list()
    top = 0

    for album, year in discography.items():
        if year not in count_list:
            count_list[year] = 1
        else:
            count_list[year] += 1

        # get the year key with the highest value
        if count_list[year] > top:
            top = count_list[year]

    # get all the years that have equally top occurrence's
    for year, number_of_occurrences in count_list.items():
        if number_of_occurrences == top:
            years.append(year)

    if len(years) > 1:
        return years
    return years[0]

def main():




    # test #REORGAINIZING CODE
    my_answers =[12, 3, 45,  5, 6, 6]
    actual_answers = [12, 5, 6, 5, 6, 6]
    pass_rate = 0.7
    result = get_result(my_answers, actual_answers, pass_rate)
    print(result)

    # test Remove duplicates
    elements = [1, 33, 4, 4, 55, 55, 6, 3, 1, 9, 34]
    print(remove_duplicates(elements))

    squares = get_squares(25)
    print(squares)

    # use the imported country list and return dict with
    # the times each country is contained within the list.
    countries_occurences = get_country_occurrence(country_list)
    print(countries_occurences)

    # Test Quiz Prolific Year
    Beatles_Discography = {"Please Please Me": 1963, "With the Beatles": 1963,
                           "A Hard Day's Night": 1964, "Beatles for Sale": 1964, "Twist and Shout": 1964,
                           "Help": 1965, "Rubber Soul": 1965, "Revolver": 1966,
                           "Sgt. Pepper's Lonely Hearts Club Band": 1967,
                           "Magical Mystery Tour": 1967, "The Beatles": 1968,
                           "Yellow Submarine": 1969, 'Abbey Road': 1969,
                           "Let It Be": 1970}

    for album_title in Beatles_Discography:
        print("title: {}, year: {}".format(album_title, Beatles_Discography[album_title]))

    year_years = most_prolific(Beatles_Discography)
    print('The Beatles most prolific year/s was {}'.format(year_years))

if __name__ == '__main__':
    main()




