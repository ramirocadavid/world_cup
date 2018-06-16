def is_consonant_j(char):
    '''A function to check if a character is a consonant. Will return Boolean value'''
    # use list of consonants rather than vowels here- just in case there is a non-letter character?
    consonants = "bcdfghjklmnpqrstvwxyz"
    if char.lower() in consonants:
        return(True)
    else:
        return(False)
    
def to_piglatin_j(words):
    '''A script to translate a string of words or a sentence into pig latin.'''
    words_list = words.split()
    pig_words = []
    
    for i in words_list:

        # check to see how many letters to put to back
        consonant_check_list = [is_consonant(x) for x in i]
        number_to_keep = 0
        for cons_bool in consonant_check_list:
            if cons_bool:
                number_to_keep += 1
            else:
                break
        
        # check to see if word was capitalized
        if i[0] in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
            capitalized = True
        else:
            capitalized = False
        
        # check to see if word contains associated period
        if "." in i:
            has_period = True
            i = i[0:len(i)-1]
        else:
            has_period = False
        
        #set case where the first letter was not a consonant
        if number_to_keep == 0:
            string_to_add = "ay"
            new_str = (i + string_to_add).lower()
        else:
            string_to_add = i[0:(number_to_keep)] + "ay"
            new_str = (i[number_to_keep:len(i)] + string_to_add).lower()

        # capitalize the word if it was originally capitalized
        if capitalized:
            new_str = new_str.capitalize()
        
        # add back a period if it originally had one
        if has_period:
            new_str = new_str + "."
        
        pig_words.append(new_str)
        
    return(" ".join(pig_words))
	
def is_consonant_k(letter):
    vowel = 'aeiou'
    if letter not in vowel:
        ans = True
        return ans
    else:
        ans = False
        return ans

def to_piglatin_k(word):
    if word[0].isupper():
        capital = True
    else:
        capital = False        
    
    new_word = word.lower()
    for letter in word:
        if is_consonant(letter) == True:
            new_word = new_word[1:] + new_word[0]
        else:
            new_word = new_word + 'ay'
            if capital == True:
                new_word = new_word.capitalize()
            print(new_word)
            return(new_word)