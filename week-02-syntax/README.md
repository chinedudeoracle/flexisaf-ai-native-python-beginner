# Week 2 — Python Syntax, Variables, Data Types & Input/Output

**Duration:** 1 week
**Phase:** Foundation
**AI Rule:** No AI-generated code

---

## 🎯 Learning Outcomes

By the end of this week, I can:
- Write small programs that accept user input, perform calculations and display clear results
- Use appropriate data types (strings, integers, floats)
- Apply type conversion, operators, f-strings and basic debugging
- Format output with fixed-width alignment and decimal precision

---

## 📦 Deliverables

| # | Deliverable | File | Status |
|---|-------------|------|--------|
| 1 | Profile Card | [`profile_card.py`](./profile_card.py) | ✅ |
| 2 | Age Calculator | [`age_calculator.py`](./age_calculator.py) | ✅ |
| 3 | Temperature Converter | [`temperature_converter.py`](./temperature_converter.py) | ✅ |
| 4 | Receipt Total | [`receipt_total.py`](./receipt_total.py) | ✅ |
| 5 | Simple Interest Calculator | [`simple_interest_calculator.py`](./simple_interest_calculator.py) | ✅ |

---

## 🛠️ How to Run

Each program is standalone. Run any of them from the `week-02-syntax/` folder:

```bash
python profile_card.py
python age_calculator.py
python temperature_converter.py
python receipt_total.py
python simple_interest_calculator.py
📝 Program Summaries
1. Profile Card
Collects user details (name, track, stage, location, email) and displays them
in a formatted profile card. Demonstrates fixed-width f-string alignment
({value:<N}), centered text ({value:^N}), and .title() string method.

2. Age Calculator
Takes a birth year and current year as input, then calculates and displays
the user's age. Demonstrates integer input conversion and basic arithmetic.

3. Temperature Converter
Converts between Celsius and Fahrenheit based on the user's choice.
Demonstrates if/elif/else branching, float() conversion, round()
for clean output, and Unicode symbols (℃, ℉).

4. Receipt Total
Takes a subtotal and tax rate, calculates tax amount and final total,
then displays a formatted receipt. Demonstrates currency formatting
(:.2f), fixed-width alignment, and string repetition for separators.

5. Simple Interest Calculator
Calculates simple interest and total amount from principal, annual rate,
and time in years. Demonstrates the formula I = P × (R / 100) × T,
currency formatting, and mixed type conversion (float for money, int for years).

🧠 What I Learned
Data types matter. Using float() for money and temperature avoids
silent precision loss that int() would cause.

f-string formatting is powerful. The :<N, :>N, :^N, and :.2f
specifiers let me align columns and format numbers cleanly.

Branching with if/elif/else lets a program respond to user choices
and handle invalid input gracefully.

Self-awareness in code. I noted limitations (like alignment issues with
variable-length input) instead of pretending they don't exist.

📚 Resources Used
B02 – Python Tutorial: https://docs.python.org/3/tutorial/

B02-V – Python Full Course for FREE: https://www.youtube.com/watch?v=YfnhD-4gKUM

## 🎥 Demo

- **Part 1:** [Week 2 — Five Mini-Programs Demo (Part 1 of 2) | Chinedu Iroanyah][https://www.loom.com/share/50ccac67ccaf40be9a04c2834b7b2254](https://www.loom.com/share/50ccac67ccaf40be9a04c2834b7b2254)
- **Part 2:** [Week 2 — Five Mini-Programs Demo (Part 2 of 2) | Chinedu Iroanyah][https://www.loom.com/share/b4d65648f3274e04b1c96b3991cee304](https://www.loom.com/share/b4d65648f3274e04b1c96b3991cee304)
- **Live URL:** N/A (scripts, not deployed)

✅ Self-Check
☑ All five mini-programs written and tested
☑ Each program uses appropriate data types
☑ Each program produces clean, formatted output
☑ I can explain every line of every script
☑ No AI-generated code was used
☑ All files committed to the repository