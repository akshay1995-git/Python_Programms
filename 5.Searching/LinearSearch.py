


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
                     
    def printList(self):
        current=self.head
        while(current!=None):
            print(current.data,end=" ==>> ")
            current=current.next
    
    def linearSearch(self,value):
        if(self.head==None):
            print("List is Empty !!!")
        else:
            index=0 
            current=self.head
            while(current.next!=None):
                if(current.data==value):
                    print("Data Found at index : ",index)
                    return True
                else:
                    index+=1
                    pass
                current=current.next
obj=LinkedList()

obj.addAtFront(20)
obj.addAtFront(10) 
obj.addAtFront(5)
obj.addAtEnd(30)
obj.addAtEnd(40)

if(obj.linearSearch(20)):
    pass
    
else:
    print("Data Not found")                                                             