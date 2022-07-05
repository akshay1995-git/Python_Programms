"""
The properties that separate a binary search tree from a regular binary tree is

All nodes of left subtree are less than the root node
All nodes of right subtree are more than the root node
Both subtrees of each node are also BSTs i.e. they have the above two properties
"""

from turtle import right


class BinarySearchTree:
   
        
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
    
    # Insert node iterartively     
def insertNode(root,data):
        node=BinarySearchTree(data)
        if root is None:
            root=node
            return
        current=root
        while(current != None):
            temp=current
            if(data<current.data):
                current=current.left
            else:
                current=current.right
                
        if(data<temp.data):
            temp.left=node
        else:
            temp.right=node
            
        return root
            
    # Inorder traversal
        
def traverseInOrder(root):
        
   
    traverseInOrder(root.left)
    print(root.data, end=' ')
    traverseInOrder(root.right)
        
def searchNode(self,root):
        value=int(input("Enter a value for search :"))
        if(root ==None):
            return False
        if(root.data==value):
            return True
        if(root.data>value):
            self.searchNode(root.left)
        elif(root.data<value):
            self.searchNode(root.right)
            
        return False
    
def minValueNodeAndData(node):
        current = node
    # Find the leftmost leaf
        while(current.left is not None):
            current = current.left

        print("Node Address : ",current,"Node Data : ",current.data)
    
def deleteNode(self,root,value):
        """
        the node to be deleted is the leaf node. In such a case, simply delete the node from the tree.
        the node to be deleted lies has a single child node. In such a case follow the steps below:
            Replace that node with its child node.
            Remove the child node from its original position.
        the node to be deleted has two children. In such a case follow the steps below:

            Get the inorder successor of that node.
            Replace the node with the inorder successor.
            Remove the inorder successor from its original position.
        """
        if root is None:
            print("No Node !!! Tree is Empty ")
        if(root.data>value):
            root.left = self.deleteNode(root.left, value)
        elif(root.data<value):
            root.right=self.deleteNode(root.right,value)
        else:
            # node to be deleted lies has a single child node.
            # left none is none
            if(root.left is None):
                temp=root.right
                root=None
                return temp
            # right none is none
            if(root.right is None):
                temp=root.left
                root=None
                return temp

root=None          
root = insertNode(root, 8)
root = insertNode(root, 3)
root = insertNode(root, 1)
root = insertNode(root, 6)
root = insertNode(root, 7)
root = insertNode(root, 10)
root = insertNode(root, 14)
root = insertNode(root, 4)

print("Inorder traversal: ", end=' ')
traverseInOrder(root)        
            