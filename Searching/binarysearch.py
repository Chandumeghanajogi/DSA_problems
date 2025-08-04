def binary(num,target):
    low=0
    n=len(num)
    high=n-1
    while low<=high:
        mid=(low+high)//2
        if num[mid]==target:
            return mid
        elif target>num[mid]:
            low=mid+1
        else:
            high=mid-1
    return -1


    
    return -1

num=[3,4,6,7,9,12,16,17]
target=6
print(binary(num,6))
# my dry run:
# low=0
# high=8
# 0<=8  right
# mid=0+8//2----4