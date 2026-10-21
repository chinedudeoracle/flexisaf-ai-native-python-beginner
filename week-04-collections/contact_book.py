"""
Week 4 — Contact Book
FlexiSAF AI-Native Python Internship (Beginner Stage)

This script demonstrates:
- Dictionaries
- Lists
- Dictionary Comprehensions

Author: Chinedu Iroanyah
Date: 2026-10-21
"""
from logo import contact_logo
import os


def clear_screen():
    # 'nt' means Windows, otherwise it falls back to Linux/macOS commands
    os.system('cls' if os.name == 'nt' else 'clear')

# The main dictionary where contacts are stored. 
# Structure: { "Name": ["phone1", "phone2"] }
contact_book = {}


def add_contact():
    # We use a list here because one contact might have multiple phone numbers.
    phone = []
    name = input("Enter the name of the contact: ")
    num_of_phone = int(input(f"How many phone numbers does {name} have?: "))
    
    # Loop to collect all phone numbers for this contact
    for _ in range(0, num_of_phone):
        num = input("Enter the phone number: ")
        phone.append(num)
    
    # Add the name (key) and the list of phones (value) to the dictionary
    contact_book[name] = phone
    print(f"{name} has been added to your contact book.")
    # Pause so the user can read the confirmation before the screen clears
    input("\nPress Enter to return to the menu...")

def view_contacts():
    if not contact_book:
        print("Your contact book is empty")
    else:
        # DICTIONARY COMPREHENSION: 
        # We sort the items alphabetically by name, then rebuild a new dictionary.
        sorted_contacts = {name: phone for (name, phone) in sorted(contact_book.items())}
        
        for name, phone in sorted_contacts.items():
            # Use join() to turn the list of numbers into a clean string (e.g. "0801, 0802")
            formatted_phones = ", ".join(phone)
            print(f"Name: {name} | Phone: {formatted_phones}")
            
    # Pause so the user can read the list before it clears
    input("\nPress Enter to return to the menu...")

def delete_contact():
    if not contact_book:
        print("Your contact book is empty")
    else:
        name = input("Enter the name of the contact you want to delete: ")
        # Check if the name exists before trying to delete it to avoid a KeyError
        if name in contact_book:
            contact_book.pop(name)
            print(f"{name} has been deleted.")
        else:
            print(f"{name} is not in your contact book")
            
    # Pause so the user can read the result before it clears
    input("\nPress Enter to return to the menu...")

print(contact_logo)
print("Welcome to the contact book!\nPick an action from the menu below")

# Main program loop
use_contact_book = True
while use_contact_book:
    clear_screen()
    print("1. Add Contact\n2. View Contacts\n3. Delete Contact\n4. Exit")
    user_choice = input("Pick a choice from the menu above: ")
    
    # Route the user to the correct function based on their choice
    if user_choice == "1":
        add_contact()
    elif user_choice == "2":
        view_contacts()
    elif user_choice == "3":
        delete_contact()
    elif user_choice == "4":
        use_contact_book = False
    else:
        print("Invalid Input. Choose between 1 to 4")