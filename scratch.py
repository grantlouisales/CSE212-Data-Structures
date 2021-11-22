# Create a list of customers.
list_of_customers = ["John Doe", "Jane Doe",
                     "Bob the builder", "Michael Jordan"]


# Lets loop through the list as if we were
while len(list_of_customers) != 0:

    # Since we are using the First In First Out method,
    # we will need to grab first item in the list and remove it.
    next_customer = list_of_customers.pop(0)
    print(next_customer, list_of_customers)

# 1st iteration output: John Doe ['Jane Doe', 'Bob the builder', 'Michael Jordan']
# 2nd iteration output: Jane Doe ['Bob the builder', 'Michael Jordan']
# 3rd iteration output: Bob the builder ['Michael Jordan']
# 4th iteration output: Michael Jordan []


# Use the append function to add customers to the queue
list_of_customers.append("Steph Curry")
list_of_customers.append("J.R Smith")
print(list_of_customers)  # Output ["Steph Curry", "J.R Smith"]
