import random

words = ["abacus", "bamboo",  "computer", "dog", "eagle", "falling", "great", "heart", "ink", "jump", "kite", "leg",  "milk", "nice", "open", "parked", "queen", "road", "sight", "train", "umbrella", "vaccum", "water", "x ray", "yoyo", "zippper"]

word = random.choice(words)
turns = 6
guesses = " "

while turns > 0:
    player = input("please guess any letter t osee if its in the word (do not us capitails when typing or spaces)")
    guesses += player

    for char in word: 
         
        if char in guesses: 
            print(char)
             
        else: 
            print("_")

    if player not in word:
        turns -= 1

