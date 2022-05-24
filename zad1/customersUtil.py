import json
from customer import Customer
from datetime import date

class CustomersUtil:
    
    # Loads customers data (by default no customer has promotion applied) 
    # If filename parameter is specified load data from ile, else load hardcoded data
    @staticmethod
    def load_customers(filename=None):
        if filename:
            # load json data from file
            with open(f'zad1/{filename}') as json_file:
                data = json.load(json_file)
            # iterate over customers list and unpack dict to Customer constructor
            return [Customer(**record) for record in data]

        return [
            Customer("Thomas", "Calderon", "09291112345", "Thomas's address", "2009-09-11"),
            Customer("Derek", "Jones", "99050712345", "Derek's address", "1999-05-07"),
            Customer("Justin", "Cunningham", "02210112345", "Justin's address", "2002-01-01"),
            Customer("Brian", "Hernandez", "95051012345", "Brian's address", "1995-05-10"),
            Customer("Bobby", "Taylor", "10230112345", "Bobby's address", "2010-03-01")]
    
    # Prints customer list in human-readable format for demonstraion pourposes 
    @staticmethod
    def print_customers(customers):
        for n, customer in enumerate(customers):
            print(f'{n}: {customer}')
    
    # Executes apply_promotion method on every customer and returns list of customers with promotion applied
    @staticmethod
    def apply_promotion(customers):
        promotion_customers = []
        for n, customer in enumerate(customers):
            customer.apply_promotion()
            if customer.promotion_applied:
                promotion_customers.append(customer)
        return promotion_customers
    
    # Serlializes customers data to JSON format
    @staticmethod
    def serialize_customers(customers):
        
        # handles serialization of date object 
        def date_handler(obj):
            if isinstance(obj, (date)):
                return obj.isoformat()
            return json.JSONEncoder().default(obj)

        json_string = json.dumps([customer.__dict__ for customer in customers], default=date_handler)
        print(json_string)
        return json_string

    # Saves JSON file
    @staticmethod
    def save_json(filename, content):
        with open(f'zad1/{filename}.json', 'w') as outfile:
            outfile.write(content)