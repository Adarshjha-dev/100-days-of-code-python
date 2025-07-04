import random
import art


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
    return random.choice(cards)


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    while 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(player_score, computer_score):
    if player_score == computer_score:
        return "It's a draw."
    elif computer_score == 0:
        return "Computer has Blackjack. You lose."
    elif player_score == 0:
        return "Blackjack! You win."
    elif player_score > 21:
        return "You went over 21. You lose."
    elif computer_score > 21:
        return "Computer went over 21. You win!"
    elif player_score > computer_score:
        return "You win with a higher score!"
    else:
        return "Computer wins with a higher score."


def play_game():
    print(art.logo)
    player_cards = []
    computer_cards = []
    player_score = -1
    computer_score = -1
    game_over = False

    for _ in range(2):
        player_cards.append(deal_card())
        computer_cards.append(deal_card())
    while not game_over:
        player_score = calculate_score(player_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {player_cards}, current score: {player_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if player_score == 0 or computer_score == 0 or player_score >= 21:
            game_over = True
        else:
            user_choice = input(
                "Type 'y' to draw another card, or 'n' to stand: "
            ).lower()
            while user_choice not in ["y", "n"]:
                user_choice = input(
                    "Please type 'y' to draw another card, or 'n' to stand: "
                ).lower()
            if user_choice == "y":
                player_cards.append(deal_card())
            else:
                game_over = True
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    print(f"Your cards: {player_cards}, final score: {player_score}")
    print(f"Computer's cards: {computer_cards}, final score: {computer_score}")
    print(compare(player_score, computer_score))


while input("Welcome to Blackjack! Type 'y' to play or 'n' to quit: ").lower() == "y":
    print("\n" * 20)
    play_game()
