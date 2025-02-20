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
      
   
def binary(arr,target):
   low=0
   high=len(arr)-1
   
   while low<=high:
      mid=(low+high)//2
      if arr[mid]==target:
         return mid
      if arr[mid]<target:
         low=mid+1
      else:
         high=mid-1
   return -1


arr=[60000,20,1,3,500,302,2]
merge(arr)
print(arr)

result=binary(arr,500)
if result!=-1:
   print(f"target is at {result}")
else:
   print("not found ")

