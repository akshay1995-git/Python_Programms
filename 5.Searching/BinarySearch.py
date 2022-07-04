


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class Binary_Search:
    def __init__(self):
        self.head=None
    
    
    def insert(self,data):
        new_node=Node(data)
        if(self.head==None):
                self.head=new_node
            
        else:
            if(data<self.head.data):
                new_node.next=self.head
                self.head=new_node
            else:
              
                current = self.head
                while (current.next != None and
                        current.next.data < new_node.data):        
                        current = current.next
          
                new_node.next = current.next
                current.next = new_node
    def getNodeCount(self):
        count=0
        if(self.head==None):
            #print("Node Count : ",0)
            return 0
        else:
            current=self.head
            while(current.next!=None):
                count+=1
                current=current.next
            count+=1    
           #print("Node Count : ",count)
            return count
            
    def printList(self):
        current=self.head
        while(current!=None):
            print(current.data,end=" ==>> ")
            current=current.next
            
    def binary_search(self,element):
        lower=0
        upper=self.getNodeCount()
        #index=-1
        
        while(lower<=upper):
            mid=(lower+upper)/2
            index=0
            temp=self.head
            while(index<=mid):
                temp=temp.next
                index+=1
                
            if(element==temp.data):
                return index
            
            elif(element>temp.data):
                lower=index+1
            elif(element<temp.data):
                upper=index-1
                
                
                
                
obj=Binary_Search()

obj.insert(10)
obj.insert(5)
obj.insert(20)
obj.insert(40)
obj.insert(30)
obj.insert(15)
obj.insert(50)
obj.printList()
#obj.getNodeCount()

#print("Index: ",obj.binary_search(20))
                
            
            
            
        