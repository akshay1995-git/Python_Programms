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
        if(self.isEmpty()):
            self.top=self.top+1 
            self.stack[self.top]=data           
            
       
    def pop(self):
        if(self.top>=0):
            element=self.stack[self.top]
            self.top=self.top-1
            return element
        
            
    
    def peek(self):
        if(self.top>=0):
            return self.stack[self.top]
        else:
            return None

    
    def findPrecedence(self,ch):
        if(ch=='+' or ch=='-'):
            return 1
        elif(ch=='*' or ch=='/'):
            return 2
        
    def reverse(self,infix):
        r_str=""
        for i in range(len(infix)-1,-1,-1):
            if(infix[i]=='('):
                r_str+=')'
            elif(infix[i]==')'):
                r_str+='('
            elif(infix[i]>='a' and infix[i]<='z'):
                r_str+=infix[i]
            else:
                r_str+=infix[i]
        return r_str    
expression=str(input("Enter a infix Expression --> "))
prefix=""
stack=Stack(12)

i=0
infix=stack.reverse(expression)
for i in range(0,len(infix)):
    if(infix[i]=="("):
        stack.push(infix[i])
    elif(infix[i]>='a' and infix[i]<='z'):
        prefix+=infix[i]
    
    elif(infix[i]=='+' or infix[i]=='-' or infix[i]=='*' or infix[i]=='/'):
        while(stack.peek()=='+' or stack.peek()=='-' or stack.peek()=='*' or stack.peek()=='/'):
            if(stack.findPrecedence(infix[i])<=stack.findPrecedence(stack.peek())):
                prefix+=stack.pop()
            else:
                break
        stack.push(infix[i])
        
    elif(infix[i]=='('):
        ch=stack.pop()
        while(ch!=')'):
            prefix+=ch #ab+(j=2)
      
print("The postfix form of given infix expression  - : ",prefix)
            