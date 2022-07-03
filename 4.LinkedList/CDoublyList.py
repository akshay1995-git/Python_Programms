class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        
    def addAtFront(self,data):
        node=Node(data)
        if(self.head==None):
            self.head=node
            self.tail=node
        else:
            
            node.next=self.head
            self.head.prev=node
            self.head=node
            
    def addAtEnd(self,data):
        node=Node(data)
        if(self.head==None):
            self.head=node
            self.tail=node
        else:
            node.prev=self.tail
            node.next=self.head
            self.tail.next=node
            self.tail=node
            
    def printListF(self):
        curr=self.head
        print("Forward Traverse : ")
        while(curr!=self.tail):
            print(curr.data,end="| <- -> |")
            curr=curr.next
        print(curr.data,end="| <--> |")
        
    def printListR(self):
        curr=self.tail
        print("Reverse Traverse : ")
        while(curr!=self.head):
            print(curr.data,end="| <- -> |")
            curr=curr.prev
        print(curr.data,end="| <--> |")
        
obj=LinkedList()

obj.addAtFront(20)
obj.addAtFront(10)
obj.addAtEnd(30)
obj.addAtEnd(40)

obj.printListF()