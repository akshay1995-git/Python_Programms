class Rearrange:
    """
    Nav­i­gate the numbers from 0 to n-1.
    Now navigate through array.
    If (i==a[j]) , then replace the element at i position with a[j] position.
    If there is any element in which -1 is used instead of the number then it
    will be replaced automatically.
    Now, iterate through the array and check if (a[i]!=i) , if it s true then replace
    a[i] with -1.
    """
    def rearrange(array):
        for i in range(0,len(array)):
          if(array[i]==-1):
              pass
          if(array[i]!=-1 and array[i]==i):
              pass
          else:
              
obj=Rearrange
arr=[1,3,0,4,6,5]
obj.rearrange(arr)