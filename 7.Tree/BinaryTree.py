class BinaryTree:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
    #Pre order Traversal    
    def traversePreOrder(self):
        print(self.data, end=' ')
        if self.left:
            self.left.traversePreOrder()
        if self.right:
            self.right.traversePreOrder()
            
    # In Order Traversal        
    def traverseInOrder(self):
        
        if self.left:
            self.left.traverseInOrder()
        print(self.data, end=' ')
        if self.right:
            self.right.traverseInOrder()
            
    #Post Order Traversal
    def traversePostOrder(self):
        if self.left:
            self.left.traversePostOrder()
        if self.right:
            self.right.traversePostOrder()
            
        print(self.data,end=" ")
    
    # check height of node 
    
    def checkHeight(self,root):
        height=0
        if root is None:
            return height
        else:
            current=root
            while(current is not None):
                    height+=1
                    current=current.left
            return height  
    #  COUNTING LEAF NODE USING ITERATION
    def countLeafI(self,root):
        """
        leafcount=0
        if root is none return 0
        elif root is not none 
            if root.left and root.right is none return 1
        else:
        temp1=root.left
        temp2=root.right
        while(temp1 is not none )
        
        """
        """
        leafCount=0
        if root is None:
            return leafCount
        if root is not None:
            if root.left is None and root.right is None:
                return 1
            else:
                current1=root.left
                current2=root.right
                while(current1.left is not None or current1.right is not None):
                    
                   current1=current1.left
                while(current2.right is not None and current2.left is not None):
                    
                    current2=current2.right
                    
                leafCount+=1
                
                return leafCount
                   
                
        
        """
    
    #  COUNTING OF LEAF NODE USING RECURSION 
    def countLeafR(self,root):
        leafCount=0
        if root is None:
            return leafCount
        elif root is not None:
            if root.left is None and root.right is None:
                return 1
        
            
                
        return self.countLeafR(root.left)+self.countLeafR(root.right)   
                       
root=BinaryTree(10)
root.left=BinaryTree(20)
root.right=BinaryTree(30)
root.left.left=BinaryTree(40)
root.left.right=BinaryTree(50)
root.right.left=BinaryTree(60)
root.right.right=BinaryTree(70)

print("Pre-Order Traversal -->> ")
root.traversePreOrder()
print("\nIn-Order Traversal -->>")
root.traverseInOrder()
print("\nPost-Order Traversal -->>")
root.traversePostOrder()

print("\n Height :",root.checkHeight(root))

print("\n Leaf Count By Recursion :",root.countLeafR(root))

print("\n Leaf Count By Iteration:",root.countLeafI(root))

"""
Types of Binary Tree :

1. Full Binary Tree
A full Binary tree is a special type of binary tree in which every parent node/internal node 
has either two or no children.

2.Perfect Binary Tree
A perfect binary tree is a type of binary tree in which every internal node has exactly two 
child nodes and all the leaf nodes are at the same level.

3.Complete Binary Tree
It is same as of Full Binary Tree but major differences
All the leaf elements must lean towards the left.
The last leaf element might not have a right sibling i.e. a complete binary tree doesn't have
to be a full binary tree.

4.Degenrate Binary Tree
A tree having single child only either left or right child

5.Skewed Binary Tree
A tree having single child lean towards either only left or only right
2 Type->left-skewed and right skewed


"""