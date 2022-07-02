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

    def size(self) :
	    return self.count
stack=Stack(10)
postfix=str(input("Enter a infix Expression -->> "))      
size = len(postfix)
		#  Create stack object

		#  Some useful variables which is using 
		#  of to storing current result
auxiliary = ""
op1 = ""
op2 = ""
isValid = True
i = 0    
    
while (i < size and isValid) :
			#  Check whether given postfix location
			#  at [i] is an operator or not
	if (postfix[i] == '+'or postfix[i] == '-'or postfix[i] == '*'or postfix[i] == '/'or postfix[i] == '^'or postfix[i] == '%') :
				#  When operator exist
				#  Check that two operands exist or not
		if (stack.size() > 1) :
			op1 = stack.pop()
			op2 = stack.pop()
			auxiliary = "(" + op2 + postfix[i] + op1 + ")"
			stack.push(auxiliary)
		else :
			isValid = False
				
	elif ((postfix[i] >= 'a'and postfix[i] <= 'z')) :
				#  When get valid operands
		auxiliary = postfix[i]
		stack.push(auxiliary)
	else :
				#  Invalid operands or operator
		isValid = False
			
		i += 1
		
if (isValid == False) :
			#  When have something wrong
			print("Invalid postfix : ", postfix)
else :
			#  Display calculated result
			print(" Postfix : ", postfix)    