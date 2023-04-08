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

#Write your code below this line 👇
import random
game = [rock, paper, scissors]

player_choice = int(input("Rock, paper, scissors?\n Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

print(game[player_choice])

#Comp_choice = random.choice(game)
#print(Comp_choice)

comp_choice = random.randint(0, 2)
print(f"Comp's choice:\n{game[comp_choice]}")

if player_choice >= 3 or player_choice < 0:
  print("You typed an invalid number, you lose!")
elif player_choice == 0 and comp_choice == 2:
  print("You win!")
elif player_choice == 2 and comp_choice == 0:
  print("You lose!")
elif comp_choice > player_choice:
  print("You lose")
elif player_choice > comp_choice:
  print("You win!")
elif comp_choice == player_choice:
  print("It's a draw")