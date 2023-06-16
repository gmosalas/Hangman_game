# Import the random module
import random

# Create a list of words
word_list = []
with open('random_words.txt', 'r') as f:
    # Read each line of the text file
    for line in f:
        # Split the line into separate words
        words = line.strip().split()
        # Add the words to the word list
        word_list.extend(words)

# Randomly select a word from the list and add it to a variable
secret_word = random.choice(word_list)
print(secret_word)
# Start with an empty list to keep track of the guesses
guessed_letters = []
used_letters = []
# Define valid characters
valid_letters = [chr(i) for i in range(ord('a'), ord('z')+1)] + [chr(i) for i in range(ord('A'), ord('Z')+1)]

# Create a variable to check for attempts, and it stars at 6
attempts = 6

while attempts > 0:
    # Ask the user to guess a letter and add it to a variable
    display_word = ''.join([letter if letter in guessed_letters else '_' for letter in secret_word])
    print(display_word)
    print(f"Used letters {used_letters}")
    print(f"You have {attempts} attempts left")
    guess = input("Guess a letter: ")
    # Check that the letters have been guessed only once
    if guess in used_letters:
        print("You have chosen that letter already. Try again")
    # Make sure the guess is only one letter
    elif len(guess) != 1 or guess not in valid_letters:
        print("Invalid input. Try again")
    # Check the guess from the user and compare it to the secret word
    elif guess in secret_word:
        # If the user's guess is in the secret word, print the word but only revealing the letter guessed
        guessed_letters.append(guess)
        used_letters.append(guess)
        print("Correct!")
    # If the guessed letter not in the word, subtract one attempt
    elif guess not in secret_word:
        print("Incorrect guess. Try again")
        attempts -= 1
        used_letters.append(guess)

    if all(letter in guessed_letters for letter in secret_word):
        print(f'You win! The word was: {secret_word}')
        break

    # If attempts == 0 game over
    if attempts == 0:
        print("You've been hanged. No more guesses left")
        print(f'The word was: {secret_word}')
        break
