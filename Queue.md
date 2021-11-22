# Queue
When you were little do you remember hearing the ice cream truck drive around your neighborhood? After you run full sprint to your parents and beg them for money, or grab whatever money you have from chores, you run outside to see the truck with a huge line of neighborhood kids. To your suprise the line was super fast due to the **FIFO** (First In First Out) method. This method is what a **Queue** is. Queues are great for many things including:

* Operating Systems maintaining processes
* Printing and uploading images
* Call center phone systems to find who is next after they are done with a caller
* Video games to keep track of the most recent input 

<br>

Using an example above lets create a list of customers and the order in which they are called. Queues are very easily applied using lists. For the tutorial we will be using lists to use Queues.

``` python
# Create a list of customers.
list_of_customers = ["John Doe","Jane Doe", "Bob the builder","Michael Jordan"]


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
```