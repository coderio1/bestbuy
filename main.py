import products
import store


def start(store_obj):
    """Runs the app, instances the store obj"""
    while True:
        print("\n   Store Menu")
        print("   ----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("\nPlease choose a number: ")

        if choice == "1":
            all_products = store_obj.get_all_products()
            print("\n------")
            for i, product in enumerate(all_products, 1):
                print(f"{i}. ", end="")
                product.show()
            print("------")

        elif choice == "2":
            print(f"\nTotal of {store_obj.get_total_quantity()} items in store")

        elif choice == "3":
            all_products = store_obj.get_all_products()
            print("\n------")
            for i, product in enumerate(all_products, 1):
                print(f"{i}. ", end="")
                product.show()
            print("------")

            shopping_list = []
            print("When you want to finish order, enter empty text.")
            while True:
                product_input = input("Which product # do you want? ")
                if product_input == "":
                    break
                quantity_input = input("What amount do you want? ")
                if quantity_input == "":
                    break
                try:
                    product_num = int(product_input)
                    quantity = int(quantity_input)
                    if 1 <= product_num <= len(all_products):
                        shopping_list.append((all_products[product_num - 1], quantity))
                        print("Product added to list!")
                    else:
                        print("Invalid product number.")
                except ValueError:
                    print("Please enter valid numbers.")

            if shopping_list:
                try:
                    total = store_obj.order(shopping_list)
                    print(f"\nOrder made! Total payment: ${total}")
                except Exception as e:
                    print(f"\nError: {e}")

        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


# list of inventory stock
product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                products.Product("Google Pixel 7", price=500, quantity=250)
                ]
best_buy = store.Store(product_list)

if __name__ == "__main__":
    start(best_buy)
