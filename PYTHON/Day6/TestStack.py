
from Employee import *
from FixedStack import FixedStack
from GrowStack import GrowStack
#main stack

fstack=FixedStack()

gstack=GrowStack()   
    
def pushData():
    id=int(input("Enter ID of employee : "))
    name=str(input("Enter Name of employee : "))
    sal=float(input("Enter a salary :"))
    obj=Employee(id,name,sal)
    if(FixedStack.top!=FixedStack.SIZE-1):
        
        fstack.push(obj)
    else:
        gstack.push(obj)
        
def popData():
    
        res=fstack.pop()
        #print("Data popped ")
        res.display()
    
def exitApp():
    flag=False
    print("Exit Successfully ")
    
    return flag

flag=True
while(flag):
   
    
    print("\n1. Push Data \n2. Pop Data \n3. Exit")
    i=int(input("Enter a choice "))


    switcher={
            
               1:pushData,
               2:popData,
               3:exitApp
            
    }
    switcher.get(i,"Invalid choice ")()
    