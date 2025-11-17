import random

comp = random.randint(1, 100)
turn = 0
print()

while True:
    guess=int(input("Enter a number between 1 and 100: "))
    if(guess == comp):
        print("You guessed the number!")
        break
    elif (guess < comp):
        print("Guess is too low!")
        turn+=1
    elif (guess > comp):
        print("Guess is too high!")
        turn+=1
print("Number of attempts to find the right amswer = ", turn+1)
