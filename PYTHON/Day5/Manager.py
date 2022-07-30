from Employee import Employee
"""
1. get mgr details :  override toString. 
2. compute net salary (formula: basic+performanceBonus) 
3. get performance bonus. 
"""
class Manager(Employee):
    def __init__(self,id,name,deptName,basic,bonus):
        super().__init__(id,name,deptName,basic)
        self.per_bonus=bonus
    def getMgrDetail(self):
        super().getDetails()
        print("Bonus :",self.per_bonus)
        
    def netSalary(self):
        total=self.basic+self.per_bonuus
        return total
    def setBonus(self,bonus):
        self.per_bonus=bonus
    def getBonus(self):
        return self.per_bonus