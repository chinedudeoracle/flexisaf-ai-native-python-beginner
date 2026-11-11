"""
Week 7 — Main Execution File
FlexiSAF AI-Native Python Internship (Beginner Stage)

This script demonstrates:
- Instantiating objects from different classes
- Inheritance (DigitalProduct from Product)
- Composition (Account holding Products)
- Validation testing with try/except
- Method execution (buy_product and top_up)

Author: Chinedu Iroanyah
Date: 2026-11-11
"""

from product import Product
from digital_product import DigitalProduct
from account import Account


# 1. Create Products
try:
    laptop = Product("Dell Inspiron XPS 15", 500000)
except ValueError as e:
    print(f"Error Caught: {e}")
try: 
    programming_ebook = DigitalProduct("FlexiSAF Native Python Beginner, 5th Edition", 150000, "www.flexisaf/downloads")
except ValueError as e:
    print(f"Error Caught: {e}")

my_account = Account("Chinedu Iroanyah", 1000000)

# 2. Buy Products
my_account.buy_product(laptop)
my_account.buy_product(programming_ebook)

# 3. Show results
print(f"Account Owner: {my_account.owner}")
print(f"Remaining Balance: ₦{my_account.balance:.2f}")
print(f"Products Bought: {my_account.products_bought}")

# 4. Test Validation
print("\n--- Testing Validation ---")
try:
    bad_product = Product("Bad Product", -500) # Negative price!
except ValueError as e:
    print(f"Error Caught Successfully: {e}")

# 5. Test Top Up
print("\n--- Testing Top Up ---")
my_account.top_up(50000)
my_account.top_up(-100)