import random

itterations = int(input("how many dice rolls do you want: "))

dice1 = random.randint(1,6)
dice2 = random.randint(1,6)
dicerolls = 0

total = dice1 + dice2

rolls_2 = 0
rolls_3 = 0
rolls_4 = 0
rolls_5 = 0
rolls_6 = 0
rolls_7 = 0
rolls_8 = 0
rolls_9 = 0
rolls_10 = 0
rolls_11 = 0
rolls_12 = 0

while dicerolls < itterations:
    

     dicerolls += 1
     
     dice1 = random.randint(1,6)
     dice2 = random.randint(1,6)
     total = dice1 + dice2
     
     print(total, dicerolls)

     
     if total == 2:
         rolls_2 += 1
     elif total == 3:
         rolls_3 += 1
     elif total == 4:
         rolls_4 += 1
     elif total == 5:
         rolls_5 += 1
     elif total == 6:
         rolls_6 += 1
     elif total == 7:
         rolls_7 += 1
     elif total == 8:
         rolls_8 += 1
     elif total == 9:
         rolls_9 += 1
     elif total == 10:
         rolls_10 += 1
     elif total == 11:
         rolls_11 += 1
     elif total == 12:
         rolls_12 += 1

print("the times 2 were rolled was:", rolls_2)
print("the times 3 were rolled was:", rolls_3)
print("the times 4 were rolled was:", rolls_4)
print("the times 5 were rolled was:", rolls_5)
print("the times 6 were rolled was:", rolls_6)
print("the times 7 were rolled was:", rolls_7)
print("the times 8 were rolled was:", rolls_8)
print("the times 9 were rolled was:", rolls_9)
print("the times 10 were rolled was:", rolls_10)
print("the times 11 were rolled was:", rolls_11)
print("the times 12 were rolled was:", rolls_12)
