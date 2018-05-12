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



if __name__ == '__main__':
    main()



