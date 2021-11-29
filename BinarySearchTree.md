# Binary Search Trees
**Binary search trees** (BST) are data structures that can help organize data with nodes. In a BST we have a root node which will be the first node in the BST and will have 2 child nodes. We will classify these child nodes as left node and right node. A sub-tree is anything that is a descendant of any given node. We use sub-trees to determine if the value inside of a node is lesser or greater than a node. The reason BST's are so useful is for their speed. Since we start with a root node it will contain a value, for example, lets say it contains the number 5. We add a value to the BST by checking if the new node value is greater or lesser than the root node value. If the value is greater than the root node it will become the roots right node. If the value is lesser it till be the root nodes left node. This not only works for the root node but for every node in the BST. Here is an image of that BST would look like, try to figure out where the 9 would go:

![BST Example](/Images/BSTImage.jpg)

After you have tried to figure out where the 9 goes lets go over it together! First we will look at the root node which happens to be the 8. Since all numbers that will be in the right sub-tree of 8 will be greater we can move to the right and get to 10. Now we will check if 9 is less than or greater than 10. Since 9 is less than 10 we will make 10's left node to be 9. We traverse through a BST by using recusion and comparing values. We would compare 9 to 10 and see that it needs to go on the left side. Since 10's left node was empty we were able to put the 9 there. If it was not empty, we would continue traversing until we found a spot for the 9.

<br>

## Performance Table

|       Description         |      Performance     |        Code         |
|      :-----------:        |     :------------:   | :---------------:   |
|  Adding node to the BST   |       O(log n)       |    BST.insert(Node) |
|  Removing node from BST   |       O(log n)       |    BST.remove(Node) |
|  Traversing through BST   |       O(log n)       |    traverse_forwards and traverse_reverse        |
|  Checking if value in BST |       O(log n)       |    Contains(Values) |
|  Height of node in BST    |       O(log n)       |    BST.height(Node) |
|  Determine if BST is empty|       O(1)           |    BST.empty()      |
|  Determining size of BST  |       O(1)           |    BST.size()       |


As you can see every functionality to a BST is O(log n) or faster. For example, lets say we are looking for the node containing the number 5 and the root node contains the number 1. Since we know 5 is greater than 1 we don't even have to search through the left side of the BST. See how fast that is? With just the first comparison we can cut the search by half immediately.

<br>

## Height of a BST
We determine the height of a BST by getting the largest amount of nodes between a leaf node and the target node. A leaf node is a node that has no child nodes. Lets use this picture as an example:

![BST Example](/Images/BSTExample.png)

Let's start at the root. I like to count from the target node to the leaf farthest away from it. We will count each node from the root to the furthest leaf node. In our case 3 and -4 will be the 2 furthest leaf nodes. The height of the root to 18 will be 2 since there is the root and 18 in that tree. With that same logic lets find the height of the left tree. What is the height of the BST? Since we will take the largest path the height of the BST will be 3. We know this is 3 because we will count the root, the node with value 2, and the node with -4 will get us 3. We can also get to the node with 3 and use that since they are both of equal height.

<br>

## Balanced BST
A balanced BST is a BST that does not have a dramatic difference of height between the right sub-tree and the left sub-tree. If any side tree has a greater height by 2 or more will cause the BST to be unbalanced. The reason why a unbalanced tree is bad is because it starts to become more and more like a linked list. If out BST becomes more and more like a linked list the slower it gets. Lets take a look at an unbalanced BST:

![Unbalanced BST](/Images/UnbalancedBST.png)

As you can see the right sub-tree is so much bigger than the left side. Now lets talk about why this is bad. If I were to ask you to search for the 6 in the BST how many nodes will you go through before you find it? Since 6 is the furthest leaf it will be the same as the height which is 5. That is really slow but, what if the data were put in differently. Lets say the order we put the numbers is this order: 4,2,5,3,1,6. Now lets look at the image below to see what the new BST will look like:

![Rearranged BST](/Images/RearrangedBST.png)

Now lets try to find 6 again and how long it takes. The amount of nodes checked will be 3 compared to 5. Might not seem like aa crazy jump but, lets say this BST had 10,000 nodes and trying to look for the node with the value 9288. If the BST was unbalanced it would take a much longer amount of time to find the value.

<br>

## Example of Inserting to a binary tree
``` python
def insert(self, data):
    """
    Insert data into the BST. If the BST is empty,
    make the value the node. Else, traverse through the
    BST.
    """

    if self.root is None:
        self.root = BST.Node(data)
    else:
        self._insert(data, self.root)


def _insert(self, data, node):
    """
    Recursively call the _insert function until you find
    and empty place to put the node.
    """

    # If the data is less than the current nodes data,
    # go down the left sub-tree.
    if data < node.data:

        # Set current node's left node to
        # the given node since there is an empty spot.
        if node.left is None:
            node.left = BST.node(data)

        # Call if the spot is not empty.
        else:
            self._insert(data, node.left)

    # If the data is greater than the current nodes data,
    # go down the right sub-tree.
    elif data >= node.data:

        # Set current node's right node to
        # the given node since there is an empty spot.
        if node.right is None:
            node.right = BST.node(data)

        # Call if the spot is not empty.
        else:
            self._insert(data, node.right)
```
<br>

# Problem to solve

You can check your code with the solution here: [Solution](SourceCodes/BST_solution.py)

[Back to Welcome Page](Welcome.md)