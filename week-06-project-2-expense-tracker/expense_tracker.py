"""
Week 6 — Project 2: File-Based Expense Tracker
FlexiSAF AI-Native Python Internship (Beginner Stage)

This script demonstrates:
- Reading and writing to a file (CSV)
- Error handling (try/except/else)
- Input validation
- Menu-driven logic

Author: Chinedu Iroanyah
Date: 2026-11-04
"""
from logo import logo


def add_expense():
    # Loop until the user provides a valid number for the amount
    while True:
        try:
            amount = float(input("Enter an amount: "))
            break  # Exit the loop immediately if the conversion succeeds
        except ValueError:
            # Catch the error if the user types letters instead of numbers
            print("Invalid amount. Please enter a number.")
            
    category = input("Enter a category (e.g., 'Food', 'Transport'): ").lower()
    description = input("Enter a description: ")
    
    # Format the data as a comma-separated string, ending with a newline
    expense_string = f"{amount},{category},{description}\n"
    
    # Open the file in Append mode ("a") so we don't overwrite previous data
    with open("./week-06-project-2-expense-tracker/expenses.csv", "a") as file:
        file.write(expense_string)

    print("Expense added successfully!")

def view_expense():
    try:
        # Attempt to open and read the file
        with open("./week-06-project-2-expense-tracker/expenses.csv", "r") as file:
            my_expense = file.readlines()
    except FileNotFoundError:
        # Catch the error if the file doesn't exist yet (e.g., first time running)
        print("You haven't Incurred any expenses yet.")
    else:
        # If no error occurred, pass the data to the summarizer
        summaries(my_expense)

def summaries(expenses):
    total_amount = 0
    food_amount = 0
    transport_amount = 0
    
    for line in expenses:
        # Split the comma-separated string into a list
        expense_list = line.split(",")
        
        # Convert the amount string back to a float to do math
        amount = float(expense_list[0])
        
        # Check the category and add to the respective totals
        if 'food' in expense_list:
            food_amount += amount
        elif 'transport' in expense_list:
            transport_amount += amount
            
        total_amount += amount
 
    # Print the final summary formatted to 2 decimal places
    print(f"Your total expense is ₦{total_amount:.2f}\nYou spent ₦{food_amount:.2f} on Food\nYou spent ₦{transport_amount:.2f} on Transportation")

def expense_tracker():
    track_expense = True
    while track_expense:
        print("1. Add Expense\n2. View Expenses & Summary\n3. Exit")
        
        choice = input("Pick a choice: ")
        
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expense()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

# Start the program
print(logo)
expense_tracker()