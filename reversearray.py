def reverse_arr(arr):
    left=0
    right=len(arr)-1
    while left<right:
        arr[left],arr[right]=arr[right],arr[left]
        left+=1
        right-=1
    return arr
arr=[1,2,3,4,5]
print(reverse_arr(arr))

#to find out the second largest element in the array

def second(arr):
    if len(arr)<2:
        return "no element is available in the array"
    first=second=float("-inf")
    for num in arr:
        if num>first:
            second=first
            first=num
        elif num>second  and num!=first:
            second=num
    return second if second!=float("-inf") else "no element available"


nums=[10,20,200,100,1]
print(second(nums))


# problem 1:


            