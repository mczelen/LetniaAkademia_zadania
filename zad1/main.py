from customersUtil import CustomersUtil

# load customers data
customers = CustomersUtil.load_customers("customers.json")

# print initial data
print("\nInitial data:")
CustomersUtil.print_customers(customers)

# apply promotion
promotion_customers = CustomersUtil.apply_promotion(customers)

# print processed data
print("\nPromotion applied:")
CustomersUtil.print_customers(customers)

# serialize customers with promotion applied
print("\nJSON serialized data:")
serialized_data = CustomersUtil.serialize_customers(promotion_customers)

# save JSON file
CustomersUtil.save_json("promotion_customers", serialized_data)