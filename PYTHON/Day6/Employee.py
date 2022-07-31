"""
Steps
1.1  Create Employee class -- id,name,salary, constructor,toString
1.2 Stack interface -- push & pop functionality for Emp refs. & declare STACK_SIZE as a constant. 
1.3 Create implementation class of Stack i/f -- FixedStack (array based)
1.4 Create another implementation class of Stack i/f-- GrowableStack (array based)

1.5
"""
class Employee:
    def __init__(self,id,name,salary):
        self.id=id
        self.name=name
        self.salary=salary
        
    def display(self):
        print("ID :",self.id)
        print("Name :",self.name)
        print("Salary :",self.salary)
        