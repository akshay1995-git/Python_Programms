class Rotation:
    def arrayRotation(arr,d,n):
        newArr=[0]*len(arr)
        temp=0
        for i in range(0,n-d):
            newArr[i]=arr[i+d]
            temp=i
        for j in range(0,d):
            newArr[temp+j+1]=arr[j]   
        print(newArr)
            
    def reverseRotation(arr,d,n):
        #Divide array in to two types from o to d and d to n
        a=arr[0:d]
        b=arr[d:n]
        print("a :",a)
        # reverse the two array
        a.reverse()
        b.reverse()
        # print("rev A :", a)
        # print("Rev B :",b)
        finalArr=[0]*n
        # concate the reverse array and assign it in new array
        finalArr=a+b
        # reverse the final array is your answer
        finalArr.reverse()
        return finalArr
obj=Rotation

arr=[1,2,3,4,5,6,7]

obj.arrayRotation(arr,2,len(arr))

print(obj.reverseRotation(arr,2,len(arr)))