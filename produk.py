def menu():
    print("\nMenu:")
    print("1. List products")
    print("2. Add product")
    print("3. Remove product")
    print("4. Remove by product number")
    print("5. Exit")

def list_products(product_list):
    if len(product_list) == 0:
        print("The product list is empty.")
    else:
        print("Product list:")
        for i, product in enumerate(product_list):
            print(f"{i + 1}. {product}")

def add_product(product_list):
    product = input("Enter product name: ")
    product_list.append(product)
    print(f"Product '{product}' has been added.")

def remove_product(product_list):
    product = input("Enter the name of the product to remove: ")
    if product in product_list:
        product_list.remove(product)
        print(f"Product '{product}' has been removed.")
    else:
        print(f"Product '{product}' not found in the list.")

def remove_by_number(product_list):
    try:
        number = int(input("Enter the number of the product to remove: "))
        if 1 <= number <= len(product_list):
            product = product_list.pop(number - 1)
            print(f"Product '{product}' with number {number} has been removed.")
        else:
            print("Invalid product number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def main():
    product_list = []
    while True:
        menu()
        choice = input("Choose an option (1-5): ")
        
        if choice == '1':
            list_products(product_list)
        elif choice == '2':
            add_product(product_list)
        elif choice == '3':
            remove_product(product_list)
        elif choice == '4':
            remove_by_number(product_list)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
