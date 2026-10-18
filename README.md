# Python for kids — first steps with Mu

Five exercises that take a kid from Scratch/MakeCode to writing real Python
programs. One exercise per session, 30–45 minutes each.

## Setup

1. Open Mu and pick the **Python** mode (the plain desktop one — not micro:bit
   or Adafruit).
2. Type the code in the editor, press **Run**. Mu will ask to save the file
   first — say yes, and save each exercise with its own name (`hello.py`,
   `quiz.py`, ...).
3. The **REPL** button opens a shell in the bottom panel — great as a quick
   calculator and for one-line experiments.

## Ground rules (for the parent)

- **He types everything himself.** No copy-paste. Typos are not a problem —
  they are the first debugging reps, and fixing them is the actual lesson.
- **Read error messages together, out loud.** Find the line number. The error
  name (SyntaxError, NameError...) is a clue, not a failure.
- **End each session by showing the program to someone else** — the other
  parent, a grandparent, a sibling. An audience is the best motivator.
- Stuck? Shrink the task: "change one word and run again" beats "let me fix it
  for you".

## Scratch → Python dictionary

Use this constantly in the first sessions. He already knows the concepts;
only the spelling is new.

| Scratch block | Python |
|---|---|
| `say "hi"` | `print("hi")` |
| `ask "What's your name?" and wait` | `input("What's your name? ")` |
| `set myvar to 5` | `myvar = 5` |
| `repeat 10` | `for i in range(10):` |
| `if ... then / else` | `if ...:` / `else:` |
| nested blocks inside an `if` | indented lines under the `if` |
| comment block (yellow note) | `# this is a comment` |

## The exercises

1. **Hello, world!** — `print`, strings, the editor, the REPL
2. **Talk with the computer** — `input`, variables, f-strings
3. **The quiz master** — `if`/`elif`/`else`, indentation
4. **Loops** — `for`, `range`, drawing patterns with text
5. **Guess my number** — `while`, `random`, everything together (+ turtle bonus)

Solutions are in `solutions/` — for the parent only, peek *after* the kid
has had an honest try.

## Common first errors

| Python says | Why | Fix |
|---|---|---|
| `SyntaxError` | missing quote or `)` | count the quotes: they come in pairs `"..."` |
| `NameError: name 'Print' is not defined` | capital letter | Python is case-sensitive: `print`, not `Print` |
| `IndentationError` | missing spaces under an `if` | everything that belongs to the `if` goes on the next line, indented |
| `ValueError` | typed letters where a number was expected | `int(input())` only likes numbers |
| `TypeError` | `"text" + 5` | mixing text and numbers needs an f-string: `f"{5}"` |
