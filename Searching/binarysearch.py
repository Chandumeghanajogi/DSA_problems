def binary(num,target):
    low=0
    high=len(num)-1
    while low<=high:
        mid=(low+high)//2
        if num[mid]==target:
            return mid
        elif target>mid:
            low=mid+1
        else:
            high=mid-1
    return -1

num=[10,20,30,40,50]
target=40
print(binary(num,40))
