class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Queue:
    def __init__(self,size):
        self.size=size
        self.front=None
        self.rear=None
        self.top=-1
    def isEmpty(self):
        if(self.top==-1):
            return True
        else:
            return False
    def isFull(self):
        if(self.top==self.size-1):
            return True
        else:
            return False
          
    def enQueue(self,data):
        node=Node(data)
        if(self.isEmpty()):
            self.front=node
            self.rear=node
            print("Push ",self.front.data)
            self.top+=1
        elif(self.top<self.size-1):
            self.rear.next=node
            
            self.rear=node
            print("Push ",self.rear.data)
            self.top+=1

        else:
            print("Queue is Full ") 
               
    def deQueue(self):
        if(not self.isEmpty()):
            print("pop ",self.front.data)
            self.front=self.front.next
            
            self.top-=1
            
        else:
            print("Queue is Empty ")

obj=Queue(4)
obj.deQueue()

obj.enQueue(10)
obj.enQueue(20)           
obj.enQueue(30)           
obj.enQueue(40)
obj.enQueue(50)                     
obj.deQueue()
obj.deQueue()
obj.deQueue()
obj.deQueue()
obj.deQueue()
