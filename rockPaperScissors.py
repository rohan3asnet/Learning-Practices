import random

emojis={'r':'🪨','s':'✂','p':'📄'}#dictionaries, it is used to store value to key
choices=('r','p','s')#tupels, it is used to eliminate unintentional changes to the elements

while True:
    myChoice=input("Rock, Paper or Scissors?(r/p/s)").lower()#lower is used to take uppercase input in lowercase form
    computerChoice=random.choice(choices)#using random function to let computer choose on a random basis

    if myChoice not in choices:
        print("Sorry, Inalid Choices")
        continue

    print(f"Your choice: {emojis[myChoice]}")
    print(f"Computer choice: {emojis[computerChoice]}")

    if myChoice==computerChoice:
        print("Tie")
    elif \
    (myChoice=='r' and computerChoice=='s') or \
    (myChoice=='p'and computerChoice=='r') or \
    (myChoice=='s'and computerChoice=='p'):
        print("BOOYAH") # \ is used to tell that single line code is written in multiline format
    else:
        print("You Lose")

    wannaContinue=input("Continue?(y/n)").lower()
    if wannaContinue=='n':
        break




