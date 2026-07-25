# Product Inventory System using OOP

class Product:
    def __init__(self, product_id, product_name, price):
        self.product_id = product_id
        self.product_name = product_name
        self.price = price

    def get_category(self):
        if self.price >= 1000:
            return "Expensive"
        else:
            return "Affordable"

    def display(self):
        print("Product ID   :", self.product_id)
        print("Product Name :", self.product_name)
        print("Price        :", self.price)
        print("Category     :", self.get_category())
        print("-" * 30)


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def display_products(self):
        if len(self.products) == 0:
            print("No products available.")
        else:
            print("\n----- Product Details -----")
            for product in self.products:
                product.display()


# Main Program
inventory = Inventory()

n = int(input("Enter number of products: "))

for i in range(n):
    print(f"\nEnter details of Product {i + 1}")
    product_id = input("Product ID: ")
    product_name = input("Product Name: ")
    price = float(input("Price: "))

    product = Product(product_id, product_name, price)
    inventory.add_product(product)

inventory.display_products()
