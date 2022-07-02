
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Stack:
    def __init__(self,size):
        self.head=None
        self.size=size
        self.top=-1
    def isEmpty(self):
        if(self.top==-1):
            return True
        else:
            return False
            
    def push(self,data):
        node=Node(data)
        if(self.isEmpty()):
            self.head=node
            print("Push : ",node.data)
            self.top+=1
        elif(self.top<self.size-1):
            node.next=self.head
            self.head=node
            print("Push : ",node.data)
            self.top+=1
        else:
            print("OVERFLOW !!! Stack is Full ")
            
    def pop(self):
        if(self.isEmpty()):
            print("UNDERFLOW !!! Stack is Empty")
        else:
            print("Pop : ",self.head.data)
            self.head=self.head.next
            self.top-=1
            
stack=Stack(4)
stack.pop() #underflow
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)#overflow

stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()#underflow