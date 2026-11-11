from product import Product

class DigitalProduct(Product):
    """Represents a digital product, inheriting from the base Product class."""

    def __init__(self, name, price, download_link):
        # Inheritance: Use super() to call the parent class (Product) constructor.
        # This reuses the name/price validation logic and sets self.name and self.price.
        super().__init__(name, price)
        
        # Add the unique attribute specific to DigitalProduct
        self.download_link = download_link