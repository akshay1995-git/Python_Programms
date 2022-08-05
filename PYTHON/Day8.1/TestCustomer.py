from Customer import Customer
from Type import *
from CustomerException import CustomerException
list_data={}
def addDetail():
    print("Enter a customer detail as per prompt :")
    name=str(input("Enter a name of customer : "))
    email=str(input("Enter a Email of customer : "))
    password=str(input("Enter a Password of customer : "))
    num=int(input("Enter a customer Type : "))
    type=Type(num)
    regAmt=float(input("Enter a Reg Amount  : "))
    dob=input("Enter a DOB of customer : ")
    #customer_key=Customer(email)
    customer_value=Customer(name,email,password,type,regAmt,dob)
    list_data={email:[]}
    list_data[email].append(customer_value)
  
    
    print("Customer data added successfully")
    
def Displaydetail():
    for value in list_data.values():
        print(value)


flag=True
while(flag):
   
        str1='''\n1. Add Customer \n2. Display Customer List \n6. Exit From cart  
        '''
        print(str1)
        i=int(input("Enter a choice "))


        try:
            switcher={
        
       
                1:addDetail,
                2:Displaydetail,
               
   
            }
            switcher.get(i,"Invalid choice ")()
            
        except CustomerException as e:
            print("\nError :",e.value)