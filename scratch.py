list_of_customers = ["John Doe", "Jane Doe", "Bob the builder", "Michael Jordan"]

# Lets loop through the list as if we were
while len(list_of_customers) != 0:

    # Since we are using the First In First Out method,
    # we will need to grab first item in the list and remove it.
    next_customer = list_of_customers.pop(0)  # Output: John Doe
    print(next_customer, list_of_customers)
