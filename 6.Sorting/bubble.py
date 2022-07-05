"""
BUBBLE SORT ==>
Bubble sort is a sorting algorithm that compares two adjacent elements and swaps them until 

they are not in the intended order.

"""
class BubbleSort:
    
    def bubble_sort(self,arr):
        
        for i in range(0,len(arr)):
            
            for j in range(i+1,len(arr)):
                
                if(arr[i]>arr[j]):
                    
                    temp=arr[j]
                    
                    arr[j]=arr[i]
                    
                    arr[i]=temp
                    
                    print("pass ",i+1)
        
        print(arr)            

obj=BubbleSort()

arr=[10,4,1,3,7,9,-1]
obj.bubble_sort(arr)