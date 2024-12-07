# main.py
from word_bank import get_random_word
from game_logic import play_game

def execute():
    word = get_random_word()
    play_game(word)

if __name__ == "__main__":
    execute()