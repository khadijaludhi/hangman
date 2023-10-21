import random
from words_list import words

def get_valid_word(words):
    word = random.choice(words) #randomly choose a word from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)
        
    return word

