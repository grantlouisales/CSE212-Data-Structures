class BST:
    """
    Implement the Binary Search Tree (BST) data structure.  The Node 
    class below is an inner class.  An inner class means that its real 
    name is related to the outer class.  To create a Node object, we will 
    need to specify BST.Node
    """

    class Node:
        """
        Each node of the BST will have data and links to the 
        left and right sub-tree if there happens to be any. 
        """

        def __init__(self, data):
            """
            Initialize the attributes needed for the 
            node class.
            """
            self.data = data
            self.left = None
            self.right = None


    def __init__(self):
        """
        Initialize an empty BST.
        """
        self.root = None


    def insert(self, data):
        """
        Insert 'data' into the BST.  If the BST
        is empty, then set the root equal to the new 
        node.  Otherwise, use _insert to recursively
        find the location to insert.
        """
        if self.root is None:
            self.root = BST.Node(data)
        else:
            self._insert(data, self.root)  # Start at the root


    def _insert(self, data, node):
        """
        This function will look for a place to insert a node
        with 'data' inside of it.  The current sub-tree is
        represented by 'node'.  This function is intended to be
        called the first time by the insert function.
        """
        # If the user tries to add a number that is not
        # unique, it will return ending the _insert method.
        if data == node.data:
            return

        if data < node.data:
            # The data belongs on the left side.
            if node.left is None:
                # We found an empty spot
                node.left = BST.Node(data)
            else:
                # Need to keep looking.  Call _insert
                # recursively on the left sub-tree.
                self._insert(data, node.left)
        else:
            # The data belongs on the right side.
            if node.right is None:
                # We found an empty spot
                node.right = BST.Node(data)
            else:
                # Need to keep looking.  Call _insert
                # recursively on the right sub-tree.
                self._insert(data, node.right)


    def get_height(self):
        """
        Determine the height of the BST.  Note that an empty tree
        will have a height of 0 and a tree with one item (root) will
        have a height of 1.
        
        If the tree is empty, then return 0.  Otherwise, call 
        _get_height on the root which will recursively determine the 
        height of the tree.
        """
        if self.root is None:
            return 0
        else:
            return self._get_height(self.root)  # Start at the root


    def _get_height(self, node):
        """
        Determine the height of the BST.  The height of a sub-tree 
        (represented by 'node') is 1 plus the height of either the 
        left sub-tree or the right sub-tree (whichever one is bigger).

        This function intended to be called the first time by 
        get_height.
        """

        # If node is none return 0
        if node is None:
            return 0

        # Get left tree height by adding 1 everytime you recurse.
        # Do the same with the right. Then use max function to get the
        # biggest height of the two trees.
        return max(1 + self._get_height(node.left), 1 + self._get_height(node.right))


    def empty(self):
        """
        Return True if tree is empty, return false
        if not empty.
        """
        return self.root is None


    def __contains__(self, data):
        """ 
        Checks if data is in the BST.  This function
        supports the ability to use the 'in' keyword:

        if 5 in my_bst:
            ("5 is in the bst")

        """
        return self._contains(data, self.root)  # Start at the root


    def _contains(self, data, node):
        """
        This funciton will search for a node that contains
        'data'.  The current sub-tree being search is 
        represented by 'node'.  This function is intended
        to be called the first time by the __contains__ function.
        """

        # Base case #1: Data is not in tree
        if node is None:
            return False

        # Base case #2: Data is in the tree.
        elif data == node.data:
            return True

        # Smaller problem: Recurse through the tree.
        else:
            if data < node.data:
                return self._contains(data, node.left)
            else:
                return self._contains(data, node.right)


    def __iter__(self):
        """
        Perform a forward traversal (in order traversal) starting from 
	    the root of the BST.  This is called a generator function.
        This function is called when a loop	is performed:

        for value in my_bst:
            print(value)

        """
        yield from self._traverse_forward(self.root)  # Start at the root


    def _traverse_forward(self, node):
        """
        Does a forward traversal (in-order traversal) through the 
        BST.  If the node that we are given (which is the current
        sub-tree) exists, then we will keep traversing on the left
        side (thus getting the smaller numbers first), then we will 
        provide the data in the current node, and finally we will 
        traverse on the right side (thus getting the larger numbers last).

        The use of the 'yield' will allow this function to support loops
        like:

        for value in my_bst:
            print(value)

        The keyword 'yield' will return the value for the 'for' loop to
	    use.  When the 'for' loop wants to get the next value, the code in
	    this function will start back up where the last 'yield' returned a 
	    value.  The keyword 'yield from' is used when our generator function
        needs to call another function for which a `yield` will be called.  
        In other words, the `yield` is delegated by the generator function
        to another function.

        This function is intended to be called the first time by 
        the __iter__ function.
        """
        if node is not None:
            yield from self._traverse_forward(node.left)
            yield node.data
            yield from self._traverse_forward(node.right)


    def get_sum(self):
        """
        Get the sum of the right subtree.
        """
        if self.root is None:
            return 0
        else:
            return self._get_sum(self.root)


    def _get_sum(self, node):

        """
        Add the left side with recursion and add the right
        side with recursion and then add that to the total and
        return the total.
        """
        total, left, right = 0, 0, 0

        if node is None:
            return 0
        else:

            # Recurse through the left side
            if node.left != None:
                left = self._get_sum(node.left)

            # Recurse through the right side
            if node.right != None:
                right = self._get_sum(node.right)

            # Add them all together
            total = node.data + left + right

        return total


# Sample Test Cases (may not be comprehensive)
print("\n=========== PROBLEM 1 TESTS ===========")
tree = BST()
tree.insert(4)
tree.insert(2)
tree.insert(5)
tree.insert(6)
tree.insert(3)
tree.insert(1)
# print("Sum of given tree is: " + str(tree.get_sum()))

for x in tree:
    print(x) 
