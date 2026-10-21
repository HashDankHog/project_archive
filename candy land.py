import random

player1_total = 0
player2_total = 0

while True:
    player1 = input("please hit enter for player one to go")
    player1_move = random.randint(1,6)
    player1_total += player1_move
    print("player one rolled a", player1_move, "and now has moved", player1_total, "squares")

    if player1_total >= 30:
        print("player 1 wins")
        break
    
    player2 = input("please hit enter for player two to go")
    player2_move = random.randint(1,6)
    player2_total += player2_move
    print("player two rolled a", player2_move, "and now has moved", player2_total, "squares")

    if player2_total >= 30:
        print("player 2 wins")
        break
    
 
