"""
Week 5 — Main Execution File
FlexiSAF AI-Native Python Internship (Beginner Stage)

This script demonstrates:
- Importing a custom module (`my_toolbox`)
- Using an alias for cleaner imports (`as mt`)
- Calling and testing functions from the imported module

Author: Chinedu Iroanyah
Date: 2026-10-28
"""

import my_toolbox as mt


print(mt.get_greeting("chinedu"))
print(f"5 + 3 = {mt.add_numbers(5, 3)}")
print(f"9 - 2 = {mt.subtract_numbers(9, 2)}")
print(f"The area of a rectangle with length 25cm and width 13cm is {mt.calculate_area(25, 13)}cm²")
print(f"The value of 100℃ in Fahrenheit is {mt.celsius_to_fahrenheit(100)}℉")
print(f"5 is not an even number {mt.is_even(5)}")