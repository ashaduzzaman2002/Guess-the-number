import random

def numberGuess():
    randomNum = random.randint(1, 100)
    for i in range(1, 11):
        num = int(input("Enter a number: "))
        if num > randomNum:
            print("Enter a lower number.")
        elif num < randomNum:
            print("Enter a higher number.")
        else:
            print(f"You won the game in {i} attemt")
            break
    else:
        print(f"You loss the game and the currect number is {randomNum}")

print("--------GUESS THE NUMBER BETWEEN 1 TO 100--------")

numberGuess()
