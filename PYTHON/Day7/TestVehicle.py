
from Vehicle import Vehicle


print("Enter a first vehicle data :")
regNo=int(input("Enter a registration No :"))
color=input("Enter a color of vehicle :")
price=float(input("Enter a price of vehicle :"))
veh1=Vehicle(regNo,color,price)
    
print("Enter a second vehicle data :")
regNo=int(input("Enter a registration No :"))
color=input("Enter a color of vehicle :")
price=float(input("Enter a price of vehicle :"))
veh2=Vehicle(regNo,color,price)
    
if(veh1.getRegNo()==veh2.getRegNo()):
        print("SAME ")
else:
        print("DIFFERENT")
    



