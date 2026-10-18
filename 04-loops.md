# Exercise 4 — Loops: make the computer work

**You will learn:** `for`, `range`, and the loop variable.

## 1. The repeat block, grown up

In Scratch you had `repeat 5`. In Python:

```python
for i in range(5):
    print("hi")
```

`i` is the **loop variable** — it counts 0, 1, 2, 3, 4. Computers start
counting at 0! Print `i` instead of "hi" and watch:

```python
for i in range(5):
    print(i)
```

## 2. Countdown

```python
for i in range(5, 0, -1):
    print(i)
print("LIFTOFF!")
```

`range(5, 0, -1)` means: start at 5, stop before 0, count down by 1.
Note that `print("LIFTOFF!")` is NOT indented — so it runs once, after the
loop is done.

## 3. Drawing with loops

```python
for i in range(1, 6):
    print("*" * i)
```

`"*" * i` means "the star character, repeated i times" — yes, you can
multiply strings!

```
*
**
***
****
*****
```

## 4. The times table machine

```python
n = 7
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
```

Ten lines, typed once. That's why loops exist: the computer does the boring part.

## 5. Predict first!

Before running, write down on paper what each of these prints:

- `range(3)`
- `range(1, 4)`
- `range(5, 0, -1)`

Then run and check. Being wrong here is the fastest way to understand
`range` — write down your guess first, always.

## Challenges

- Make the user choose the times table: `n = int(input("Which table? "))`
- Full pyramid (spaces + stars):

```python
for i in range(1, 6):
    spaces = " " * (5 - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)
```

- Combine exercises: print a staircase of stars, then "LIFTOFF!" — a rocket.

## What you know now

- `for i in range(n):` repeats n times
- The loop variable `i` counts inside the loop
- Indented lines repeat; unindented lines run after
- `"*" * 3` repeats strings
