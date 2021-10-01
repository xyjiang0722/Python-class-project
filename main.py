# -*- coding: utf-8 -*-
# Name: Xiaoyan Jiang
import csv

CLASS_LABEL_COLUMN = 0
TEXT_MESSAGE_COLUMN = 1

symbols_manual = "!@#$%^&*()`~,<.>/?;:'\|[{]}=+-_"


def has_links(text):
    # links have "www." or "http"
    if text.find("www.") != -1 or text.find("http") != -1:
        return True
    else:
        return False


def has_spammy_words(text, spam):
    number_of_spammy_words = 0
    # get a list of words in the given text
    words = text.split(' ')

    # count the number of spammy words
    for word in words:
        if word in spam:
            number_of_spammy_words += 1

    # if the number of spammy words = 0, then the text doesn't contain spammy words
    if number_of_spammy_words == 0:
        return False
    else:
        return True


def length_of_texts(text):
    return len(text)


def number_of_symbols(text):
    number_of_symbols = 0

    # count the number of symbols in the text
    for char in text:
        if char in symbols_manual:
            number_of_symbols += 1

    return number_of_symbols


def number_of_words_containing_letters_and_numbers(text):
    # each word in the text is a string in a list
    words = text.split(' ')
    number_of_single_quotes = 0

    # if any one of the character in the word is a letter and any one of the character in the word is a number, then count 1
    for word in words:
        if any(char.isalpha() for char in word) and any(char.isdigit() for char in word):
            number_of_single_quotes += 1

    return number_of_single_quotes


def number_of_words_containing_only_letters(text):
    # get a list of words in the given text
    words = text.split(' ')
    number_of_words = 0

    # count number of words containing only letters
    for word in words:
        if word.isalpha():
            number_of_words += 1

    return number_of_words


def number_of_words_containing_only_uppercase_letters(text):
    # get a list of words in the given text
    words = text.split(' ')
    number_of_uppercase_words = 0

    # count number of words containing only uppercase letters
    for word in words:
        if word.isupper():
            number_of_uppercase_words += 1

    return number_of_uppercase_words


def write_features(link, spammy_words, length, symbols, words_containing_letters_and_numbers, words_containing_only_letters, words_containing_only_uppercase_letters, class_label, file):
    # feature 1: does have links
    if link:
        file.write('True')
    else:
        file.write('False')
    file.write(',')

    # feature 2: does have spammy words
    if spammy_words:
        file.write('True')
    else:
        file.write('False')
    file.write(',')

    # feature 3: length of texts
    file.write(length)
    file.write(',')

    # feature 4: number of symbols
    file.write(symbols)
    file.write(',')

    # feature 5: number of words containing letters and numbers
    file.write(words_containing_letters_and_numbers)
    file.write(',')

    # feature 6: number of words containing only letters
    file.write(words_containing_only_letters)
    file.write(',')

    # feature 7: number of words containing only uppercase letters
    file.write(words_containing_only_uppercase_letters)
    file.write(',')

    # add class label
    file.write(class_label)

    # next line
    file.write("\n")


def main():
    # Part 1 of main: get a list of spammy words
    # opens the csv file
    in_file = open("training_data.csv", 'r', encoding="ISO-8859-1")

    # csv file object
    csv_reader = csv.reader(in_file, delimiter=',')

    # create lists
    spam_messages = []
    ham_messages = []
    words_in_all_spam_messages = []
    words_in_all_ham_messages = []
    flat_list_of_words_in_all_spam_messages = []
    flat_list_of_words_in_all_ham_messages = []
    spammy_words = []

    # create a list of spam messages and a list of ham messages
    for row in csv_reader:
        if row[CLASS_LABEL_COLUMN] == "spam":
            spam_messages.append(row[TEXT_MESSAGE_COLUMN])
        elif row[CLASS_LABEL_COLUMN] == "ham":
            ham_messages.append(row[TEXT_MESSAGE_COLUMN])

    # create a list of words from spam messages
    for message in spam_messages:
        words_in_one_spam_message = message.split(' ')
        words_in_all_spam_messages.append(words_in_one_spam_message)

    # words_in_all_spam_messages is a list of lists, so flatten it to get one list of spam words, and convert them to lower case letters
    for sublist in words_in_all_spam_messages:
        for word in sublist:
            flat_list_of_words_in_all_spam_messages.append(word.lower())

    # repeat to get a list of ham words
    for message in ham_messages:
        words_in_one_ham_message = message.split(' ')
        words_in_all_ham_messages.append(words_in_one_ham_message)
    for sublist in words_in_all_ham_messages:
        for word in sublist:
            flat_list_of_words_in_all_ham_messages.append(word.lower())

    # words in spam messages but not in ham messages are spammy
    for word in flat_list_of_words_in_all_spam_messages:
        if word not in flat_list_of_words_in_all_ham_messages:
            spammy_words.append(word)

    in_file.close()

    # Part 2 of main: compute features (merging the 2 parts causes stopiteration error)
    # opens the csv file
    in_file_2 = open("training_data.csv", 'r', encoding="ISO-8859-1")

    # csv file object
    csv_reader_2 = csv.reader(in_file_2, delimiter=',')

    # skips the first row
    header_row = next(csv_reader_2)

    # create feature.csv and its first row
    out_file = open("features.csv", 'a')
    out_file.write('doesHaveLinks,doesHaveSpammyWords,lengthOfText,numberOfSymbols,'
                   'numberOfWordsContainingLettersAndNumbers,numberOfWordsContainingOnlyLetters,'
                   'numberOfWordsContainingOnlyUppercaseLetters,class label')
    out_file.write("\n")

    file = out_file
    for row in csv_reader_2:
        # compute features for each line in the file
        links = has_links(row[TEXT_MESSAGE_COLUMN])
        spammy_word = has_spammy_words(row[TEXT_MESSAGE_COLUMN], spammy_words)
        length = str(length_of_texts(row[TEXT_MESSAGE_COLUMN]))
        num_of_symbols = str(number_of_symbols(row[TEXT_MESSAGE_COLUMN]))
        num_of_words_containing_letters_and_numbers = str(number_of_words_containing_letters_and_numbers(row[TEXT_MESSAGE_COLUMN]))
        num_of_words_containing_only_letters = str(number_of_words_containing_only_letters(row[TEXT_MESSAGE_COLUMN]))
        num_of_words_containing_only_uppercase_letters = str(number_of_words_containing_only_uppercase_letters(row[TEXT_MESSAGE_COLUMN]))
        class_label = row[CLASS_LABEL_COLUMN]

        write_features(links, spammy_word, length, num_of_symbols,
                       num_of_words_containing_letters_and_numbers, num_of_words_containing_only_letters,
                       num_of_words_containing_only_uppercase_letters, class_label, file)

    out_file.close()

    in_file_2.close()


main()
