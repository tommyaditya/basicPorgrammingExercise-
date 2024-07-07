def check_even_and_greater_than_10(num):
    if num % 2 == 0 and num > 10:
        print("The number is even and greater than 10.")
    else:
        print("The number is not even or not greater than 10.")

num = int(input("Enter a number: "))
check_even_and_greater_than_10(num)
