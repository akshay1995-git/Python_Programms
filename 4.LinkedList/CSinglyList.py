class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
        
    def addFromFront(self,data):
        node=Node(data)
        if(self.head==None):
            self.head=node
            
        else:
            node.next=self.head
            self.head=node
    
    def addFromRear(self,data):
        node=Node(data)
        if(self.head==None):
            self.head=node
            
        else: 
            curr=self.head
            while(curr.next!=self.head):
                curr=curr.next
            curr.next=node
            node.next=self.head #last node contain address of first node instead of none
            
    def deleteFromFront(self):
        if(self.head==None):
            print("List is Empty ")
        else:
            self.head=self.head.next
            
    def deleteFromRear(self):
        if(self.head==None):
            print("List is Empty ")
        else:
            curr=self.head
            temp=None
            while(curr.next!=self.head):
                temp=curr
                curr=curr.next
            temp.next=curr.next
            curr.next=None
            
    def printList(self):
        current=self.head
        while(current!=None):
            print(current.data,end=" ==>> ")
            current=current.next
                           
                           
obj=LinkedList()
obj.deleteFromFront()
obj.deleteFromRear()

obj.addFromFront(20)
obj.addFromFront(10)
obj.addFromRear(30)
obj.printList()