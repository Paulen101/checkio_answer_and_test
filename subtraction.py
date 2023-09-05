from random import randint
num1 = randint(1, 100)
num2 = randint(1, 100)

if num1 < num2:
    num1, num2 = num2, num1

def subtraction(num1, num2):
    print("What is " + str(num1) + " - " + str(num2) + "?")
    answer = int(input("Your answer: "))
    while answer != num1 - num2:
        print("Wrong answer. Try again." + " What is " + str(num1) + " - " + str(num2) + "?" )
        answer = int(input("Your answer: "))
    else:
        print("You got it!")
    
