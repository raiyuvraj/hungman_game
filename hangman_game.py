import random

# List of words for the game
words = ['python', 'hangman', 'computer', 'programming', 'gaming', 'code', 'developer', 'algorithm', 'debugging']

def choose_word(words):
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter + ' '
        else:
            display += '_ '
    return display

def hangman():
    word = choose_word(words)
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print("You have 6 attempts to guess the word.")
    print(display_word(word, guessed_letters))

    while True:
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            attempts -= 1
            print(f"Sorry, {guess} is not in the word. You have {attempts} attempts left.")
            if attempts == 0:
                print("Game over! The word was:", word)
                break
        else:
            print("Good guess!")

        print(display_word(word, guessed_letters))

        if all(letter in guessed_letters for letter in word):
            print("Congratulations! You guessed the word:", word)
            break

hangman()
