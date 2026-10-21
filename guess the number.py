import random

number = random.randint(1,10)
guess = 0


while True:
    game = int(input("guess a number between 1 and 10: "))

    if game == number:
        guess = guess + 1
        print("congrats you got it rightand it took", guess,"guesses to find it")

    elif game >= number:
        print("guess lower")
        guess = guess + 1
    elif game <= number:
        print("guess higher")
        guess = guess + 1    
    else:
        print("sorry that doesnt make sense")
