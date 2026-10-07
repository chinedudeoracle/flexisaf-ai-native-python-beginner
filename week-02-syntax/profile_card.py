"""
Week 2 — Profile Card
FlexiSAF AI-Native Python Internship (Beginner Stage)

This script demonstrates:
- Input, process, output
- Variables and data types
- f-strings for formatted output

Author: Chinedu Iroanyah
Date: 2026-10-06
"""
# Print the welcome message
print("Welcome to the Profile Card!")
print("This program displays a formatted personal profile.")

# Input user details
user_name = input("What is your full name?: ")
user_track = input("Which of the tracks in the FlexiSAF internship are you part of?: ")
user_learning_stage = input("What learning stage do you belong to?: ")
user_location = input("What location are you attending from (city/state)?: ")
user_email = input("What is your email address?: ")

print()
print(f"|{"=" * 46}|")
print(f"|{"PROFILE CARD":^46}|")
print(f"|{"=" * 46}|")
print(f"|{"Name:":<12}{user_name.title():<34}|")
print(f"|{"Track:":<12}{user_track:<34}|")
print(f"|{"Stage:":<12}{user_learning_stage:<34}|")
print(f"|{"Location:":<12}{user_location:<34}|")
print(f"|{"Email:":<12}{user_email:<34}|")
print(f"|{"=" * 46}|")

# Note: Rows use fixed-width padding to align with the card border.
# The {:<34} syntax left-aligns each value in a 34-character field.