# Exercise 3 — The quiz master

**You will learn:** `if`/`elif`/`else` and indentation (the spaces DO matter).

## 1. One question

```python
answer = input("What is the capital of Spain? ")
if answer == "Madrid":
    print("Correct!")
else:
    print("Nope, it's Madrid")
```

Two new things:

- `==` asks "are these equal?" — while a single `=` puts a value into a box.
  Two equals = check. One equals = store.
- The **spaces** before `print` are not decoration! Everything indented under
  the `if` runs only when the condition is true. It's exactly Scratch's
  nested blocks — if the condition is true, do the blocks inside:

```
Scratch:                                Python:
if <answer = Madrid> then               if answer == "Madrid":
    say "Correct!"                          print("Correct!")
```

Four spaces is the convention. Python counts them for you — keep them
consistent.

## 2. Three-way decisions

`elif` means "otherwise, if". You can chain them:

```python
score = 1

if score == 3:
    print("Perfect!")
elif score > 0:
    print("Not bad!")
else:
    print("Better luck next time")
```

Change `score` and run a few times. Only the first matching branch runs.

## 3. Build the quiz

```python
score = 0

print("=== MY QUIZ ===")

answer = input("1) Capital of Spain? ")
if answer == "Madrid":
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
```

`score = score + 1` looks like broken math — read it as "make score be
itself plus one". It just adds a point to the box.

## Challenges

- Add two more questions.
- Right now "madrid" (no capital M) fails. Fix it with `answer.lower() == "madrid"`
  — `.lower()` turns the answer to all lowercase first.
- Secret gate: ask for a password. If it is `"python"`, print
  "Welcome, agent." — anything else prints "INTRUDER ALERT".

## What you know now

- `if`/`elif`/`else` make decisions
- `==` checks equality, `=` stores
- `>` `<` `>=` `<=` compare numbers
- Indented lines belong to the `if` — indentation is Python's nesting
