class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

class Transaction:
    def __init__(self):
        self.transactions = []
        self.profit = 0
    
    def add_transaction(self, product, quantity):
        if product.stock >= quantity:
            self.transactions.append((product, quantity))
            product.stock -= quantity
            self.profit += product.price * quantity
            print(f"Transaction successful: {quantity} {product.name}(s) purchased.")
        else:
            print("Insufficient stock.")

    def display_summary(self):
        print("Transaction Summary:")
        total_transactions = len(self.transactions)
        print(f"Total transactions: {total_transactions}")
        print(f"Total profit: ${self.profit}")

def main():
    # Create some products
    products = [
        Product("Item1", 10, 20),
        Product("Item2", 15, 15),
        Product("Item3", 20, 10)
    ]
    
    # Create a transaction instance
    transaction = Transaction()
    
    while True:
        print("\nAvailable Products:")
        for i, product in enumerate(products, start=1):
            print(f"{i}. {product.name} - ${product.price} - Stock: {product.stock}")
        
        choice = input("Enter the number of the product you want to buy (0 to exit): ")
        
        if choice == '0':
            break
        
        try:
            choice = int(choice)
            if 0 < choice <= len(products):
                quantity = int(input("Enter the quantity: "))
                transaction.add_transaction(products[choice-1], quantity)
            else:
                print("Invalid choice. Please enter a number between 1 and", len(products))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    # Display transaction summary
    transaction.display_summary()

if __name__ == "__main__":
    main()
