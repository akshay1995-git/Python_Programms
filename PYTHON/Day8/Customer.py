"""
Customer : name(string),email(string),password(string),registrationAmount(double),dob(Date),type (CustomerType : enum)
CustomerType : SILVER,GOLD,PLATINUM
Add/generate suitable constructor & toString
Unique ID(Primary Key ) : email  (2 customers are SAME iff their email ids are same)
Will you add any other data member in Customer class for parsing n formatting dates ? 
HOW ? : 


2.2 Create custom exception (checked exception )class in a separate package
CustomerHandlingException
"""
class Customer:
    def __init__(self,name,email,password,type,regAmt,dob):
        self.name=name
        self.email=email
        self.password=password
        self.type=type
        self.regAmt=regAmt
        self.dob=dob
        
    def display(self):
        print("Name :",self.name)
        print("Email :",self.email)
        print("Password :",self.password)
        print("Type :",self.type)
        print("Reg amount :",self.regAmt)
        print("DOB :",self.dob)
        
    def setEmail(self,email):
        self.email=email
    
    def getEmail(self):
        return self.email
    