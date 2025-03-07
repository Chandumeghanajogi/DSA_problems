def lower(arr,target):
    low,high=0,len(arr)-1
    ans=-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]<=target:
            ans=mid
            low=mid+1
        else:
            high=mid-1
    return ans


arr=[1,2,2,2,3]
target=2
print(lower(arr,target))

def upper(arr,target):
    low,high=0,len(arr)-1
    ans=-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]>target:
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans



arr=[1,2,2,2,3]
target=2
print(upper(arr,target))
