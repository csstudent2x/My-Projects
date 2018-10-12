
Word counter and more!

This program allows user to input a file and output a file including the
frequency of the words! In addition, the program prints the longest word and
the five most common words in the console!

"""
import string

def count_words(file_name):

    """
    function will create and return dictionary for user-inputted filename
    parameters: file
    returns: dictionary

    """
    word_dict = {}
    with open(file_name, 'r', encoding='utf8') as output_file, \
            open('out.txt', 'w', encoding='utf8') as new_file:
        for line in output_file:
            line = line.lower()
            for word in line.split():
                word = word.strip(string.punctuation + string.digits)
                if word != '': # does not whitespace
                    if word in word_dict:
                        word_dict[word] += 1
                    else:
                        word_dict[word] = 1
                else:
                    pass

        for word in sorted(word_dict): # writing stats to out.txt
            new_file.write("%s: %d\n" % (word, word_dict[word]))

    return word_dict

def report(word_dict):

    """
    calculates and prints the longest word and 5 most common words from file
    parameters: dictionary
    returns: none

    """
    print("The longest word is: " + max(word_dict, key=len)) # longest word

    print("The 5 most common words are:") # prints first five sorted values
    for sort_word in sorted(word_dict, key=word_dict.get, reverse=True)[:5]:
            print("%s: %d" % (sort_word, word_dict[sort_word]))

    return

def main():
    file_name = input('Enter file name: ') # set file to variable
    word_count = count_words(file_name) # set dictionary to variable
    report(word_count) # call report to print other stats


if __name__ == '__main__':
    main()
