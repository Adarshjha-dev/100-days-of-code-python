import art
import random

def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        return 10
    else:
        return 5

def check_guess(guess, number):
    if guess > number:
        print("Too high.")
        return False
    elif guess < number:
        print("Too low.")
        return False
    else:
        print(f"Congratulations! You guessed it. The number was {number}.")
        return True

def play_game():
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    number = random.randint(1, 100)
    chances = set_difficulty()
    game_over = False

    while not game_over:
        print(f"\nYou have {chances} attempts remaining.")
        guess = int(input("Make your guess: "))

        is_correct = check_guess(guess, number)
        if is_correct:
            game_over = True
        else:
            chances -= 1
            if chances == 0:
                print(f"You've run out of attempts. The correct number was {number}.")
                game_over = True
            else:
                print("Try again.")

play_game()
