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

