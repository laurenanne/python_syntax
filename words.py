def print_upper_words(words, letters):
    """takes a string of words and return the words in uppercase"""
    cap_letters = letters.upper()
    
    for word in words:
        cap_word = word.upper()
        for letter in cap_letters:
            if cap_word.startswith(letter):    
                print(word.upper())
        
    

#print_upper_words(["hello", "hey", "goodbye", "yo", "yes"])