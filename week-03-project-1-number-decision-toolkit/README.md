# Week 3 — Project 1: Number & Decision Toolkit

**Project:** Project 1 of 4 — Beginner Stage
**Duration:** 1 week
**AI Rule:** No AI-generated code — all code is learner-written and explained.

---

## 🎯 Learning Outcomes

By the end of this project, I can:
- Use `if/elif/else` for multi-branch decision-making
- Use `while` loops for repetition and menu-driven programs
- Use `range()` to define score boundaries
- Validate user input and handle invalid choices gracefully
- Write pseudocode before coding
- Explain every branch of my program in a live walkthrough

---

## 📦 Deliverables

| # | Deliverable | File | Status |
|---|-------------|------|--------|
| 1 | Main toolkit program | [`number_decision_toolkit.py`](./number_decision_toolkit.py) | ✅ |
| 2 | ASCII logo module | [`logo.py`](./logo.py) | ✅ |
| 3 | Pseudocode plan | [`pseudocode.md`](./pseudocode.md) | ✅ |
| 4 | Test cases | [`test_cases.md`](./test_cases.md) | ✅ |

---

## 🛠️ What the Toolkit Does

The toolkit is a **menu-driven CLI application** with three tools:

### 1. Calculator
Performs arithmetic (+, −, ×, ÷) with two numbers and supports
**continuous calculation** — the previous result can become the
first number in the next operation. Handles division by zero and
invalid operator input.

### 2. Temperature Converter
Converts between Celsius and Fahrenheit based on the user's choice.
Uses `float()` for precision and `round()` for clean output.

### 3. Decision Checker
Classifies a score (0–100) into a letter grade (A–F) using
`range()` boundaries. Handles out-of-range scores gracefully.

All three tools return to the main menu when finished, and the
user can pick another tool or exit.

---

## 🚀 How to Run

From inside the `week-03-project-1-number-decision-toolkit/` folder:

```bash
python number_decision_toolkit.py
```
Requirements: Python 3.10 or later. No external packages needed
(uses only the standard library: os).

🖥️ Sample Interaction
text
Welcome to the Number & Decision Toolkit
********MENU********
1. Calculator
2. Converter
3. Decision Checker
4. Exit

Pick a number (1 - 4) from the menu above to proceed: 3
...
Enter your score: 95
Your grade is A
Choose y to continue or n to exit: n

Welcome to the Number & Decision Toolkit
********MENU********
...
🧠 What I Learned
while loops are the backbone of menu-driven programs. The main loop keeps the toolkit alive; inner loops keep each tool running until the user exits.

range() is a natural fit for scoring bands. It expresses "between X and Y" clearly, and boundary tests (89 vs 90) confirm the boundaries are correct.

Dictionary dispatch beats long if/elif chains. Mapping "+" → add and "-" → subtract made the calculator easier to extend and cleaner to read.

Input validation has two layers. "Invalid choice" (like typing 5 for a 1–4 menu) is handled in Week 3. "Invalid type" (like typing abc for a number) requires try/except, which is a Week 6 topic.

Honest documentation matters. I noted the global usage and non-numeric input limitation rather than hiding them.

📁 Folder Structure
text
week-03-project-1-number-decision-toolkit/
├── README.md                          ← this file
├── number_decision_toolkit.py         ← main program
├── logo.py                            ← ASCII art for the three tool headers
├── pseudocode.md                      ← pre-coding plan
└── test_cases.md                      ← 40+ test scenarios
🧪 Test Coverage
Full test suite in test_cases.md. Summary:

Category	Tests	Passed
Menu navigation	7	7
Calculator	9	9
Converter	8	8
Decision Checker	13	13
Edge cases	7	4
Total	44	41
Includes boundary tests (89/90, 49/50, 0/100) and error paths
(invalid menu choices, invalid operators, division by zero).

⚠️ Known Limitations
Non-numeric input crashes the program.
Entering letters instead of numbers raises ValueError because
int() and float() cannot convert text. Fixing this requires
try/except, which is a Week 6 topic. Once learned, all three
tools will be updated to prompt again instead of crashing.

continue_tool() uses a module-level global.
The function updates run_tool using global, which works but
is not ideal. A cleaner design would return a boolean. Planned
refactor for Week 5 (Functions & Clean Code).

These limitations are documented in the code with inline comments
and in test_cases.md.

📚 Resources Used
B03 – Control Flow: https://docs.python.org/3/tutorial/controlflow.html

B05 – Defining Functions: https://docs.python.org/3/tutorial/controlflow.html#defining-functions

🎥 Demo
- **Title:** Week 3 — Number & Decision Toolkit Demo | Chinedu Iroanyah
- **Recording:** [https://www.loom.com/share/10d2df0873f3440e856a31661eeaaf47](https://www.loom.com/share/10d2df0873f3440e856a31661eeaaf47)

- **Live code walkthrough:** Scheduled separately with mentor

- **Live URL:** N/A (CLI tool, not deployed)

✅ Self-Check
☑ Toolkit runs without errors
☑ All three tools work (Calculator, Converter, Decision Checker)
☑ Menu loops correctly and option 4 exits cleanly
☑ Division by zero is handled
☑ Invalid menu choices and operators are handled
☑ Score boundaries are correct (tested at 89/90, 49/50, 0/100)
☑ Pseudocode written before coding
☑ Test cases documented and executed
☑ Known limitations noted honestly
☑ I can explain every line of the code
☑ No AI-generated code was used