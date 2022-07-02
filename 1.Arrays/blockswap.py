class BlockSwap:
    @classmethod
    def swapMethod(arr, fi, si, d):
        for i in range(d):
            temp = arr[fi + i]
            arr[fi + i] = arr[si + i]
            arr[si + i] = temp
     
    # def rotateMethod(arr,d,n):
    #     firstArr=arr[0:d]
    #     secondArr=arr[d:n]
    #     len1=len(firstArr)
    #     len2=len(secondArr)
        # while(len1!=len2):
            
        #     if(len1<len2):
        #         secondArrL=secondArr[0:len2-len1-1]
        #         secondArrR=secondArr[len2-len1-1:len2]
        #         self.swapMethod(arr,firstArr,secondArrR,d)
        #         len2=len2-len1
        #     elif(len1>len2):
        #         firstArrL=firstArr[0:len1-len2]
        #         firstArrR=firstArr[]
    def leftRotate(arr, d, n):
        if(d == 0 or d == n):
            return
        i = d
        j = n - d
        while (i != j):
         
            if(i < j): # A is shorter
                BlockSwap.swapMethod(arr, d - i, d + j - i, i)
                j -= i
         
            else: # B is shorter
                BlockSwap.swapMethod(arr, d - i, d, j)
                i -= j
     
        BlockSwap.swapMethod(arr, d - i, d, i)    
    def printArray(arr, size):
        for i in range(size):
            print(arr[i], end = " ")
        print();            
obj=BlockSwap

arr=[1,2,3,4,5,6,7]
print(arr)
obj.leftRotate(arr,2,len(arr))

obj.printArray()