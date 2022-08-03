from tkinter import E
from Customer import *
from validation import *
from Type import *
"""
1. Customer registration (no dups pls!)
i/p : customer details
o/p err mesg in case of invalid / dup inputs or success mesg
2. Customer login
i/p : email , password
o/p invalid email or invalid password or login successful mesg
3. Unsubscribe customer
i/p : email
o/p  invalid email mesg or delete customer details
"""
list_data=[]
def addDetail():
    print("Enter a customer detail as per prompt :")
    name=str(input("Enter a name of customer : "))
    email=str(input("Enter a Email of customer : "))
    password=str(input("Enter a Password of customer : "))
    num=int(input("Enter a customer Type : "))
    type=Type(num).name
    regAmt=float(input("Enter a Reg Amount  : "))
    dob=input("Enter a DOB of customer : ")
    customer=Customer(name,emailValidate(list_data,email),validatePass(password),type,validateRegAmt(regAmt),convertDate(dob))
    list_data.append(customer)
    print("Customer data added successfully")
    
def Displaydetail():
    for i in range(len(list_data)):
        list_data[i].display()
        

def logIN():
    print("Enter a Credentials : ")
    email=input("Enter a Email : ")
    password=input("Enter a passsowrd :")
    for detail in list_data:
        if(detail.email==email and detail.password==password):
            print("# LOG IN SUCCESSFUL #")
            detail.display()
        else:
            pass
    else:
        raise CustomerException("Log in unsuccessful")
    
def unsubscribe():
    email=input("Enter a email : ")
    for detail in list_data:
        if(detail.email==email):
            list_data.remove(email)
            print("Unsubscribe successfully ")
        else:
            pass
    
flag=True
while(flag):
   
        str1='''\n1. Add Customer \n2. Display Customer List \n3. Log in for Customer \n4. Unsubscribe the Customer \n6. Exit From cart  
        '''
        print(str1)
        i=int(input("Enter a choice "))


        try:
            switcher={
        
       
                1:addDetail,
                2:Displaydetail,
                3:logIN,
                4:unsubscribe
   
            }
            switcher.get(i,"Invalid choice ")()
            
        except CustomerException as e:
            print("\nError :",e.value)