#linearsearch

arr=list(map(int,input().split()))
target=int(input())
flag=False
arr.sort()
print(arr)
for i in range(len(arr)):
    if arr[i]==target:
        flag=True
        break

if flag:
    print(f" {target} is found  at", i)  
else:
    print(f"{target} is not found") 


def binary(arr,target):
    
    low,high=0,len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return -1

arr=[1,2,6]
target=2
print(binary(arr,target))


# def binary(arr,target):

def binary1(a,target):
    sqrt=target**2
    low,high=0,len(a)-1
    while low<=high:
        mid=(low+high)//2
        if a[mid]==sqrt:
            return mid
        elif a[mid]<sqrt:
            low=mid+1
        else:
            high=mid-1
    return -1
a=[1,2,3,4]
target=2
print(binary1(a,target))


      