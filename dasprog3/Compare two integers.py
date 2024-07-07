def compare_integers(a, b):
    if a > b:
        print("First integer is greater.")
    elif a < b:
        print("Second integer is greater.")
    else:
        print("Both integers are equal.")

num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
compare_integers(num1, num2)
