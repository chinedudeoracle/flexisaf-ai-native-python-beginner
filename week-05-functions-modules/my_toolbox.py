"""
Week 5 — Utility Toolbox
FlexiSAF AI-Native Python Internship (Beginner Stage)

This module contains a collection of six reusable utility functions.
It demonstrates:
- Function definition and return values
- Writing descriptive docstrings
- Separation of logic into a reusable module

Author: Chinedu Iroanyah
Date: 2026-10-28
"""

def add_numbers(a, b):
    """Returns the sum of two numbers"""
    return a + b

def subtract_numbers(a, b):
    """Returns the difference of two numbers"""
    return a - b

def calculate_area(length, width):
    """Returns the area of a rectangle based on provided length and width"""
    return length * width

def celsius_to_fahrenheit(c):
    """Returns converted temperature in fahrenheit for provided celsius"""
    return round(c * (9 / 5) + 32, 2)

def get_greeting(name):
    """Returns a string like 'Hello, Henry'"""
    return f"Hello, {name.upper()}"

def is_even(number):
    """Returns True if even, False if odd"""
    return number % 2 == 0

