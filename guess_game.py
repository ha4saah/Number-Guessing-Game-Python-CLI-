import random

def welcome():
    print("Welcome to Number Guessing Game")
    print("Created by Ha4saah")

def choose_difficulty():
    try:
        choice = int(input("Select your difficulty level: \n1. Easy (10 guesses)\n2. Medium (5 guesses)\n3. Hard (3 guesses)\nEnter: "))
        if choice == 1:
            return 10, "EASY"
        elif choice == 2:
            return 5, "MEDIUM"
        elif choice == 3:
            return 3, "HARD"
        else:
            print("Error: Invalid choice. Try Again.")
            return None, None
    except ValueError:
        print("Error: Please enter a number (1, 2 or 3).")
        return None, None

def get_guess():
    try:
        guess = int(input("Enter your guessed number: "))
        if 1 <= guess <= 100:
            return guess
        else:
            print("Enter a correct number between 1 and 100.")
            return None
    except ValueError:
        print("Invalid input! Please enter a number.")
        return None

def play_game():
    welcome()
    attempts, difficulty = choose_difficulty()
    if attempts is None:
        return

    print(f"Difficulty: {difficulty}")
    target = random.randint(1, 100)
    print("I am thinking of a number between 1 and 100")

    turn = 1
    while turn <= attempts:
        guess = get_guess()
        if guess is None:
            continue

        if guess == target:
            print("YOU GUESSED IT RIGHT!\nThe number was", guess)
            return
        else:
            print("Wrong\nTry Again")
            if guess < target:
                print("Hint: Try a HIGHER number.")
            else:
                print("Hint: Try a LOWER number.")
        turn += 1

    print("You lose! The correct number was", target)

# Run the game
play_game()
