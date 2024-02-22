def get_valid_input():
    while True:
        user_input = input("Enter a letter: ").lower()
        if user_input.isalpha() and len(user_input) == 1:
            return user_input
        else:
            print("Invalid input. Please enter a single letter.")
