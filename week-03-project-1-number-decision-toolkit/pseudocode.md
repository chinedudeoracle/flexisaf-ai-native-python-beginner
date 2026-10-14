# Pseudocode — Number & Decision Toolkit

**Project:** Week 3 — Project 1: Number & Decision Toolkit
**Author:** Chinedu Iroanyah
**Date:** 2026-10-14

This document describes the logic of the toolkit **before** it was coded. It captures the plan, the structure, and the decisions made along the way.

---

## Overview

The toolkit is a menu-driven program with three tools and an exit option. The user picks a tool, uses it, then either continues with the same tool or returns to the main menu.

The program has two levels of repetition:
- **Outer loop** — keeps the main menu alive until the user exits
- **Inner loops** — keep each individual tool running until the user decides to leave

---

## Main Flow
START
SET run_toolkit = True

WHILE run_toolkit is True:
SET run_tool = True
Show welcome menu with 4 options:

Calculator

Converter

Decision Checker

Exit
Get user_choice

IF user_choice == "4":
SET run_toolkit = False
ELSE IF user_choice == "1":
CALL calculator()
ELSE IF user_choice == "2":
WHILE run_tool is True:
CALL converter()
ELSE IF user_choice == "3":
WHILE run_tool is True:
CALL decision_checker()
ELSE:
Show "Invalid choice" message
END

text

**Notes:**
- The calculator has its own internal continue-loop, so it's not wrapped in `WHILE run_tool`.
- The converter and decision checker are wrapped because they return to the menu after a single operation unless the user chooses to continue.

---

## Calculator
FUNCTION calculator():
Clear screen
Show calculator logo
Get num1 (as a number)

SET continue_calculation = True

WHILE continue_calculation is True:
Show available operators (+, -, /, *)
Get operator

IF operator is one of the valid symbols:
Get num2 (as a number)

IF operator is "/" AND num2 is 0:
Show "You cannot divide by 0"
ELSE:
Look up the function for the operator in the symbols dictionary
CALL that function with num1 and num2 → store as result
Show result

Get continue_choice ("y" or "n")

IF continue_choice is "y":
SET num1 = result
ELSE:
Clear screen
SET continue_calculation = False
ELSE:
Show "Invalid choice" message
END FUNCTION

text

**Design decisions:**
- Validate the operator **before** dispatching to prevent a `KeyError`.
- Check for division by zero **before** performing the operation.
- Use a `continue_calculation` flag to control the internal loop.
- When the user continues, the previous result becomes the new `num1` — this supports chained calculations.

---

## Converter (Temperature)
FUNCTION converter():
Clear screen
Show converter logo
Show conversion options:

Celsius to Fahrenheit

Fahrenheit to Celsius
Get user_choice

IF user_choice == "1":
Get temperature in Celsius (as a number)
Calculate Fahrenheit = Celsius × (9 / 5) + 32
Round to 2 decimal places
Show "X°C = Y°F"
ELSE IF user_choice == "2":
Get temperature in Fahrenheit (as a number)
Calculate Celsius = (Fahrenheit − 32) × 5 / 9
Round to 2 decimal places
Show "X°F = Y°C"
ELSE:
Show "Invalid choice" message

CALL continue_tool()
END FUNCTION

text

**Design decisions:**
- Use `float()` for temperature because decimals are common.
- Round to 2 decimal places to keep output clean.
- `continue_tool()` is called **once at the end** — so it runs whether the conversion succeeded or the user chose an invalid option.

---

## Decision Checker
FUNCTION decision_checker():
Clear screen
Show decision checker logo
Get score (as a whole number)

IF score is between 90 and 100: grade = "A"
ELSE IF score is between 80 and 89: grade = "B"
ELSE IF score is between 70 and 79: grade = "C"
ELSE IF score is between 60 and 69: grade = "D"
ELSE IF score is between 50 and 59: grade = "E"
ELSE IF score is between 0 and 49: grade = "F"
ELSE: grade = "Invalid score"

Show "Your grade is X"
CALL continue_tool()
END FUNCTION

text

**Design decisions:**
- Each grade band uses a `range()` check — the boundaries are clear and easy to test.
- The final `else` branch catches **both** scores below 0 and above 100, so the print statement never fails on an undefined variable.
- Boundary tests (89 vs 90, 49 vs 50, 0, 100) are included in `test_cases.md`.

---

## Continue Prompt
FUNCTION continue_tool():
Get user input ("y" or "n")

IF user input is "n":
Clear screen
SET run_tool = False

text

**Note:** Uses `global` to update `run_tool`. A cleaner approach would return a boolean — noted as a Week 5 refactor.

---

## Helper Functions

### Screen Clearing
FUNCTION clear_screen():
IF operating system is Windows:
Run "cls"
ELSE:
Run "clear"

text

### Arithmetic Functions
FUNCTION add(n1, n2):
RETURN n1 + n2

FUNCTION subtract(n1, n2):
RETURN n1 - n2

FUNCTION multiply(n1, n2):
RETURN n1 * n2

FUNCTION divide(n1, n2):
RETURN n1 / n2

text

### Operator Dictionary
symbols = {
"+": add,
"-": subtract,
"/": divide,
"*": multiply,
}

text

**Design decision:** Store each operator's function in a dictionary. This replaces a long `if/elif` chain with a single lookup: `symbols[operator](n1, n2)`. Adding a new operation becomes a one-line change.

---

## Data Flow Summary
User → Menu → Tool choice
│
├── Calculator → Number input → Operator choice → Validation
│ ↓
│ [Valid] [Invalid]
│ ↓ ↓
│ Compute Show error
│ ↓ ↓
│ Show result → Continue prompt
│
├── Converter → Conversion choice → Temperature input
│ ↓
│ Apply formula
│ ↓
│ Show result
│
└── Decision Checker → Score input → Grade lookup
↓
Show grade

↓

Continue prompt → [y] Loop back to tool
→ [n] Return to main menu

text

---

## Known Limitations (Anticipated)

These were anticipated during the planning phase:

1. **Non-numeric input crashes the program.**  
   `int()` and `float()` cannot convert text to numbers. Proper handling requires `try/except` — a Week 6 topic.

2. **`global` state in `continue_tool()`.**  
   The function updates `run_tool` using `global`. A cleaner pattern would return a boolean; planned refactor for Week 5.

---

## How This Pseudocode Was Used

- Written **before** coding to plan the toolkit's structure and flow.
- Updated during coding where a design decision changed (e.g., adding the operator validation check).
- Serves as the reference document for the **live code walkthrough** in Week 3.