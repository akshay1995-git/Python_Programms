class Solution:
    def moveZeroes(nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(0,len(nums)):
            
            for j in range(0+i,len(nums)):
                
                if(nums[i]==0 and nums[j]!=0):
                    temp=nums[j]
                    nums[j]=nums[i]
                    nums[i]=temp
                    
                if(nums[i]==0 and nums[j]==0):
                    
                    pass
                
        return nums
    
obj=Solution
arr=[1,0,3,0,12,0,4,5,0]
print(obj.moveZeroes(arr))
        