import queue


class Entity:
    def __init__(self,key,value):
        self.__key=key
        self.__value=value
    def getKey(self):
        return self.__key
    def getValue(self):
        return self.__value
    def setKey(self,key):
        self.__key=key
    def setValue(self,value):
        self.__value=value
        
class Priority:
    def __init__(self,size):
        self.size=size
        self.queue=[]
        self.front=-1
        self.rear=-1
        
    def enQueue(self,data):
        if(self.front==-1 and self.rear==-1):
            self.front=0
            self.rear=0
            self.queue[self.rear]=data
            print("data pushed :",self.rear)
        
        else:
            for i in range(self.rear,self.front,-1):
                if(queue[i].getKey()>data.getKey()):
                   # self.rear+=1
                    self.queue[i+1]=self.queue[i]
                else:
                    break
            self.queue[i+1]=data
            self.rear+=1
            print("data pushed : ",self.rear)


obj=Priority(4)
e1=Entity(4,33)
e2=Entity(2,55)
obj.enQueue(e1)
obj.enQueue(e2)



              