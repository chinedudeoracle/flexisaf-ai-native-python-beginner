"""
Week 2 — Age Calculator
FlexiSAF AI-Native Python Internship (Beginner Stage)

This script demonstrates:
- Input, process, output
- Variables and data types
- f-strings for formatted output

Author: Chinedu Iroanyah
Date: 2026-10-06
"""
# Print the welcome message
print("Welcome to the Age Calculator!")
print("This program calculates age based on year of birth.")

# Get user's birth year and current year
birth_year = int(input("What year were you born?: "))
current_year = int(input("What is the current year?: "))

# Calculate age
age = current_year - birth_year

# Display calculated age
print(f"You are {age} years old.")