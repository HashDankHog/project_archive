x = 0
y = 0

print("* * *")
print("* * *")
print("p * *")
while True:

    #takes user input
    user_input = input("what direction would you liket to go w for forward a for left s for backwards and d for right: ")

    #interprets user input
    if user_input == "w":
        y = y + 1
    elif user_input == "a":
        x = x - 1
    elif user_input == "s":
        y = y - 1
    elif user_input == "d":
        x = x + 1
    #sees if the user typed something besides wasd
    else:
        print("sorry that doenst make sense")
        
    #figures out where the user actually is
    if y == 0 and x == 0:
        print("* * *")
        print("* * *")
        print("p * *")
    elif y == 1 and x == 0:
        print("* * *")
        print("p * *")
        print("* * *")
    elif y == 2 and x == 0:
        print("p * *")
        print("* * *")
        print("* * *")
    elif y == 0 and x == 1:
        print("* * *")
        print("* * *")
        print("* p *")
    elif y == 1 and x == 1:
        print("* * *")
        print("* p *")
        print("* * *")
    elif y == 2 and x == 1:
        print("* p *")
        print("* * *")
        print("* * *")
    elif y == 0 and x == 2:
        print("* * *")
        print("* * *")
        print("* * p")
    elif y == 1 and x == 2:
        print("* * *")
        print("* * p")
        print("* * *")
    elif y == 2 and x == 2:
        print("* * p")
        print("* * *")
        print("* * *")

    #makes sure that if the player tries to go off screen they will fail and resets there position
    else:
        x = 0
        y = 0
