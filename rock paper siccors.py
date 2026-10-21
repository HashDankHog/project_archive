import random

computer_choice = random.randint(1,3)
player_choice = int(input("rock paper or siccers. 1. for rock 2. for paper 3. for siccors"))


if player_choice == computer_choice:
    print("you chose option number", player_choice,"and the computer chose option number", computer_choice, "so it is a tie")
                    
elif player_choice == 1 and computer_choice == 3 or player_choice == 2 and computer_choice == 1 or player_choice == 3 and computer_choice == 1:
    print("you chose option number", player_choice,"and the computer chose option number", computer_choice, "so you win")
else:
    print("you chose option number", player_choice,"and the computer chose option number", computer_choice, "so you lose")
