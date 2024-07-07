def check_age_not_less_than_21(age):
    if age >= 21:
        print("You are 21 years old or older.")
    else:
        print("You are younger than 21 years old.")

age = int(input("Enter your age: "))
check_age_not_less_than_21(age)
