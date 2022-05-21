import json
from customer import Customer
from datetime import date

class CustomersUtil:
    
    # Loads hardcoded customers data (by default no customer has promotion applied)
    @staticmethod
    def load_customers():
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

        json_c = json.dumps([customer.__dict__ for customer in customers], default=date_handler)
        print(json_c)