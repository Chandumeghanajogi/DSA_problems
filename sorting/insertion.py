def insertion(arr):
    for i in range(1,len(arr)):
        j=i
        while j>0 and arr[j]<arr[j-1]:
            arr[j],arr[j-1]=arr[j-1],arr[j]
            j-=1
    return arr

arr=[1,2,222222,159,12,600,59]
print(insertion(arr))
