from customer import Customer

customers = [
    Customer("Thomas", "Calderon", "99010111229", "1999-01-01"),
    Customer("Derek", "Jones", "99010111229", "1999-01-01"),
    Customer("Justin", "Cunningham", "99010111229", "1999-01-01"),
    Customer("Brian", "Hernandez", "99010111229", "1999-01-01"),
    Customer("Bobby", "Taylor", "99010111229", "2010-01-01")
    ]

for n, customer in enumerate(customers):
    print(f'{n}: {customer}')