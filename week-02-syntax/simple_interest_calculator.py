"""
Week 2 — Simple Interest Calculator
FlexiSAF AI-Native Python Internship (Beginner Stage)

This script demonstrates:
- Input, process, output
- Variables and data types
- f-strings for formatted output

Author: Chinedu Iroanyah
Date: 2026-10-06
"""
# Print welcome message
print("This program is a Simple Interest Calculator")

# Input principal, rate, and time
principal = float(input("Principal (₦): "))
rate = float(input("Annual rate (%): "))
time = int(input("Time (years): "))

# Calculate Interest earned and print output
interest_earned = principal * (rate / 100) * time
total_amount = principal + interest_earned

print()
print(f"{'Interest earned:':<18}₦{interest_earned:.2f}")
print(f"{'Total amount:':<18}₦{total_amount:.2f}")