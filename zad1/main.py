from customer import Customer

customers = [
    Customer("Thomas", "Calderon", "09291112345", "Thomas's address", "2009-09-11"),
    Customer("Derek", "Jones", "99050712345", "Derek's address", "1999-05-07"),
    Customer("Justin", "Cunningham", "02210112345", "Justin's address", "2002-01-01"),
    Customer("Brian", "Hernandez", "95051012345", "Brian's address", "1995-05-10"),
    Customer("Bobby", "Taylor", "10230112345", "Bobby's address", "2010-03-01")]

print("\nBEFORE:")
for n, customer in enumerate(customers):
    print(f'{n}: {customer}')

for n, customer in enumerate(customers):
    customer.apply_promotion()

print("\nAFTER:")
for n, customer in enumerate(customers):
    print(f'{n}: {customer}')