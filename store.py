from typing import List
from products import Product


class Store:
    """Represents a store that manages a collection of products."""

    def __init__(self, product_list: List[Product]):
        """Initializes the Store with a list of products"""
        self.products = product_list

    def add_product(self, product: Product):
        """Adds product to the store"""
        self.products.append(product)

    def remove_product(self, product: Product):
        """Removes product from the store"""
        self.products.remove(product)

    def get_total_quantity(self) -> int:
        """Returns the total number of items in the store"""
        return sum(p.get_quantity() for p in self.products)

    def get_all_products(self) -> List[Product]:
        """List of all products in the store that are active"""
        return [p for p in self.products if p.is_active()]

    def order(self, shopping_list: List[tuple]) -> float:
        """
        Order for multiple products.
        Receives a list of tuples (product, quantity) for purchase.
        Returns Total cost of the entire order.
        """
        total = 0.0
        for product, quantity in shopping_list:
            total += product.buy(quantity)
        return total


product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                Product("Google Pixel 7", price=500, quantity=250),
               ]

# best_buy = Store(product_list)
# products = best_buy.get_all_products()
# print(best_buy.get_total_quantity())
# print(best_buy.order([(products[0], 1), (products[1], 2)]))