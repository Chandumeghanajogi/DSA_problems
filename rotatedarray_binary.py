# def rotate(arr,target):
#     low,high=0,len(arr)-1
#     while low<=high:
#         mid=(low+high)//2
#         if arr[mid]==target:
#             return mid
#         if arr[low]<=arr[mid]:
#             if arr[low]<=target and target<=arr[mid]:
#                 high=mid-1
#             else:
#                 low=mid+1
#         else:
#             if arr[mid]<=target and target<=arr[high]:
#                 low=mid+1
#             else:
#                 high=mid-1
#     return -1

    

# arr=[7,8,9,2,3,4,5]
# target=9
# result=rotate(arr,target)
# if result!=-1:
#     print(f"found at {result}")
# else:
#     print("the {target} is not found ..")

#to find out the  minimum in the rotated array:
def linear(arr):
    min=arr[0]
    for i in range(1,len(arr)-1):
        if arr[i]<min:
            min=arr[i]
    return min

arr=[4,5,6,0,1,2,3]
print(linear(arr))




