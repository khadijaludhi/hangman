import random
from words_list import words

def get_valid_word(words):
    word = random.choice(words) #randomly choose a word from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)
        
    return word

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) #letters in the word
    alphabet = set(string.ascii.uppercase)
    used_letters = set()
    
    user_letter = input('Guess a letter: ').upper()
    if user_letter in alphabet - used_letters:
        used_letters.add(used_letters)
        if user_letter in word_letters:
            word_letters.remove(user_letter)
            
        elif user_letter in used_letters:
            print('You already used that character. Try again :)')
            
        else:
            print('Invalid character, try again')

user_input = input('Type a character: ')
print (user_input)