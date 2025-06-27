import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
options = [rock, paper, scissors]

player = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors\n"))
if player < 0 or player > 2:
    print("Invalid Option, try again")
else:
    print(options[player])

    computer = random.randint(0, 2)
    print(f"Computer chose:\n{options[computer]}")

    if (player == 0 and computer == 2) or (player == 1 and computer == 0) or (player == 2 and computer == 1):
        print("You Win")
    elif player == computer:
        print("It's a Draw")
    else:
        print("You Lose")
