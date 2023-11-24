rock =("""
_______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
import random

your_choice=int(input("What do you choose? Type 0 for Rcok, 1 for Paper, 2 for Scissors"))
computers_choice = random.randint(0, 2)

choices = [rock, paper, scissors]
print(choices[your_choice])
print("computer chose")
print(choices[computers_choice])

if your_choice >= 3 or your_choice < 0:
    print("you typed a wrong number")

if your_choice == 0 and computers_choice == 2:
    print("you win")
elif computers_choice == 0 and your_choice == 2:
    print("you lose")
elif your_choice < computers_choice:
    print("you lose")
elif your_choice > computers_choice:
    print("you win")
elif your_choice == computers_choice:
    print("you draw")