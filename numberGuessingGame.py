import random

numbers=[i for i in range(1, 101)]#list of numbers for 1 to 100
randomNum=random.choice(numbers)#store a random value betweem 1 to 100

while True:
    try:
        guess=int(input("Guess the number between 1 and 100: "))
        if guess<randomNum:
            print('low')
        elif guess>randomNum:
            print("high")
        else:
            print("Congratulation, you have guessed the number")
            break
    except ValueError:
        print("Please enter a valid number")
        
        
        
