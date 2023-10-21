import random
from words import words
import string
from hangman_visual import lives_visual  # Import the visual representation of the hangman

# Function to retrieve a valid word from the provided list
def get_valid_word(words):
    # Pick a random word from the list
    word = random.choice(words)
    
    # Ensure the word doesn't contain '-' or ' ' (spaces)
    while '-' in word or ' ' in word:
        word = random.choice(words)
        
    # Return the chosen word in uppercase
    return word.upper()

# Main function to run the hangman game
def hangman():
    # Get a valid word for the game
    word = get_valid_word(words)
    
    # Extract unique letters from the word
    word_letters = set(word)
    
    # Define the allowable alphabet for the game
    alphabet = set(string.ascii_uppercase)
    
    # Initialize an empty set to store letters that have been used by the player
    used_letters = set()
    
    # Initialize the player's lives count
    lives = 7
    
    # Game loop: Continue as long as there are letters to guess and player has lives remaining
    while len(word_letters) > 0 and lives > 0:
        # Display the hangman visual based on the number of lives left
        print(lives_visual[7 - lives])
        
        # Display letters that have been guessed so far
        print('You have', lives, 'lives left. And you have already used the following letters: ', ' '.join(used_letters))
        
        # Show the current state of the word (display guessed letters, hide the rest with '-')
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))
        
        # Get a letter guess from the player
        user_letter = input('Guess a letter: ').upper()
        
        # Check if the letter has been guessed before
        if user_letter in used_letters:
            print('You already used that character. Try again :)')
        # Check if the guessed letter is in the allowed alphabet
        elif user_letter in alphabet:
            used_letters.add(user_letter)  # Add the letter to the set of used letters
            # Check if the guessed letter is in the target word
            if user_letter in word_letters:
                word_letters.remove(user_letter)  # If yes, remove the letter from the set of letters to be guessed
            else:
                lives -= 1  # If no, decrement the player's lives count
                print('Looks like you guessed the wrong letter.')
        else:
            # If the guessed letter isn't in the allowed alphabet, show an error message
            print('Invalid character. Try again :)')
            
    # End-game scenarios
    # Check if the player has run out of lives
    if lives == 0:
        print("And it appears that you're dead... How sad. ANYWAY, the word that cost you your life was", word)
    else:
        # Player has guessed the word correctly
        print('You guessed the word', word, '! Looks like you get to live for just a teensy bit longer :)')

# Execute the hangman game
hangman()
