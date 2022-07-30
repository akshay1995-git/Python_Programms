from Employee import Employee

class Worker(Employee):
    hour=8
    def __init__(self,id,name,deptName,basic,rate):
        super().__init__(id,name,deptName,basic)
        self.rate=rate
    def getWorkDetail(self):
        super().getDetails()
        print("Rate :",self.rate)
    
    def getRate(self):
        return self.rate
    def setRate(self,rate):
        self.rate=rate
        
    def calSal(self):
        return self.basic+Worker.hour*(self.rate/100)*30