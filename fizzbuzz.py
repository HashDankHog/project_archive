num = 0
output = ""

while num < 100:
    num += 1
    output = ""
    if num % 3 == 0:
        output += "fizz"
    elif num % 5 == 0:
        output += "buzz"
    else:
        output += str(num)

    print(output)
