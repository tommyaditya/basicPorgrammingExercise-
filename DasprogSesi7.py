# Printing numbers from 1 to 10 using a loop
for i in range(1, 11):
    print(i)

# Reversing a string by inputting your name
name = input("Enter your name: ")
reversed_name = ''
for char in name[::-1]:
    reversed_name += char
print("Reversed name:", reversed_name)

# Finding the largest and smallest number in a list
numbers = [10, 20, 5, 40, 30, 72, 34]
largest = numbers[0]
smallest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num
print("Largest number:", largest)
print("Smallest number:", smallest)

# Removing duplicates from a list
numbers = [1, 2, 3, 4, 2, 3, 5, 6, 1]
unique_numbers = []
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)
print("List with duplicates removed:", unique_numbers)
