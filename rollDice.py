import random

dice1=[1,2,3,4,5,6]
dice2=[1,2,3,4,5,6]
def rolldice():
    d1=random.choice(dice1)
    d2=random.choice(dice2)
    print(f'({d1},{d2})')
while True:
    choice=input("Roll the dice? (y/n)")
    if choice=="y":
         rolldice()
    elif choice=="n":
        print("Thank you for playing")
        break
    else:
         print("!!!!Invalid character!!!!")

