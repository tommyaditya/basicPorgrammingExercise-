def extract_domain(email):
    domain = email.split('@')[-1].split('.')[0]
    return domain

email = input("Enter your email address: ")
domain_name = extract_domain(email)
print("Domain name:", domain_name)
