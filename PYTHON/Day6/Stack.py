from abc import ABC,abstractmethod


class Stack(ABC):
     SIZE=2
     top=-1
    #  list_data=[0]*SIZE
     @abstractmethod
     def push(self):
         pass
     @abstractmethod
     def pop(self):
         pass