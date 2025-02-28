# # # arr=[1,2,2,3,10,4]
# # # x=2
# # # output=3
# # def upper(arr,x):
# #     low,high=0,len(arr)-1
# #     while low<=high:
# #         mid=(low+high)//2
# #         if arr[mid]>x:
# #             high=mid-1
# #         else:
# #             low=mid+1
# #     return low

# # arr=[1,2,2,3,10,4]
# # x=10
# # print(upper(arr,x))

# def binary(arr,target):

#     low=0
#     high=len(arr)-1
#     while low<=high:
#         mid=(low+high)//2
#         if arr[mid]==target:
#             return mid
#         elif arr[mid]>target:
#             high=mid-1
#         else:
#             low=mid+1
#     return -1


# arr=[1,2,6,4,9,77]
# target=9

# result=binary(arr,target)
# print(result)
# # if result!=-1:
# #     print("found at {result}".format(result))
# # else:
# #     print("not found")


#to find out the peak element

# def peak(arr):
#     low=0
#     high=len(arr)-1
#     arr1=max(arr)
#     while low<=high:
#         mid=(low+high)//2
#         left=arr[:mid]
#         n1=len(left)
#         right=arr[mid:]
#         for i in range(n1):
#             if (arr1 in left) and arr1>arr[arr1]-1 and (arr1>arr[arr]+1):
#                 return arr1.index()
            
def peak(arr):
    low=0
    high=len(arr)
    arr1=max(arr)
    while low<=high:
        mid=(low+high)//2
        if (mid==0 or  (arr[mid]>arr[mid]-1)) and (mid==high or (arr[mid]>arr[mid]+1)):
            return mid
        elif mid>0 and arr[mid-1]>mid:
            high=mid-1
        else:
            low=mid+1
    return -1


elements=[1,2,3,4,10,4]
print(peak(elements))

        