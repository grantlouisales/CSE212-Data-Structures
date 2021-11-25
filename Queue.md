# Queue
When you were little do you remember hearing the ice cream truck drive around your neighborhood? After you run full sprint to your parents and beg them for money, or grab whatever money you have from chores, you run outside to see the truck with a huge line of neighborhood kids. To your suprise the line was super fast due to the **FIFO** (First In First Out) method. This method is what a **Queue** is. Queues are great for many things including:

* Operating Systems maintaining processes
* Printing and uploading images
* Call center phone systems to find who is next after they are done with a caller
* Video games to keep track of the most recent input 

<br>

Here is a diagram of using Queues:
![Queue Example](Images/QueueExample.png)

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

## Why use queues over other data structures
As you can see up above the most time consuming performance was to remove an item from the queue. The performance was a worst case scenario of O(n) time. The reason why the .pop() method has this performance is because if you need to pop off the last item in the queue you would have to check every item in the queue before you got to the wanted index. Queues are very great performance wise but lets talk about why else it is good. Some of the reasons are:

* Easy to learn
* Organized
* Dont need to know what is next since a queue is used for FIFO
* Can use queues after only knowing a couple of python functionality

<br>

Using an example from above lets create a list of customers to imitate a line. This will be showing how to use all of the list functions up above.

# Example

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

# Problem to solve
We will be going back and coding out the ice cream scenario and create the line for it. We will need mutiple things to make this scenario. Things we need to include:
* A way to add people to the line
* A way to remove the first person from the line
* Dont add a person to the line if the line is over 10 people
* If out of ice cream end the program

I will be supplying the function names and some other stuff in the program to make it easier. Here are the functions and how they will be used in the program. Here is the template:

``` python
class Ice_cream_truck:
    def __init__(self,max_size, stock):
        self.stock = stock
        self.max_size = max_size

        self.line = []

    def add_to_line(self, name):
        """
        Purpose: Add a person to the end of the line
        with the name given as an argument. Have a 
        conditional that will compare the queue size
        to the max size and return a phrase saying
        you cant add more people since the max size has
        been reached.
        """
        pass


    def remove_first_in_line(self):
        """
        Purpose: Remove the first person in the line.
        If someone is removed from the line we know that
        an ice cream is given away. Since everyone
        is only allowed 1, deduct from the stock here.
        """
        pass


    def subtract_from_stock(self):
        """
        Purpose: Subtract amount from ice cream stock.
        """
        pass


    def get_line_size(self):
        """
        Purpose: Returns the size of the line
        """
        pass


    def out_of_ice_cream(self):
        """
        Purpose: Return a boolean to see if the truck
        is out of ice cream.
        """
        pass


    def __str__(self):
        """
        Purpose: Loop through self.line and grab the names of all
        who are in the line. Return everyone in the line.
        """
        front = "[ "
        end = "]"
        names = ""
        for name in self.line:
            names += name + " "
        return front + names + end


stock = 8
line = Ice_cream_truck(10, stock)

# ============== Test 1 ============== #
print("============== Test 1 ==============")
print()
line.add_to_line("Grant") 
line.add_to_line("Jeremy")
line.add_to_line("Breanna")
line.add_to_line("Hunter")
line.add_to_line("John")
line.add_to_line("Wyatt")
print(line) # Output: Grant Jeremy Breanna Hunter John Wyatt
print()

# ============== Test 2 ============== #
print("============== Test 2 ==============")
print()
line.remove_first_in_line()
line.remove_first_in_line()
print(line) # Output: Breanna Hunter John Wyatt

line.add_to_line("Ed")
line.add_to_line("Dawson")
line.add_to_line("Spencer")
line.add_to_line("Will")
line.add_to_line("Lori")
line.add_to_line("Amber")
print(line)  # Output: Breanna Hunter John Wyatt Ed Dawson Spencer Will Lori Amber
print()

# ============== Test 3 ============== #
print("============== Test 3 ==============")
print()
line.add_to_line("Lauren") # Output: Line is too big! Wait for more people to leave.
line.add_to_line("Linda") # Output: Line is too big! Wait for more people to leave.
print(line)  # Output: Breanna Hunter John Wyatt Ed Dawson Spencer Will Lori Amber

for person in range(line.get_line_size()):
    """
    We will then remove everyone from the line and give them
    ice cream. 

    Output: Have a great day guys!!
    """
    if line.out_of_ice_cream():
        print("Have a great day guys!!")

    line.remove_first_in_line()

print(line) # Ouptut: [ ]
``` 
Play around with it a little! If you want to dive in fully, add more tests, or add more to the class! Add a method that will allow people to ask how much ice cream they want and deduct that from the stock. You can have a lot of fun with Queues and create many functional programs! Explore and enjoy!


You can check your code with the solution here: [Solution](Queue_solution.py)

[Back to Welcome Page](Welcome.md)
