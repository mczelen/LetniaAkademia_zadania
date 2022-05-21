from customersUtil import CustomersUtil

customers = CustomersUtil.load_customers()

print("\nInitial data:")
CustomersUtil.print_customers(customers)

promotion_customers = CustomersUtil.apply_promotion(customers)

print("\nPromotion applied:")
CustomersUtil.print_customers(customers)

print("\nJSON serialized data:")
CustomersUtil.serialize_customers(promotion_customers)