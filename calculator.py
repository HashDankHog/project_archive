operation = input("choose what operation you want to do: ")
number1 = int(input("choose your first number: "))
number2 = int(input("choose your second number: "))

if operation == "+":
    result = number1 + number2

elif operation == "-":
    result = number1 - number2

elif operation == "*":
    result = number1 * number2

elif operation == "/":
    result = number1 / number2
else:
    print("sorry the symbpl you typed in for the operation doesnt make sense")

print("your final result is: ", result)
