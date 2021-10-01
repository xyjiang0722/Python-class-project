# -*- coding: utf-8 -*-
import csv

links_column = 0
spammy_words_column = 1
length_column = 2
symbols_column = 3
class_label_column = 4


def make_prediction(links, spammy_words, length_of_text, symbols):
    # Convert the decision tree diagram into python code using conditionals
    if spammy_words == "True":
        if length_of_text <= 106:
            if links == "True":
                return True
            elif links == "False":
                return False
        elif length_of_text > 106:
            if symbols <= 13:
                if length_of_text <= 167:
                    return True
                elif length_of_text > 167:
                    if length_of_text <= 181:
                        return True
                    elif length_of_text > 181:
                        return False
            elif symbols > 13:
                return False
    elif spammy_words == "False":
        if links == "True":
            if length_of_text <= 66:
                return False
            elif length_of_text > 66:
                return True
        elif links == "False":
            return False


def write_features(link, spammy, length, symbol, actual_label, predicted_label, file):
    # write features to the file
    file.write(link)
    file.write(',')
    file.write(spammy)
    file.write(',')
    file.write(length)
    file.write(',')
    file.write(symbol)
    file.write(',')
    file.write(actual_label)
    file.write(',')
    file.write(predicted_label)

    # next line
    file.write("\n")


def main():
    # open and read the csv file and skip the first row
    in_file = open("testing_data.csv", 'r', encoding="ISO-8859-1")
    csv_reader = csv.reader(in_file, delimiter=',')
    header_row = next(csv_reader)

    # create feature.csv and its first row
    out_file = open("predictions.csv", 'a')
    out_file.write(
        'doesHaveLinks,doesHaveSpammyWords,lengthOfText,numberOfSymbols,actual_class_label,predicted_class_label')
    out_file.write("\n")

    number_of_predictions = 0
    number_of_correct_predictions = 0
    file = out_file
    for row in csv_reader:
        # obtain the features
        does_have_links = row[links_column]
        does_have_spammy_words = row[spammy_words_column]

        # set length_of_text and number_of_symbols as numbers and strings respectively since the prediction function
        # uses numbers and the write function uses strings
        length_of_text_float = float(row[length_column])
        length_of_text_str = str(row[length_column])
        number_of_symbols_float = float(row[symbols_column])
        number_of_symbols_str = str(row[symbols_column])

        actual_class_label = row[class_label_column]

        # make predictions using the features
        if make_prediction(does_have_links, does_have_spammy_words, length_of_text_float, number_of_symbols_float):
            predicted_class_label = "spam"
        else:
            predicted_class_label = "ham"

        # write features and predicted class label to the csv file
        write_features(does_have_links, does_have_spammy_words, length_of_text_str, number_of_symbols_str, actual_class_label,
                       predicted_class_label, file)

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
    # accuracy = 0.97

main()
