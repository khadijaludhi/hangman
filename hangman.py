import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)  # randomly choose a word from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)
        
    return word.upper()  # Convert word to uppercase

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    
    lives = 7
    
    while len(word_letters) > 0 and lives > 0:
        # letters that have been used 
        print('You have', lives, 'lives left. And you have already used the following letters: ', ' '.join(used_letters))
        
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
                lives = lives - 1 # removes a life
                print('Looks like you guessed the wrong letter.')
        else:
            print('Invalid character. Try again :)')
            
    # gets here when len(word_letters) == 0 OR when the lives == 0
    if lives == 0:
        print('You died... How sad. ANYWAY, the word that cost you your life was', word)
    else:
        print('You guessed the word', word, '! Looks like you get to live for just a teensy bit longer :)')

hangman()
