import random
from art import logo, vs
from game_data import data


def format_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description} from {country}."


def is_correct(choice, a_followers, b_followers):
    if choice == "A":
        return a_followers > b_followers
    elif choice == "B":
        return b_followers > a_followers
    else:
        return False


def game():
    print(logo)
    score = 0
    game_over = False
    account_a = random.choice(data)

    while not game_over:
        account_b = random.choice(data)
        while account_b == account_a:
            account_b = random.choice(data)
        print(f"Compare A: {format_data(account_a)}")
        print(vs)
        print(f"Against B: {format_data(account_b)}")

        guess = input("Who has more followers? Type 'A' or 'B': ").upper()
        print("\n" * 20)
        print(logo)
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        if is_correct(guess, a_follower_count, b_follower_count):
            score += 1
            print(f"You are right! Current Score: {score}")
            if b_follower_count > a_follower_count:
                account_a = account_b
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            game_over = True


game()
