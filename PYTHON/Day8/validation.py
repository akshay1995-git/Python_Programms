from CustomerException import *
from Customer import Customer
from datetime import *
"""
Rules 
email must contain "@" & should be from ".com" domain
password must be min 4 max 10 chars long
reg amount should be multiples of 500
dob should be before 1st Jan 1995
duplicate customer details should not be stored.
"""

    
# Password validation
 
def validatePass(password) :
       
        if(len(password)>4 and len(password)<10):
            return password
        else:
            raise CustomerException("Length of Password is between 4 to 10")

#email validation
  
def emailValidate(list_data,email):
        
    
    #for i in list_data: 
        if(email.endswith(".com") and email.find("@")<len(email)):
            for i in list_data:
                if(i.email==email):
                    raise CustomerException("Same mail Found ")
            else:
                    return email
            
    
        else:
            raise CustomerException("Email must contain @ and .com ")

#Reg amt validation
       
def validateRegAmt(regAmt):
    if(regAmt%500==0):
        return regAmt
    else:
        raise CustomerException("Registration Amount must be multiple of 500")

#Date  validation 

def convertDate(dob):
    dt=datetime.fromisoformat(dob)#sting to date object conversion
    #print("First date type ",type(dt))
   
    dt1 = datetime.strptime('1995-01-01', '%Y-%m-%d')
    #print("second date type ",type(dt1))

    
    if(dt<dt1):#condition to check date vaidity
        return dob
    else:         
        raise CustomerException("Date must be before 1995-01-01 ")
           