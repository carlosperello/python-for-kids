# Exercise 5 — Guess my number (the grand finale)

**You will learn:** `while` loops, `random`, and putting EVERYTHING together.

## 1. Random numbers

```python
from random import randint

secret = randint(1, 20)
print("Psst, the secret number is", secret)  # cheating! only for testing
```

`randint(1, 20)` picks a random number from 1 to 20 — every run is different.
Remove that cheat line when the game works.

## 2. The full game

```python
from random import randint

print("=== GUESS MY NUMBER ===")
print("I'm thinking of a number from 1 to 20")

secret = randint(1, 20)
guess = 0
tries = 0

while guess != secret:
    guess = int(input("Your guess: "))
    tries = tries + 1
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")

print(f"You got it in {tries} tries!")
```

- `while guess != secret:` means "keep going as long as the guess is NOT the
  secret". It's like Scratch's *repeat until*, but flipped: while this is
  true, keep looping.
- `!=` means "not equal". Two new symbols in one day — you're rich.
- Everything inside the loop repeats: ask, count, check, again and again,
  until the guess finally hits the secret.

## 3. Make it yours

- Bigger challenge: change the range to 1–100.
- Five guesses max, or you lose. Change the loop condition to
  `while guess != secret and tries < 5:` (the `and` glues two conditions
  together), and at the end check who won:

```python
if guess == secret:
    print(f"You got it in {tries} tries!")
else:
    print("Out of guesses! The number was", secret)
```

- What happens if someone types "banana" instead of a number? Try it! The
  crash is a `ValueError` — `int()` only likes numbers. Finding bugs like
  this makes you a tester.

## Bonus — real drawing with turtle

Python can also draw! Type this and run:

```python
import turtle

t = turtle.Turtle()
t.speed(0)
t.pencolor("purple")

for i in range(36):
    t.forward(100)
    t.left(170)

turtle.done()
```

A window pops up and draws a starburst. The turtle is just a loop moving a
pen: forward, turn, forward, turn... Change `170` to `172` or `120` and see
what shapes you get. If the window doesn't open on your machine, ask your
teacher for help — you already proved you can program with the guessing game.

## What you know now

- `while` repeats as long as a condition is true
- `!=` means not equal, `and` glues conditions
- `randint(a, b)` gives a random number
- You can now write a complete game: input, variables, decisions, loops,
  randomness. That's a real program.
