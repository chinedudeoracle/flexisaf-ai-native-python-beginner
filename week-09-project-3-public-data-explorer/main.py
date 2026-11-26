"""
Week 9 — Project 3: Public Data Explorer
FlexiSAF AI-Native Python Internship (Beginner Stage)

This script provides a Command-Line Interface (CLI) that allows the user to:
- Search for books using the Open Library API
- Validate user input (preventing empty searches)
- Display formatted book details (title, author, publish year)
- Handle API failures and missing data gracefully using try/except

Author: Chinedu Iroanyah
Date: 2026-11-19
"""
import api_client

# Display the initial welcome message to the user
print("Welcome to FlexiSAF Library Book Search")

# Initialize a boolean variable to keep the program running until the user decides to exit
search_repo = True

# Start the main application loop
while search_repo:
    # Display the menu options
    print("1. Search for a Book \n2. Exit")
    
    # Prompt the user for their menu choice
    user_choice = input("Type either 1 or 2 to continue: ")
    
    # Input Validation: Check if the user typed something other than 1 or 2
    if user_choice != "1" and user_choice != "2":
        print("Invalid Choice, you have to type either 1 or 2")
        
    # Option 1: Search for a book
    elif user_choice == "1":
        user_title = input("Enter the title of the book you want to search for: ")
        
        # Edge Case Handling: Check if the user just pressed Enter without typing a title
        # .strip() removes whitespace so a space-only input is also caught
        if not user_title.strip():
            print("Book title cannot be empty")
            continue  # Skip the rest of the loop and show the menu again
        
        # Call the API client function and store the returned string in a variable
        search_result = api_client.search_book(user_search=user_title)
        
        # Check if the API returned the specific "No books found" string
        if search_result == "No books found":
            print("This book title is not available. Would you like to try again?")
        else:
            # If it's not an empty result, print the successful book details (or network error)
            print(search_result)
            
    # Option 2: Exit the program
    elif user_choice == "2":
        print("Thanks for using FlexiSAF Library Book Search!")
        # Change the loop condition to False to safely exit the while loop
        search_repo = False

