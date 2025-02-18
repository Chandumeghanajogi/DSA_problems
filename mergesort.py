def merge(arr):
   if len(arr)>1:
      mid =len(arr)//2
      left=arr[:mid]
      right=arr[mid:]
      merge(left)
      merge(right)

      i=j=k=0
      while i<len(left) and j<len(right):
         if left[i]<right[j]:
            arr[k]=left[i]
            i+=1
         else:
            arr[k]=right[j]
            j+=1
         k+=1

      while i<len(left):
         arr[k]=left[i]
         i+=1
         k+=1
        #  i+=1

      while j<len(right):
         arr[k]=right[j]
         j+=1
         k+=1
        #  j+=1
        #  k+=1
      return arr

arr=[20,60000,20,1,3,500,302,2]
print(merge(arr))
