# -*- coding: utf-8 -*-
# Name: Xiaoyan Jiang
import csv

links_column = 0
spammy_words_column = 1
length_column = 2
symbols_column = 3
words_column = 4
class_label_column = 5


def make_prediction(spammy_words):
    # Convert the decision tree diagram into python code using conditionals
    if spammy_words == "True":
        return True
    elif spammy_words == "False":
        return False
    # the decision tree diagram created using my feature.csv only has two branches: doesHaveSpammyWords == True ->
    # spam; doesHaveSpammyWords == False -> ham. This happened because in my features.csv, I included all the words
    # that are in the spam messages but not in the ham messages. So the prediction can be accurate only using the
    # feature doesHaveSpammyWords. In the classifier output summary in Weka, the correctly classfied instances is
    # 99.9265%.


def write_features(link, spammy, length, symbol, words, actual_label, predicted_label, file):
    # write features to the file
    file.write(link)
    file.write(',')
    file.write(spammy)
    file.write(',')
    file.write(length)
    file.write(',')
    file.write(symbol)
    file.write(',')
    file.write(words)
    file.write(',')
    file.write(actual_label)
    file.write(',')
    file.write(predicted_label)

    # next line
    file.write("\n")


def main():
    # open and read the csv file and skip the first row
    in_file = open("extra_credit_testing_data.csv", 'r', encoding="ISO-8859-1")
    csv_reader = csv.reader(in_file, delimiter=',')
    header_row = next(csv_reader)

    # create feature.csv and its first row
    out_file = open("extra_credit_predictions.csv", 'a')
    out_file.write('doesHaveLinks,doesHaveSpammyWords,lengthOfText,numberOfSymbols,'
                   'numberOfWordsContainingLettersAndNumbers,actual_class_label,predicted_class_label')
    out_file.write("\n")

    number_of_predictions = 0
    number_of_correct_predictions = 0
    file = out_file
    for row in csv_reader:
        # obtain the features
        does_have_links = row[links_column]
        does_have_spammy_words = row[spammy_words_column]
        length_of_text = str(row[length_column])
        number_of_symbols = str(row[symbols_column])

        number_of_words_containing_both = str(row[words_column])
        actual_class_label = row[class_label_column]

        # make predictions using the features
        if make_prediction(does_have_spammy_words):
            predicted_class_label = "spam"
        else:
            predicted_class_label = "ham"

        # write features and predicted class label to the csv file
        write_features(does_have_links, does_have_spammy_words, length_of_text, number_of_symbols,
                       number_of_words_containing_both, actual_class_label, predicted_class_label, file)

        # count the total number of predictions
        number_of_predictions += 1

        # count the  number of correct predictions
        if actual_class_label == predicted_class_label:
            number_of_correct_predictions += 1

    out_file.close()
    in_file.close()

    # compute accuracy
    accuracy = number_of_correct_predictions / number_of_predictions
    print(accuracy)
    # accuracy = 0.985


main()
