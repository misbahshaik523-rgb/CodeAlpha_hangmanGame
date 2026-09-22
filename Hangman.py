import random

# The five words that can be selected for the game.
words = ["python", "internship", "computer", "keyboard", "developer"]

# Select one word randomly.
secret_word = random.choice(words)

# Keep track of letters guessed by the player.
guessed_letters = []

# Display an underscore for every hidden letter.
display_word = ["_"] * len(secret_word)

# The player can make up to six incorrect guesses.
incorrect_guesses = 0
maximum_incorrect_guesses = 6

print("Welcome to Hangman!")
print("Guess the word one letter at a time.")

# Continue until the player wins or uses all six incorrect guesses.
while incorrect_guesses < maximum_incorrect_guesses and "_" in display_word:
    print("\nWord:", " ".join(display_word))
    print("Remaining attempts:", maximum_incorrect_guesses - incorrect_guesses)

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1:
        print("Please enter exactly one letter.")
    elif guess in guessed_letters:
        print("You already guessed that letter.")
    elif guess not in "abcdefghijklmnopqrstuvwxyz":
        print("Please enter a letter from A to Z.")
    else:
        guessed_letters.append(guess)

        if guess in secret_word:
            print("Correct guess!")

            position = 0
            while position < len(secret_word):
                if secret_word[position] == guess:
                    display_word[position] = guess
                position = position + 1
        else:
            incorrect_guesses = incorrect_guesses + 1
            print("Incorrect guess.")

if "_" not in display_word:
    print("\nCongratulations! You guessed the word:", secret_word)
else:
    print("\nGame over! The word was:", secret_word)

print("Final word:", " ".join(display_word))
