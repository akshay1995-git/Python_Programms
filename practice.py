# class Solution:
#     def runningSum(self, nums):
#         sum=0
#         k=0
#         new_list=[0]*4
#         count=3
#         for i in range(len(nums)-1,0,-1):#1,2,3,4==4
#             for j in range(0,i,1):
#                 sum+=nums[j]#0+1
                
#             new_list[count]=sum
#             print(new_list[count])
#             count=count-1
            
#         for i in new_list:
#             print(i)
    
# nums=[2,3,4,5]

# obj=Solution()
# obj.runningSum(nums)class Solution:

def sortSentence(s: str):
        arr=s.split()
        new_arr=[]
        for i in range(0,len(arr)):
            priority=int(arr[i][len(arr[i])-1])
            print(priority,"--> ",type(priority))
            
            new_arr.insert(priority-1,arr[i][0:len(arr[i])-1])
        for j in range(0,len(new_arr)):
            print(new_arr[j])
            
        
        str=""
        for words in new_arr:
            str += words+" "
            
        return str
print(sortSentence("is2 sentence4 This1 a3"))               
            