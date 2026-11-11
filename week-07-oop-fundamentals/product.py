class Product:
    """Represents a physical product with a name and price."""

    def __init__(self, name, price):
        # Encapsulation: Validate data immediately to prevent bad state.
        # A product with a negative price should not exist.
        if price < 0:
            raise ValueError("Price cannot be negative")
            
        self.name = name
        self.price = price