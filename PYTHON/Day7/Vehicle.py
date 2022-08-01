

class Vehicle:
    def __init__(self,regNo,color,price):
        self.__regNo=regNo
        self.__color=color
        self.__price=price
        
    def display(self):
        print("Reg No :",self.__regNo)
        print("Color :",self.__color)
        print("Price :",self.__price)
        
    def getRegNo(self):
        return self.__regNo