class Product:
    """Class of products in the store app"""

    def __init__(self, name: str, price: float, quantity: int):
        if not name:
            raise ValueError("Name cannot be empty.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self.name: str = name
        self.price: float = price
        self.quantity: int = quantity
        self.active: bool = True

    def get_quantity(self) -> int:
        """Returns product quantity"""
        return self.quantity

    def set_quantity(self, quantity: int):
        """Sets product quantity and deactivates if reached zero"""
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        """Flag if product is active"""
        return self.active

    def activate(self):
        """Activate the product"""
        self.active = True

    def deactivate(self):
        """Deactivate the product"""
        self.active = False

    def show(self):
        """Print product info"""
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity: int) -> float:
        """Purchase a given quantity of the product.
        Returns total cost of the purchase
        """
        if quantity <= 0:
            raise ValueError("Purchase quantity must be greater than 0.")
        if not self.active:
            raise Exception("Product is not active.")
        if quantity > self.quantity:
            raise Exception("Not enough stock available.")
        self.set_quantity(self.quantity - quantity)
        return self.price * quantity

# bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
# mac = Product("MacBook Air M2", price=1450, quantity=100)

# print(bose.buy(50))
# print(mac.buy(100))
# print(mac.is_active())
#
# bose.show()
# mac.show()
#
# bose.set_quantity(1000)
# bose.show()