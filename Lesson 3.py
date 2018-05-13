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

    temp = dict(name='joe', age=25)

    temp['home'] = 'IRE'

    name = temp.get('name', default='Unknown name')

    print(temp)

    if 'home' in temp:
        print('I have a home')
        print(name)


    squares = get_squares(25)
    print(squares)

if __name__ == '__main__':
    main()

from countries import country_list # Note: since the list is so large, it's tidier
                                   # to put in in a separate file. We'll learn more
                                   # about "import" later on.

country_counts = {}
for country in country_list:
    #todo: insert countries into the country_count dict.
    # If the country isn't in the dict already, add it and set the value to 1
    # If the country is in the dict, increment its value by one to keep count
    if country_counts.get(country) is None:
        country_counts[country] = 1
    else:
        country_counts[country] += 1




