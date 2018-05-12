import csv
from datetime import datetime as dt
import sys

# Get the scores from the file scores.csv
# Each line in the file contains a list of scores.
# For each list of scores get a corresponding rating.
# Write the rating to a csv file preceded by current date.
# If an invalid entry is loaded from file exit the program.

def get_scores():
    '''
    Return the scores gathered in one day.
    :return: a list of scores for one day
    '''
    scores = []
    filename = 'scores.csv'
    with open(filename, 'r', newline='') as score_file:
        score_reader = csv.reader(score_file)
        for row in score_reader:
            scores.append(row)
    return scores

def score_to_rating_string(average_score):
    '''
    Return the rating based on the average score.
    1 Terrible
    2 Bad
    2 OK
    3 Good
    4 Excellent
    :param average_score:
    :return: rating
    '''
    rating = None
    if 0 <= average_score < 1:
        rating = 'Terrible'
    elif average_score < 2:
        rating = 'Bad'
    elif average_score < 3:
        rating = 'OK'
    elif average_score < 4:
        rating = 'Good'
    elif average_score < 5:
        rating = 'Excellent'

    if rating:
        return rating
    else:
        return 'Unknown rating'

def get_avg(scores):
    '''
    Get the average of the scores discount for
    the max and min scores in the data set.
    :param scores:
    :return: an average.
    '''
    total = 0
    for i in scores:
        total += i

    # remove the max and min scores
    total -= (min(scores) + max(scores))
    # discount for the max and min when getting the average.
    return total / (len(scores) - 2)


def convert_to_numeric(score, default=None):
    '''
    Convert the type of score to int
    :param score:
    :param default:
    :return: score as type int
    '''
    try:
        return int(score)
    except(ValueError, TypeError):
        return default


def scores_to_rating(scores):
    """
    Turns scores into a rating by averaging the
    middle three of the five scores and assigning this average
    to a written rating.
    """
    checked_scores = []

    for score in scores:
        temp = convert_to_numeric(score)
        if temp:
            checked_scores.append(temp)
        else:
            # if any of the scores are not a number exit the program.
            sys.exit()

    average_score = get_avg(checked_scores)

    # turn average score into a rating
    rating = score_to_rating_string(average_score)

    return rating


def main():
    scores = get_scores()
    ratings = []

    for days_scores in scores:
        ratings.append(scores_to_rating(days_scores))

    with open('ratings.csv', 'a', newline='') as output:
        csv_writer = csv.writer(output)
        for rating in ratings:
            csv_writer.writerow([[str(dt.now().date()) + ' : ' + rating], ''])


if __name__ == '__main__':
    main()








