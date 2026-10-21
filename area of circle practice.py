import random

diamater = random.randint(1,100)
radius = diamater/2
answer = radius * radius * 3.14
print(answer)
print(diamater)
result = int(input("hi welcome to circle area caclulation program, plese try to calculate a circle with the diamater above type your anwser in when your done and hit enter use 3.14 as a approximation for pi"))
if result == answer:
    print("good job")
else:
    print("sorry thats wrong")
