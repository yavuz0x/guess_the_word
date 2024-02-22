def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    print(display)

def play_game(secret_word):
    guessed_letters = []
    attempts = 6

    while attempts > 0:
        display_word(secret_word, guessed_letters)
        user_input = get_valid_input()

        if user_input in secret_word:
            print("Correct!")
            guessed_letters.append(user_input)
        else:
            print("Incorrect!")
            attempts -= 1

        if set(guessed_letters) == set(secret_word):
            print("Congratulations! You guessed the word:", secret_word)
            break

    if attempts == 0:
        print("Sorry, you ran out of attempts. The word was:", secret_word)

