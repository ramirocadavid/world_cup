from score_word import score_word
import sys

""" Receives a sequence of characters, representing a Scrabble rack,
    and returns all the possible combinations of these characters that
    are valid words in Scrabble, with the corresponding score for
    each. Allows up to two wild cards to be entered as '*' or '?'.
"""

# Import letter scoring dictionary
scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
        "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
        "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
        "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
        "x": 8, "z": 10, '*': 0, '?': 0}

# Import words dictionary
with open("sowpods.txt","r") as infile:
    raw_input = infile.readlines()
    data = [datum.strip('\n') for datum in raw_input]


# # INPUTS VALIDATION

# # Enter only two arguments (function and characters)
# if len(sys.argv) == 1:
#     raise Exception("Characters should be entered. You did not enter characters argument.")
# if len(sys.argv) > 2:
#     raise Exception("Only one argument should be entered (characters). You have entered more than one argument.")

# # Allow anywhere from 2-7 character tiles to be inputted
# if len(sys.argv[1]) < 2 or len(sys.argv[1]) > 7:
#     raise Exception("Enter 2-7 characters. You have entered less than 2 or more than 7 characters.")

# # There can be a total of two wild cards in any user input (one of each character).
# #  Only use the * and ? as wildcard characters
chars = sys.argv[1]
# if chars.count('*') + chars.count('?') > 2:
#     raise Exception("Make sure to enter up to two wildcards ('*' or '?'). You have entered more than two.")

# # Entered a character not defined in the dictionary
# for char in chars:
#     if char.lower() not in scores.keys():
# 	    raise Exception("Invalid character: \'" + char + "\'. Enter only English alphabet characters or wildcards ('*' or '?')")


# VALID WORDS AND SCORES

results = []
# For each valid word
for word in data:
    rack = chars.lower()
    word_score = word.lower()
    word = word.lower()
    # Check if each character in the word exists in the tiles available (or if a wildcard can be used)
    for i in range(len(word)):
        if word[i] in rack:
            rack = rack.replace(word[i], '', 1)
        elif '*' in rack:
            word_score = word_score[:i] + '*' + word_score[i + 1:]
            rack = rack.replace('*', '', 1)
        elif '?' in rack:
            word_score = word_score[:i] + '?' + word_score[i + 1:]
            rack = rack.replace('?', '', 1)
        else:
            break
    # If all the characters in the word can be formed from the tiles, add it to results
    else:
        word_score = word_score.lower()
        results.append((score_word(word_score, scores), word.lower()))

# Sort words by score (use merge_sort algorithm)
for i in range(1, len(results)):
    while i > 0:
        if results[i][0] > results[i - 1][0]:
            temp = results[i]
            results[i] = results[i - 1]
            results[i - 1] = temp
        i -= 1

# Print results
for result in results:
    print('(' + str(result[0]) + ', ' + str(result[1]) + ')', end = '\n')
print('Total number of words:', len(results))