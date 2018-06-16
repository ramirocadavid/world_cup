def score_word(word, score_table):
    """ Receives a word and calculate its total score
        by adding up the score of each letter in word.
        Score is found in the score table entered.
    """
    score = 0
    for letter in word:
        score += score_table[letter]
    return score