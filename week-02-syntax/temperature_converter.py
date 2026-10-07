"""
Week 2 — Temperature Converter
FlexiSAF AI-Native Python Internship (Beginner Stage)

This script demonstrates:
- Input, process, output
- Variables and data types
- f-strings for formatted output

Author: Chinedu Iroanyah
Date: 2026-10-06
"""
# Print the welcome message with options
print("Welcome to the Temperature Converter!")

# Display options
print("These are the possible conversions:")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

# Get user's choice
user_choice = input("Choose an option (1 or 2): ")

# Get value based on user's choice
if user_choice == "1":
    temp_in_celsius = float(input("Enter temperature in Celsius: "))
    temp_in_fahrenheit = round(temp_in_celsius * (9 / 5) + 32, 2)
    print(f"{temp_in_celsius}℃ = {temp_in_fahrenheit}℉")
elif user_choice == "2":
    temp_in_fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    temp_in_celsius = round((temp_in_fahrenheit - 32) * 5 / 9, 2)
    print(f"{temp_in_fahrenheit}℉ = {temp_in_celsius}℃")
else:
    print("Invalid choice. Please select either 1 or 2.")