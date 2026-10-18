# Exercise 4 solution — Loops

# User-chosen times table
n = int(input("Which times table? "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

# Full pyramid
print()
for i in range(1, 6):
    spaces = " " * (5 - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)

# Rocket: staircase then liftoff
print()
for i in range(1, 6):
    print("*" * i)
print("LIFTOFF!")
