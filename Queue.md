# Queue
When you were little do you remember hearing the ice cream truck drive around your neighborhood? After you run full sprint to your parents and beg them for money, or grab whatever money you have from chores, you run outside to see the truck with a huge line of neighborhood kids. To your suprise the line was super fast due to the **FIFO** (First In First Out) method. This method is what a **Queue** is. Queues are great for many things including:

* Operating Systems maintaining processes
* Printing and uploading images
* Call center phone systems to find who is next after they are done with a caller
* Video games to keep track of the most recent input 

<br>
<br>

## Python list functionality
Queues are very easily applied using lists. For the tutorial we will be using lists to learn Queues. Queues, like customer lines, need to allow people to go to the back of the line and leave the line after they have been helped. Here are some python list methods needed to compliment Queues:

<br>

|       Description         |      Python Code      |     Performance     | 
|      :-----------:        |     :------------:    |     :-----------:   |
|Add value to end of queue  |  queue.append(value)  |         O(1)        |
|Remove value from front of queue| value = queue.pop(0)|      O(n)        |
|Get length of queue        |   length = len(queue) |         O(1)        |
|Check if queue is empty    | if len(queue) == 0:   |         O(1)        |

<br>
<br>

Using an example from above lets create a list of customers to imitate a line. This will be showing how to use all of the list functions up above.

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


# Use the append function to add customers to the queue
list_of_customers.append("Steph Curry")
list_of_customers.append("J.R Smith") 
print(list_of_customers) # Output ["Steph Curry", "J.R Smith"]
```
<br>
<br>

# Example: 