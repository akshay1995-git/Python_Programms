# class Solution:
#     def isValid(self,s):
#         for i in range(0,len(s)):
#             if(s[i]=='('and s[i+1]==')'or s[i]=='[' and s[i+1]==']'or s[i]=='{'and s[i+1]=='}'):
#                 return True
#             else:
#                 return False
                
                
# obj=Solution()
# s=input("Enter a string : ")

# print("Result : ",obj.isValid(s))
# def insertAtBegin(arr,data):
   
#     for i in range(len(arr),1,-1):
#         arr[i+1]=arr[i]
#     arr[0]=data
#     print("Data inserted at start ")

import array
    
def insertAtEnd(arr):
    arr[len(arr)-1]=20 #assign element to that block
    
def insertAtBegin(arr):#insert at beginning
    for i in range(0,len(arr)-1):#shif all element to right by one position
        arr[i+1]=arr[i]
        
    arr[0]=29 #assign value to first position
    
def insertAtPos(arr,pos):
    for i in range(pos,len(arr)-1):
        arr[i+1]=arr[i]
        
    arr[pos]=30  


arr=array.array("i",[0]*6)#1.allocate size of block for element

insertAtEnd(arr)
print(arr[5])#print that element 

insertAtBegin(arr)
print(arr[0])#print that element

pos=int(input("Enter a position  : ")) 

insertAtPos(arr,pos)

print(arr[pos])

for i in arr:
    print(i)

        