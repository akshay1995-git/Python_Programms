"""
id(int), name, deptId(string) , basic(double)

Behaviour ---1.  get emp details -- use toString.
2. compute net salary ---
eg : public double computeNetSalary()
"""

class Employee:
    def __init__(self,id,name,deptName,basic):
        self.id=id
        self.Name=name
        self.deptName=deptName
        self.basic=basic
    def getDetails(self):
        print("ID :",self.id)
        print("Name :",self.Name)
        print("Dept Name:",self.deptName)
        print("Basic:",self.basic)
    def getID(self):
        return self.id
    def __hash__(self):
        # necessary for instances to behave sanely in dicts and sets.
        return hash((self.Manager))