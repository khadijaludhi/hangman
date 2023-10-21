import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words) #randomly choose a word from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)
        
    return word

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    
    while len(word_letters) > 0:
        # letters that have been used 
        print('You have already used the following letters: ', ' '.join(used_letters))
        
        # display the current status of the word
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))
        
        user_letter = input('Guess a letter: ').upper()
        
        if user_letter in used_letters:
            print('You already used that character. Try again :)')
        elif user_letter in alphabet:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
        else:
            print('Invalid character. Try again :)')

hangman()