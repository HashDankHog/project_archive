number = int(input("please choose a seed number: "))
steps = 0
run = True

print()

while run:
    print("number:", number)
    if number % 2 == 0:
        number = number/2
        steps += 1
    else:
        number = number*3+1
        steps += 1
    if number == 4:
        run = False
print()
print("steps:",steps)
    
