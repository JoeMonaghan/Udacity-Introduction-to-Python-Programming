def convert_to_numeric(score, default = None):
    try:
        return int(score)
    except(ValueError, TypeError):
        return default

def sum_of_middle_three(score1,score2,score3,score4,score5):
    # create an arry
    scores = [score2, score3, score4, score1, score5]
    sum = 0
    for i in scores:
        if not i is None:
           sum +=i

    sum -= (min(scores) + max(scores))
    return sum


def score_to_rating_string(average_score):
    '''
    Return the rating based on the average score.
    Average Score	Rating
    0 <= score < 1	Terrible
    1 <= score < 2	Bad
    2 <= score < 3	OK
    3 <= score < 4	Good
    4 <= score <= 5	Excellent

    :param average_score:
    :return: rating
    '''
    return {
        0: 'Terrible',
        1: 'Bad',
        2: 'OK',
        3: 'Good',
        4: 'Excellent',
        5: 'Excellent'
    }.get(average_score, 'Unknown rating')

def scores_to_rating(score1,score2,score3,score4,score5):
    """
    Turns five scores into a rating by averaging the
    middle three of the five scores and assigning this average
    to a written rating.
    """
    #STEP 1 convert scores to numbers
    score1 = convert_to_numeric(score1)
    score2 = convert_to_numeric(score2)
    score3 = convert_to_numeric(score3)
    score4 = convert_to_numeric(score4)
    score5 = convert_to_numeric(score5)

    #STEP 2 and STEP 3 find the average of the middle three scores
    average_score = sum_of_middle_three(score1,score2,score3,score4,score5)/3

    #STEP 4 turn average score into a rating
    rating = score_to_rating_string(average_score)

    return rating
