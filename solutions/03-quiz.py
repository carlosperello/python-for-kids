# Exercise 3 solution — The quiz master

score = 0

print("=== MY QUIZ ===")

answer = input("1) Capital of Spain? ")
if answer.lower() == "madrid":
    score = score + 1

answer = input("2) How many legs does a spider have? ")
if answer == "8":
    score = score + 1

answer = input("3) Is Python a snake or a programming language? ")
if answer == "both":
    score = score + 1

print(f"You scored {score} out of 3")
if score == 3:
    print("Genius!")
elif score > 0:
    print("Pretty good!")
else:
    print("Try again!")

# Secret gate
password = input("Password: ")
if password.lower() == "python":
    print("Welcome, agent.")
else:
    print("INTRUDER ALERT")
