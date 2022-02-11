class word:
    """stores a word and information about a word"""
    def __init__(self, word, letter_score, four_score, three_score, four_matches, three_matches):
        self.identity = word
        self.letter_score = letter_score
        self.four_score = four_score
        self.three_score = three_score
        self.four_matches = four_matches
        self.three_matches = three_matches
        self.total_match_score = (self.four_score * 2) + self.three_score

    def identity(self):
        return self.identity

    def letter_score(self):
        return self.letter_score

    def four_score(self):
        return self.four_score

    def three_score(self):
        return self.three_score

    def total_match_score(self):
        return self.total_match_score

    def four_matches(self):
        return self.four_matches

    def three_matches(self):
        return self.three_matches

    def __str__(self):
        return self.id_string()

    def __repr__(self):
        return self.id_string()

    def id_string(self):
        return f"{self.identity} : {self.total_match_score}"


class letter:
    """stores a letter and information about a letter"""
    def __init__(self, letter, score):
        self.identity = letter
        self.score = score

    def score(self):
        return str(self.score)

    def __str__(self):
        return self.id_string()

    def __repr__(self):
        return self.id_string()

    def id_string(self):
        return f"{self.identity}"
