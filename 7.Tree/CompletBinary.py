
"""
COMPLETE BINARY TREE :==>>
A complete binary tree is a binary tree in which all the levels are completely filled except 
possibly the lowest one, which is filled from the left.

A complete binary tree is just like a full binary tree, but with two major differences

All the leaf elements must lean towards the left.
The last leaf element might not have a right sibling i.e. a complete binary tree doesn't
have to be a full binary tree.
"""

class CompleteBinary:
    def __init__(self,data):
        self.right=None
        self.left=None
        self.data=data
        
  # Count the number of nodes
def count_nodes(root):
    if root is None:
        return 0
    return (1 + count_nodes(root.left) + count_nodes(root.right))


# Check if the tree is complete binary tree
def is_complete(root, index, numberNodes):

    # Check if the tree is empty
    if root is None:
        return True

    if index >= numberNodes:
        return False

    return (is_complete(root.left, 2 * index + 1, numberNodes)
            and is_complete(root.right, 2 * index + 2, numberNodes))


root = CompleteBinary(1)
root.left = CompleteBinary(2)
root.right = CompleteBinary(3)
root.left.left = CompleteBinary(4)
root.left.right = CompleteBinary(5)
root.right.left = CompleteBinary(6)

node_count = count_nodes(root)
index = 0

if is_complete(root, index, node_count):
    print("The tree is a complete binary tree")
else:
    print("The tree is not a complete binary tree")
        
    
        
