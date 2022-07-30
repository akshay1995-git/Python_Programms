from turtle import update
from Manager import Manager
from Worker import Worker
from array import *
#main class
def exitApp():
    print("Exit Successfully ")
    flag=False
    return flag
    
list_detail=[]
count=0
def hireManager():
    global count
    id=int(input("Enter ID of employee : "))
    name=str(input("Enter Name of employee : "))
    deptname=str(input("Enter dept of employee : "))

    basic=float(input("Enter basic of employee : "))

    bonus=int(input("Enter bonus of employee : "))

    obj=Manager(id,name,deptname,basic,bonus)
    print("Data Entered Successfully ")
    list_detail.append(obj)
    obj.getMgrDetail()
    
def hireWorker():
    id=int(input("Enter ID of employee : "))
    name=str(input("Enter Name of employee : "))
    deptname=str(input("Enter dept of employee : "))

    basic=float(input("Enter basic of employee : "))
    rate=float(input("Enter a hourly Rate of Worker"))
    worker=Worker(id,name,deptname,basic,rate)
    list_detail.append(worker)
    worker.getWorkDetail()
    
def showDetail():
    i = 0
    while i != len(list_detail):
        if(isinstance(list_detail[i],Manager)):
            list_detail[i].getMgrDetail()
        elif(isinstance(list_detail[i],Worker)):
            list_detail[i].getWorkDetail() 
        i += 1
        
def getOnlyManager():
    i = 0
    while i != len(list_detail):
        if(isinstance(list_detail[i],Manager)):
            list_detail[i].getMgrDetail()
        else:
            pass
            
        i +=1
        
def getOnlyWorker():
    i = 0
    while i != len(list_detail):
        if(isinstance(list_detail[i],Worker)):
            list_detail[i].getWorkDetail()
        else:
            pass
        i +=1
    
        
  
def updateBonus():
    iD=int(input("Enter a ID of Employee :"))
    for i in list_detail:
        if(i.getID()==iD):
            b=int(input("Employee Found !!!Enter a New Bonus :"))
            i.setBonus(b)
        else:
            pass
    print("Bonus Update Successfully")
        
            

flag=True
while(flag):
    print("\n1. Hire Manager\n2. Hire Worker\n3. Display Employee Detail\n4. Display only manager\n5. Display only Worker\n6. Update bonus of Employee\n7. Exit")

    i=int(input("Enter a choice "))


    switcher={
                1:hireManager,
                2:hireWorker,
                3:showDetail,
                4:getOnlyManager,
                5:getOnlyWorker,
                6:updateBonus,
                7:exitApp
            
    }
    switcher.get(i,"Invalid choice ")()
    