# Exercise 2 — Talk with the computer

**You will learn:** `input`, variables, and f-strings (the pro way to build sentences).

## 1. Ask a question

```python
name = input("What's your name? ")
print("Hello,", name)
```

Run it and type your answer in the bottom panel, then press Enter.

The word `name` is a **variable** — a labelled box where Python stores the
answer. In Scratch you'd use `set name to answer`. Same idea, new spelling.

## 2. Numbers too

```python
age = int(input("How old are you? "))
print("Next year you'll be", age + 1)
```

`int(...)` turns `"12"` (text) into `12` (a number). Without it, `"12" + 1`
is an error — text and numbers don't mix.

## 3. The pro way: f-strings

There's a neater way to build sentences with variables. Put an `f` before the
quotes and drop variables inside `{}`:

```python
print(f"Hello {name}! Next year you'll be {age + 1}.")
```

You can even do math inside the braces — Python calculates it first.

## 4. Mad Libs — the silly story machine

Type this, then run it and feed it words:

```python
adjective = input("Give me an adjective: ")
animal = input("Give me an animal: ")
food = input("Give me a food: ")
place = input("Give me a place: ")

print(f"In a {adjective} world there lived a {animal}.")
print(f"Every day it ate {food} for breakfast in the {place}.")
print(f"One day the {animal} met a wizard who said:")
print(f"'You are too {adjective} for this world!'")
```

Run it twice with different words. The story changes every time!

## Challenges

- Ask how many days until your birthday, then print how many **seconds**
  that is. (Hint: days × 24 × 60 × 60.)
- Add two more words to the story: a verb and a villain.
- Run the program and press Enter *without typing anything*. The variable is
  now an **empty string** — the box is empty. What does the story look like?

## What you know now

- `input(...)` asks a question and stores the answer in a variable
- `=` puts a value into a variable
- `int(...)` converts text to a number
- f-strings mix text and variables: `f"Hello {name}"`
