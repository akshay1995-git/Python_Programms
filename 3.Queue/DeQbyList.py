class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Queue:
    def __init__(self,size):
        self.size=size
        self.front=None
        self.rear=None
        self.head=-1
        self.tail=-1
    def isFull(self):
        if(self.tail==self.size-1 and self.head==0):
            return True
        else:
            return False
    def isEmpty(self):
        if(self.head==-1 and self.tail==-1):
            return True
        else:
            return False  
            
    def addFromFront(self,data):
        node=Node(data)
        if(self.isEmpty()):
            self.front=node
            self.rear=node
            self.head,self.tail=0,0
            print("Push : ",self.front.data)
        elif(self.head>0):
            node.next=self.front
            self.front=node
            print("Push : ",self.front.data)
            self.head-=1
        elif(self.isFull() or self.head==0):
             print("DeQueue is Full front Front ")  
            
    def addFromRear(self,data):
        
        node=Node(data)
        if(self.isEmpty()):
            self.front=node
            self.rear=node
            self.head,self.tail=0,0
            print("Push : ",self.rear.data)
        elif(self.tail<self.size-1):
            self.rear.next=node
            self.rear=node
            print("Push : ",self.rear.data)
            self.tail+=1
        else:
            print("Dequeue is Full from Rear ")
            
    def deleteFromFront(self):
        if(self.isEmpty()):
            print("Dequeue is Empty ")
        else:
            print("Removed : ",self.front.data)
            self.front=self.front.next
            self.head+=1
    def deleteFromRear(self):
        if(self.isEmpty()):
            print("Dequeue is Empty ")
        else:
            print("Removed : ",self.rear.data)        
            self.rear=None
            self.tail-=1
            
obj=Queue(3)
obj.deleteFromFront()
obj.deleteFromRear()
obj.addFromFront(10)
obj.addFromRear(20)
obj.addFromRear(30)
obj.addFromFront(10)
obj.addFromRear(20)
obj.deleteFromFront()
obj.deleteFromRear()
obj.addFromFront(10)
obj.addFromFront(0)

obj.deleteFromFront()
obj.deleteFromFront()
obj.deleteFromFront()
obj.deleteFromRear()
