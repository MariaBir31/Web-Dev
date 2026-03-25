class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total_value(self):
        return self.price * self.quantity

    def __str__(self):                            
        return f"Product: {self.name}, Price: {self.price}"


class DiscountedProduct(Product):
    def __init__(self, name, price, quantity, discount):
        super().__init__(name, price, quantity)
        self.discount = discount

    def get_total_value(self):
        total = self.price * self.quantity
        return total * (1 - self.discount)

    def __str__(self):
        return f"Product: {self.name}, Price: {self.price}, Discount: {int(self.discount * 100)}%"


product = Product("Apple", 1.5, 10)
discounted = DiscountedProduct("Laptop", 1000.0, 2, 0.2)

print(product)
print(discounted)
print(product.get_total_value())
print(discounted.get_total_value())