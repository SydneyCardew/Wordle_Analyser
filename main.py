import functions as f


def main():
    """Main program"""
    main_dictionary = f.get_dictionary()
    alphabet = f.get_letters(main_dictionary)
    letters = f.letter_maker(f.letter_count(main_dictionary, alphabet))
    words = f.word_maker(letters, main_dictionary)
    f.make_csv(words)


if __name__ == "__main__":
    main()
