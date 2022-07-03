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
            self.tail.next=node
            self.tail=node
    """        
    def addAtRandom(self,pos,data):
        node=Node(data)
        if(self.head==None):
            self.head=node
            self.tail=node
        else:
            i=0                         #  1000\15\2000
            current=self.head  ##  500\10\2000|1500---->1500|1000\20\3000
            while(i<pos):
                current=current.next
                i+=1
            node.prev=current#1000
            node.next=current.next#2000
            current.next=node
            #node.prev.next=node#1500
            node.next.prev=node#1500
            
            # newNode.prev = current;
			# newNode.next = current.next;
			# current.next = newNode;
			# newNode.value = data;
			# newNode.next.prev = newNode;
            
    """      
    def deleteAtRandom(self,pos):
        if(self.head==None):
            print("List is Empty ")
        else:
            i=0
            current=self.head
            while(i<pos):
               current=current.next
               i+=1
            
         
    def deleteFromFront(self):
        if(self.head==None):
            print("List is Empty ")
        else:
            self.head=self.head.next 
               
    def deleteFromEnd(self):
        if(self.head==None):
            print("List is Empty ")
        else:
            self.tail=self.tail.prev 
                     
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

obj =LinkedList()

obj.addAtFront(20)
obj.addAtFront(10)
obj.addAtEnd(30)
obj.addAtFront(5)
obj.addAtEnd(40)
#obj.addAtRandom(2,50)
obj.printListF()
print()
obj.printListR()
print()
obj.deleteFromEnd()
obj.deleteFromFront()

obj.printListF()
print()
obj.printListR()
