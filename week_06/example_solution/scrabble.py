import sys
from scores import score_word

def has_num(text):
    return any(char.isdigit() for char in text)

def scrabble(args):
    if len(args) > 2:
        raise Exception("More than one argument. Must use one string for scrabble rack.")
    elif len(args) < 2:
        raise Exception("Needs a rack of up to 7 letters including up to two wildcards: * or ?")
    elif len(args[1]) > 7:
        raise Exception("Too many characters in scrabble rack. Try again.")
    elif args[1].count("*") > 1 or args[1].count("?") > 1:
        raise Exception("Too many wildcards. Try again.")
    elif has_num(args[1]):
        raise Exception("Contains number(s). Try again.")
    else:
        # 1. Get rack
        rack = str(args[1]).upper()

        # 2. Read in text file of all words
        with open("sowpods.txt","r") as infile:
            raw_input = infile.readlines()
            all_words = [datum.strip('\n') for datum in raw_input]
       
        # 3. Go thru every word in the valid word list
        valid_words = []
        for word in all_words:
            temp = [c for c in rack]
            count = 0
            for char in word:
                if char in temp:
                    count += 1
                    temp.remove(char)
                elif "*" in temp:
                    count += 1
                    temp.remove("*")
                elif "?" in temp:
                    count += 1
                    temp.remove("?")
                else:
                    break
                if len(word) == count:
                    valid_words.append(word.lower())

        # 4. Score each word in the list using score dict
        scored_list = []
        for word in valid_words:
            scored_list.append([score_word(word, rack), word])
        sorted_scores = sorted(scored_list)
        for pair in sorted_scores[::-1]:
            print("(" + str(pair[0]) + ", " + str(pair[1]) + ")")
        print("Total number of words:", len(sorted_scores))
        return None

try:
    scrabble(sys.argv)
except Exception as e:
    print(str(e))