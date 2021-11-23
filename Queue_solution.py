class Ice_cream_truck:
    def __init__(self,max_size, stock):
        self.stock = stock
        self.max_size = max_size

        self.line = []

    def add_to_line(self, name):
        """
        Purpose: Add a person to the end of the line
        with the name given as an argument.
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

    
    def get_line_size(self):
        """
        Purpose: Returns the size of the line
        """
        return len(self.line)


    def out_of_ice_cream(self):
        """
        Purpose: Return a boolean to see if the truck
        is out of ice cream.
        """
        return self.stock == 0


    def __str__(self):
        """
        Purpose: Loop through self.line and grab the names of all
        who are in the line. Return everyone in the line.
        """
        names = ""
        for name in self.line:
            names += name + " "

        return names


stock = 12
line = Ice_cream_truck(10, stock)

# ============== Test 1 ============== #
line.add_to_line("Grant") 
line.add_to_line("Jeremy")
line.add_to_line("Breanna")
line.add_to_line("Hunter")
line.add_to_line("John")
line.add_to_line("Wyatt")
print(line) # Output: Grant Jeremy Breanna Hunter John Wyatt

# ============== Test 2 ============== #
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


# ============== Test 3 ============== #
line.add_to_line("Lauren")
line.add_to_line("Linda")
print(line)  # Output: Breanna Hunter John Wyatt Ed Dawson Spencer Will Lori Amber


for person in range(line.get_line_size()):
    """
    We will then remove everyone from the line and give them
    ice cream.
    """
    if line.out_of_ice_cream():
        print("Have a great day guys!!")

    line.remove_first_in_line()


    

