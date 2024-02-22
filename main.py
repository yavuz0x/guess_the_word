from word_generator import generate_word
from input_validator import get_valid_input
from game_logic import play_game

def main():
    print("Welcome to Guess the Word Game!")
    secret_word = generate_word()
    play_game(secret_word)

if __name__ == "__main__":
    main()
