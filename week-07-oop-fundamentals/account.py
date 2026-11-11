class Account:
    """Represents a user's wallet and purchase history."""

    def __init__(self, owner_name, balance):
        # Initialize account details and an empty list for purchased products
        self.owner = owner_name
        self.balance = balance
        self.products_bought = []

    def top_up(self, amount):
        # Validation: Prevent adding negative amounts to the balance
        if amount < 0:
            print("Top up amount cannot be negative")
        else:
            self.balance += amount
            print(f"Top up successful. Account balance is ₦{self.balance:.2f}")

    def buy_product(self, product):
        # Composition: The Account uses the Product object passed into this method.
        # It checks if the balance is sufficient before making the purchase.
        if product.price > self.balance:
            print("Insufficient funds!")
        else:
            # Deduct price and record the product name
            self.balance -= product.price
            self.products_bought.append(product.name)