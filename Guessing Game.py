# GUESSING GAME
from random import randrange    # modify later and ask users to set the max num of tries
answer = randrange(1, 10)
guess = int()

counter = 1
total = 0
print("you have a maximum of THREE attempts to WIN this game\n")
while guess != answer:
    guess = eval(input("Enter GUESS!: "))
    total += counter
    if total >= 3:
        print("GAME OVER!!! You have exceeded the maximum limit")
        break
    if guess < answer:
        print("your guess is too low\n")
    elif guess > answer:
        print("your guess is too high\n")
    elif guess == answer:
        print("YOU WIN!!! It took you ", total, " tries to get the correct answer!")
print()
print()
