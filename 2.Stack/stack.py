"""
The operations work as follows:

A pointer called TOP is used to keep track of the top element in the stack.
When initializing the stack, we set its value to -1 so that we can check if the stack is empty by comparing TOP == -1.
On pushing an element, we increase the value of TOP and place the new element in the position pointed to by TOP.
On popping an element, we return the element pointed to by TOP and reduce its value.
Before pushing, we check if the stack is already full
Before popping, we check if the stack is already empty
"""
class Stack:
    def __init__(self,size):
        self.size=size
        self.top=-1
        self.stack=[0]*size
        
    def isFull(self):
        if(self.top==self.size-1):
            return True
        else:
            return False
    def isEmpty(self):
        if(self.top<self.size-1):
            return True
        else:
            return False
        
    def push(self,data):
        if(self.top<self.size-1):
            self.top=self.top+1 
            self.stack[self.top]=data           
            print("Data Pushed :",data)
        else:
            print("Stack is full")
    def pop(self):
        if(self.top>=0):
            element=self.stack[self.top]
            self.top=self.top-1
            return element
        else:
            print("Stack is Empty")
            return 0
    
    def Top(self):
        if(self.top>=0):
            return self.stack[self.top]
        else:
            return None
obj=Stack(3)

obj.push(10)
obj.push(20)
obj.push(30)
obj.push(40)
print("popped :",obj.pop())
print("popped :",obj.pop())
print("popped :",obj.pop())
print("popped :",obj.pop())

print("Top :",obj.Top())

