"""
PERFECT BINARY TREE :==>
A perfect binary tree is a type of binary tree in which every internal node has exactly 
two child nodes and all the leaf nodes are at the same level.
"""
class PerfectTree:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
        
    # Calculate the depth
    def calculateDepth(node):
        d = 0
        while (node is not None):
            d += 1
            node = node.left
        return d
    #check whether tree is perfect or not     
    def isPerfectTree(self,root,depth,level=0):
        # An empty tree is perfect
        if (root == None):
            return True
 
        # If leaf node, then its depth must
        # be same as depth of all other leaves.
        if (root.left == None and root.right == None):
            return (depth == level + 1)
 
        # If internal node and one child is empty
        if (root.left == None or root.right == None):
            return False
 
        # Left and right subtrees must be perfect.
        return (self.isPerfectTree(root.left, depth, level + 1) and
                self.isPerfectTree(root.right, depth, level + 1))
        
root = None
root = PerfectTree(1)
root.left = PerfectTree(2)
root.right = PerfectTree(3)
root.left.left = PerfectTree(4)
root.left.right = PerfectTree(5)

if (root.isPerfectTree(root, root.calculateDepth(root))):
    print("The tree IS a perfect binary tree")
else:
    print("The tree IS NOT a perfect binary tree")