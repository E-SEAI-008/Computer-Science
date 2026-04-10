# CLI Projects

## Overview
In these projects you'll apply everything learned so far to build three small but complete command-line programs. Each project runs from the terminal and takes input via `sys.argv`.

---

## sys.argv — Taking Input from the Terminal

So far you've seen `input()` to get data from the user while a program is running. `sys.argv` is different — it lets you pass data directly when you launch the script from the terminal.

```python
import sys

# sys.argv is a list of strings
# sys.argv[0] is always the script name
# sys.argv[1] is the first argument you pass
# sys.argv[2] is the second, and so on

print(sys.argv)
```

Run it like this:
```bash
python script.py hello world
# ['script.py', 'hello', 'world']
```

A few things to keep in mind:
- Everything in `sys.argv` is a **string**. Convert to `int` or `float` if you need numbers
- Always check `len(sys.argv)` before accessing an index to avoid crashes
- If your argument has spaces, wrap it in quotes: `py script.py "hello world"`
- To collect all arguments after the script name: `" ".join(sys.argv[1:])`

```python
import sys

if len(sys.argv) < 2:
    print("Please provide an argument")
else:
    name = sys.argv[1]
    print(f"Hello, {name}!")
```

```bash
py script.py Alice
# Hello, Alice!
```

---

## Project 1: Rock Paper Scissors

Implement a command-line Rock Paper Scissors game.

### Requirements
- Take the player's move as input from `sys.argv`
- Randomly generate a move for the computer
- Determine the winner based on the rules of Rock Paper Scissors
- Output the result (win, lose, or draw) to the console

### How to run
```bash
python rock_paper_scissors.py rock
```

### Expected output
```
You chose rock. Computer chose scissors. You win!
```

### Rules reminder
| Player | Computer | Result |
|--------|----------|--------|
| Rock | Scissors | Win |
| Scissors | Paper | Win |
| Paper | Rock | Win |
| Any | Same | Draw |

> Tip: use the `random` module to generate the computer's move.

---

## Project 2: English to Pig Latin Translator

Create a program that translates an English phrase into Pig Latin.

### Requirements
- Take an English phrase as input from `sys.argv`
- Convert each word according to the Pig Latin rules below
- Output the translated phrase to the console

### Pig Latin Rules

| Rule | Condition | Example |
|------|-----------|---------|
| Starts with a vowel | Add `way` to the end | `Awesome` → `Awesomeway` |
| Starts with one consonant | Move consonant to end, add `ay` | `Happy` → `appyHay` |
| Starts with two consonants | Move both to end, add `ay` | `Child` → `ildChay` |

### How to run
```bash
python pig_latin.py Pig Latin is hard to speak
```

### Expected output
```
Igpay Atinlay isway ardhay otay eakspay
```

---

## Project 3: Caesar Cipher

Implement a basic Caesar Cipher — one of the oldest encryption techniques.

### Requirements
- Take a phrase and a shift number as inputs from `sys.argv`
- Encrypt the phrase by shifting each letter by the given number
- Non-letter characters (spaces, punctuation) stay unchanged
- Case insensitive — output is lowercase
- A negative shift moves letters left, a positive shift moves them right

### How to run
```bash
python caesar_cipher.py "hello world" 3
```

### Expected output
```
khoor zruog
```

### How the shift works
```
a b c d e f g h i j k l m n o p q r s t u v w x y z
            shift right by 3 →
d e f g h i j k l m n o p q r s t u v w x y z a b c

h → k
e → h
l → o
o → r
```

> Tip: Python's `ord()` and `chr()` functions convert between characters and their ASCII numbers. `% 26` handles wrapping around the alphabet.

---

## Getting Started

1. Create a new `.py` file for each project
2. Start with the `sys.argv` setup and a print to verify your input is coming through
3. Build and test one function at a time before putting it all together
