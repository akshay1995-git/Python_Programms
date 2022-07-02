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
        
infix=str(input("Enter a infix Expression -->> "))
postfix=""
stack=Stack(12)

i=0
while(i<len(infix)):
    #scanned character is operator and stack is empty
    if(infix[i]=='('):
        stack.push(infix[i])# (,*(
    elif(infix[i]>='a' and infix[i]<='z' or infix[i]>='A' and infix[i]<='Z'):#if scanned character is operand
        postfix+=infix[i] # a(j=0)b(j=1),ab+c(j=3),ab+cd(j=4)
       
        #if stack is not empty
    elif(infix[i]=='+' or infix[i]=='-' or infix[i]=='*' or infix[i]=='/'):
        while(stack.peek()=='+' or stack.peek()=='-' or stack.peek()=='*' or stack.peek()=='/'):
                print(stack.peek())
                if(stack.findPrecedence(infix[i])<=stack.findPrecedence(stack.peek())):
                    postfix+=stack.peek()
                   
                else:
                    break
        stack.push(infix[i]) #(+,*(+
    elif(infix[i]=='('):
        ch=stack.pop()
        while(ch!=')'):
            postfix+=ch #ab+(j=2)
            
                        
    i+=1
#postfix[j]="\0"
  
print("The postfix form of given infix expression  - : ",postfix)
