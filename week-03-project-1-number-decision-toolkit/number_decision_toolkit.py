"""
Week 3 — Project 1: Number & Decision Toolkit
FlexiSAF AI-Native Python Internship (Beginner Stage)

A menu-driven toolkit with three tools:
    1. Calculator     — arithmetic with continuous calculation support
    2. Converter      — Celsius ↔ Fahrenheit conversion
    3. Decision Checker — grade classification by score range

This script demonstrates:
- Control flow with if/elif/else
- Repetition with while loops
- range() for scoring bands
- Input validation and error handling
- Dictionary dispatch for operations
- Cross-platform screen clearing

Author: Chinedu Iroanyah
Date: 2026-10-14
"""
from logo import calculator_logo, converter_logo, decision_checker_logo
import os

# Used across multiple functions so the message stays consistent — change it once, changes everywhere.
INVALID_CHOICE = "Invalid choice. Please select one of the choices."

run_tool = True

def clear_screen():
    # 'nt' means Windows, otherwise it falls back to Linux/macOS commands
    os.system('cls' if os.name == 'nt' else 'clear')

# Four small functions — one per math operation. 
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def divide(n1, n2):
    return n1 / n2

def multiply(n1, n2):
    return n1 * n2

# Using a dictionary of symbols to map each operator character to the function that implements it
symbols = {
    "+": add,
    "-": subtract,
    "/": divide,
    "*": multiply,
}

# This repeatedly asks for an operator and a second number, 
# then asks if the user wants to continue with the result. 
# Runs until the user types n at the continue prompt.
def calculator():
    clear_screen()
    print(calculator_logo)
    num1 = float(input("What is the first number?: "))
    # This is the Loop control flag
    # the calculator keeps running until the user chooses to exit.
    continue_calculation = True
    while continue_calculation:
        # Show available operators, then get the user's choice.
        for symbol in symbols:
            print(symbol)
        operator = input("Select an operation from one above: ")
        # Validate the operator before dispatching
        # to avoid the dictionary lookup raising a KeyError.
        if operator in symbols:
            num2 = float(input("What is the next number?: "))
            # Check for division by zero, to avoid crash of program
            if operator == "/" and num2 == 0:
                print("You cannot divide by 0")
            else:
                result = symbols[operator](num1, num2)
                print(f"{num1} {operator} {num2} = {result}")
                continue_choice = input(f"Type y to continue calculation with {result} or n to exit calculator: ").lower()
                if continue_choice == "y":
                    # If the user wants to continue, the previous result becomes the new first number.
                    num1 = result
                else:
                    clear_screen()
                    continue_calculation = False
        else:
            print(INVALID_CHOICE)

def continue_tool():
    # Note: uses `global` to update the run_tool flag.
    # A cleaner design would be to return a boolean and let
    # the caller update the flag. Deferred to a Week 5 refactor.
    global run_tool
    cont_tool = input("Choose y to continue or n to exit: ").lower()
    if cont_tool == "n":
        clear_screen()
        run_tool = False


def converter():
    clear_screen()
    print(converter_logo)
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
        print(INVALID_CHOICE)
    
    continue_tool()

def decision_checker():
    clear_screen()
    print(decision_checker_logo)
    print("Welcome to the Decision Checker!")
    print("This program takes your score and tells you the grade between A and F")

    score = int(input("Enter your score: "))
    # Each grade band is a range of scores. 
    # The else branch catches scores below 0 or above 100 and assigns 'Invalid score' so the print statement never fails.
    if score in range(90, 101):
        grade = "A"
    elif score in range(80, 90):
        grade = "B"
    elif score in range(70, 80):
        grade = "C"
    elif score in range(60, 70):
        grade = "D"
    elif score in range(50, 60):
        grade = "E"
    elif score >= 0 and score < 50:
        grade = "F"
    else:
        grade = "Invalid score"

    print(f"Your grade is {grade}")
    continue_tool()

def welcome_menu():
    print("Welcome to the Number & Decision Toolkit")
    print(f"{"*" * 8}MENU{"*" * 8}")
    print("1. Calculator")
    print("2. Converter")
    print("3. Decision Checker")
    print("4. Exit")
    print()


run_toolkit = True
# This keeps the toolkit running
while run_toolkit:
    # This prepares for the tool the user picks
    run_tool = True
    welcome_menu()
    user_choice = input("Pick a number (1 - 4) from the menu above to proceed: ")
    if user_choice == "4":
        run_toolkit = False
    elif user_choice == "1":
        calculator()
    elif user_choice == "2":
        # This keeps a single tool(converter) running
        while run_tool:
            converter()
    elif user_choice == "3":
        # This keeps a single tool(decision_checker) running
        while run_tool:
            decision_checker()
    else:
        print(INVALID_CHOICE)
