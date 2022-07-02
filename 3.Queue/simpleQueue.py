import queue


class Queue:
    def __init__(self,size):
        self.size=size
        self.queue=[]
        self.front=-1
        self.rear=-1
        
    def isFull(self):
        if(self.rear==self.size-1):
            return True
        else:
            return False
    def isEmpty(self):
        if(self.front==-1 or self.front==self.size-1):
            return True
        else:
            return False
        
    def enqueue(self,data):
        if(self.isEmpty()):
            self.rear=self.rear+1
            self.front=self.front+1
            self.queue.insert(self.rear,data)
            print("Data enqueue")
            
        elif(self.isFull()):
            
            print("Queue is Full")
            
        else:
            self.rear=self.rear+1
            self.queue.insert(self.rear,data)
            print("Data enqueue")
           
            
    def dequeue(self):
        if(self.isEmpty()):
            print("Queue is Empty")
            return 0
        elif(self.isFull()):
            return self.queue.pop(self.front)
        
        else:
            self.front=self.front+1
            return self.queue.pop(self.front)
            
    def peek(self):
        return self.queue[self.front]
    
    
obj=Queue(4)
obj.enqueue(10)
obj.enqueue(20)
obj.enqueue(30)
print("Peek : ",obj.peek())
obj.enqueue(40)
obj.enqueue(50)

print(obj.dequeue(),"dequeue")
print(obj.dequeue(),"dequeue")
print(obj.dequeue(),"dequeue")
print(obj.dequeue(),"dequeue")
print(obj.dequeue(),"dequeue")




