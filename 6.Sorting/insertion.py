class InsertionSort:
    
    def insertion_sort(self,arr):
        
        for i in range(1,len(arr)):
            
            temp=arr[i]# start loop from 1 
            
            j=i-1
            
            while(j>=0 and arr[j]>temp):
                arr[j+1]=arr[j]
                j-=1
            
            arr[j + 1] = temp
            
        print(arr)

obj=InsertionSort()

arr=[9, 5, 1, 4, 3]
obj.insertion_sort(arr)            
                    