from random import randrange

#Quiz: Flying Circus cast list
#You're going to create a list of the actors who appeared in the television programme Monty Python's Flying Circus.

# Write a function called create_cast_list that takes a filename as input and returns a list of actors' names.
# It will be run on the file flying_circus_cast.txt (this information was collected from imdb.com).
# Each line of that file consists of an actor's name, a comma, and then some (messy) information
# about roles they played in the programme. You'll need to extract only the name and add it to a
# list. You might use the .split() method to process each line.


def create_list(filename):
    cast_list = []

    with open(filename, 'r') as file:
        for line in file:
            actor_name = line.split(',')
            cast_list.append(actor_name[0])

    return cast_list

# Quiz: Password Generator
# Write a function called generate_password that selects three random
# words from the list of words word_list and concatenates them
# into a single string. Your function should not accept any arguments
# and should reference the global variable word_list to build the password.

# Use an import statement at the top


def get_word_list(word_file):
    word_list = []

    #fill up the word_list
    with open(word_file,'r') as words:
        for line in words:
            # remove white space and make everything lowercase
            word = line.strip().lower()
            # don't include words that are too long or too short
            if 3 < len(word) < 8:
                word_list.append(word)
    return word_list

# Add your function generate_password here
# It should return a string consisting of three random words
# concatenated together without spaces
def generate_password(word_file, number_of_words = 3):
    password = ''

    word_list = get_word_list(word_file)

    for n in range(number_of_words):
        random = randrange(0, (len(word_list) - 1), 1)
        password = password + word_list[random]

    return password


def main():

    create_list('flying_circus_cast.txt')

    word_file = "words.txt"

    # test your function
    print(generate_password(word_file))



if __name__ == '__main__':
    main()