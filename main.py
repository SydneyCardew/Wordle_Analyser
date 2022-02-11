from classes import word
from classes import letter
import functions as f
import csv


def main():
    main_dictionary = f.get_dictionary()
    alphabet = f.get_letters(main_dictionary)
    letters = f.letter_maker(f.letter_count(main_dictionary, alphabet))
    words = f.word_maker(letters, main_dictionary)
    with open('Output/five_letter_words.csv', 'w+') as sheet:
        writer = csv.writer(sheet)
        top_row = ['Name', 'Letter Score', 'Four Letter Matches', 'Three Letter Matches', 'Four Letter Words',
                   'Three Letter Words', 'Total Matches']
        writer.writerow(top_row)
        for entry in words:
            new_row = [entry.identity, entry.letter_score, entry.four_score,
                       entry.three_score, entry.four_matches, entry.three_matches, entry.total_match_score]
            writer.writerow(new_row)


if __name__ == "__main__":
    main()
