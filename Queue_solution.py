class Ice_cream_truck:
    def __init__(self,max_size, stock):
        self.stock = stock
        self.max_size = max_size

        self.line = []

    def add_to_line(self, name):
        """
        Purpose: Add a person to the end of the line
        with the name given as an argument. If there happens to be 
        0 people in the line then the ice cream truck will go to the next
        neighborhood. Return the string "Have a good day" if the line is 
        empty.
        """
        pass


    def remove_first_in_line(self):
        """
        Purpose: Remove the first person in the line.
        Add a condition in the function to return a string saying "Have a good day"
        if the line is empty since you can remove nothing and the driver is
        going to a new neighborhood. Everyone will only be allowed 1 ice cream each.
        Deduct from the stock before you remove a person from the line.
        This function will only manipulate the line, stock, or return the given string.
        """
        pass

    def out_of_ice_cream(self):
        """
        Purpose: Return a boolean to see if the truck
        is out of ice cream or not. Return the string
        "Have a good day" if out of ice_cream.
        """
        return self.stock == 0

    def __str__(self):
        print(self.line)

def main():
    stock = 12
    ice_cream_truck_line = Ice_cream_truck(10, stock)
    
    print(ice_cream_truck_line)