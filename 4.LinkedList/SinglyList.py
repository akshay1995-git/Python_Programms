


class Node:
    
    def __init__(self,data):
        self.data=data
        self.next=None
        
class LinkedList:
    
    def __init__(self):
        self.head=None
        
    def addAtEnd(self,data):
        
        node=Node(data)

        if(self.head==None):
            
            self.head=node
            node.next=None
            
        else:
            curr=self.head
            while(curr.next!=None):
                curr=curr.next
            curr.next=node
            node.next=None
    def getNodeCount(self):
        count=0
        if(self.head==None):
            print("Node Count : ",0)
        else:
            current=self.head
            while(current.next!=None):
                count+=1
                current=current.next
            count+=1    
            print("Node Count : ",count)
                    
    def addAtFront(self,data):
        
        node=Node(data)
        
        if(self.head==None):
            
            self.head=node
            node.next=None
        else:
            node.next=self.head
            self.head=node
            
    def addAtRand(self,pos,data):
        
        node=Node(data)
        
        if(self.head==None):
            self.head=node
            node.next=None
        else:
            current=self.head
            i=1
            while(i<=pos):
                current=current.next
                i+=1
            node.next=current.next   
            current.next=node
    
    def deleteFromFront(self):
        
        if(self.head==None):
            print("List is Empty !!! ")
        else:
            self.head=self.head.next
            
    def deleteFromEnd(self):
        
        if(self.head==None):
            print("List is Empty !!! ")
        else:
            curr=self.head
            temp=None
            while(curr.next!=None):
                temp=curr
                curr=curr.next
            temp.next=None
            
    def deleteAtRand(self,pos):
        if(self.head==None):
            print("List is Empty !!! ")
        else:
            current=self.head
            temp=None
            i=1
            while(i<pos):
                temp=current
                current=current.next
                i+=1
            temp.next=current.next                     
    def printList(self):
        current=self.head
        while(current!=None):
            print(current.data,end=" ==>> ")
            current=current.next
    
                      
obj=LinkedList()
obj.deleteFromFront()
obj.deleteFromEnd()
obj.getNodeCount()
obj.addAtEnd(10)
obj.addAtEnd(20)
obj.addAtEnd(30)
obj.addAtFront(40)
obj.addAtRand(2,50)
obj.getNodeCount()
obj.printList()
obj.deleteFromEnd()
print()
obj.printList()
obj.deleteFromFront()
print()
obj.printList()
print()
obj.getNodeCount()
obj.deleteAtRand(2)
obj.printList()
