class Solution:
    def minimumDeletions(nums) -> int:
        min_index=0
        max_index=0
        minE=nums[0]
        maxE=nums[0]
        for i in range(0,len(nums)):
            if(minE>nums[i]):
                minE=nums[i]
                min_index=i
                
            elif(maxE<nums[i]):
                maxE=nums[i]
                max_index=i
                
        print(minE," ",min_index)#5
        print(maxE," ",max_index)#1
        posmin=0
        posmax=0
        #(if((1+1)<(7-2)) and (6)>(7-6))
        if(min_index+1<len(nums)-min_index):
            posmin=min_index+1
            print("pos_min :",posmin)
        elif(min_index+1>len(nums)-min_index):
            posmin=len(nums)-min_index
            print("pos_min :",posmin)
        
        if(max_index+1<len(nums)-max_index):
            posmax=max_index+1
            print("Pos_max :",posmax)
        elif(max_index+1>len(nums)-max_index):
            posmax=len(nums)-max_index
            print("Pos_max :",posmax)
        
        
        return posmin+posmax
            
            
obj=Solution
arr=[0,-4,19,1,8,-2,-3,5]
print(obj.minimumDeletions(arr))