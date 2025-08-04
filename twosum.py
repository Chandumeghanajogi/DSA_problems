# #Date:09-02-2024
# #two sum
# # to find the sum of 2 numbers in the list to give the target and print the  indices of those numbers
# # example:
# # a=[2,7,11,15]
# # target=9

# # solutions :
# # 1.brute force
# # 2.better using the hashing/dictionary
# # 3.using the two pointer approach

# # solutions:
# # 1. brute force

# def twosum(a,target):
#     for i in range(len(a)):
#         for j in range(len(a)):
#             if i==j:
#                 continue
#             else:
#                 if a[i]+a[j]==target:
#                     return [i,j]

# a=list(map(int,input().split()))
# target=int(input())
# print(twosum(a,target))

# # time complexity:O(n^2)

# # 2. better using the hashing/dictionary

# def twoSum(nums,target):
#     dictionary={}
#     for i in range(len(nums)):
#         if nums[i] in dictionary:
#             return [dictionary[nums[i]],i]
#         else:
#             dictionary[target-nums[i]]=i

# nums=list(map(int,input().split()))
# target=int(input())
# print(twoSum(nums,target))

# # time complexity:O(n)


def two(arr,tar):
    dici={}
    for i in range(len(arr)):
        if arr[i] in dici:
            return [dici[arr[i]],i]

        else:
            dici[target-arr[i]]=i

    print(dici)

arr=[2,7,11,15]
target=9
print(two(arr,target))

s="chandu"
print(s.index("h"))

