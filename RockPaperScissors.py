import random
from tkinter import image_names

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

images = [rock, paper, scissors]

player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
print(images[player])

computer = random.randint(0, 2)
print("Computer chose:")
print(images[computer])

if player >= 3 or player < 0:
    print("You typed an invalid number. You lose!")

elif player == 0 and computer == 2:
    print("You Win!")
elif computer == 0 and player == 2:
    print("You lose!")
elif computer > player:
    print("You lose!")
elif player > computer:
    print("You Win!")
elif computer == player:
    print("It's a draw!")
