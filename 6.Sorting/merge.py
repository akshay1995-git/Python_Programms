"""
MERGE SORT ==>>
Merge Sort is one of the most popular sorting algorithms that is 
based on the principle of Divide and Conquer Algorithm.
Here, a problem is divided into multiple sub-problems. Each sub-problem is solved individually. 
Finally, sub-problems are combined to form the final solution.
"""
class MergeSort:
    # merging of two sorted array
    def merge_sorting(self,s_arr1,s_arr2,final_arr):
        len1=len(s_arr1)
        len2=len(s_arr2)
        f_len=len1+len2
        i,j,k=0,0,0
        while(i<len1 and j<len2):
            
            if(s_arr1[i]<s_arr2[j]):
                
                final_arr[k]=s_arr1[i]
                i+=1
                k+=1
            elif(s_arr1[i]>s_arr2[j]):
                final_arr[k]=s_arr1[j]
                j+=1
                k+=1
            if(j>=len2):   
                while(i<len1):
                    final_arr[k]=s_arr1[i]
                    i+=1
                    k+=1
            elif(i>=len1):
                    final_arr[k]=s_arr1[j]
                    j+=1
                    k+=1
                
                
       
        
        return final_arr
    
obj=MergeSort()
arr1=[5,7,9]
arr2=[1,4,6,8]
arr=[0]*(len(arr1)+len(arr2))
print(obj.merge_sorting(arr1,arr2,arr))