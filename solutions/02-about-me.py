# Exercise 2 solution — Mad Libs

adjective = input("Give me an adjective: ")
animal = input("Give me an animal: ")
food = input("Give me a food: ")
place = input("Give me a place: ")

print(f"In a {adjective} world there lived a {animal}.")
print(f"Every day it ate {food} for breakfast in the {place}.")
print(f"One day the {animal} met a wizard who said:")
print(f"'You are too {adjective} for this world!'")

# Bonus: seconds until birthday
days = int(input("How many days until your birthday? "))
seconds = days * 24 * 60 * 60
print(f"That's {seconds} seconds!")
