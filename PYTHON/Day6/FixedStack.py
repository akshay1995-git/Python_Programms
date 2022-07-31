from Employee import *
from Stack import Stack
class FixedStack(Stack):
    

    #list_data=[0]*self.size
    def __init__(self):
        self.list_data=[0]*super().SIZE
     
 
    def push(self,obj):
        if(self.top!=self.SIZE-1):
            self.top += 1
            self.list_data[self.top]=obj
            
            print("Data Pushed at top",self.top)
            self.list_data[self.top].display()
        else:
            print("Stack is Full :")
     
    
    def pop(self):
        if(self.top!=-1):
            ele=self.list_data[self.top]
            print("Data popped from top ",self.top)
            self.top -= 1
            return ele
        else:
            print("Stack is Empty ")
            return 0
    