


class Dequeue:
    def __init__(self,size):
        self.size=size
        self.queue=[]*size
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
    def addAtFront(self,data):
        if(not self.isFull()):
            if(self.front==-1):
                self.front=0
                self.rear=0
                self.queue.insert(self.front,data)
                print("From Front at index : ",self.front)
            elif(self.front>0):
                self.front-=1
                self.queue.insert(self.front,data)
                print("From Front at index : ",self.front)
        else:
            print("OVERFLOW !!! Queue is Full ")

                
    def addAtRear(self,data):
        if(not self.isFull()):
            if(self.rear==-1):
                self.front=0
                self.rear=0
                self.queue.insert(self.rear,data)
                print("From Rear at index : ",self.rear)
            else:
                self.rear+=1
                self.queue.insert(self.rear,data)
                print("From Rear at index : ",self.rear)
        else:
            print("OVERFLOW !!! Queue is Full ")
            
    def deleteFromFront(self):
        if(not self.isEmpty()):
        
            print(self.queue[self.front]," Data Removed ")
            self.front+=1
           
        else:
            print("UNDERFLOW !!! Queue is Empty ")
            
    def deleteFromRear(self):
        if(not self.isEmpty()):
            print(self.queue[self.rear]," Data Removed ")
            self.rear-=1
            
        else:
            print("UNDERFLOW !!! Queue is Empty ")




                  
obj=Dequeue(4)

obj.addAtFront(10)
obj.addAtRear(20)
obj.addAtRear(30)
obj.addAtRear(40)
obj.addAtFront(5)#Overflow
obj.addAtRear(50)#overflow
obj.deleteFromFront()
obj.deleteFromFront()
obj.deleteFromRear()
obj.deleteFromRear()


obj.addAtFront(10)
obj.addAtFront(20)

obj.deleteFromFront()
obj.deleteFromFront()
