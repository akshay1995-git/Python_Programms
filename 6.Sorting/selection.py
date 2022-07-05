"""
SELECTION SORT ==>
Selection sort is a sorting algorithm that selects the smallest element from an unsorted list 
in each iteration and places that element at the beginning of the unsorted list.
"""
class SelectionSort:
    
    def selection_sort(self,arr):
        
        min=arr[0]
        
        for i in range(0,len(arr)):
            
            min_index=i #assume ith element is minimum element
            
            for j in range(i+1,len(arr)):
                
                if(arr[min_index]>=arr[j]): #compare i th with adjacent element 
                    #swapping perform if true
                    temp=arr[j]
                    arr[j]=arr[min_index]
                    arr[min_index]=temp
                    print("pass ",i+1)
        print(arr) #print array if all loop over
            
obj=SelectionSort()

arr=[10,4,1,3,7,9,-1]
obj.selection_sort(arr) 
            