def check_voting_eligibility(age):
    if age >= 18 and age <= 65:
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote.")

age = int(input("Enter your age: "))
check_voting_eligibility(age)
