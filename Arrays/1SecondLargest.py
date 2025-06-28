def second(arr):
    first=float("-inf")
    second=float("-inf")
    for i in arr:
        if i>first:
            second=first
            first=i
        elif first>i and i>second:
            second=i
    return second if second!=float("-inf") else 0


arr=[1,200,2,3,5,10,99,122,3000,4000]
print(second(arr))

def second(arr):
    first=float("inf")
    second=float("inf")
    for i in arr:
        if i<first:
            second=first
            first=i
        elif first<i and i<second:
            second=i
    return second if second!=float("-inf") else 0


arr=[0,1,200,2,3,5,10,99,122,3000,4000]
print(second(arr))

arr=[17,2,3,4,18]
arr=[18,]