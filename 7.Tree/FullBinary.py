from dataclasses import dataclass
"""
A full Binary tree is a special type of binary tree in which every parent node/internal 
node has either two or no children.
"""

class FullBinary:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
        
    def isFullTree(self,root):
        if root is None:
            return True
        #check whether child is present or not
        if root.left is None and root.right is None:
            return True
        
        if root.left is not None and root.right is not None:
            return (self.isFullTree(root.left) and self.isFullTree(root.right))
        
        return False


    
root=FullBinary(10)
root.left=FullBinary(20)
root.right=FullBinary(30)
root.left.left=FullBinary(40)
root.left.right=FullBinary(50)
root.right.left=FullBinary(60)
root.right.right=FullBinary(70)

if root.isFullTree(root):
    print("The tree is a full binary tree")
else:
    print("The tree is not a full binary tree")