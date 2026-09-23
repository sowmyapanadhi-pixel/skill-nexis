#Billing System
class Product:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity


class Bill:

    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def calculate_total(self):
        total = 0

        for product in self.products:
            total = total + product.total_price()

        return total

    def calculate_tax(self, total):
        tax = total * 0.18
        return tax

    def display_bill(self):

        total = self.calculate_total()
        tax = self.calculate_tax(total)
        final_total = total + tax

        print("\n========== BILL ==========")
        print(f"{'Product':<20}{'Price':<10}{'Qty':<10}{'Total':<10}")
        print("-" * 50)

        for product in self.products:
            print(
                f"{product.name:<20}"
                f"{product.price:<10}"
                f"{product.quantity:<10}"
                f"{product.total_price():<10}"
            )

        print("-" * 50)
        print("Subtotal:", total)
        print("Tax (18%):", tax)
        print("Final Total:", final_total)
        print("===========================")


# Create products
product1 = Product("Notebook", 50, 2)
product2 = Product("Pen", 20, 3)
product3 = Product("Bag", 500, 1)

# Create bill
bill = Bill()

# Add products
bill.add_product(product1)
bill.add_product(product2)
bill.add_product(product3)

# Display bill
bill.display_bill()