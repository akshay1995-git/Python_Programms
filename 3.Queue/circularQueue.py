class CircularQueue:
    def __init__(self,size):
        self.size=size
        self.queue=[]
        self.front=-1
        self.rear=-1
    def isEmpty(self):
        if(self.front==-1 and self.rear==-1):
            return True
        else:
            return False
    def isFull(self):
        if(self.rear+1%self.size==self.front):
            return True
        else:
            return False
    def enQueue(self,data):                  
        if(self.isEmpty()):
            self.front=0
            self.rear=0
            self.queue.insert(self.rear,data)
            print("insert at index : ",self.rear)
        elif(self.front>0):
            if(self.rear>self.front):
                self.rear=self.rear+1%self.size
                self.queue.insert(self.rear,data)
                print("insert at index when front= 0 at: ",self.rear)
            elif(self.rear==self.front):
                print("OVERFLOW !!! Queue is Full ")
        elif(self.rear+1==self.size):
            print("OVERFLOW !!! Queue is Full ")
        else:
            self.rear=self.rear+1
            self.queue.insert(self.rear,data)
            print("insert at index : ",self.rear)
            
    
    def deQueue(self):
        if(self.isEmpty()):
            print("UNDERFLOW !!! Queue is Empty ")
            
        elif(self.front==self.rear):
            print("UNDERFLOW !!! Queue is Empty ")

        else:
            print(self.queue[self.front]," data removed from index : ",self.front)
            self.front=self.front+1
            
obj=CircularQueue(4)
obj.deQueue()#underflow
obj.enQueue(10)
obj.enQueue(20)
obj.enQueue(30)
obj.enQueue(40)
obj.enQueue(50)#overflow

obj.deQueue()
obj.deQueue()
obj.enQueue(10)
obj.enQueue(20)
obj.enQueue(60)#overflow


obj.deQueue()
obj.deQueue()
obj.deQueue()
obj.deQueue()
obj.deQueue()#underflow

