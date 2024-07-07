def sum_of_digits(num):
    sum_digits = 0
    while num > 0:
        digit = num % 10
        sum_digits += digit
        num //= 10
    return sum_digits

num = int(input("Enter an integer: "))
print("Sum of digits:", sum_of_digits(num))
