
# AVL tree implementation in Python


import sys

class Treenode:
    def __init__(self,data):
        self.height=1
        self.left=None
        self.right=None
        self.data=data
        
class AVL:
    #get height of node 
    def getHeight(self, root):
        if not root:
            return 0
        return root.height

    # Get balance factore of the node
    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)
    
    #insert node RECURSIVELY ---------------------------------------------------->>  
    def insertNodeR(self,root,value):
        node=Treenode(value)
        if root is None:
            return node
        elif(root.data<value):
            root.left = self.insertNodeR(root.left,value)
        else:
            root.right = self.insertNodeR(root.right, value)

        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))
        # Update the balance factor and balance the tree
        balanceFactor = self.getBalance(root)
        #if balenceFactor between -1 , 0 , 1 then no need of rotation
        #case 1 balenceFactor > 1
        if balanceFactor > 1:
        
            if value < root.left.key:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
        #case 2 balenceFactor < -1
        if balanceFactor < -1:
            if value > root.right.key:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
        return root
    # Right rotation 
    def rightRotate(self,root):
        temp1=root.left
        temp2=temp1.right
        temp1.right=root
        root.left=temp2
        
        root.height = 1 + max(self.getHeight(root.left),
                           self.getHeight(root.right))
        temp1.height = 1 + max(self.getHeight(temp1.left),
                           self.getHeight(temp1.right))
        return temp1
    #Left Rotation
    def leftRotate(self,root):
        temp1=root.right
        temp2=temp1.left
        temp1.left=root
        root.right=temp2
        
        root.height = 1 + max(self.getHeight(root.left),
                           self.getHeight(root.right))
        temp1.height = 1 + max(self.getHeight(temp1.left),
                           self.getHeight(temp1.right))
        return temp1
    
    #insert node Iteratively  ----------------------------------------------->>>
    def insertNodeI(self,root,value):
        
        node=Treenode(value)#create node
        if root is None:# check root is empty
            root=node
        else:#if not
            current=root
            while(current!=None):#iterate till insertion
                temp=current
                if(value<current.data):
                    current=current.left
                elif(value>current.data):
                    current=current.right
            #after getting position insert node at position
            if(value<temp.data):
                temp.left=node
            else:
                temp.right=node        
        # Update the balance factor and balance the tree
        balanceFactor = self.getBalance(root)
        #if balenceFactor between -1 , 0 , 1 then no need of rotation
        #case 1 balenceFactor > 1
        if balanceFactor > 1:
        
            if value < root.left.key:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
        #case 2 balenceFactor < -1
        if balanceFactor < -1:
            if value > root.right.key:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
        return root         
    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root
        return self.getMinValueNode(root.left) 
       
    def deleteNodeR(self,root,value):
        
        if root is None:
            return
        elif root.data>value:
            root.left=self.deleteNodeR(root.left,value)
        elif root.data<value:
            root.right=self.deleteNodeR(root.right,value)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
        temp = self.getMinValueNode(root.right)
        root.data= temp.data
        root.right = self.deleteNodeR(root.right,
                                          temp.data)
        if root is None:
            return root

        # Update the balance factor of nodes
        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        balanceFactor = self.getBalance(root)

        # Balance the tree
        if balanceFactor > 1:
            if self.getBalance(root.left) >= 0:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
        if balanceFactor < -1:
            if self.getBalance(root.right) <= 0:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
        return root
        
    def preOrder(self, root):
        if not root:
            return
        print("{0} ".format(root.data), end="")
        self.preOrder(root.left)
        self.preOrder(root.right)

    # Print the tree
    def printHelper(self, currPtr, indent, last):
        if currPtr != None:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "
            print(currPtr.data)
            self.printHelper(currPtr.left, indent, False)
            self.printHelper(currPtr.right, indent, True)




obj = AVL()
root = None
nums = [33, 13, 52, 9, 21, 61, 8, 11]
for num in nums:
    root = obj.insertNodeI(root, num)
obj.printHelper(root, "", True)
key = 13
root = obj.deleteNodeR(root, key)
print("After Deletion: ")
obj.printHelper(root, "", True) 