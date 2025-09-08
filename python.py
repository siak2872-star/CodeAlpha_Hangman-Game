import random

def hangman():
    words = ["python", "code", "alpha", "intern", "script"]
    chosen_word = random.choice(words)
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print("_ " * len(chosen_word))

    while attempts > 0:
        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in chosen_word:
            print("Good guess!")
        else:
            attempts -= 1
            print(f"Wrong guess! Attempts left: {attempts}")

        # Display current progress
        word_display = ""
        for letter in chosen_word:
            if letter in guessed_letters:
                word_display += letter + " "
            else:
                word_display += "_ "
        print(word_display.strip())

        # Win condition
        if all(letter in guessed_letters for letter in chosen_word):
            print("Congratulations! You guessed the word correctly!")
            break
    else:
        print(f"Game over! The word was: {chosen_word}")

# Run the game
if __name__ == "__main__":
    hangman()
