# Binary Search Trees
**Binary search trees** (BST) are data structures that can help organize data with nodes. In a BST we have a root node which will be the first node in the BST and will have 2 child nodes. We will classify these child nodes as left node and right node. A sub-tree is anything that is a descendant of a node node. We use sub-trees to determine if the value inside of a node is lesser or greater than a node. The reason BST's are so useful is for their speed. Since we start with a root node it will contain a value, for example, lets say it contains the number 5. We add a value to the BST by checking if the new node value is greater or lesser than the root node value. If the value is greater than the root node it will become the roots right node. If the value is lesser it till be the root nodes left node. This not only works for the root node but for every node in the BST. Here is an image of that BST would look like, try to figure out where the 9 would go:

![BST Example](/Images/BSTImage.jpg)

After you have tried to figure out where the 9 goes lets go over it together! First we will look at the root node which happens to be the 8. Since all numbers that will be in the right sub-tree of 8 will be greater we can move to the right and get to 10. Now we will check if 9 is less than or greater than 10. Since 9 is less than 10 we will make 10's left node be 9. We traverse through a BST by using recusion and comparing values. We would compare 9 to 10 and see that it needs to go on the left side. Since 10's left node was empty we were able to put the 9 there. If it was not empty, we would continue traversing until we found a spot for the 9.

<br>

## Performance Table

|       Description         |      Performance     |        Code        |
|      :-----------:        |     :------------:   | :---------------:  |
|  Adding node to the BST   |       O(log n)       |    BST.insert(Node)|
|  Removing node from BST   |       O(log n)       |    BST.remove(Node)|
|  Traversing through BST   |       O(log n)       |    traverse_forwards and traverse_rerse          |
|  Checking if value in BST |       O(log n)       |    Contains(Values)|
|  Height of node in BST    |       O(log n)       |    BST.height(Node)|
|  Determine if BST is empty|       O(1)           |    BST.empty()     |
|  Determining size of BST  |       O(1)           |    BST.size()      |

<br>

## Balanced BST
BST's like above are great because of the speed of them.



You can check your code with the solution here: [Solution](SourceCodes/BST_solution.py)

[Back to Welcome Page](Welcome.md)