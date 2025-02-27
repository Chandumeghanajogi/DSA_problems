# def rotation_linear(arr):
#     min=0
#     for i in range(len(arr)):
#         if arr[i]<arr[min]:
#             min=i
#     return min


# arr1=list(map(int,input().split()))
# print(rotation_linear(arr1))


# using the binary search
def binary(arr):
    low=0
    high=len(arr)-1
    while low<high:
       mid=(low+high)//2
       if arr[mid]>arr[high]:
            low=mid+1
       else:
            high=mid
    return arr[low]

arr=[4,5,6,1,2,3]
print(binary(arr))
    

    





    
