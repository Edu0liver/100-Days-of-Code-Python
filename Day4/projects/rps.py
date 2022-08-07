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
game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

computer_choice = random.randint(0, 2)

if computer_choice == 0 and user_choice == 0:
    print(f"{game_images[user_choice]}\n{game_images[computer_choice]}\nDraw!")

elif computer_choice == 0 and user_choice == 1:
    print(f"{game_images[user_choice]}\n{game_images[computer_choice]}\nYou Win!")

elif computer_choice == 0 and user_choice == 2:
    print(f"{game_images[user_choice]}\n{game_images[computer_choice]}\nYou Lose!")

##########################################################################

elif computer_choice == 1 and user_choice == 0:
    print(f"{game_images[user_choice]}\n{game_images[computer_choice]}\nYou Lose!")

elif computer_choice == 1 and user_choice == 1:
    print(f"{game_images[user_choice]}\n{game_images[computer_choice]}\nDraw!")

elif computer_choice == 1 and user_choice == 2:
    print(f"{game_images[user_choice]}\n{game_images[computer_choice]}\nYou Win!")

##########################################################################

elif computer_choice == 2 and user_choice == 0:
    print(f"{game_images[user_choice]}\n{game_images[computer_choice]}\nYou Win!")

elif computer_choice == 2 and user_choice == 1:
    print(f"{game_images[user_choice]}\n{game_images[computer_choice]}\nYou Lose!")

elif computer_choice == 2 and user_choice == 2:
    print(f"{game_images[user_choice]}\n{game_images[computer_choice]}\nDraw!")

