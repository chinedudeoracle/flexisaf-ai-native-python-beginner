"""
Week 2 — Receipt Total
FlexiSAF AI-Native Python Internship (Beginner Stage)

This script demonstrates:
- Input, process, output
- Variables and data types
- f-strings for formatted output

Author: Chinedu Iroanyah
Date: 2026-10-06
"""
# Print welcome message
print("This program calculates your receipt total")

# Get subtotal and tax rate
sub_total = float(input("Enter subtotal: "))
tax_rate = float(input("Enter tax rate (%): "))

# Calculate total and print receipt
tax_amount = sub_total * (tax_rate / 100)
total = sub_total + tax_amount

print()
print(f"{'Subtotal:':<12}{f'₦{sub_total:.2f}':>15}")
print(f"{f'Tax({tax_rate:.2f}%)':<12}{f'₦{tax_amount:.2f}':>15}")
print("-" * 27)
print(f"{'Total:':<12}{f'₦{total:.2f}':>15}")
