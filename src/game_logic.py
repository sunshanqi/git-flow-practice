# game_logic.py
def display_word(word, guessed_letters):
    pass
    # """Displays the word with guessed letters revealed and the rest as underscores."""
    # return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def play_game(word):
    pass
    # guessed_letters = set()
    # attempts = 6
    # print("Welcome to the Word Guessing Game!")

    # while attempts > 0:
    #     print("\nWord: ", display_word(word, guessed_letters))
    #     print(f"Remaining attempts: {attempts}")
    #     guess = input("Guess a letter: ").lower()

    #     if guess in guessed_letters:
    #         print("You already guessed that letter. Try again!")
    #     elif guess in word:
    #         print(f"Good guess! '{guess}' is in the word.")
    #         guessed_letters.add(guess)
    #     else:
    #         print(f"Wrong guess! '{guess}' is not in the word.")
    #         attempts -= 1

    #     if all(letter in guessed_letters for letter in word):
    #         print("\n🎉 Congratulations! You guessed the word:", word)
    #         return True

    # print("\n😞 You've run out of attempts! The word was:", word)
    # return False