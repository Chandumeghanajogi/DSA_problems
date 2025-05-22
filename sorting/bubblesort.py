def bubble(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
               arr[j],arr[j+1]=arr[j+1],arr[j]

    return arr

def binary(arr1,element):
    low,high=0,len(arr1)-1
    while low<=high:
        mid=(low+high)//2
        if arr1[mid]==element:
            return mid
        elif arr1[mid]<element:
            low=mid+1
        else:
            high=mid-1


    return -1

arr=[1,4,3,2,100,8,33]
element=8
sort=bubble(arr)
answer=binary(sort,element)
if answer!=-1:
    print(f'{element} found at {answer}')
else:
    print("not there")





