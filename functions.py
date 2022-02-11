import json
from classes import word
from classes import letter
from difflib import SequenceMatcher


def get_dictionary():
    """Pulls the dictionary list from the json file"""
    with open('lists/dictionary.json', 'r+') as dictionary_json:
        dictionary = json.load(dictionary_json)
    return dictionary


def get_letters(dictionary):
    """Gets the alphabet for this dictionary"""
    glue_string = ''
    for word in dictionary:
        glue_string += word
    return sorted(list(set(list(glue_string))))


def letter_count(dictionary, alphabet):
    """Takes the letters and returns their frequencies in the dictionary in dict form"""
    alphabet_scores = {k: 0 for k in alphabet}
    for word in dictionary:
        for individual_letter in word:
            alphabet_scores[individual_letter] += 1
    ordered_scores = {k: v for k, v in sorted(alphabet_scores.items(), key=lambda item: item[1])}
    final_scores = {}
    indexer = len(ordered_scores)
    while indexer > 0:
        final_scores[list(ordered_scores)[indexer - 1]] = indexer
        indexer -= 1
    return final_scores


def letter_maker(letter_list):
    """Turns the scores from other functions into 'letter' objects"""
    letter_values = []
    for individual_letter in letter_list:
        letter_values.append(letter(individual_letter, letter_list[individual_letter]))
    return letter_values


def word_maker(letters, dictionary):
    new_dictionary = []
    for entry in dictionary:
        letter_score = get_letter_score(entry, letters)
        four_score, four_matches = get_four_score(entry, dictionary)
        three_score, three_matches = get_three_score(entry, dictionary)
        new_word = (word(entry, letter_score, four_score, three_score, four_matches, three_matches))
        print(new_word)
        new_dictionary.append(new_word)
    return new_dictionary


def get_letter_score(word, letters):
    letter_score = 0
    for each in list(word):
        for every in letters:
            if str(every) == each:
                letter_score += every.score
    return(letter_score)


def get_four_score(entry, dictionary):
    four_matches = []
    four_score = 0
    for each in dictionary:
        if SequenceMatcher(None, entry, each).ratio() == 0.8:
            four_matches.append(each)
            four_score += 1
    return four_score, four_matches


def get_three_score(entry, dictionary):
    three_matches = []
    three_score = 0
    for each in dictionary:
        if SequenceMatcher(None, entry, each).ratio() == 0.6:
            three_matches.append(each)
            three_score += 1
    return three_score, three_matches
