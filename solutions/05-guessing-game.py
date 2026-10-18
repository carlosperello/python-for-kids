# Exercise 5 solution — Guess my number (max 5 tries version)

from random import randint

print("=== GUESS MY NUMBER ===")
print("I'm thinking of a number from 1 to 100")
print("You have 5 tries!")

secret = randint(1, 100)
guess = 0
tries = 0

while guess != secret and tries < 5:
    guess = int(input("Your guess: "))
    tries = tries + 1
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")

if guess == secret:
    print(f"You got it in {tries} tries!")
else:
    print("Out of guesses! The number was", secret)
