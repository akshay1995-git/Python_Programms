class MinByRotation:
    """
    The minimum element is the only element whose previous is greater than it. If there is no 
    previous element, then there is no rotation (the first element is minimum). We check this 
    condition for the middle element by comparing it with (mid-1)’th and (mid+1)’th elements.
        If the minimum element is not at the middle (neither mid nor mid + 1), then the minimum
        element lies in either the left half or right half. 
        If the middle element is smaller than the last element, then the minimum element lies 
        in the left half
    Else minimum element lies in the right half.
    
    """
    def search_min(arr):
        
        low=0
        high=len(array)-1
        
        while (low < high):
            mid = low + (high - low) // 2
         
            if (arr[mid] == arr[high]):
                high -= 1
            elif (arr[mid] > arr[high]):
                low = mid + 1
            else:
                high = mid
        return arr[high]
                
            
            
obj=MinByRotation

array=[3,4,5,6,7,1,2]

print("Min Element :",obj.search_min(array))
                
                