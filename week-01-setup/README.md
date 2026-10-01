# Week 1 — Programming Mindset, Digital Tools & Setup

**Duration:** 1 week
**Phase:** Foundation
**AI Rule:** No AI-generated code

---

## 🎯 Learning Outcomes

By the end of this week, I can:
- Set up a working Python environment
- Explain input–process–output
- Create, save, and run a simple Python file without AI assistance

---

## 📦 Deliverables

| Deliverable | File | Status |
|-------------|------|--------|
| Environment checklist | [`environment_checklist.md`](./environment_checklist.md) | ✅ |
| First script | [`first_script.py`](./first_script.py) | ✅ |
| Algorithm / flowchart | [`algorithm_flowchart.md`](./algorithm_flowchart.md) | ✅ |

---

## 🛠️ Setup Instructions

### 1. Install Python
- Installed Python 3.13.5 on Windows
- Verified: `python --version` returns the installed version
- Python is accessible from PowerShell (no PATH issues)

### 2. Install VS Code
- Installed VS Code
- Added the **Python extension** by Microsoft
- Added the **Pylance** extension (auto-installed with Python extension)
- Created a virtual environment in the project folder

### 3. Run the first script
```bash
"""
Week 1 — First Script
FlexiSAF AI-Native Python Internship (Beginner Stage)

This script demonstrates:
- Input, process, output
- Variables and data types
- f-strings for formatted output

Author: Chinedu Iroanyah
Date: 2026-10-01
"""
# Print the welcome message
print("Welcome to my first script!\nThis program tells you your year of birth when you input your age.\nNote: Current year is 2026.")

# Input your name
name = input("What is your name: ")

# Accept age input as string, then convert to integer using int()
age = int(input("What is your age (Enter a whole number, e.g. 25): "))

# Calculate year_of_birth as: current_year - age
current_year = 2026
year_of_birth = current_year - age

# Create message using f-string (used .title() to make name title cased) and print message
message = f"Hello, {name.title()}! You are {age} years old. You were born around {year_of_birth}."
print(message)
```

🧠 What I Learned
A program is a sequence of instructions that takes input, processes it, and produces output.

Python files use the .py extension and are run with python filename.py.

The terminal is where I run commands; VS Code is where I write code.

📚 Resources Used
B01 – VS Code Python Tutorial: https://code.visualstudio.com/docs/python/python-tutorial

B02 – Python Tutorial: https://docs.python.org/3/tutorial/

## 🎥 Demo

- **Title:** Week 1 — First Script Demo | Chinedu Iroanyah
- **Recording:** [https://www.loom.com/share/fe76a3cb0a8f496da95fc7f5a8be9d05](https://www.loom.com/share/fe76a3cb0a8f496da95fc7f5a8be9d05)
- **Live URL:** N/A (script, not deployed)

✅ Self-Check
✅ Python installed and python --version works
✅ VS Code installed with Python extension
✅ first_script.py runs successfully
✅ I can explain input–process–output in my own words
✅ I can explain every line of first_script.py