def score_word(word, score_table):
    """ Receives a word and calculates its total score
        by adding up the score of each letter in word.
        Score is found in the score_table entered.
    """
    score = 0
    for letter in word.lower():
        score += score_table[letter]
    return score